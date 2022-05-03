HL_CASUALTIES = 2398759958
OLD_WORLD_POP = 6381185114
NEW_WORLD_POP = OLD_WORLD_POP - HL_CASUALTIES

city_pop = int(input('Enter city population (no commas): '))
new_pop = int(city_pop * (NEW_WORLD_POP / OLD_WORLD_POP))
print('New city population:', new_pop)

