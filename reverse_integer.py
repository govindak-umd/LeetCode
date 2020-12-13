class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        if x > 0:
            rev_x = ''
        else:
            rev_x = '-'
        for num in reversed(range(len(str_x))) :
            rev_x += str_x[num]
        rev_x = str(int(rev_x))
        if -2**31> int(x) or -2**31> int(rev_x) or int(x) > 2**31-1 or int(rev_x) > 2**31-1:
            return 0
        return rev_x