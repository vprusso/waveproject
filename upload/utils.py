import dateutil.parser 


def sanitize_date_format(date):    
    return dateutil.parser.parse(date).strftime('%Y-%m-%d')


def sanitize_float_format(str_float_val):
    # TODO (more checking here...)

    str_float_val = str_float_val.replace(',', '')
    str_float_val = dollars_to_cents(str_float_val)

    return str_float_val


def dollars_to_cents(dollars, truncate=True):
    cents = float(dollars) * 100
    if truncate:
        return int(cents)
    else:
        return cents


def cents_to_dollars(cents):
    return format(float(cents) / 100.0, '.2f')


def month_name(month_num):
    names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    return names[month_num]
