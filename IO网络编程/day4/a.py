"""
你好,文件演示,donadoendz=cndXn

"""

# data = f.readline(100)
# print(data)
# def find01(a):
#     f = open("dict.txt", "r")
#     while True:
#         data = f.readline()
#         if not data:
#             break
#         if a in data:
#             return data
#     f.close()
#
# b = find01("little")
#
# print(b)

# with open("a.py","r") as f:
#     data = f.read()
#     print(data)

# file_name = input("请输入您要拷贝的文件名:")
# f= open("dict.txt","r")
# # f1= open("file_name","r")
# # data = f.readline()
# for line in f:
#     f1.write(line)
#
# # with open("file_name","r") as f:
# #     f.read()
file_name = input("请输入您要拷贝的文件名:")
f= open("dict.txt","r")
f2= open(file_name,"w")
# data = f.readline()
for line in f:
    f2.write(line)


print(f2)

