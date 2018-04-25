for i in [1, 2, 3, 4]:
    for j in [1, 2, 3, 4]:
        pass


apart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304],
    [401, 402, 403, 404]
]

for floor in apart:
    for room in floor:
        print("Newspaper derivery: %d " % room)
