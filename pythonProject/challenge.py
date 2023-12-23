message = 'Happy Christmas Everyone!'
if k in message:
    if k in "aeoiu":
print(k.upper(), end='')
elif k.isspace():
print('k', end='')
else:
print('*', end='')