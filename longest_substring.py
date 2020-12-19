def longest_substring(q1,q2):
    s1, s2, long, common = q2, q1, '', ''
    if len(q1) > len(q2): s1, s2 = q1, q2
    for i in range(1, len(s1)+len(s2)):
        for a,s in zip(s1[:i][-(i%(len(s1))):][-len(s2):],s2[-i:]):
            if a == s: common += a
            elif a != s and common != '': long, common = max(long, common, key = len), ''
        if common != '': long,common = max(long, common, key = len), ''
    return long
