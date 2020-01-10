#  Q : 找出 早餐 當中花費最多的帳目,並印出其資訊
#  增加dict的新索引
from typing import List

file = open("CostData.txt")
data_list = file.readlines()

# words_1 =  [伙食 | 2019/11/18 $50-早餐
# words_2=  [ | 伙食
# words_3 =  2019/11/18 | 50-早餐
# words_4 =  $50 | 早餐

def get_tag_date_cost(text):
    cost_data = text
    # 拿取資料的tag
    words = cost_data.split("]")
    words_2 = words[0].split("[")
    tag = words_2[1]
    words_3 = words[1].split(" $")
    date = words_3[0]
    words_4 = words_3[1].split("-")
    # print(len(words_4))
    event = ""
    if len(words_4) > 1:
        # 有事件資料 words_4[1] => 事件名稱
        event = words_4[1]
    cost = int(words_4[0])
    return tag, date, cost, event

class Receipt:
     def __init__(self, tag: str, date: str, cost: int, event: str):
        self.tag = tag
        self.date = date
        self.cost = cost
        self.event = event
     def print_receipt(self):
        print(f'[{self.tag}] {self.date} ${self.cost}')
     # 有問題?
     def fix_tag(self,t):
        self.tag = t

receipt_list = []
for data in data_list:
    if data != "\n":
        tag, date, cost, event = get_tag_date_cost(data)
        event = event.replace("\n", "")
        r = Receipt(tag, date, cost, event) #生成 Receipt 物件
        receipt_list.append(r)
        #print(receipt_list)



# Q: 查詢日期,並輸出當日消費總額
#date_input = input("請輸入查詢日期:")
#total_cost = 0
#for r in receipt_list:
   # if r.date == date_input:
       # total_cost += r.cost
#print(total_cost)

# Q: 制定函式 (輸入字典), 輸出原始資料
# 有問題? 已解決
def print_info(cost_dict:dict):
    s = f'[{cost_dict["tag"]}]{cost_dict["date"]} ${cost_dict["cost"]}'
    if cost_dict["event"] != "":
        s = s + "-" + cost_dict["event"]
    print(s)

# Q: 制定函式 (輸入Receipt物件), 輸出原始資料
def print_receipt(receipt:Receipt):
    s = f'{receipt.tag} {receipt.date} $ {receipt.cost}'
    if receipt.event != "":
        s = s + "-" + receipt.event
    print(s)

print_receipt(receipt_list[1])

# tag_input = input("請輸入查詢類別:")
# for r in receipt_list:
    #if r.tag == tag_input:
      #  r.print_receipt()

# Q : 找出花費在50~100(含)的  Receipt 物件,並印出原始格式
#for r in receipt_list:
    #if r.cost>=50 and r.cost<=100:
        #print_receipt(r)

# TypeHint
# print(high_cost_dict)
# num:int = 12345
# num ="str"
# num_list:List[int] = []
# num_list.append("123")