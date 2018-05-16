# 전체 아파트 세대
apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
# 제외할 아파트 세대
arrears = [101, 203, 301, 404]

# 아파트 전체 세대
for floor in apart:
    for room in floor:
        if(room in arrears):
            continue
        else:
            print(room,'is delivered')