PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70p
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split('\n')
new_dict = {x.split()[0]: int(x.split()[1].replace('p', '').replace('р', '')) for x in new_list}

print(new_dict)
