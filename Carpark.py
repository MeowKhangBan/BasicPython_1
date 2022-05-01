hour_come = int(input('เข้ามาชั่วโมงที่ :'))
min_come = int(input('เข้ามานาทีที่ :'))
hour_out = int(input('ออกชั่วโมงที่ :'))
min_out = int(input('ออกมานาทีที่ :'))

def total_min(min_come,min_out,hour_come,hour_out):
    a = min_out-min_come
    if min_out == min_come: return (hour_out-hour_come)*60
    elif min_come > min_out :return (min_out+(60-min_come))+((hour_out-hour_come)*60)
    elif min_out > min_come : return (min_out-min_come)+((hour_out-hour_come)*60)

fullmin = total_min(min_come,min_out,hour_come,hour_out)

if fullmin <= 15: print(0)
elif fullmin > 15 and fullmin <= 239:
    if 15 < fullmin <= 60:
        print(10) 
    elif 60 < fullmin <= 120:
        print(20)
    elif 120 < fullmin <=180:
        print(30)
    elif 180 < fullmin <= 239:
        print(50)
elif 240 <= fullmin <= 360:
    if 240 <= fullmin <= 300:
        print(70)
    elif 300 < fullmin <= 360:
        print(90) 
elif fullmin > 360 :
    print(200)