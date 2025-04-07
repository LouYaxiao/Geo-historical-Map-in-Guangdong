import os
import folium
import pandas as pd

# 获取当前脚本文件所在的目录
script_dir = os.path.dirname(__file__)

# 读取包含经纬度信息的Excel文件，并指定dtype参数
df = pd.read_excel(r"C:\Users\Lou13\Desktop\广西进士_带坐标_去重.xlsx", dtype={'坐标': str})

# 创建一个空地图
m = folium.Map(location=[23.835400, 108.327000], zoom_start=6)  # 设置地图中心和缩放级别

# 根据年份创建不同的图层
for year in df['年份'].unique():
    # 创建一个新的FeatureGroup图层
    year_fg = folium.FeatureGroup(name=str(year))

    # 根据年份过滤数据
    year_data = df[df['年份'] == year]

    # 在图层上添加数据点
    for index, row in year_data.iterrows():
        # 检查坐标是否为 NaN，如果是，则跳过该行
        if pd.notnull(row['坐标']):
            folium.Marker([float(row['坐标'].split(',')[1]), float(row['坐标'].split(',')[0])],
                          tooltip=row['姓名']).add_to(year_fg)

    # 将图层添加到地图上
    year_fg.add_to(m)

# 添加地图控制器
folium.LayerControl().add_to(m)

# 保存地图为HTML文件，保存在当前脚本文件所在的目录下
html_file_path = os.path.join(script_dir, 'guangxi_map.html')
m.save(html_file_path)

print(f"地图已保存至 {html_file_path}")