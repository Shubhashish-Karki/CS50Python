import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
        if matches := re.search(
            r"^(\d[0-2]?)(?:\:([0-5][0-9]))? (A|P)M to (\d[0-2]?)(?:\:([0-5][0-9]))? (A|P)M",
            s,
        ):
            # initializing a list with groups start with time[0]
            time = matches.groups()
            # checkin if hour is greater than 12
            if int(time[0]) > 12 or int(time[3]) > 12:
                raise ValueError
            # for start time
            start = working_time(time[0], time[1], time[2])
            # for end time
            end = working_time(time[3], time[4], time[5])
            return f"{start} to {end}"
        else:
            raise ValueError


def working_time(hour, min, am_pm):
    # convert string hour to int
    hour = int(hour)
    # for am
    if am_pm == "A":
        if hour == 12:
            work_hour = 0
        else:
            work_hour = hour
    # for pm
    else:
        if hour == 12:
            work_hour = 12
        else:
            work_hour = hour + 12
    # if the format is fist type = 9 am to 4 pm
    if min == None:
        work_min = ":00"
        new_form = f"{work_hour:02}" + work_min
    # if the format is of second type
    else:
        new_form = f"{work_hour:02}" + ":" + min
    return new_form


if __name__ == "__main__":
    main()
