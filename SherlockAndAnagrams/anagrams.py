def are_anagrams(s1, s2):
    for c1, c2 in zip(sorted(s1), sorted(s2)):
        if c1 != c2:
            return False

    return True


def sherlockAndAnagrams(s):
    n = len(s)

    n_anagrams = 0
    for i_begin in range(n):
        for i_end in range(i_begin+1, n+1):
            ref_string = s[i_begin:i_end]
            m = len(ref_string)
            for j_begin in range(i_begin+1, n - m + 1):
                j_end = j_begin + m
                comp_string = s[j_begin:j_end]
                if are_anagrams(ref_string, comp_string):
                    n_anagrams += 1

    return n_anagrams


assert sherlockAndAnagrams("abba") == 4
assert sherlockAndAnagrams("abcd") == 0
