array = [123, 321, 654, "문자열", True, False]

print(array[-3][0]) #이중 인덱싱

array.append("피곤")
array.insert(1,"집갈래")

print(array)

del array[0]
print(array)

array.pop(0)
print(array)