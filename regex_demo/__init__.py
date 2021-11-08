import regex


qq = '1826755263'
res = regex.match(r'[1-9]\d{4,11}', qq)
print(res, type(res))

