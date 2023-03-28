class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_sub_lst, t_lst):
            for t_elem in t_lst:
                if t_elem in s_sub_lst:
                    s_sub_lst.remove(t_elem)
                else:
                    return False
            return True

        if not s or not t:
            return ''

        win_size = len(t)

        for size in range(win_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_sub = s[left : left+size]
                if contains(list(s_sub), list(t)):
                    return s_sub
        return ''
    
# time error O(n^2)