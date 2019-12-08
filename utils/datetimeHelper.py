from datetime import datetime, timezone

def convertdatetimestring(in_str, in_format: str = "%Y-%m-%d %H:%M:%S", in_tz: timezone = timezone.utc,
                          out_tz: timezone = timezone.utc, out_format: str = "%Y-%m-%d %H:%M:%S",
                          default: str = None):
    """
    Parses a date/time string with the given format, converts it from the given in_timezone to
    the out_timezone and returns a date/time string in the given format.

    :param in_str: An input string with a date-time
    :param in_format: Format to parse the date-time string
    :param in_tz: Timezone of the input string (default: UTC), set to None for system timezone
    :param out_tz: Timezone to convert to (default: UTC), set to None for system timezone
    :param out_format: Format to export the string
    :param default: Default value if in_str is empty
    :return: Converted date in the given format,
    """
    if not in_str:
        return default
    in_dt = datetime.strptime(in_str, in_format)
    if in_tz is not None:
        in_dt = in_dt.replace(tzinfo=in_tz)
    if out_tz is not None:
        out_dt = in_dt.astimezone(tz=out_tz)
    return out_dt.strftime(out_format)
