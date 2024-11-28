def num1():
    num = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
    use_num = {}

    for i in num:
        if i not in use_num:
            use_num[i] = 0
        else:
            use_num[i] += 1

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

    for i in range(0, len(input_dna), 3):
        codon = input_dna[i:i + 3]
        if len(codon) == 3:
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1

    print(codon_counts)
num3()

def num4():
    list_2d = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
    list_1d = []
    for i in list_2d:
        if type(i) == list:
            for j in range(len(i)):
                list_1d.append(i[j])
        else:
            list_1d.append(i)

    print(list_1d)
num4()