def power(item):
    return item * item


def under_3(item):
    return item < 3


list_input_a = [1, 2, 3, 4, 5,6,7,8,9]
output_a = map(power, list_input_a)
print(output_a)
print(list(output_a))

output_b = filter(under_3,list_input_a)
print(output_b)
print(list(output_b))

#filter map lamda 사용
#lista [1,23]
#3의 배수만 뽑아서 그수를 제곱한 리스트를 리턴받아 출력
# 3의 배수만 필터링하고 그 수를 제곱하는 코드

output = map(lambda x: x * x, filter(lambda x: x % 3 == 0, list_input_a))

# 결과 출력
print(list(output))

