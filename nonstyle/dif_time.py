# -*- coding: cp932 -*-

#�����̍������v�Z����

#�������擾����
time_now = "2024/01/09 21:00"   #���݂̔N����
time_base = "2021/12/31 00:00"  #��ɂ������N����

dif_year = ""
dif_month = ""
dif_day = ""
dif_min = ""


#�����̍������v�Z����

#�N�̍���
now_year = time_now[0:4]
base_year = time_base[0:4]

dif_year = str(int(now_year) - int(base_year))
print dif_year


#���̍���
now_month = time_now[5:7]
base_month = time_base[5:7]

#print(now_month)
#print(base_month)

dif_month = str(int(now_month) - int(base_month))
#print dif_month

if now_year == base_year:
    print "1�N�ȓ��ł��B"
    
elif int(dif_year) > 0:
    print dif_year + "�N�O�ł��I"

else:
    print "0�b�O"
