output = ""

line = int(input("행의 개수 입력>>"))
for i in reversed(range(0,line)):
    for j in range(i,(line-1)):
        output+= " "
    output+="*"
    for k in range(1,2*i):
        output+='#'
    if i > 0:
        output += "*"
    output +="\n"

print(output)

# for i in range(1,line+1):
#     for j in range(0,(i-1)):
#         output+= " "
#     output+="*"
#     for k in range(2*(line-1),-1,-1):
#         if k==0 or k==2*(line-i):
#             output+="*"
#         else:
#             output+="#"
#     output +="\n"
#
# print(output)