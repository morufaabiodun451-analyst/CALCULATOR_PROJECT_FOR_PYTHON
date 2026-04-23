name = ['Morufa', 'Faith', 'Dami', 'Margaret']
num = 1
for n in name:
    print(f'(num += 1). {name}')

for i in range(len(name)):
    print(f'{i + 1}.{name}')

for index, name in enumerate(name,start=1):
    print(index,'.', name)