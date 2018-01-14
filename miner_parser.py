import re
# python-dateutil is used in datadog, perhaps...
from dateutil.parser import parse


def parse_miner(logger, line):
    syslog_header, message = line.split(']:', 1)

    # hash rate
    matches = re.search(r'accepted: .+?\),\s([0-9\.]+)\s(\S)(hash|H)/s\s\((yes|yay)!+\)', message)
    if not matches:
        return None

    raw_value = float(matches.group(1))
    si_unit = matches.group(2)
    if si_unit.upper() == 'G':
        value = raw_value * 1000 * 1000 * 1000
    elif si_unit.upper() == 'M':
        value = raw_value * 1000 * 1000
    elif si_unit.upper() == 'K':
        value = raw_value * 1000

    # timestamp
    time_string = " ".join(syslog_header.split(" ", 3)[0:3])
    timestamp = int(parse(time_string).strftime('%s'))
    return ("miner.hashrate", timestamp, value, {'metric_type': 'gauge', 'unit': 'hash/s'})
