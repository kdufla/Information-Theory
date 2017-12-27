
#from DecodingTable import decoding_table
#from Encode import encode
from ParityCheck import parity_check
#from Decode import decode


def test_decoding_table():
    from os import listdir
    examples = [word for word in listdir('Tests/C') if word.endswith('.dat')]
    print("Decoding Table")
    for example in examples:
        dat = 'Tests/C/' + example[:-4] + ".dat"
        num = 'Tests/C/' + example[:-4] + ".num"
        res = 'Tests/C/' + example[:-4] + ".res"

        decoding_table(dat, num, res)
        print("{} correct".format(example))


def test_encode():
    from os import listdir
    from filecmp import cmp
    from time import time
    examples = [word for word in listdir('Tests/D') if word.endswith('.dat')]
    print("ENCODE")
    for example in examples:
        code = 'Tests/D/' + example[:-4] + ".code"
        dat = 'Tests/D/' + example[:-4] + ".dat"
        ans = 'Tests/D/' + example[:-4] + ".ans"
        res = 'Tests/D/' + example[:-4] + ".res"
        cur_time = time()
        encode(code, dat, res)
        cur_time = time() - cur_time
        print("{} - {}, time - {}".format(example, cmp(res, ans), cur_time))


def test_parity_check():
    from os import listdir
    examples = [word for word in listdir('B') if word.endswith('.dat')]
    print("PARITY CHECK")
    for example in examples:
        skip = False
        dat = 'B/' + example[:-4] + ".dat"
        res = 'B/' + example[:-4] + ".res"
        parity_check(dat, res)

        data = open(res, 'r').read().split("\n")
        n, k = (int(x) for x in data[0].split())
        parity = [list(s) for s in data[1:k + 1]]

        data = open(dat, 'r').read().split("\n")
        n, k = (int(x) for x in data[0].split())
        grid = [list(s) for s in data[1:k + 1]]

        if len(parity) != (n - k):
            print("{} length not correct".format(example))
        else:
            for row1 in parity:
                if skip:
                    break
                for row2 in grid:
                    x = 0
                    for i in range(n):
                        x += 1 if row1[i] == row2[i] == '1' else 0
                    if x % 2:
                        skip = True
                        break
            if skip:
                print("{} parity not correct".format(example))
            else:
                print("{} correct".format(example))


def test_decode():
    from os import listdir
    from filecmp import cmp
    examples = [word for word in listdir('Tests/C') if word.endswith('.dat')]
    print("DECODE")
    for example in examples:
        code = 'Tests/C/' + example[:-4] + ".res"
        dat = 'Tests/E/' + example[:-4] + ".dat"
        ans = 'Tests/E/' + example[:-4] + ".ans"
        res = 'Tests/E/' + example[:-4] + ".res"
        decode(code, dat, res)
        print("{} - {}".format(example, cmp(res, ans)))


funcs = [
     test_parity_check,
     # test_encode,
     # test_decoding_table,
     # test_decode
]


if __name__ == '__main__':
    for func in funcs:
        func()
