# class stu:
#     def __init__(self):
#         self.name='박민환'
#     def answer(self,q):
#         print("네, 이해됐습니다.")
#
#
#
# class jun(stu):
#     def answer(self,q):
#         print("질문은: ",q)
#         print("전 이해가 안됩니다.")
#
#
# p=stu()
# print(p.name)
#
# p.answer("이해되나여?")
# k=jun()
# k.answer("이해되나여?")

num = [1, 2, 3, 4]
alph = ['A', 'B', 'C']

for i, j in zip(num, alph):
    print(i, j)
