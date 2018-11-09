alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")
print("Total number of aliens: " + str(len(aliens)))

#alien_0 = {'color': 'green', 'points': 5}
#
# print(alien_0['color'])
# print(alien_0['points'])
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
#
# print(alien_0)
#
# alien_1 = {}
# alien_1['color'] = 'red'
# alien_1['points'] = 6
#
# alien_1['color'] = 'green'
#
# print(alien_1)