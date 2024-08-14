# -*- coding: cp932 -*-

#日時の差分を計算する

#時刻を取得する
time_now = "2024/01/09 21:00"   #現在の年月日
time_base = "2021/12/31 00:00"  #基準にしたい年月日

dif_year = ""
dif_month = ""
dif_day = ""
dif_min = ""


#時刻の差分を計算する

#年の差分
now_year = time_now[0:4]
base_year = time_base[0:4]

dif_year = str(int(now_year) - int(base_year))
print dif_year


#月の差分
now_month = time_now[5:7]
base_month = time_base[5:7]

#print(now_month)
#print(base_month)

dif_month = str(int(now_month) - int(base_month))
#print dif_month

if now_year == base_year:
    print "1年以内です。"
    
elif int(dif_year) > 0:
    print dif_year + "年前です！"

else:
    print "0秒前"
