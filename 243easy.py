with open("243easyinput", "r") as f:
    input = [int(line) for line in f.readlines()]


def abundeficient(num):
    factorsum = num
    for ii in range(1, num):
        if (num % ii) == 0:
            factorsum += ii

    return factorsum - (num * 2)

for num in input:
    perfection = abundeficient(num)
    if perfection > 0:
        print("{} abundant by {}".format(num, perfection))
    elif perfection < 0:
        print("{} deficient by {}".format(num, abs(perfection)))
    else:
        print("{} perfect".format(num))