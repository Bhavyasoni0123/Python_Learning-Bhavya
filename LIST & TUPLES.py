# LISTS IN PYTHON - 
marks = [90, 70, 80, 100, 20]
print(marks)
print(type(marks))
print(marks[0])
print(marks[4])
print(len(marks))
# STRINGS ARE IMMMUTABLE WHILE LISTS ARE MUTABLE -
marks[0] = 100
print(marks)
# LIST SLICING -
print(marks[1:4])
print(marks[::2])
# LIST METHODS 
marks.append(75)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(3, 85)
print(marks)
marks.remove(85)
print(marks)
marks.pop(0)
print(marks)
# TUPLES IN PYTHON -
tup = (1, 2, 3, 4, 5, 1)
print(tup)
print(type(tup))
# SLICING TUPLES -
print(tup[1:4])
# METHODS IN TUPLES -
print(tup.index(1))
print(tup.count(1))
