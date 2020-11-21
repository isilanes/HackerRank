REF = "hackerrank"


def hr_in_string(s):
    if not s:
        return "NO"

    i_seeking = 0
    for c in s:
        if c == REF[i_seeking]:
            i_seeking += 1

        if i_seeking == len(REF):
            return "YES"

    return "NO"


if __name__ == "__main__":
    with open("input01.txt") as f:
        n = int(f.readline())
        for i in range(n):
            s = f.readline()
            result = hr_in_string(s)
