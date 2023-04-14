# Title: Zellers algorithm
# Date: 04/06/2023
# Author: Sunmi Kim
# Description: Program to display day of the week for a given date
# Note: 1) doesn't check for days completely. For April, Nov. etc. Should check day < 30
# 2) Can make program simpler by using: c = year % 100

import sys
dates = []

# display a welcome function
def display_welcome():
    print("===== Zellers algorithm =====")
    print()
    print("=============================")

# return True if the given year is a leap year, otherwise, False
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_date():
    month = int(input("Enter birthday month (mm): "))
    day = int(input("Enter birthday date (dd): "))
    year = int(input("Enter birthday year (yyyy): "))

    if month < 1 or month > 12:
        print("Invalid month input.")
        sys.exit(1)  # break
    elif year < 1582 or year > 4902:
        print("Invalid year input.")
        sys.exit(1)  # break
    elif month == 2 and day == 29 and is_leap_year(year) == False:
        print("Invalid date input as it is not leap year.")
        sys.exit(1)  # error exit
    else:
        dates.append(month)
        dates.append(day)
        dates.append(year)
        #print(dates)
        # sys.exit(0) # success exit

def calc_a():  # a = month
    if dates[0] == 3:
        a = 1
    elif dates[0] == 4:
        a = 2
    elif dates[0] == 5:
        a = 3
    elif dates[0] == 6:
        a = 4
    elif dates[0] == 7:
        a = 5
    elif dates[0] == 8:
        a = 6
    elif dates[0] == 9:
        a = 7
    elif dates[0] == 10:
        a = 8
    elif dates[0] == 11:
        a = 9
    elif dates[0] == 12:
        a = 10
    elif dates[0] == 1:
        a = 11
    else:  # dates[0] == 2:
        a = 12
    return a

def calc_b():  # b = day
    b = dates[1]
    return b

def calc_c():  # c = year
    # if month == Jan. or Feb. decrement 1 year
    if dates[0] == 1 or dates[0] == 2:
        if dates[2] >= 2000:
            c = (dates[2] - 2000) - 1
            return c
        elif dates[2] >= 1900 and dates[2] < 2000:
            c = (dates[2] - 1900) - 1
            return c
        elif dates[2] >= 1800 and dates[2] < 1900:
            c = (dates[2] - 1800) - 1
            return c
        elif dates[2] >= 1700 and dates[2] < 1800:
            c = (dates[2] - 1700) - 1
            return c
        elif dates[2] >= 1600 and dates[2] < 1700:
            c = (dates[2] - 1600) - 1
            return c
        else: # dates[2] >= 1582 and dates[2] < 1600:
            c = (dates[2] - 1500) - 1
            return c
    else:
        if dates[2] >= 2000:
            c = dates[2] - 2000
            return c
        elif dates[2] >= 1900 and dates[2] < 2000:
            c = dates[2] - 1900
            return c
        elif dates[2] >= 1800 and dates[2] < 1900:
            c = dates[2] - 1800            
            return c
        elif dates[2] >= 1700 and dates[2] < 1800:
            c = dates[2] - 1700            
            return c
        elif dates[2] >= 1600 and dates[2] < 1700:
            c = dates[2] - 1600            
            return c
        else: # dates[2] >= 1582 and dates[2] < 1600:
            c = dates[2] - 1500
            return c
        #print(type(c))

def calc_d():  # get century of the year
    year = dates[2]
    century = year // 100
    #print("The century of the adjusted year", year, "is", century)
    return century

def calc_w_x_y_z_r(): # get w, x, y, z, r (day of the week)
    a = calc_a()
    b = calc_b()
    c = calc_c()
    d = calc_d()
    w = int((13 * a - 1)/5)
    x = int(c / 4)
    y = int(d / 4)
    z = int(w + x + y + b + c - 2*d)
    r = int(z % 7)
    print("w, x, y, z, r =", w, x, y, z, r)
    if r == 0:
        print("Day of the week: Sunday")
    elif r == 1:
        print("Day of the week: Monday")
    elif r == 2:
        print("Day of the week: Tuesday")
    elif r == 3:
        print("Day of the week: Wednesday")
    elif r == 4:
        print("Day of the week: Thursday")
    elif r == 5:
        print("Day of the week: Friday")
    elif r == 6:
        print("Day of the week: Saturday")
    print("=============================")

def main():
    display_welcome()
    get_date()
    a = calc_a()
    b = calc_b()
    c = calc_c()
    d = calc_d()
    print(f"a, b, c, d = {a}, {b}, {c}, {d}")
    calc_w_x_y_z_r() 
    sys.exit(0) # success exit

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
