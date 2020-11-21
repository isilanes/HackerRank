def highestValuePalindrome(s, n, k):
    odd_len = len(s) % 2
    if odd_len:
        half = (len(s) - 1) // 2
    else:
        half = len(s) // 2

    left = s[:half]
        
    differents = []
    largests = []
    for i, cl in enumerate(left):
        cr = s[-i-1]
        if cl != cr:
            m = max(int(cl), int(cr))
            differents.append(i)
            largests.append(m)
            
    if len(differents) > k:
        return -1
    
    as_array = list(s)
    for index, value in zip(differents, largests):
        as_array[index] = str(value)
        as_array[-index-1] = str(value)

    remaining = k - len(differents)
    for i, cl in enumerate(as_array[:half]):
        if remaining < 1:
            break

        if cl == "9":
            continue

        if i in differents and remaining > 0:
            as_array[i] = "9"
            as_array[-i-1] = "9"
            remaining -= 1

        elif remaining > 1:
            as_array[i] = "9"
            as_array[-i-1] = "9"
            remaining -= 2

    if remaining > 0 and odd_len:
        as_array[half] = "9"

    return "".join(as_array)


print("3943", "->", highestValuePalindrome("3943", 0, 1))
print("092282", "->", highestValuePalindrome("092282", 0, 3))
print("0011", "->", highestValuePalindrome("0011", 0, 1))
print("0921282", "->", highestValuePalindrome("0921282", 0, 3))
print("0921282", "->", highestValuePalindrome("0921282", 0, 4))
print("0921282", "->", highestValuePalindrome("0921282", 0, 5))
print("0921282", "->", highestValuePalindrome("0921282", 0, 6))

with open("input10.txt") as f:
    _, k = f.readline().split()
    k = int(k)
    s = f.readline()

with open("output10.txt") as f:
    expected = f.readline()

out = highestValuePalindrome(s, 0, k)

assert out == expected
