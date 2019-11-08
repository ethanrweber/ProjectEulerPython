from datetime import datetime, timedelta

def method():
    print("how many sundays fell on the first of the month during the twentieth century (1 jan 1901 through 31 dec "
          "2000)?")

    begin = datetime(1901, 1, 1)
    end = datetime(1000, 12, 31)

    count = 1

    # find the first sunday
    day = 1
    first_sunday = datetime(1901, 1, day)
    for i in range(7):
        if first_sunday.weekday() == 6:  # 6: sunday
            break
        day += 1
        first_sunday = datetime(1901, 1, day)

    while first_sunday.year < 2001:
        count += 1
        first_sunday = first_sunday + timedelta(days=7)

    print("sundays: " + str(count))
    return
