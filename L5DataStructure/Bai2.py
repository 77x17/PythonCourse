Dic = {
    'a': 'apple, add',
    'b': 'banana, bomb',
    'c': 'carrot, count',
    'd': 'dragonFruit, double'
}

print (Dic)
print (Dic.keys())

Dic['e'] = 'eggFruit, error'
print (Dic)

Str = str(input())
if Str in Dic:
    print (f'{Str}: {Dic[Str]}')
else:
    print (f'{Str} does not appear in Dic.keys')

Str = str(input())

appear = False
for idx in Dic:
    if Str in Dic[idx]:
        print (f'{idx}: {Dic[idx]}')
        appear = True
if not appear:
    print (f'{Str} does not appear in Dic.values')

Str = str(input())
del(Dic[Str])
print (Dic)
