import json

def config(value):
    with open("config.json", 'r', encoding='utf-8 sig') as file:
        data = json.load(file)
        token = data['bot']['token']
        category = data['values']['guild2']['category']
        guild = data['values']['guild']
        guild2 = data['values']['guild2']['id']
        if value == "token":
            return token
        elif value == "category":
            return category
        elif value == "guild":
            return guild
        elif value == "id":
            return guild2
def user_data(value):
    with open("datas/user_data.json", 'r', encoding='utf-8 sig') as file2:
        data2 = json.load(file2)
        if value == "user_data":
            return data2
def black_user(value):
    with open("datas/black-lists.json", 'r', encoding='utf-8 sig') as file3:
        data3 = json.load(file3)
        if value == "black_user":
            return data3['black-user-id']