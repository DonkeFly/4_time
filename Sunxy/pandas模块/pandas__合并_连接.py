#合并
import pandas as pd
df1 = pd.DataFrame({'一班': [90, 80,80 , 75, 99, 55, 76, 78, 98, None, 90],
                        '二班': [75, 98, 100, None, 77, 45, None, 66, 56, 80, 57],
                        '三班': [45, 89, 77, 67, 65, 100, None, 75, 64, 88, 99]})
df2 = pd.DataFrame({'一班': [90, 80, 66, 75, 99, 55, 76, 78, 98, None, 90],
                        '二班': [71, 98, 100, None, 77, 45, None, 66, 56, 80, 57],
                        '三班': [45, 89, 77, 67, 65, 100, None, 75, 64, 88, 99]})
df1.append(df2)
pd.concat([df1,df2],axis=0) #行合并（竖着）
pd.concat([df1,df2],axis=1) #列合并（横着）
pd.merge(df1,df2,on = '一班')  #按相同字段合并，且取两个都有的。
pd.merge(df1,df2) #取数据完全相同的（没参数）
#左右内外合并
pd.merge(df1,df2,left_on='一班',right_on='二班',suffixes=('_1','_2'))#d筛选出df1与df2相同的部分,suffixes作用为给两个表的列名进行标识

pd.merge(df1,df2,on = '一班' ,how = 'inner') #取交集
pd.merge(df1,df2,on = '一班' ,how = 'outer') #取并集
df1['一班'].combine_first(df1['二班'])  #(重叠合并)一班为空的 由二班同行补过来， 重叠合并，当两者皆有以前者为准，为空时，则使用后者的补上。
import pandas as pd
df3 = pd.DataFrame({'name':['A','B','C','D','E','F'],
        'age':[11,12,13,14,15,16],
        'class':[1,2,3,4,5,6]})
df4 = pd.DataFrame({'name':['C','D','E','F','G','H'],
        'age':[13,13,14,15,16,17],
        'class':[3,2,3,4,5,6]})
df3
df4
df3.append(df4)
pd.concat([df3,df4],axis= 0)
pd.concat([df3,df4],axis= 1)

pd.merge(df3,df4)
pd.merge(df3,df4,on='name')  #取name列相同 的所用列内容
pd.merge(df3,df4,left_on= 'name',right_on= 'name',suffixes=('_x','_y'))
pd.merge(df3,df4,on='name',how='inner')  #取所选列共有元素 交集
pd.merge(df3,df4,on='name',how='outer')  #并集
pd.merge(df4,df3,on='name',how='left')   #左连接 根据第一个列表
pd.merge(df4,df3,on='name',how='right')  #右连接
