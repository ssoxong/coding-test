str = input()
for s in str:
    if s>='A' and s<'a':
        print(s.lower(), end='')
    else:
        print(s.upper(), end='')