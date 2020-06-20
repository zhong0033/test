#13.罗马数字转整数
def romanToInt(s):
    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    a = 0
    if len(s) == 1:
        return dic[s]
    a += dic[s[0]]
    for i in range(1,len(s)):
        if dic[s[i]] > dic[s[i-1]]:
            a = a - dic[s[i-1]] * 2 + dic[s[i]]
        else:
            a += dic[s[i]]
    return a

print(romanToInt('IV'))

#