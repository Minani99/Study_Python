mina = {
    "name" : "박민환",
    "sex" : "남",
    "age" : 26,
    "job" : "student"
}

value = mina.get("존재하지 않는 키")
print("값:",value)

if value == None:
    print('없음')