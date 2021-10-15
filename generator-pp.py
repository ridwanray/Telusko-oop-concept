

# def topTen():
#     yield  3
#     yield  4
#     # yield  5
#     # yield  6

# values = topTen()

# print(next(values))
# print(next(values))



def topTen():

    n = 1
    while n<= 10:
        sq = n*n
        yield sq
        n +=1

values = topTen()
# print(values)
# print(next(values))
# print(next(values))
for i in values:
    print(i)


