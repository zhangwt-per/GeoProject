# coding: UTF-8
# 栅格数据 要求为整型
# 要求：
# 1. value为土地编码字段值且为正
# 2. count为value个数
# 3. 两期栅格数据的value编码必须一致
# 4. 编码规则：
import arcpy
from PyQt4.QtGui import QApplication
from arcpy.sa import *
import value_base


# 计算地类面积
def sum_area_by_codes(arr, codes, cellarea):
    sumarea = 0

    for code in codes:
        # 栅格数据的Value和Count可能首字母大写
        # 也可能全部字母大写
        # 所以捕捉错误
        try:
            if len(arr['Count'][arr['Value'] == code]) == 0:
                area = 0
            else:
                area = (arr['Count'][arr['Value'] == code][0]) * cellarea
        # 一旦出错，意味着全部字母大写
        except:
            if len(arr['COUNT'][arr['VALUE'] == code]) == 0:
                area = 0
            else:
                area = (arr['COUNT'][arr['VALUE'] == code][0]) * cellarea

        sumarea = sumarea + area

    return sumarea


def vtei(land_in_region, cellarea, regionid, regionname, land, codes):
    landview = 'landview'
    arcpy.MakeTableView_management(land_in_region, landview)

    # 转为数组
    arr = arcpy.da.TableToNumPyArray(landview, '*')
    arcpy.Delete_management(landview)

    # 总用地面积
    TOT = float(arr['Count'].sum() * cellarea)

    # 1. 耕地面积
    AGR = float(sum_area_by_codes(arr, codes['AGR'], cellarea))

    # 耕地比重%
    AGR_P = AGR / TOT * 100

    # 2. 林地面积
    FRT = float(sum_area_by_codes(arr, codes['FRT'], cellarea))

    # 林地比重%
    FRT_P = FRT / TOT * 100

    # 3. 草地面积
    GRS = float(sum_area_by_codes(arr, codes['GRS'], cellarea))

    # 草地比重
    GRS_P = GRS / TOT * 100

    # 4. 水域湿地面积
    WAT = float(sum_area_by_codes(arr, codes['WAT'], cellarea))

    # 水域湿地比重%
    WAT_P = WAT / TOT * 100

    # 5. 建设用地面积
    BUL = float(sum_area_by_codes(arr, codes['BUL'], cellarea))

    # 建设用地比重%
    BUL_P = BUL / TOT * 100

    # 6. 未利用地面积
    UUS = float(sum_area_by_codes(arr, codes['UUS'], cellarea))

    # 未利用地比重
    UUS_P = UUS / TOT * 100

    # 生境质量指数
    EQI = (0.35 * FRT_P +
           0.21 * GRS_P +
           0.28 * WAT_P +
           0.11 * AGR_P +
           0.04 * BUL_P +
           0.01 * UUS_P)

    # 植被覆盖指数
    VCI = (0.38 * FRT_P +
           0.34 * GRS_P +
           0.19 * AGR_P +
           0.07 * BUL_P +
           0.02 * UUS_P)

    # 水网密度指数
    WDI = WAT_P

    # 人类干扰指数
    HDI = (0.90 * BUL_P +
           0.10 * AGR_P)

    # 生态环境质量指数
    VTEI = (0.30 * EQI +
            0.25 * VCI +
            0.25 * WDI +
            0.20 * (100 - HDI))
    veti_data_list = [regionname,
                      TOT,
                      AGR,
                      AGR_P,
                      FRT,
                      FRT_P,
                      GRS,
                      GRS_P,
                      WAT,
                      WAT_P,
                      BUL,
                      BUL_P,
                      UUS,
                      UUS_P,
                      EQI,
                      VCI,
                      WDI,
                      HDI,
                      VTEI]
    return veti_data_list


def veti_input(self):
    print value_base.input_dir
    arcpy.env.workspace = unicode(value_base.input_dir)
    nameField = 'XZQMC'

    # 设置土地利用数据分辨率
    cellsize = 30.0
    cellarea = cellsize ** 2.0
    codesize = 2

    resultfile = 'D:\\result.txt'
    resultfields = ['ID', 'Name', 'Land', 'Indicator', 'Value']
    matrixfile = 'D:\\matrix.csv'

    args_list = []
    for year in value_base.inital_years:
        year = str(year)
        value_base.veti_data_dict[year] = []
    with arcpy.da.UpdateCursor(str(value_base.regions), [str(value_base.idField), nameField, 'SHAPE@']) as cursor:
        i = 0
        for row in cursor:
            args_list.append([row[0], row[1], row[2]])
            value_base.inital_areas.append(row[1])
            QApplication.processEvents()
            i += 1
        length = 100.0 / (i * len(value_base.inital_years))
        # 计算各类用地面积、比例和各项指数
        for arg in args_list:
            for land in value_base.inital_years:
                land = str(land)
                self.step += length
                land_in_region = ExtractByMask(land, arg[2])
                self.pbar.setValue(self.step)
                QApplication.processEvents()
                # 按掩膜提取评价区域内的土地利用数据
                veti_data = vtei(land_in_region,
                                 cellarea,
                                 arg[0],
                                 arg[1],
                                 land,
                                 value_base.codes)
                value_base.veti_data_dict[land].append(veti_data)