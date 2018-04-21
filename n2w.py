print(''.join(reversed('Alice' + 'Tom')))

str = 'а роза упала на лапу азора'
if ''.join(reversed(str.replace(' ', ''))) == str.replace(' ', ''):
    print('True!')
    print(str)
    print(''.join(reversed(str)))

# at = ['Alice', 'Tom']
#
# print(''.join(at))
