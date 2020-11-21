CASES = (
    ("input02.txt", "YES"),
    ("input07.txt", "YES"),
    ("input18.txt", "YES"),
)

def isValid(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    items_of = {}
    for c, f in freq.items():
        items_of[f] = items_of.get(f, [])
        items_of[f].append(c)

    res = sorted([(f, len(e)) for f, e in items_of.items()])

    if len(res) == 1:
        return "YES"

    if len(res) > 2:
        return "NO"

    (f_small, n_small), (f_big, n_big) = res

    if n_small == 1 and f_small == 1:
        return "YES"

    if (f_big == f_small + 1) and n_big == 1:
        return "YES"

    return "NO"


for fn, expected in CASES:
    with open(fn) as f:
        string = f.readline()
        
    assert isValid(string) == expected
