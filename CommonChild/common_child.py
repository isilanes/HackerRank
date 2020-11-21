def find_pair(s1, s2, p1, p2):
    for i, c in enumerate(s1[p1:]):
        try:
            j = s2.index(c, p2)
            return p1 + i, j
        except ValueError:
            pass

    return None, None


def commonChild(s1, s2):
    word_indices1, word_indices2 = [], []
    mwi = []
    max_len = 0
    p1, p2 = 0, 0
    while True:
        pre1 = p1
        pre2 = p2

        p1, p2 = find_pair(s1, s2, p1, p2)

        if p1 is None:
            if not word_indices1:
                return max_len

            if len(word_indices1) > max_len:
                mwi = word_indices1
                max_len = len(word_indices1)


            p1 = word_indices1[-1] + 1
            word_indices1 = word_indices1[:-1]

            if len(word_indices2) > 1:
                p2 = word_indices2[-2] + 1
            else:
                p2 = 0

            word_indices2 = word_indices2[:-1]

        else:
            word_indices1.append(p1)
            word_indices2.append(p2)
            p1 += 1
            p2 += 1



assert commonChild("HARRY", "SALLY") == 2
assert commonChild("AA", "BB") == 0
assert commonChild("SHINCHAN", "NOHARAAA") == 3

with open("input01.txt") as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()

assert commonChild(s1, s2) == 15

with open("input10.txt") as f:
    s1 = f.readline().strip()
    s2 = f.readline().strip()

assert commonChild(s1, s2) == 1618
