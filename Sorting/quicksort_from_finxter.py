def A(s):
    if len(s) < 2:
        return s
    else:
        return A([x for x in s[1:] if x < s[0]]) \
               + [s[0]] \
               + A([x for x in s[1:] if x >= s[0]])

print(A([2, 3, 1, 6, 4, 9]))
