#print(int(input("인치 입력:")) * 2.54,"cm임")

h,w = input("키와 몸무게 입력:").split()
bmi = int(w)/((int(h)/100)**2)
print("bmi=",format(bmi,".2f"))

a = input(">>:")
b = input(">>:")
print(a)
print(b)
a,b = b,a
#튜플안쓰기
"""c = a
a = b
b = c
"""
print(a)
print(b)