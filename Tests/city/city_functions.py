def country_and_cities(city, country, population=None):
    if population:
        info = f'{city} {country} {population}'
    else:
        info = f'{city} {country}'
    return info


print(country_and_cities("Monrovia", 'Liberia'))
