def is_palindrome(s):
    y = s[:(len(s)//2)]
    return y + y[::-1] == s if len(s) % 2 == 0 else y + s[len(s)//2] + y[::-1] == s

def is_palindrome2(s):
    if len(s) <= 1:
        return True

    y = s[:(len(s)//2)]
    if len(s) % 2 == 0:
        return y + y[::-1] == s
    else:
        return y + s[len(s) // 2] + y[::-1] == s

print(is_palindrome2("ahfa"))