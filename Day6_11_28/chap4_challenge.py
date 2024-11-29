def num1():
    num = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
    use_num = {}

    for i in num:
        if i not in use_num:
            use_num[i] = 0
        use_num[i] += 1

    print("{}에서 \n사용된 숫자의 종류는 {}개 입니다.".format(num,len(use_num)))
    print(use_num)

num1()

def num2():
    input_dna = input("염기 서열을 입력하세요 >> ").upper()

    dna = {
        'A': 0,
        'T': 0,
        'G': 0,
        'C': 0
    }

    for i in input_dna:
        if i in dna:
            dna[i] += 1

    for key in dna:
        print(f"{key}의 개수: {dna[key]}")

num2()

def num3():
    input_dna = input("염기 서열을 입력하세요 >> ")
    codon_counts = {}

    #teacher
    l = [input_dna[i:i+3] for i in range(0,len(input_dna),3) if len(input_dna[i:i+3])==3]
    for i in l:
        if i not in codon_counts:
            codon_counts[i] = 0
        codon_counts[i] += 1
    print(codon_counts)

    #my solved
    # for i in range(0, len(input_dna), 3):
    #     codon = input_dna[i:i + 3] #키를 추가하는 활동
    #     print(codon_counts)
    #     if len(codon) == 3:
    #         if codon in codon_counts:
    #             codon_counts[codon] += 1
    #         else:
    #             codon_counts[codon] = 1

    for key, element in codon_counts.items():
        print("코돈 {} 은 = {}개".format(key,element))

    for key in codon_counts:
        print(f"{key}의 개수 = {codon_counts[key]}")

    print(codon_counts)

num3()

def num4():
    list_2d = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
    list_1d = []
    for i in list_2d:
        if type(i) == list:
            for j in range(len(i)):
                list_1d.append(i[j])
            #equals
            # for j in i:
            #     list_1d.append(j)
        else:
            list_1d.append(i)

    print(list_1d)
num4()