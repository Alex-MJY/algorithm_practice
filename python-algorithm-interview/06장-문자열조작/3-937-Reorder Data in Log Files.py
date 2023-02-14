class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key= lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
sol = Solution()
print(sol.reorderLogFiles(logs))

'''
문자열을 sorting(정렬)할 때 
sort()는 변수값 자체를 바꾸기 때문에 메모리를 신경 안써도 되지만
sorted()는 새로운 변수를 생성하기에 메모리를 더 소모한다.

sorting하는 기준이 다르거나 여러개일 경우 key 값으로 lambda함수를 할당해서
라인을 적게 적는 게 효율적이다.
'''