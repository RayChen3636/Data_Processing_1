file = open("CostData.txt")
data_list = file.readlines()
print(data_list)

# words_1 =  [伙食 | 2019/11/18 $50-早餐
# words_2 =  "" | 伙食

def get_tag(text):
    cost_data = text
    # 拿取資料的tag
    words_1 = cost_data.split("]")
    # print(words[0])
    words_2 = words_1[0].split("[")
    # 輸出tag
    # print(words_2[1])

for data in data_list:
    if data != "\n":
        get_tag(data)
