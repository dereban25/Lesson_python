

enemy ={
    'loc x': 70,
    'loc y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Dereban',
}

print('Location object in X position '+str(enemy['loc x']))
print('Location object in Y position '+str(enemy['loc y']))
enemy['rank'] = 'Admiral'
print(enemy)
del enemy['rank']
print(enemy)

enemy['loc x'] = enemy['loc x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'


print(enemy)
print(enemy.keys())
print(enemy.values())