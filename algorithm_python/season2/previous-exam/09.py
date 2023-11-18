# 문자열 압축 (p323, p516)
'''
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘 구현.
"aabbaccc"의 경우 "2a2ba3c"로 표현 가능. 반복되는 문자가 적은 경우 압축률이 낮다는 단점 존재.
단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하려고 한다.
"abcabcdede"의 경우 2개 단위로 잘라서 압축하면 "abcabc3de"가 되지만 3개 단위로 압축하면 "2abcdede"가 되어 더 짧게 압축 가능.
문자열 s가 주어질 때 1개 이상 단위로 문자열을 잘라 압축하여 가장 짧은 것의 길이를 return 하도록 solution함수를 완성해라.
'''
# 입력으로 주어지는 문자열의 길이가 1000이하이기 때문에 완전 탐색 수행 가능
# 길이가 n인 문자열이라면 n/2까지의 모든 수를 단위로 하여 문자열을 압축하고 길이 비교

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0 : step]  # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            if prev == s[j : j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step] 
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

data = str(input("data : "))
print(solution(data))