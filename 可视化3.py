import matplotlib.pyplot as plt

# 论文数据
data = {
    "出版年份": [
        1977, 2004, 1998, 1975, 1952, 1994, 2013, 2003, 2018,
        1971, 1969, 2019, 2012, 2011, 2007, 2005, 2017, 1997,
        2001, 1964, 1989, 1986, 1985, 1983, 1978, 1976, 1973
    ],
    "频数": [
        4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1
    ]
}

# 将年份和频数转换为列表
years = data["出版年份"]
counts = data["频数"]

# 创建柱状图
plt.figure(figsize=(10, 8))
plt.bar(years, counts, color='skyblue')

# 设置标题和标签
plt.title('Publication Year Counts')
plt.xlabel('Publication Year')
plt.ylabel('Counts')

# 显示数值标签
for i, count in enumerate(counts):
    plt.text(years[i], count + 0.05, str(count), ha='center')

# 调整x轴的标签角度，以便更好地显示
plt.xticks(rotation=90)

# 显示图形
plt.tight_layout()  # 调整整体空白
plt.show()