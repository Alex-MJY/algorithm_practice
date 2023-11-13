# 럭키 스트레이트 (p321, p515)

n = str(input())
 
left_pos, right_pos = 0, len(n) - 1
left_val, right_val = 0, 0
for i in range(len(n) // 2):
    left_val += int(n[left_pos])
    right_val += int(n[right_pos])
    left_pos += 1
    right_pos -= 1
    
if left_val == right_val:
    print("LUCKY")
else:
    print("READY")