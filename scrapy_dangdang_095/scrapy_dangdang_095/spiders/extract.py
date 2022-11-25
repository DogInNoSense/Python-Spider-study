import json

with open('book.json', 'r', encoding='utf-8') as fp:
    # 读取文件
    print(type(fp))
    # print(fp.read())
    book_str = str(fp.read())
    print(type(book_str))
    book_list = list(book_str)
    # print(book_str)
    # print(len(book_str))
    # eg2：组成[{}, {}] 格式
    # 格式  （自动化参数化需要的数据格式）
    for index in range(len(book_list)):
        # print(index)
        book_list[0] = '[{'
        if book_list[index] == '}' and index != len(book_list) - 1:
            book_list[index] = '},'
        if book_list[index] == "'":
            book_list[index] = '"'
        book_list[len(book_list) - 1] = '}]'
    # 重新转换成原来的字符串形式
    book_str = ''.join(book_list)
    print(book_str)
    for index in range(len(name_list)):
     with open('book_content_test.json', 'w', encoding='utf-8') as fp:
        fp.write(book_str)

    fp.close()


    # result = json.load(fp)
    # print(result.get('name'))  # 书名
    # print(result.get('price'))  # 价格
    # print(result.get('src'))  # 图片链接
    # print(type(result))

    # 获取城市
    # print(result.get('address').get('city'))  # 上海
