# -*- coding: utf-8 -*-
import value_base
import geopandas as gpd
import pandas as pd
from matplotlib import pyplot as plt


def create_data_map(key, value, index):
    data = gpd.read_file(unicode(value_base.input_shp_dir))
    veti_data = pd.DataFrame(value, columns=['XZQMC',
                                             'TOT',
                                             'AGR',
                                             'AGR_P',
                                             'FRT',
                                             'FRT_P',
                                             'GRS',
                                             'GRS_P',
                                             'WAT',
                                             'WAT_P',
                                             'BUL',
                                             'BUL_P',
                                             'UUS',
                                             'UUS_P',
                                             'EQI',
                                             'VCI',
                                             'WDI',
                                             'HDI',
                                             'VTEI'])
    veti_data = data.merge(veti_data, on='XZQMC', how='left')
    veti_data = gpd.GeoDataFrame(veti_data)
    ax = veti_data.plot(figsize=(8, 8), column=index, k=4, cmap=plt.cm.Blues, edgecolor='white', alpha=0.8,
                        legend=True)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    for n, i in enumerate(veti_data['geometry'].apply(lambda x: x.representative_point().coords[0])):
        plt.text(i[0] - 0.2, i[1], veti_data['XZQMC'][n], fontsize=8, horizontalalignment="left")

    ax.set_axis_off()

    result = value_base.output_dir +"\\"+ key + index + ".png"
    plt.savefig(str(result))
    return result
