mina = {
    "name" : "박민환",
    "sex" : "남",
    "age" : 26,
    "job" : "student"
}

print(mina)

mina["job"] = "rich"

print(mina["job"])

print(type(mina))

myState = {}

myState["지금"] = "개피곤"
myState["12시이후"] = "혈당스파이크로 더피곤"

print(myState)

del myState["12시이후"]
print(myState)