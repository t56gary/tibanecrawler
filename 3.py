import pandas as pd

df=pd.read_csv("ted_main.csv",encoding="utf-8")
# print(df)
#單行操作:["行標籤名"] => Series
# print(df["comments"])

#多行操作[["標1","標2","標3"]]
#裡面[]:list 外面[]:行操作
print(df[["comments","description"]])
#純粹耍帥一下:翻轉
df.T.to_csv("ted_transpose.csv",encoding="utf-8")
print(df.T)