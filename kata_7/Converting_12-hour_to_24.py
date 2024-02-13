# def to24hourtime(hour, minute, period):
#     # If period is "am", keep hour as is
#     if period == "am":
#         # Special case: if hour is 12, convert it to 0
#         if hour == 12:
#             hour = 0
#     # If period is "pm", add 12 to hour (except if it's 12 pm)
#     elif period == "pm":
#         if hour != 12:
#             hour += 12
#
#     # Format the hour and minute as two-digit strings
#     hour_str = str(hour).zfill(2)
#     minute_str = str(minute).zfill(2)
#
#     # Concatenate hour and minute strings
#     return hour_str + minute_str

#hour_str = str(hour).zfill(2):

#str(hour): This converts the integer variable hour to a string. This is necessary because the zfill() method works
#on strings, not integers..zfill(2): This is a string method that pads the string with zeros on the left until it
#reaches the specified length. In this case, we want the string to be 2 characters long, so if hour is a single digit
#(e.g., 7), it will be padded with a zero to become '07'. If hour is already two digits (e.g., 12), it will remain unchanged.

def to24hourtime(hour, minute, period):
    if period == 'pm' and 0 < hour < 12: hour += 12
    elif period == 'am' and hour == 12: hour = 0
    return f'{hour:02d}{minute:02d}'


def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    if int(hour) == 12 and int(minute) == 0 and period == 'am':
        return '0000'
    elif int(hour) == 12 and int(minute) == 0 and period == 'pm':
        return '1200'
    elif period == 'am':
        if hour >= 12: return '00' + minute
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
        return hour + minute
    else:
        if int(hour) + 12 >= 24:
            return '12' + minute
        else:
            return str(int(hour) + 12) + minute

        