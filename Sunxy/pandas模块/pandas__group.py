import pandas as pd #
data = pd.read_excel("C:\\Users\\sun\\Documents\\Tencent Files\\201629608\\FileRecv\\original_data.xls")
data1 = pd.DataFrame(data)
data1['发生时间'] = pd.to_datetime(data1['发生时间'],format='%Y%m%d%H%M%S')
data1['发生时间']
data1['日期'] = [i.day for i in data1['发生时间']]
data1['日期']
data2=data1.groupby('日期') #对相同日期进行分组
data3 = data1.groupby(['有无水流','日期'])    #两个分
len(data3)  #共有多少组
len(data2) #共有多少组
data2.groups#分组之后属于该组数据的索引
data2.count() #每一列数据的数量，精确到每一列
data2.size() #每一列数据的数量，只有个结果
data2.max() #求每个分组里的最大值
data2.mean()#求均值，只列出能够进行平均值的列
data2.median()#每一组的中位数
data2.cumcount()#对每个分组中组员的进行标记，0至n-
data2[['发生时间','水流量']].agg(max)  #.agg中位字典格式
data2.agg({'发生时间':max,'水流量':sum}) #求时间的最大值，并求水流量的和 （不能求均值）
data2.agg({'水流量':lambda x:x.mean(),'发生时间':lambda x:x.max()}) #agg求均值的方法
data2.apply(lambda x:x.max()) #只能对所有列进行同一种运算  无法求特定列
data2['热水器编号'].transform(lambda x:x.astype(str)+'china').head() #astype 将每一个元素转化为字符串
data2.transform(lambda x:x.astype(str)+'china').head()
data2['热水器编号','发生时间'].transform(lambda x:x.astype(str)+'china').head() #transform对每一个列进行操作
data2['水流量'].transform(lambda x:x**2) #transform对每一个列进行操作
