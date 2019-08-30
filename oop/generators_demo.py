def even_nums(start, end):
    start = start if start % 2 == 0 else start + 1
    for n in range(start, end + 1, 2):
        yield n



g = even_nums(10, 20)
print(type(g))
for v in g:
    print(v)

g = even_nums(10,14)

print( next(g))
print( next(g))
print( next(g))
print( next(g))

