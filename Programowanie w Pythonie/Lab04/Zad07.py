import re

regex_ip = re.compile(r"""(?P<ip>(?:\d|[1-9]\d|1\d\d|2[0-5][0-5])\.(?:\d|[1-9]\d|1\d\d|2[0-5][0-5])\.(?:\d|[1-9]\d|1\d\d|2[0-5][0-5])\.(?:\d |[1-9]\d |1\d\d|2[0-5][0-5]))""", re.VERBOSE)

text = "255.255.255.1 241.32.51.2"
for mach_object in regex_ip.finditer(text):
    print(mach_object.groupdict())