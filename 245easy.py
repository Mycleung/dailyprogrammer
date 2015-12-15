# Yesterday, Devon the developer made an awesome webform, which the sales team would use to record the results from
# today's big new marketing campaign, but now he realised he forgot to add a validator to the "delivery_date" field! He
# proceeds to open the generated spreadsheet but, as he expected, the dates are all but normalized...
# Some of them use M D Y and others Y M D, and even arbitrary separators are used! Can you help him parse all the messy
# text into properly ISO 8601 (YYYY-MM-DD) formatted dates before beer o'clock?
import re

infile = "245easyinput"
date_matcher = "(\d+)[^\d]+(\d+)[^\d]+(\d+)"

def format_sf(num, sf, filler):
    """
    Format a number to a specified number of significant figures.
    :param num: Number to be formatted
    :param sf: Number of digits required
    :param filler: Template string from which to obtain filler digits. E.g. "2000" for years or "00" for dates/months
    :return: String representing integer with sf digits.
    """
    assert len(num) <= sf
    if len(num) < sf:
        return filler[0:(sf-len(num))] + num
    return num


def format_month_date(num):
    """
    Format the month or day into a 2sf number. Input can be one or two digit string
    :param num: One or two digit string. E.g. "3", "15"
    :return: Two digit string representing a date or string. E.g. "15", "03"
    """
    return format_sf(num, 2, "00")


def format_year(year):
    """
    Format the year string given.
    :param year: Year string, either 4 digits or 2 (e.g. 2015 or 15)
    :return: 4 digit year string (e.g. 2015)
    """
    return format_sf(year, 4, "2000")


def output(dates):
    """
    Helper output function, for now simply prints out each date
    """
    for date in dates:
        print(date)

with open(infile, "r") as input:
    raw_dates = input.readlines()

out_dates = []

for date in raw_dates:
    match = re.search(date_matcher, date)
    assert match is not None
    assert len(match.groups()) == 3

    is_ymd = len(match.group(1)) == 4

    if is_ymd:
        # Year-Month-Day format
        out_dates.append(format_year(match.group(1)) + "-" +
                         format_month_date(match.group(2)) + "-" +
                         format_month_date(match.group(3)))

    else:
        # Month-Day-Year format
        out_dates.append(format_year(match.group(3)) + "-" +
                         format_month_date(match.group(1)) + "-" +
                         format_month_date(match.group(2)))

output(out_dates)