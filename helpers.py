def pretty_print(d, indent=2):
    for key, value in d.items():
        print("\t" * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print("\t" * (indent + 1) + str(value))


def reverse_date(date):
    parts = date.split("/")
    reversed_parts = parts[::-1]
    reversed_date = "/".join(reversed_parts)
    return reversed_date


def format_number(num):
    if isinstance(num, float):
        decimal_part = num - int(num)
        if decimal_part < 0.01:
            return float("{:.2f}".format(num))
        else:
            return float("{:.2f}".format(round(num, 2)))
    else:
        return float(num)
