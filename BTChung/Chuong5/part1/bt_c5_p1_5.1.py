def add(L, x, k):
    if k >= 0:
        if k < count(L):
            L[:] = L[:k] + [x] + L[k:]
        else:
            L += [x]

# # version of add() which can handle negative input for k:
# def add(L, x, k):
#     if k < count(L) and k > -1 - count(L):
#         L[:] = L[:k] + [x] + L[k:]
#     elif k >= count(L):
#         L[:] += [x]
#     else:
#         L[:] = [x] + L[:] 

def search(L, x):
    indexes = []
    for i in range(count(L)):
        if L[i] == x:
            add(indexes, i, count(indexes)) # indexes.append(i)
    if count(indexes) == 0:
        return None
    return indexes

def delete(L, x):
    i = 0
    while i < count(L):
        if L[i] == x:
            L = L[:i] + L[i+1:]
        else:
            i += 1

def count(L):
    count = 0
    for _ in L:
        count += 1
    return count

def update(L, x, y):
    for i in range(count(L)):
        if L[i] == x:
            L[i] = y

# test bai 1 - add()
def bai1_add():
    L = [1, 2, 3, 4]
    add(L, 'x0', 0)
    print(L)
    add(L, 'x1', 1)
    print(L)
    add(L, 'x8', 8)
    print(L)
    add(L, 'x-1', -1)
    print(L)
    add(L, 'x-3', -3)
    print(L)
    add(L, 'x-15', -15)
    print(L)

# test bai 2 - search()
def bai2_search():
    L = [1, 2, 2, 3, 2, 4, 2]
    print(search(L, 2))
    print(search(L, 'x'))

# test bai 3 - delete()
def bai3_delete():
    L = [1, 2, 3, 2, 4]
    delete(L, 2)
    print(L)

# test bai 4 - count()
def bai4_count():
    L = [1, 2, 3, 4]
    print(count(L))

# test bai 5 - update()
def bai5_update():
    L = [1, 2, 3, 2, 4]
    update(L, 2, 'x')
    print(L)

bai1_add()
bai2_search()
bai3_delete()
bai4_count()
bai5_update()


