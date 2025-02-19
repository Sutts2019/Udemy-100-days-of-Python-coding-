def is_leap_year(year):
    if year % 4 == 0:
        leap = True
    else:
        leap = False
    if year % 100 == 0 and year % 400 != 0:
        leap = False
    return leap

print(is_leap_year(2400))
print(is_leap_year(1989))