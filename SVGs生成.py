import pandas as pd
import svgwrite

# 读取Excel文件
excel_file = r"C:\Users\Lou13\Desktop\广西进士_带坐标_去重.xlsx"
df = pd.read_excel(excel_file)

# 提取姓名和坐标列的数据
names = df['姓名']
years = df['年份']
coordinates = df['坐标']

# 创建SVG图层
svg_file = r'D:\Python\modified_广西.svg'
dwg = svgwrite.Drawing(svg_file, profile='tiny')

# 定义一些常量
circle_radius = 5
circle_color = 'red'

# 遍历每个条目，在SVG文件中绘制点
for name, year, coord in zip(names, years, coordinates):
    x, y = map(float, coord.split(','))  # 将坐标字符串分割为x和y坐标
    # 计算在SVG中的位置，这里简单处理，具体情况根据实际需要调整
    svg_x = x
    svg_y = y
    # 绘制圆形表示点
    dwg.add(dwg.circle(center=(svg_x, svg_y), r=circle_radius, fill=circle_color))
    # 添加文本标签，显示姓名和年份
    dwg.add(dwg.text(f'{name} ({year})', insert=(svg_x + circle_radius + 2, svg_y),
                     fill='black', font_size=10, font_family='Arial'))

# 保存SVG文件
dwg.save()
print(f'SVG文件已保存至 {svg_file}')
