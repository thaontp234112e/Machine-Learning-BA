#du lieu co chuoi: utf-8 vao de no ve dinh dang dung
#csv thi dung \t ( moi dong)
#low_memory cung cap them tai nguyen cho ham chay
import pandas as pd
df=pd.read_csv("../dataset/SalesTransactions/SalesTransactions.csv",
               sep=',',encoding='utf-8',low_memory=False)

print(df)
#json,xml lam cau hinh
#xuat dang tho: csv