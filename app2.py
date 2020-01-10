file = open("CostData.txt")
data_list = file.readlines()

# words_1 =  [伙食 | 2019/11/18 $50-早餐
# words_2 =  "" | 伙食
# words_3 =  2019/11/18 | $50-早餐
# words_4 =  $50 | 早餐
def get_tag(text):
    cost_data = text
    # 拿取資料的tag
    words_1 = cost_data.split("]")
    # print(words[0])
    words_2 = words_1[0].split("[")
    tag = words_2[1]
    words_3 = words_1[1].split(" $")
    date = words_3[0]
    words_4 = words_3[1].split("-")
    # 濾掉換行符號 $
    cost = int(words_4[0])
    return tag,date,cost

# tag_list = []
# date_list = []
# cost_list = []

# Q1: 印出種類，時間與花費
# Q2: 印出食物的總共花費
total_food_cost = 0
for data in data_list:
    if data != "\n":
        tag,date,cost = get_tag(data)
        if tag == "伙食":
            total_food_cost += cost
        # 串在同一字串內
        print(f"種類:{tag} / 時間:{date} / 花費:{cost}")

print("食物的總共花費",total_food_cost)
