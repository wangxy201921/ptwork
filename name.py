name = "dhaodhoadD ahodhoa"
print(name.title())#首字母大写并且其他字母转为小写
print(name.upper())#全员大写
print(name.lower())#全员小写
time = 1
first_name = 'haodh'
last_name='ahohoa'
full_name= first_name+last_name
no_name= f"{first_name}{last_name}" #f"xxxxxx，{}"

print(full_name)
print(no_name)

#制表符与换行 \n\t \t对应大小为四个小写英文字母
print("daohdaodh\n\tadhoahd\n\tahdoahdo\n\taodhao") 

#Python对引号标记出来的字符串内的空白敏感
favorite_language = ' Python对引号标记出来的字符串内的 空白敏感 '
print(favorite_language.rstrip())#尾巴
print(favorite_language.strip())#两端
print(favorite_language.lstrip())#开头

3+2
3 ** 2 == 9

#变量赋值
x,y,z=1,2,3
print(x,y,z)



bicyle = ['ducadi','dhaodhoadD','dagdo_123']
print(bicyle)
print(bicyle[0])
bicyle[2]='adogi'#根据索引修改表格内容
message=f"my favorite bicyle is {bicyle[0].title()}"
print(message)
print(bicyle[2])#索引从0开始数 第n个元素的正续索引为n-1

bicyle.append('suzuki')#不能用带list.append（‘’）来为新的列表或者变量赋值
print(bicyle)
bicyle2 = bicyle.append('ahhu') #无效的赋值#会返回none
print(bicyle2)

#append可以用于空表添加元素
cun =[]
cun.append('cun1')
cun.append('cun2')
cun.append('cun2')#list 内的元素值不唯一 且存在顺序
print(cun)

cun.insert(-1,88) #insert 同样不可以赋值，索引号用于放置需要插入的元素，原有元素右移
print(cun)

#删除 
del cun[2] #操作语句,纯操作，不可赋值  不可保存删除内容[cun1,cun2,cun2,88]中删掉88
print(cun)

#pop 删除末尾元素 ，可以用于赋值，但在删除操作这一行未赋值则丢失此次操作的数值 可在pop(0)内增加索引从而弹出所需元素
cun.pop()  #cun1，cun2，cun2中删掉cun2 且未将最后一个cun2保存到变量中
print(cun)
cun4 = cun.pop() #cun1，cun2中删掉后者并保存到cun4这个变量中去
print(cun)
print(cun4)

last_own = cun[0] 
print(last_own)

#remove 基于值的删除操作，操作执行不可赋值,但因为是基于值的操作，可以先将对应的值赋值给某一变量，然后在remove中引用变量的值来删除列表内的元素，而变量则保留了被删除的元素的对应值
bicyle5 = 'ducadi'
bicyle.remove(bicyle5)
print(bicyle)
print(bicyle5) 
#remove 只删除第一个值  后面的值需要依靠循环来完成

#sort带来的排序修改是永久的
bicyle.sort()
print(bicyle)
bicyle.sort(reverse=True) #倒序 True是必须首字母大写
print(bicyle)
print(sorted(bicyle))
print(bicyle)

tad =['dao','qiang','fuck','bert']
print(sorted(tad,reverse=True))#首字母倒序展示
print(tad)

#原顺序 倒序展示 永久修改 不可赋值
tad.reverse()
print(tad)
print(len(tad))

for x in range(1,10):#range在循环中遇到最后一个数是停止操作 因为此range（1，n）只运行n-1次
	print(x)

magicians = ['alice','david','carolina']
for  magician in magicians:
	print(f'{magician.upper()},that\'s a good show')
	print(magician+'that\'s a good show')

#list（）将range（）生成的数变为列表,直接打印的话即为横向列表
print(list(range(11)))

#range内的参数(起始数，尾数，步长)
list1=list(range(1,10,2))
print(list1)

squares=[]
for value in range(1,10):
	squares.append(value**2)
print(squares)

print(sum(squares))
print(min(squares))
print(max(squares))

#解析 快速生成数表
thr = [value ** 3 for value in range(1,11)]
print(thr)

print(thr[0:9]) #此处的索引还是少一个，只输出到索引为8的位置上
print(thr[:9])

print(thr[:-2:2])#[1:3:2][起始索引：终止索引：步长]
#列表切片可以当做列表直接使用

for x in thr[0:8:3]:
	print(x)

tad =['dao','qiang','fuck','bert']
print(sorted(tad[0:2],reverse=True))#首字母倒序展示
print(tad)





