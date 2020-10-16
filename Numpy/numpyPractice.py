import numpy as np


# 1.数组定义、创建、运算和广播机制
data1 = np.arange(12).reshape(3,4)
print(data1)
print(type(data1))  # 结果为n维数组
print(data1.ndim)   # 数组维度的个数，2
print(data1.shape)  # 数组的维度，（3，4）
print(data1.size)   # 数组元素个数，12
print(data1.dtype)
print('\n')

data2 = np.array([1,2,3])   # 创建一维数组
print(data2)
data3 = np.array([[1,2,3], [4,5,6]])    # 创建一个二维数组
print(data3)
print(np.zeros((3,4)))  # 创建一个全0数组
print(np.ones((4,3)))   # 创建一个全1数组
print(np.empty((5,2)))  # 创建全空数组，其实每个值都是接近0的数（每次都重新随机）
print(np.arange(1,21,5))# 创建一维数组，1起步（闭区间），21结尾（开区间），步长为5（等差），默认步长为1，默认起始为0
print(np.array([1,2,3,4], float).dtype)   # 将数组内的数都转为浮点数float
print((np.ones((2,3), dtype='float64')))  # 另一种形式转float的方法
print('\n')

data4 = np.array([[1,2,3], [4,5,6]])
data5 = np.array([[1,2,3], [4,5,6]])
print(data4 + data5)    # 对应数字相加
print(data4 * data5)    # 对应数字相乘
print(data4 - data5)    # 对应数字相减
print(data4 / data5)    # 对应数字相除，变为浮点数
print('\n')

arr1 = np.array([[0],[1],[2],[3]])
print(arr1.shape)
arr2 = np.array([[1,2,3]])
print(arr2.shape)
print(arr1 + arr2)  # 广播，补充两个数组使其可以进行运算
print(arr1 + 1)
print('\n')


# 2.整数索引和切片
arr3 = np.arange(8)
print(arr3)
print(arr3[5])      # 获取索引为5的元素
print(arr3[3:5])    # 获取索引3-5的元素，包括3不包括5
print(arr3[1:5:2])  # 获取索引为1-5的元素，步长为2，包括1不包括5
arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr4)
print(arr4[1])      # 获取索引为1的元素，第1行的元素
print(arr4[0,1])    # 获取第0行第1列的元素
print(arr4[:2])     # 获取前2行的元素，不包括2
print(arr4[0:2, 0:2])   # 获取前两行前两列的元素
print(arr4[1, :2])  # 获取第1行上前2列的元素，不包括2
print('\n')

student_name = np.array(['Tom','Lily','Jack','Rose'])
print(student_name == 'Jack')   # 返回bool值


# 3.数组的转置
arr5 = np.arange(12).reshape(3,4)
print(arr5)
print(arr5.T)    # 转置矩阵
print('\n')
arr6 = np.arange(16).reshape((2,2,4))
print(arr6)
print(arr6.transpose(1,0,2))    # 将第一维和第二维交换位置
print(arr6.transpose(0,1,2))    # 不变，原来的顺序就是012
print(arr6.swapaxes(1,0))       # 用交换轴的方式，对数组进行转置，第一维和第二维交换
print('\n')


# 4.数组的运算
arr7 = np.array([4,9,16])
print(np.sqrt(arr7))        # 对每个元素开方
print(np.abs(arr7))         # 对每个元素取绝对值
print(np.square(arr7))      # 对每个元素取平方

x = np.array([12,9,13,15])
y = np.array([11,10,4,8])
print(np.add(x,y))   # 计算数组对应元素的和
print(np.multiply(x,y))        # 计算数组对应元素的乘积
print(np.maximum(x,y))         # 求两个数组对应元素的最大值，组成新的数组
print(np.greater(x,y))         # 返回bool值，若x对应元素大于y对应元素则返回True，反之为False

arr_x = np.array([1,5,7])
arr_y = np.array([2,6,8])
arr_con = np.array([True,False,True])
result = np.where(arr_con,arr_x,arr_y)  # 满足条件con，则输出x，否则输出y（比如True则为强制满足，输出就是x）
print(result)

arr8 = np.arange(10)
print(arr8.sum())   # 求和
print(arr8.mean())  # 求平均值
print(arr8.min())   # 求最小值
print(arr8.max())   # 求最大值
print(arr8.argmin())    # 求最小值的索引
print(arr8.argmax())    # 求最大值的索引
print(arr8.cumsum())    # 求元素的累计和
print(arr8.cumprod())   # 求元素的累计积

x1 = np.arange(1,16).reshape((3,5))
print(x1)
print(np.diff(x1,axis=1))    # 默认axis=1,同一行上取与前一列值的差值，最后会少一列
print(np.diff(x1,axis=0))    # 同一列上取与前一行值的差值，最后会少一行
print(np.floor([-0.6,-1.4,-0.1,-1.8,0,1.4,1.7]))    # 向左取整
print(np.ceil([-0.6,-1.4,-0.1,-1.8,0,1.4,1.7]))    # 向右取整

x2 = np.array([[1,0],[2,-2],[-2,1]])
print(x2)
print(np.where(x>0,x,0))    # 利用where实现了小于0的值用0代替，大于0的值不变

arr9 = np.array([[6,2,7],[3,6,2],[4,3,2]])
print(arr9)
print(arr9.sort())      # 对每一行的元素进行排序,（默认为行,axis=1）
print(arr9.sort(0))     # 对每一列的元素进行排序，0代表列上进行操作

arr10 = np.array([[1,-2,-7],[-3,6,2],[-4,3,2]])
print(arr10)
print(np.any(arr10 > 0))    # 监测所有元素中是否有一个大于0的，若有返回True
print(np.all(arr10 > 0))    # 监测所有元素中是否全部都大于0的，若有返回True

arr11 = np.array([12, 11, 34, 23, 12, 8, 11])
print(np.unique(arr11))     # 将其唯一化处理，重复的元素去掉，并按照从小到大顺序排列
np.in1d(arr11, [11, 12])    # 监测各个元素是否是后面的11、12中的任意一个，不是的话返回False，是的话返回True

arr_x1 = np.array([[1,2,3],[4,5,6]])
arr_y1 = np.array([[1,2],[3,4],[5,6]])
print(arr_x1.dot(arr_y1))       # 数组的乘法运算


# 5.np中的随机数种子,rand生成的数字是在0-1中随机
print(np.random.rand(3,3))      # 随机生成一个3*3的二维数组，0-1的随机数
print(np.random.rand(2,3,3))      # 随机生成一个2*3*3的三维数组，0-1的随机数
np.random.seed(0)      # 生成随机数种子，代号0，每次参数取0的随机数都相同
print(np.random.rand(5))
np.random.seed(0)       # 随机数种子代号相同的话，整个序列相同，但并不会全部显示，是程序选择显示其中的部分
print(np.random.rand(6))
np.random.seed(2)       # 不同的随机数种子代号生成的随机数不同
print(np.random.rand(5))
np.random.seed()        # 生成随机数种子，每次完全随机，因为没有种子代号
print(np.random.rand(5))

