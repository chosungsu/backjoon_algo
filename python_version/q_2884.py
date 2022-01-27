hh, mm = map(int, input().split())
if mm >= 45 :
    print(hh, (mm - 45))
elif mm < 45 and hh > 0 :
    print((hh - 1), (mm + 15))
else :
    print(23, (mm + 15))