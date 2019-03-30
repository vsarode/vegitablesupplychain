from datetime import datetime

from vegitablesupplychain.utils.exceptions import ValidationException


def get_date_time_from_time_stamp(timestamp=""):
    if not timestamp:
        return datetime.now()
    try:
        return datetime.fromtimestamp(int(timestamp) / 1000)
    except:
        raise ValidationException(errorMessage="Invalid datetime format")
