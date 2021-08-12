enc = "label"

dec = ""

for x in enc:
    dec += chr(ord(x) ^ 13)

print('crypto{{{}}}'.format(dec))
