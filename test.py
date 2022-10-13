sql_origin = {
    "zong_sdjs": {
        "name": "审贷件数",
        "sql": "a",
        "results": 0,
    },
    "zong_sxtgjs": {
        "name": "授信通过件数",
        "sql": "b",
        "results": 0,
    },
    "zong_yxsqjs": {
        "name": "用信申请件数",
        "sql": "c",
        "results": 0,
    }
}

print(type(sql_origin.items()))

# print(list(sql_origin.items()))
# print(type(list(sql_origin.items())[0][1]))
#
# for  index,value in enumerate(sql_origin.items()):
#     print()
