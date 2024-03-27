WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
def decode(string, n):
    st = ""
    for i in range(n,len(string),n*2):
        st += string[i:i+n]
    return st


print(decode("#P#y#t#h#o#n",1))
print(decode("AxYLet1x3’s T74codaa7e!",3))


def  pattern_count(string, pat):
    count = 0
    for i in range(len(string)):
        if pat == string[i:i+len(pat)]:
            count += 1
    return count


print(pattern_count("bcabcabca", "abc"))
print(pattern_count("aaaa", "aa"))
print(pattern_count("A long time ago in a galaxy far, far away...", "a"))
print(pattern_count("If you must blink, do it now.", "code"))


def palindrome(string):
    lst = str(string)
    newlist = str.lower(lst)
    import string
    nonnewlist = newlist.translate(str.maketrans('', '', string.punctuation))
    for i in range(len(nonnewlist)):
        a = nonnewlist[-len(nonnewlist)+i]
        b = nonnewlist[-1-i]
        if a == b:
            return True
            i += 1
        else:
            return False


print(palindrome("RacecaR"))
print(palindrome("66racecar77"))
print(palindrome("Racecar"))
print(palindrome("Madam, I’m Adam"))
print(palindrome("#4Satire: Veritas4"))
