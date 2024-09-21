import pandas as pd
import matplotlib.pyplot as plt

# 加载 CSV 文件 (从第四行开始)
file_path = r'C:\Users\china\Desktop\pfad-main\daily_KP_UV_2024.csv'
df = pd.read_csv(file_path, skiprows=3)  # 跳过前三行

# 打印实际的列名，检查是否有意外的情况
print("Original Columns:", df.columns)

# 手动重命名列名，不包括第五列
df.columns = ['年/Year', '月/Month', '日/Day', '數值/Value']

# 打印重命名后的列名
print("Renamed Columns:", df.columns)

# 打印年、月、日列的前几行，检查是否有异常值
print(df[['年/Year', '月/Month', '日/Day']].head())

# 将“年/Year”, “月/Month”, “日/Day”列中的非数字字符转换为NaN，然后再转换为整数
df['年/Year'] = pd.to_numeric(df['年/Year'], errors='coerce').fillna(1).astype(int)
df['月/Month'] = pd.to_numeric(df['月/Month'], errors='coerce').fillna(1).astype(int)
df['日/Day'] = pd.to_numeric(df['日/Day'], errors='coerce').fillna(1).astype(int)

# 检查处理后的年、月、日列
print("After conversion:")
print(df[['年/Year', '月/Month', '日/Day']].head())

# 使用 apply 函数逐行生成日期，确保没有浮点数
def create_date(row):
    try:
        # 确保 year, month, day 都是整数
        return pd.Timestamp(year=int(row['年/Year']), month=int(row['月/Month']), day=int(row['日/Day']))
    except ValueError:
        return pd.NaT  # 如果有错误返回 NaT

df['Date'] = df.apply(create_date, axis=1)

# 检查生成的日期列
print(df[['年/Year', '月/Month', '日/Day', 'Date']].head())

# 绘制折线图，显示每日的數值/Value
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['數值/Value'], marker='o', linestyle='-', color='b')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Daily Value for 2024')
plt.xticks(rotation=45)

# 显示图表
plt.tight_layout()
plt.show()
