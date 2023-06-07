# 原始数组
my_array = [
    {"list_id": 3, "other_key": "value3"},
    {"list_id": 1, "other_key": "value1"},
    {"list_id": 2, "other_key": "value2"}
]

# 使用sorted函数进行排序，根据字典中的'list_id'键进行排序
sorted_array = sorted(my_array, key=lambda x: x['list_id'])



print(sorted_array)
