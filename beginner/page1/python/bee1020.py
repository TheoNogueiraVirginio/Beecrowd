age = int(input())

print(f'{age//365} ano(s)')
print(f'{age%365//30} mes(es)')
print(f'{age%365%30} dia(s)')