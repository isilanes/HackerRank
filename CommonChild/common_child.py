def find_pair(s1, d1, p1, p2):
    for i, c in enumerate(s1[p1:]):
        for j in d1[c]:
            if j >= p2:
                return p1 + i, j

    return None, None


def build_dict(s1, s2):
    output = {}
    for c in s1:
        if c not in output:
            output[c] = []
            p2 = 0
            while True:
                try:
                    p2 = s2.index(c, p2)
                    output[c].append(p2)
                    p2 += 1
                except ValueError:
                    break

    return output


def commonChild(s1, s2):
    d1 = build_dict(s1, s2)

    word_indices1, word_indices2 = [], []
    max_len = 0
    p1, p2 = 0, 0
    while True:
        p1, p2 = find_pair(s1, d1, p1, p2)

        if p1 is None:
            if not word_indices1:
                return max_len

            if len(word_indices1) > max_len:
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


def test1():
    assert commonChild("HARRY", "SALLY") == 2
    assert commonChild("AA", "BB") == 0
    assert commonChild("SHINCHAN", "NOHARAAA") == 3


def test_fn(fn, expected):
    with open(fn) as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()

    assert commonChild(s1, s2) == expected


if __name__ == "__main__":
    test1()
    test_fn("input01.txt", 15)
    #test_fn("input10.txt", 1618)
