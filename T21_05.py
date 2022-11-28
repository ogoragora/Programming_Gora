import re


DATE1 = r"\b(?P<y1>\d{1,4})/(?P<m1>\d{1,2})/(?P<d1>\d{1,2})"
DATE2 = r"\b(?P<d2>\d{1,2})\.(?P<m2>\d{1,2})\.(?P<y2>\d{1,4})"
DATE3 = r"\b(?P<y3>\d{1,4})\-(?P<m3>\d{1,2})\-(?P<d3>\d{1,2})"
DATE = DATE1 + "|" + DATE2 + "|" + DATE3


def change_dates(string, n):

    def _change_date(match):
        date = match.group()
        if "/" in date:
            k = "1"
        elif "." in date:
            k = "2"
        else:
            k = "3"

        year = match.group("y" + k)
        month = match.group("m" + k)
        day = match.group("d" + k)

        while len(year) != 4:
            year = "0" + year
        if len(month) != 2:
            month = "0" + month
        if len(day) != 2:
            day = "0" + day

        if n == 1:
            date = "/".join((year, month, day))
        elif n == 2:
            date = ".".join((day, month, year))
        else:
            date = "-".join((year, month, day))
        return date

    return re.sub(DATE, _change_date, string)


if __name__ == "__main__":
    n = int(input())

    with open("input.txt", "r", encoding="utf-8") as inp:
        s = inp.read()
        s = change_dates(s, n)
    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(s)
