def format_kml_str(str_to_format):
    return str_to_format.replace("km/l", "").replace(",", ".").replace("-", "")


def format_kmt_str(str_to_format):
    return str_to_format.replace("sek.", "").replace(",", ".").replace("-", "")


def format_price_str(str_to_format):
    return int(str_to_format.replace(" kr.", "").replace(".", "").replace("Ring", "0").replace("/md",""))

def format_kwh_str(str_to_format):
    return int(str_to_format.replace("-", "").replace(" kWh", "") or 0)

def format_range_str(str_to_format):
    return int(str_to_format.replace("-", "").replace(" km", "") or 0)

def format_kms_str(str_to_format):
    return int(str_to_format.replace(".", ""))

def format_hk_str(str_to_format):
    return int(str_to_format.replace("-", "").replace(" HK", "") or 0)