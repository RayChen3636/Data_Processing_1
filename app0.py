# file = open("CostData.txt")
# data = file.read()
# print(data)

# file = open("CostData.txt")
# data_list = file.readlines()
# for  data in data_list:
#     print(data)

#----------------------------------
# Q 試試看, 擷取出tag / 日期 / 花費
# 編碼問題!!!

# [伙食]2019/11/18 $50-早餐
cost_data = "[伙食]2019/11/18 $50-早餐"

# 拿取資料的tag
words = cost_data.split("]")
# print(words[0])

words_2 = words[0].split("[")
print("tag:",words_2[1])
# 拿出日期
words_3 = cost_data.split("$")
# print(words_3)
words_4 = words_3[0].split("]")
print("日期:", words_4[1])
# 拿出花費
words_5 = words_3[1].split("-")
# words_4 = words_3[1].split("]")
# print(words_4[0])
print("花費:", words_5[0])

#----------------------------------
