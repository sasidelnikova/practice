# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

price = int(input())

if price % 10 != 0: print(0)
else:
    two = price // 200
    price -= two * 200
    one = price // 100
    price -= one * 100
    five = price // 50
    price -= five * 50

    if price > 0: print(0)
    else:
        print(two * 4 + one * 2 + five)
