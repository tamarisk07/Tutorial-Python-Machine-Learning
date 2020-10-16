import pandas as pd
import numpy as np

# Series
s = pd.Series([1, 3, 6, np.nan, 44, 1])     # 默认index从0，可以通过修改index参数来改变索引设置
print(s)
ss = pd.Series([1, 3, 6, np.nan, 44, 1], index=[3, 4, 3, 7, 8, 9])


# DataFrame
dates = pd.date_range('2020-10-12', periods=6)  # 起始日期，持续天数
'''
等价式为 
dates = pd.date_range('2020-10-12', '2020-10-17')   #起始日期，结束日期
'''
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns = ['a','b','c','d'])
print(df)   # 生成一个6行4列的满足标准正态分布的数组，行索引为日期，列索引为a、b、c、d
print(df['b'])  # 生成一个6行1列的数组，行索引不变，列索引选取b但不显示

df1 = pd.DataFrame(np.arange(12).reshape(3,4))  # 未指定行列索引的数据，会自动添加index从0开始
print(df1)
df2 = pd.DataFrame({
    'A':[1,2,3,4],
    'B':pd.Timestamp('20180819'),
    'C':pd.Series([1,6,9,10],dtype='int32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(['test','train','test','train']),
    'F':'foo'
})  # 另一个方式，列索引标注，行索引从0开始
print(df2)
print(df2.index)    # df2的行索引
print(df2.columns)  # df2的列索引
print(df2.values)   # df2的value数组，类似一个矩阵，不显示索引index
print(df2.describe())   # 数据总结的方式
print(df2.T)    # 数据翻转   或者用np.transpose(df2)效果一样，列索引变成行索引，行索引变成列索引
print(df2.sort_index(axis=1,ascending=False))
# axis=1表示列索引操作，0表示行索引操作，默认ascending为True升序，False降序
print(df2.sort_values(by='C',ascending=False))  # 表示以C列为标准降序排列


# pandas选择数据
dates = pd.date_range('20201014',periods=6)
df3 = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,columns=['A','B','C','D'])

print(df3['A'])  # 检索A列元素，显示行名称和元素
print(df3.A)     # 另一种写法,检索A列
print(df3[0:3])  # 选取前三行
print(df3['20201014':'20201016'])    # 选取20201014行到20202016行的元素
print(df3.loc['20201014'])  #指定行数据
print(df3.loc['20201014':'20201015'])   # 指定行数据的另一种方式
print(df3.loc[['20201014','20201016']]) # 指定行数据的另一种方式
print(df3.loc[:,'A':'C'])    # 指定列数据
print(df3.loc[:,['A','C']])  # 指定列数据的另一种方式
print(df3.loc['20201014',['A','B']])    # 行列同时检索
print(df3.iloc[3,1])    # 获取特定位置的值
print(df3.iloc[3:5,1:3])    # 不包含末尾5、3，同列表切片
print(df3.iloc[[1,3,5],1:3])    # 跨行操作
print(df3.iloc[:3,[0,2]])   # 跨行操作
print(df3[df3.A>8])  # 通过判断条件选择
print(df3.loc[df3.A>8])  # 同上，判断条件选择


# Pandas设置值
dates = pd.date_range('20201014',periods=6)
df4 = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])    #创建数据
print(df4)
# 根据位置设置值
df4.iloc[2,2] = 111
df4.loc['20201014','B'] = 2222
print(df4)
# 根据条件设置值
df4.B.loc[df4.A>4] = 0  # A列中的值大于4的行，使其B列值为0
print(df4)
# 按照行列设置值
df4['F'] = np.nan   #将一整列都设置为NaN，且若无此列则新增一列
print(df4)
# 添加Series序列，添加在末尾,若有未添加项则值为NaN
df4['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20201018',periods=6))
print(df4)
df4['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20201014',periods=6))
print(df4)
# 设定某行某列为特定值
df4.loc['20201014','A'] = 56
print(df4)
df4.iloc[0,0] = 76
print(df4)
# 修改一整行数据
df4.iloc[1] = np.nan
print(df4)
df4.loc['20201014'] = np.nan
print(df4)
df4.iloc[2,:] = np.nan
print(df4)
# 修改一列数据
df4.iloc[:,1] = np.nan
print(df4)
df4.loc[:,'D'] = np.nan
print(df4)


# Pandas处理丢失数据
dates1 = pd.date_range('20201015',periods=6)
df5 = pd.DataFrame(np.arange(24).reshape(6,4),index=dates1, columns = ['A','B','C','D'])
print(df5)
df5.iloc[0,1] = np.nan  # 填充NaN数据
df5.iloc[1,2] = np.nan
print(df5)
print(df5.dropna()) # 删除掉有NaN的行，默认对行操作
print(df5.dropna(
    axis=0,     # 0对行操作，1为对列操作
    how='any'   # any为只要存在NaN就删掉，all为全部是NaN才删掉
))
print(df5.dropna(axis=1,how = 'any'))
print(df5.fillna(value=0))  # 将数组中的NaN值替换为value
print(df5.isnull())     # 一个bool value的数组，检查是否为空，若是，则值为True，反之为False
print(df5.isna())       # 检查是否为NaN
print(df5.isnull().any())   # 检测某列是否有缺失数据NaN，若有，返回True
print(df5.isnull().sum())   # 检测每一列中含有缺失数据NaN的数量
print(np.any(df5.isnull()) == True)   # 监测数据中是否存在NaN，如果存在则返回True


