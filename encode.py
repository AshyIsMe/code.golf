source = open('emirp.py').read()
if len(source) % 2 != 0:
    source += ' '
c = source.encode().decode('u16')

print(f"exec(bytes('{c}','u16')[2:])")