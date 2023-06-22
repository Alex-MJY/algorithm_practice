# using lambda + operator
# isdigit() : 숫자 여부 / isalpha() : 알파벳 여부 / isalnum() : 숫자 + 알파벳 여부
class Solution:
    def reorderLogFiles(self, logs: list]) -> list:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # sorting with lambda
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits