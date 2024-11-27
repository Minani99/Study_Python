output = ""
for i in range(1,10):
    for j in range(0,i):
        output += "*"
    output+= "\n"
print(output)

for i in range(1,10):
    for j in range(14,i,-1):
        output+= " "
    for k in range(0,2*i-1):
        output+='*'
    output +="\n"

print(output)