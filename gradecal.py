# 80 ≤ x ≤ 100 A
# 75 ≤ x < 80 B+
# 70 ≤ x < 75 B
# 65 ≤ x < 70 C+
# 60 ≤ x < 65 C
# 55 ≤ x < 60 D+
# 50 ≤ x < 55 D
# 0 ≤ x < 50 F
# กรณีอื่น ๆ ERROR

score = float(input('Enter your score :'))
def gradecal(score):
    if 80<= score <=100: return 'A'
    elif 75<= score <80: return 'B+'
    elif 70<= score <75: return 'B'
    elif 65<= score <70: return 'C+'
    elif 60<= score <65: return 'C'
    elif 55<= score <60: return 'D+'
    elif 50<= score <55: return 'D'
    elif score <50 : return 'F'
    else: return 'Error'

print(gradecal(score))