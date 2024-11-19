# Joshua Phillips
# 11/18/24
# Default Values for Parameters Practice

# 8-3 (T-Shirt)
def make_shirt(size='Large', text='I luv Pythen'):
    print(f'The shirt will be: {size}, with the text: {text}.')

make_shirt('XXL', 'Vome')
make_shirt(text='Nidus Prime', size='XL')

# 8-4 (Large Shirts)
make_shirt()
make_shirt('medium')


# 8-5 (Cities)
def describe_city(city='Mancelona', country='America'):
    print(f'{city} is a part of {country}.')


describe_city(city='Schlatt', country='Germany')
describe_city(city='Toad Suck', country='America')
describe_city()