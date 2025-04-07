import pandas as pd

# 读取 xlsx 文件
file_path = r"C:\Users\Lou13\Desktop\广西进士_带坐标.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# 假设坐标列的列名为“坐标”
coordinate_column = '坐标'


# 处理坐标列中的重复数据
def modify_duplicates(df, column):
    # 找到重复的值
    duplicates = df[df.duplicated(subset=[column], keep=False)]

    # 对重复值进行修改
    for idx, (coord, group) in enumerate(duplicates.groupby(column)):
        increment = 0.00001  # 每次增加的值，修改经纬度的小数位
        for i, index in enumerate(group.index):
            # 拆分经纬度
            longitude, latitude = df.at[index, column].split(',')

            # 将字符串转换为浮点数
            longitude = float(longitude)
            latitude = float(latitude)

            # 根据索引增加经度或纬度的最后两位小数
            longitude += i * increment
            latitude += i * increment

            # 格式化为字符串，保留6位小数
            df.at[index, column] = f"{longitude:.6f},{latitude:.6f}"

    return df


# 调用函数处理重复的坐标
df = modify_duplicates(df, coordinate_column)

# 保存修改后的文件
output_path = r"C:\Users\Lou13\Desktop\广西进士_带坐标_去重.xlsx"
df.to_excel(output_path, index=False)

print("处理完成，文件已保存为:", output_path)