# Pandas导入导出
'''
data = pd.read_csv('student.csv')   #读取csv，导入数据
print(data)      #打印出data
print(data.head(3))     #前三行
print(data.tail(3))     #后三行

data.to_pickle('student.pickle')    #将data存取为pickle文件
print(pd.read_pickle('student.pickle')) #读取pickle文件并打印
'''


# Pandas合并操作
df6 = pd.DataFrame(np.ones((3,4))*0, columns = ['a','b','c','d'])
df7 = pd.DataFrame(np.ones((3,4))*1, columns = ['a','b','c','d'])
df8 = pd.DataFrame(np.ones((3,4))*2, columns = ['a','b','c','d'])
print(df6)
print(df7)
print(df8)
res = pd.concat([df6,df7,df8],axis=0)   # 纵向合并，若出现原来没有值的地方填充为NaN
print(res)
res = pd.concat([df6,df7,df8],axis=0,ignore_index=True)     # 运用ignore_index可以让index重置而不重复
print(res)
df9 = pd.DataFrame(np.ones((3,4))*0, columns = ['a','b','c','d'], index = [1,2,3])
df10 = pd.DataFrame(np.ones((3,4))*1, columns = ['b','c','d','e'], index = [2,3,4])
print(df9)
print(df10)
# join为outer，是函数默认值。此方法依照column进行纵向合并，相同column上下合并在一起，其他独自的column独自成列，原来没有值的地方NaN填充
res = pd.concat([df9,df10],axis=0,join='outer')
print(res)
res = pd.concat([df9,df10],axis=0,join='outer',ignore_index = True)
print(res)
# join为inner，合并相同的字段，column不相同的部分舍去
res = pd.concat([df9,df10],axis=0,join='inner')
print(res)
# join_axes方法可以依照axes合并,原来没有的值填充为NaN，但此法现已取消
# res = pd.concat([df9,df10],axis=1,join_axes=[df9.index])
res = pd.concat([df9,df10],axis=1)
print(res)
res = res.reindex(df9.index)
print(res)
# append方法只能纵向合并，ignore_index重置参数
res = df6.append(df7,ignore_index=True)
print(res)
res = df6.append([df7,df8],ignore_index=True)
print(res)
# append方法还可以合并Series
s1 = pd.Series([1,2,3,4],index = ['a','b','c','d'])
print(s1)
res = df6.append(s1,ignore_index=True)
print(res)
# 两种纵向合并的方法是一样的
res = pd.concat([df6,df7,df8],axis=0,ignore_index=True)
res1 = df6.append([df7,df8],ignore_index=True)
print(res)
print(res1)


# Pandas合并merge
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})
print(left)
print(right)
res = pd.merge(left,right,on='key') # 根据key列进行合并
print(res)

# 使用两组key合并，使用key1与key2列进行合并，并打印出四种结果，left，right，outer，inner
left = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                     'key2':['K0','K1','K0','K1'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key1':['K0','K1','K1','K2'],
                      'key2':['K0','K0','K0','K0'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})
print(left)
print(right)
# 使用inner，inner是取两个dataframe的连接键列中元素的交集,取这几行（key1与key2都相同）
res = pd.merge(left,right,on=['key1','key2'],how='inner')
print(res)
# 使用outer则是取了连接键列中元素的并集，没有的元素则用NaN补充
res = pd.merge(left,right,on=['key1','key2'],how='outer')
print(res)
# 按照左边那个dataframe的连接键，若该行右边有相同的连接键，则读入右边其他列的值，若有多行满足，则会增加行，若没有，则为NaN
res = pd.merge(left,right,on=['key1','key2'],how='left')
print(res)
# 同left法，只不过依据对象为右边dataframe
res = pd.merge(left,right,on=['key1','key2'],how='right')
print(res)

# Indicator设置合并列名称，会显示出合并项的合并列是left_only还是right_only还是both
df11 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df12 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df11)
print(df12)
res = pd.merge(df11,df12,on='col1',how='outer',indicator=True)
print(res)
# 自定义Indicator的名称，这样也会默认值为True
res = pd.merge(df11,df12,on='col1',how='outer',indicator='indicator_column')
print(res)

# 根据index进行合并,设置left_index=True
left = pd.DataFrame({'A':['A0','A1','A2'],
                     'B':['B0','B1','B2']},
                    index = ['K0','K1','K2'])
right = pd.DataFrame({'C':['C0','C2','C3'],
                     'D':['D0','D2','D3']},
                    index = ['K0','K2','K3'])
print(left)
print(right)
res = pd.merge(left,right,left_index=True,right_index=True,how='outer')
print(res)
res = pd.merge(left,right,left_index=True,right_index=True,how='inner')
print(res)

# 解决overlapping的问题
boys = pd.DataFrame({'k':['K0','K1','K2'], 'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K0','K3'], 'age':[4,5,6]})
print(boys)
print(girls)
# 进行k连接键合并时，age重复了，可以通过suffixes设置增加后缀，来保证不重复不同名，（不增加后缀的话默认左为_x右为_y）
res = pd.merge(boys,girls,on='k',how='inner')
print(res)
res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print(res)
print('\n')


# Pandas plot画图
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000),index=np.arange(1000))   #标准正态分布
print(data)
print(data.cumsum())
data.plot()
plt.show()  # 横轴是index，纵轴是value

data2 = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list('ABCD')
)   # 1000行4列的数据进行画图
data2.cumsum()
data2.plot()
plt.show()
# 将两个data画在同一个ax上面的散点图
ax_ = data2.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data2.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax_)
plt.show()
