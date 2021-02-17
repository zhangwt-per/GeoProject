# coding: UTF-8
regions = ''
idField = ''
codes = {}
veti_data_dict = {}
input_dir = ""
input_shp_dir = ""
output_dir = ""
map_type = [u'数据地图', u'柱状图', u'折线图', u'雷达图']
inital_indexs = [u'总用地面积', u'耕地面积', u'耕地比重', u'林地面积', u'林地比重', u'草地面积', u'草地比重', u'水域湿地面积', u'水域湿地比重', u'建设用地面积',
                 u'建设用地比重', u'未利用地面积', u'未利用地比重', u'生境质量指数', u'植被覆盖指数', u'水网密度指数', u'人类干扰指数', u'生态环境质量']
inital_areas = []
inital_years = []
current_indexs = []
current_areas = []
current_years = []
radar_schema = []
index_dict = {
    u'总用地面积': 'TOT', u'耕地面积': 'AGR', u'耕地比重': 'AGR_P', u'林地面积': 'FRT', u'林地比重': 'FRT_P',
    u'草地面积': 'GRS', u'草地比重': 'GRS_P', u'水域湿地面积': 'WAT', u'水域湿地比重': 'WAT_P', u'建设用地面积': 'BUL',
    u'建设用地比重': 'BUL_P', u'未利用地面积': 'UUS', u'未利用地比重': 'UUS_P', u'生境质量指数': 'EQI', u'植被覆盖指数': 'VCI', u'水网密度指数': 'WDI',
    u'人类干扰指数': 'HDI', u'生态环境质量': 'VTEI'
}
index_num_dict = {
    u'总用地面积': 1, u'耕地面积': 2, u'耕地比重': 3, u'林地面积':4, u'林地比重': 5,
    u'草地面积': 6, u'草地比重': 7, u'水域湿地面积': 8, u'水域湿地比重': 9, u'建设用地面积': 10,
    u'建设用地比重': 11, u'未利用地面积': 12, u'未利用地比重': 13, u'生境质量指数': 14, u'植被覆盖指数': 15, u'水网密度指数': 16,
    u'人类干扰指数': 17, u'生态环境质量': 18
}