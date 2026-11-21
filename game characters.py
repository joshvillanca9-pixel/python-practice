

characters =[
    {'roles':'knight','Damage':100, 'weapon':'sword' },
    {'roles':'archer','Damage':150, 'weapon':'bow and arrow' },
    {'roles':'mage','Damage':200, 'weapon':'staff'}
]

for i in characters:
    print(f"{i['roles']} {i['Damage']} {i['weapon']}")

