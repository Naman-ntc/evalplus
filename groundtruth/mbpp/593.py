"""
Write a function to remove leading zeroes from an ip address.
"""

import re
def removezero_ip(ip):
 assert isinstance(ip, str), "invalid inputs" # $_CONTRACT_$
 assert len(ip) > 0, "invalid inputs" # $_CONTRACT_$
 return re.sub('\.[0]*', '.', ip)




assert removezero_ip("216.08.094.196")==('216.8.94.196')
assert removezero_ip("12.01.024")==('12.1.24')
assert removezero_ip("216.08.094.0196")==('216.8.94.196')
