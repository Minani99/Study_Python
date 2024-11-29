s1 = set([1,2,3,3,5,1,2,8])
print(s1)

s2=set("hello")

print(s1)
print(s2)

#set 데이터 타입은 중복 x
#set 데이터 타입은 순서가 없는 데이터 타입임
#중복제거 용도로 한번 set변환했다가 다시 다른 데이터 타입으로 변환
#인덱스 사용 불가 >> 순서가 없기때문
#딕셔너리도 순서 없음

li = list(s1)
print(li)

t1 = tuple(s1)
print(t1)
print(t1[0])

s3 = set([4,1,2,3,4,5,6,7,8,9])

#교집합
print(s1&s3)
print(s1.intersection(s3))

#합집합 - 중복은 제거
print(s1|s3)
print(s1.union(s3))

#차집합
print(s1-s3)
print(s3-s1)
print(s1.difference(s3))
print(s3.difference(s1))

#집합에 추가
s1.add(100)
print(s1)
#여러 값 추가
s1.update([500,600,700])
print(s1)
#집합 데이터 제거
s1.remove(500)