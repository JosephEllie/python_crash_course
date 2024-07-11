from city_functions import country_and_cities


def test_check_cities_and_countries():
    formatted_name = country_and_cities('Monrovia', 'Liberia')
    assert formatted_name == 'Monrovia Liberia'


def test_check_cities_countries_and_population():
    formatted_name = country_and_cities('Monrovia', 'Liberia', 5000000)
    assert formatted_name == 'Monrovia Liberia 5000000'
