file = open("CostData.txt")
data_list = file.readlines()

# words_1 =  [伙食 | 2019/11/18 $50-早餐
# words_2 =  "" | 伙食
# words_3 =  2019/11/18 | 50-早餐
# words_4 =  $50 | 早餐


def get_tag(text):
    cost_data = text
    # 拿取資料的tag
    words_1 = cost_data.split("]")
    words_2 = words_1[0].split("[")
    tag = words_2[1]
    words_3 = words_1[1].split(" $")
    date = words_3[0]
    words_4 = words_3[1].split("-")
    cost = int(words_4[0])
    return tag, date, cost

# tag_list = []
# date_list = []
# cost_list = []

# tag_list.append(tag)
# date_list.append(date)
# cost_list.append(cost)
# 字典儲存 => 將散亂的資料包成一筆

dict_list = []
for data in data_list:
    if data != "\n":
        tag,date,cost= get_tag(data)
        d = {"tag":tag,"date":date,"cost":cost}
        dict_list.append(d)

# print(dict_list[4]["date"])

# Q1 : 2019/11/20 的伙食花費
total_cost = 0
for d in dict_list:
    if d["date"] == "2019/11/20" and d["tag"] == "伙食":
        total_cost += d["cost"]
        print(total_cost)

# print(total_cost)

# Q:找出 早餐 當中花費最多的帳目,並印出其資訊
# 增加dict的新索引