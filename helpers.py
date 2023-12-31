import re
import math
from bs4 import BeautifulSoup
from lxml import etree


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


def format_number(param, as_float_str=False):
    if isinstance(param, str) or as_float_str:
        param = str(param)
        if param.isdigit():
            return int(param)
        elif all(
            char.isdigit() or char == "," or char == "." or char == "-"
            for char in param
        ):
            param = param.replace(",", ".")
            param = (
                param.rsplit(".", 1)[0].replace(".", "")
                + "."
                + param.rsplit(".", 1)[-1]
            )
            param = param.replace(",", "")
            if as_float_str and param.rfind(".") != -1:
                param = "{:,.2f}".format(float(param)).replace(",", ".")
                dot_index = param.rfind(".")
                param = param[:dot_index] + "," + param[dot_index + 1 :]
                return param
            try:
                return float(param)
            except:
                return 0.0

    if isinstance(param, float):
        rounded_value = round(param, 2)
        float_value = float(rounded_value)
        return float_value

    return param


# def format_number(num):
#     if isinstance(num, float) or (isinstance(num, str) and not num.isdigit()):
#         if isinstance(num, str):
#             num = num.replace(",", ".").replace(".", "", 1)
#         return float(num)
#         # decimal_part = num - math.floor(num)

#         # if decimal_part < 0.01:
#         #     return float("{:.2f}".format(num))
#         # else:
#         #     return float("{:.2f}".format(round(num, 2)))

#     return int(num)


def get_dom_by_page_source(source):
    soup = BeautifulSoup(source, "html.parser")
    dom = etree.HTML(str(soup))
    return dom


def get_content_in_parentheses(string):
    pattern = r"\((.*?)\)"

    match = re.search(pattern, string)

    if match:
        content = match.group(1)
        return content
    else:
        return None


def is_string_float(string):
    try:
        float(string)
        return True
    except:
        return False
