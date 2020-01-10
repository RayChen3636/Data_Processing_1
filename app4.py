file = open("CostData.txt")
data_list = file.readlines()

# words_1 = [伙食 | 2019/11/18 $50-早餐
# words_2 =  "" | 伙食
# words_3 =  2019/11/18 | 50-早餐
# words_4 =  $50 | 早餐

def get_tag(text):
    cost_data = text
    # 拿取資料的tag
    words = cost_data.split("]")
    words_2 = words[0].split("[")
    tag = words_2[1]
    words_3 = words[1].split(" $")
    date = words_3[0]
    words_4 = words_3[1].split("-")
    cost = int(words_4[0])
    if len(words_4)<2:
        words_4.append("無")
        remark = str(words_4[1])
    else:
        remark = str(words_4[1])
    return tag, date, cost, remark

# tag_list = []
# date_list = []
# cost_list = []
# tag_list.append(tag)
# date_list.append(date)
# cost_list.append(cost)

# 字典儲存 => 將散亂的資料包成一筆
dict_list1 = []

for data in data_list:
    if data != "\n":
        tag,date,cost,remark= get_tag(data)
        d = {"tag":tag,"date":date,"cost":cost,"remark":remark}
        dict_list1.append(d)
        #print(dict_list1)
# print(dict_list[4]["date"])

# Q1: 2019/11/20 的伙食花費
total_cost = 0
for d in dict_list1:
    if d["date"] == "2019/11/20" and d["tag"] == "伙食":
        total_cost += d["cost"]
        #print(total_cost)
        #print(d["remark"])

print(total_cost)

# Q2: 找出 早餐 當中花費最多的帳目,並印出其資訊
#  增加dict的新索引
dict_list2 = []
for d1 in dict_list1:
    if d1["remark"] == ("早餐\n"):
        dict_list2.append(d1["cost"])
        print(d1["cost"])
print("全部的早餐:",dict_list2)
print("花費最多的早餐:",max(dict_list2))

