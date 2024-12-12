def flatten(data):
    output = []
    for i in data:
        if type(i) is list:
            output += flatten(i)
        else:
            output.append(i)

    return output


example = [1, 2, [3, 4, 5], [6, [7, 8], 9], 10]
print(flatten(example))
