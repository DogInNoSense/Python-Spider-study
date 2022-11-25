import json
import jsonpath

# obj = json.load(open('book_content.json', 'r', encoding='utf-8'))
# name_list = jsonpath.jsonpath(obj, '$..id')
# # name_list = jsonpath.jsonpath(obj, '$..name')
# print(name_list)
# name_list1 = jsonpath.jsonpath(obj, '$..regionName')
# # name_list = jsonpath.jsonpath(obj, '$..name')
# print(name_list1)

obj = json.load(open('book_content_test.json', 'r', encoding='utf-8'))
# name_list = jsonpath.jsonpath(obj, '$..id')
name_list = jsonpath.jsonpath(obj, '$..name')
price_list = jsonpath.jsonpath(obj, '$..price')

with open('name.txt', 'w', encoding='utf-8') as fp:
    for index in range(len(name_list)):
        fp.write(name_list[index] + '\n')
print(name_list)
