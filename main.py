# Student name
# Current date
# Default Values for Parameters Practice

# 8-3 (T-Shirt)
#def make_shirt(shirt_size, shirt_text):
   # print(f'My shirt is a {shirt_size} and has the message "{shirt_text}" written on it.')

 #make_shirt("Large", "python is cool")
 #make_shirt(shirt_size = 'Medium', shirt_text= "I like food")
# 8-4 (Large Shirts)
def make_shirt(shirt_text,shirt_size = 'Large'):
    print(f'My shirt is a {shirt_size} and has the message "{shirt_text}" written on it.')


make_shirt(shirt_text= "I love Python")
make_shirt(shirt_size = "Medium", shirt_text = 'I love Python')
make_shirt(shirt_size = 'Fits All', shirt_text ="Python is lit")

# 8-5 (Cities)
def describe_city(name_city, country = 'Russia'):
    print(f'{name_city} is located in {country}')

describe_city(name_city = 'Moscow' )
describe_city(name_city = 'Omsk')
describe_city(name_city = 'Paris', country = 'France')