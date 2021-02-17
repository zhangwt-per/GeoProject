# -*- coding: utf-8 -*-
from pyecharts import Bar, Timeline, Line, Radar

import value_base


def bar_map():
    kwargs = dict(
        label_text_color=None,
        is_label_show=True,
        legend_orient='vertical',
        legend_pos='right',
        legend_top='center',
        legend_selectedmode='single',
        legend_text_size=18,
        label_text_size=18,
        label_emphasis_textsize=18,
        xaxis_name_size=18,
        xaxis_label_textsize=18,
        xaxis_margin=5,
        xaxis_line_width=2,
        yaxis_name_size=18,
        yaxis_label_textsize=18,
        bar_category_gap=25,
        yaxis_line_width=2,
        is_splitline_show=False,
        is_xaxis_boundarygap=True,
        is_toolbox_show=False,
    )
    timeline = Timeline(timeline_bottom=0, width=1400, height=700, timeline_symbol_size=10)
    for year in value_base.current_years:
        bar = Bar('村镇对比图', title_pos='center', title_text_size=30, title_top=10)
        for index in value_base.current_indexs:
            data = []
            for i in value_base.current_areas:
                for veti_data in value_base.veti_data_dict[year]:
                    if veti_data[0] == i:
                        data.append(veti_data[value_base.index_num_dict[index]])
            bar.add(index, value_base.current_areas, data, **kwargs)
        timeline.add(bar, year)
    result = str(value_base.output_dir + u"村镇对比.html")
    timeline.render(result)


def line_map():
    kwargs = dict(
        label_text_color=None,
        is_label_show=True,
        legend_orient='vertical',
        legend_pos='right',
        legend_top='center',
        legend_selectedmode='single',
        legend_text_size=18,
        label_text_size=18,
        label_emphasis_textsize=18,
        xaxis_name_size=18,
        xaxis_label_textsize=18,
        xaxis_margin=5,
        xaxis_line_width=2,
        yaxis_name_size=18,
        yaxis_label_textsize=18,
        yaxis_line_width=2,
        is_splitline_show=False,
        is_xaxis_boundarygap=True,
        is_toolbox_show=False,
        line_width=3
    )
    timeline = Timeline(timeline_bottom=0, width=1400, height=700, timeline_symbol_size=10)
    for area in value_base.current_areas:
        line = Line('时间序列图', title_pos='center', title_text_size=30, title_top=10)
        for index in value_base.current_indexs:
            data = []
            for year in value_base.current_years:
                for veti_data in value_base.veti_data_dict[year]:
                    if veti_data[0] == area:
                        data.append(veti_data[value_base.index_num_dict[index]])
            print data
            print value_base.current_years
            line.add(index, value_base.current_years, data, **kwargs)
        timeline.add(line, area)
    result = str(value_base.output_dir + u"时间序列图.html")
    timeline.render(result)


def radar_map():
    kwargs = dict(
        label_text_color=None,
        is_label_show=True,
        legend_orient='vertical',
        legend_pos='right',
        legend_top='center',
        legend_text_size=18,
        label_text_size=18,
        label_emphasis_textsize=18,
        xaxis_name_size=18,
        xaxis_label_textsize=18,
        xaxis_margin=5,
        xaxis_line_width=2,
        yaxis_name_size=18,
        yaxis_label_textsize=18,
        yaxis_line_width=2,
        is_splitline_show=False,
        is_xaxis_boundarygap=True,
        is_toolbox_show=False,
        line_width=3
    )
    timeline = Timeline(timeline_bottom=0, width=1400, height=700, timeline_symbol_size=10)
    for year in value_base.current_years:
        radar_map = Radar('雷达图', title_pos='center', title_text_size=30, title_top=10)
        for area in value_base.current_areas:
            data = [[]]
            for index in value_base.current_indexs:
                for veti_data in value_base.veti_data_dict[year]:
                    if veti_data[0] == area:
                        data[0].append(round(veti_data[value_base.index_num_dict[index]],2))
            radar_map.set_radar_component(schema=value_base.radar_schema)
            radar_map.add(area, data, **kwargs)
        timeline.add(radar_map, year)
    result = str(value_base.output_dir + u"雷达图.html")
    timeline.render(result)
