# num = 1
# string = '1'
# num2 = int(string)
# print(num + num2)

# words = 'hi' * 3
# print(words)
#
# word = 'vbsjbgkwabfbgre'
# num = 1
# string = 'f '
# total = string * (len(word) - num)
# print(total)

# name = 'my name is mike'
# print(name[0])
# print(name[-4])
# print(name[11:14])
# print(name[11:15])
# print(name[5:])
# print(name[:5])

# def f_converter(c):
#     f = c * 9 / 5 + 32
#     return str(f) + ''
#
#
# c2f = f_converter(35)
# print(c2f)

# def g_kg_comverter(kg):
#     g = kg*1000
#     return str(g)
# kg2g = g_kg_comverter(12)
# print(kg2g)

# def find_z(x,y):
#     z = x*x +y*y
#     return str(z)
# zz = find_z(3,4)
# print('z is',zz)

# file =open('/Users/lei0j/Desktop/text.txt','w')
# file.write('hi bitch')

# def text_create(name,msg):
#     desktop_path = '/Users/lei0j/Desktop/'
#     full_path = desktop_path + name + '.txt'
#     file = open(full_path,'w')
#     file.write(msg)
#     file.close()
#     print('donw')
# # text_create('file name','this is main text')text_create('file name','this is main text')
#
# def text_filter(word,censored_word = 'lame',change_world = 'good'):
#     return word.replace(censored_word,change_world)
# text_filter('python is lame')
#
# def censored_text_create(name,msg):
#     clean_msg = text_filter(msg)
#     text_create(name,clean_msg)
# censored_text_create('Try','lame!')


# album=['s','w',25,True]
# print(album)
# album.append('x')
# print(album)
# print(album[1],album[2])


# def account_login():
#     password = input('123')
#     if password == '123':
#         print('fucking right')
#     else:
#         print('back off')
#     account_login()
# account_login()

# password_list =['123','456']
# def account_login():
#     password= input('input ur p.w')
#     password_correct = password == password_list[-1]
#     password_reset = password== password_list[0]
#     if password_correct:
#         print('correct')
#     elif password_reset:
#         new_password = input('set a new pw')
#         password_list.append(new_password)
#         print('set succeed')
#         account_login()
#     else:
#         print('wrong')
#         account_login()
# account_login()

# for every_letter in 'fuck you':
#     print(every_letter)

# for num in range(1,11):
#     print (str(num)+ '+1=', num +1)


# for i in range(1,10):
#     for j in range (1,10):
#         print ('{} x {} = {}'.format(i,j,i*j))

# while 1<3:
#     print('a')

# cunt = 0
# while True:
#     print('Repeat this line !')
#     cunt = cunt +1
#     if cunt == 5:
#         break

# password_list = ['****','12345']
#
# def account_login():
#     tries = 3
#     while tries > 0:
#         password = input('input ur password: ')
#         password_correct = password==password_list[-1]
#         password_reset = password == password_list[0]
#
#         if password_correct:
#             print('login success')
#             return
#         elif password_reset:
#             new_password = input('set your new password: ')
#             password_list.append(new_password)
#             print('set success')
#             account_login()
#         else:
#             print('wrong pass')
#             tries = tries -1
#             print(tries,'time left')
#     else:
#         print('account locked')
# account_login()
#
# def invest(amount, rate,time):
#     print('principal amount :{}'.format(amount))
#     for t in range(1,time+1):
#         amount = amount*(1+rate)
#         print('year {}:${}'.format(t,amount))
# invest(100,0.1,8)

# msg = 'hi'
# print(msg)
# msg ='ok'
# print(msg)

# name = 'E'
# print('hi',name,'would you')

# name = '1 jie lei 1'
# print(name.upper())
# print(name.lower())
# print(name.title())
# word = 'i like dick'
# mes = name.title() + 'once said,' +'"'+word+'"'
# print(mes)
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())


# print(0.1+0.67899999997765789)

# age = 23
# ms = 'happy ' + str(age)
# print(ms)
#
# print( 5+3)
# print(9-1)
# print(2*4)
# print(int(16/2))
#
# num = 1
# print('my fav num is: '+str(num))

# import this
#
# name = ['mike','tom','j','pussy','dick']
# print(name[0],name[1],name[2],name[-2],name[-1])
# print('hi,',name[0])


# guest = ['tom','harry','jie','lei']
# print(guest)
# cantmakeit = guest.pop(0)
# print(cantmakeit,'cant make it')
# print(guest)
#
# guest.insert(0,'kk')
# print(guest)
# guest.append('oo')
# print(guest)
# guest.pop(-1)
# print(guest)
# guest.pop(-1)
# print(guest)
# guest.pop(-1)
# print(guest)
#
# print(guest)

# place = ['new york','tokyo','london','canada','amsterdam']
# print(place)
#
# print(sorted(place))
# print(place)
# place.reverse()
# print(place)
# print(place)

# pizza = ['pizza1','pizza2','pizza3']
# for pizzas in pizza:
#    # print(pizzas)
#     print('I like',pizzas)
# print('i really like pizza')
#
# x = list(range(2,60,2))
# print(x)

# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)

# squares = [value**2 for value in range (1,11)]
# print(squares)

# shudaoershis =[]
# for value in range(1,21):
#     shudaoershi=value
#     shudaoershis.append(shudaoershi)
# print(shudaoershis)
#
# ershi = list(range(1,21))
# print(ershi)
#
# abillion = list(range(1,1000001))
# print(abillion)

# abillion_fors =[]
# for value in range (1,1000001):
#     abillion_for = value
#     abillion_fors.append(abillion_for)
# print(abillion_fors)
#
# print(sum(abillion_fors))
#
# x=[]
# x=list(range(3,31,3))
# print(x)

# for value in range(1,11):
#     xx = value**2
#     x.append(xx)
#     print(xx)
# print(x)
# numbers = list(range(1,6))
# print(numbers)

# abillion_fors =[]
# for value in range (1,12):
#     abillion_for = value
#     abillion_fors.append(abillion_for)
# print(abillion_fors)
# first_three = abillion_fors[0:3]
# print('first three is:',first_three)
# mid_three = abillion_fors[3:6]
# print(mid_three)
# last_three = abillion_fors[-3:]
# print(last_three)

#
# pizza = ['pizza1','pizza2','pizza3']
# for pizzas in pizza:
#     print(pizzas)
#     print('I like',pizzas)
# print('i really like pizza')
# pizza.append('pizza4')
# print(pizza)
# firend_pizza  = pizza[:]
# firend_pizza.append('pizza5')
# print(firend_pizza)
#
# food = (1,2,3,4,5)
# print(food)
# for foods in food:
#     print(foods)
#
#
# food = (0,0,3,4,5)
# print(food)
# for foods in food:
#     print(foods)

# cars = ['audi','bmw','auto','toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
#
#
# alien_color =['green','yellow','red']
#
# if 'green' in alien_color:
#     print('add 5')
# if 'yellow' in alien_color:
#     print('add 10')
# if 'red' in alien_color:
#     print('add 15')

#
# age = 15
# if age <2:
#     print('<2')
# elif age <10:
#     print('<10')
# elif age <18:
#     print('<18')


# usernames = ['1','2','admin','4','5','admin']
# if usernames:
#
#     for username in usernames:
#         if 'admin' in username:
#             print('hellow, would you like to see')
#         else:
#             print('hi',username)
# else:
#     print('no data')

# current_users = ['u1','u2','u3','u4','u5']
# new_users =     ['U1','u2','u6','u7','u8']
#
# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(new_user,'in current users')
#     else:
#         print(new_user)

# nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# for num in nums:
#     if num == '1':
#         print(num, 'st')
#     elif num == '2':
#         print(num, 'nd')
#     elif num == '3':
#         print(num, 'rd')
#     else:
#         print(num, 'th')
#
#
# dic = {
#     'first_name': 'Jie',
#     'last_name': 'Lei',
#     'age': '23',
#     'city': 'huoshan',
# }
#
# # print(person)
# # print()
#
#
# #
# # dic = {'key1': 'v1'
# #        'key2': 'v2'
# #         }
#
# for asa, qqq in dic.items():
#     print(asa)
#     print(qqq)
#
# for key in dic.keys():
#     print(key.title())
# for value in dic.values():
#     print(value.title())


# dic = {'nile': 'egypt',
#        'yellow river': 'china',
#        'yangzi river': 'china',
#        'times': 'uk',
#        'tyne': 'uk'}
# # print(dic)
# for river, country in dic.items():
#     print('The', river.title(), 'runs through', country.title())
# for river in dic.keys():
#     print(river.title())
# for country in set(dic.values()):
#     print(country)
# if 'japan' not in dic.values():
#     print('?')

# a0 = {'c':'21'}
# a2 = {'w2':'2'}
#
# a = [a0, a2]
# print(a)
# for aa in a:
#     print(aa)

# # 6-7
# people = {'tim': {'surname': 'smith',
#                   'sex': 'male',
#                   'color': 'white',
#                   'from': 'UK'},
#           'lucy': {'surname': 'natoro',
#                    'sex': 'female',
#                    'color': 'brown',
#                    'from': 'india'},
#           'jie': {'surname': 'lei',
#                   'sex': 'male',
#                   'color': 'yellow',
#                   'from': 'china'},
#           }
#
# for first_name, other_inform in people.items():
#     # print('\n', first_name)
#     # sex = other_inform['sex']
#     # color = other_inform['color']
#     come_from = other_inform['from']
#     print(come_from.title())

#
# msg = input('What car you looking for\n')
# print('I can find you',msg)


# num = input('How maney people? \n')
# num = int(num)
# if num % 10 == 0:
#     print('ok')
# else:
#     print('no')


# if num > 8:
#     print('no')
# else:
#     print('ok')

# current_num = 1
# while current_num <=5:
#     print(current_num)
#     current_num += 1

# current_num = 0
# while current_num <10:
#     current_num += 1
#     if current_num %2 ==0:
#          continue
#     print(current_num)

# 7-4
# tose = '\n Please add a topping'
# tose +=':'
# msg = ''
# while msg != 'quit':
#     msg = input(tose)
#     print('we will add',msg)
#
#     if msg != 'quit':
#         print(msg)

# tose = '\n Please add a topping'
# tose +=':'
#
# active = True
# while active:
#     msg = input(tose)
#
#     if msg == 'quit':
#         active = False
#     else:
#         print('we will add',msg)


# tose = 'how old r u?'
# age = int(input(tose))
#
# while age >0:
#     age = int(input(tose))
#     if age<3:
#         print('free')
#
#     elif age >3 & age <12:
#         print('charge 10')
#
#     elif age >12:
#         print('charge 15')
#
# sandwich_orders = ['sw1','sw2','sw3','sw4']
# finished_sandwiches = []

# for sandwich_order in sandwich_orders:
#     print(sandwich_order)


# while sandwich_orders:
#     sw = sandwich_orders.pop()
#     print(sw)
#     finished_sandwiches.append(sw)
#     print('add',finished_sandwiches)
# print(finished_sandwiches)
#
# sandwich_orders = ['sw1', 'wuxiang', 'sw2', 'sw3', 'sw4', 'wuxiang']
# print('first print\n', sandwich_orders)
# while 'wuxiang' in sandwich_orders:
#     sandwich_orders.remove('wuxiang')
#     print(sandwich_orders)
# print(sandwich_orders)


# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input('\n name?')
#     response = input('\n where?')
#
#     responses[name] = response
#
#     repeat = input('\n continue?')
#     if repeat == 'no':
#         polling_active = False
#     elif repeat =='yes':
#         polling_active = True
#     else:
#         print('please choose yes or no')
#
#
# print('\n Results')
# for name, response in responses.items():
#     print(name+'want to go to'+response,'.')
#
# def display_meassage():
#     print('这一章学了函数')
# display_meassage()
#
# def fav_book(title):
#     print('my fav book is',title)
# fav_book(input())
#
# def make_shirt(size,style):
#     print('ur shirt is size',size,'and',style)
#
# make_shirt(size ='3',style ='usa')

# def city_cpuntry(city_name, country):
#     city_inform = city_name + ' '+ country
#     return city_inform
# output = city_cpuntry('huoshan','china')
# print(output)
# print(city_cpuntry('hefei','china'))
# print(city_cpuntry('london','uk').title())

# def make_ablum(singer_name, album_name, num=''):
#     album ={'singer name':singer_name, 'album':album_name}
#     if num:
#         album['num'] =num
#     return album
# output = make_ablum('adel','hello')
# print(output)
#

# def make_ablum(singer_name, album_name, num=''):
#     album ={'singer name':singer_name, 'album':album_name}
#     if num:
#         album['num'] =num
#     return album
# while True:
#     print('\n Name a singer and album or num of songs')
#     print('\n press Q to quit')
#
#     input_singer_name = input('Singer name:')
#     if input_singer_name == 'q':
#         break
#
#     input_album_name = input('Album_name')
#     if input_album_name == 'q':
#         break
#
#     input_num_songs = input('num of songs if know, if dont press d')
#     if input_num_songs == 'q':
#         break
#     if input_num_songs == 'd':
#
#
#     output = make_ablum(input_singer_name,input_album_name,input_num_songs )
#     print(output)
#


# #8-10
# def make_great(moshushi, greats):
#     while moshushi:
#         current = moshushi.pop()
#         print('great'+ current)
#         greats.append(current)
#
#
# def show_magi(moshushi):
#     print('print moshushi')
#     for name in moshushi:
#         print(name)
#
#
# moshushi = ['1', '2', '3', '4']
# maked_great = []
#
# show_magi(moshushi)
#
# make_great(moshushi,maked_great)


# 8-11
# def make_great(moshushi, greats):
#     while moshushi:
#         current = moshushi.pop()
#         print('great'+ current)
#         greats.append(current)
#
#
# def show_magi(moshushi):
#     print('print moshushi')
#     for name in moshushi:
#         print(name)
#
#
# moshushi = ['1', '2', '3', '4']
# maked_great = []
#
# show_magi(moshushi)
#
# make_great(moshushi,maked_great)
#
# print(moshushi)
# print(maked_great)
#
# def add(*foods):
#     print(foods)
#     for food in foods:
#         print(food)
# add('1','2','3')
#
# def user_profile(first,last,**other):
#     profile = {}
#     profile['first'] = first
#     profile['last'] = last
#
#     for key,value in other.items():
#         profile[key] =value
#     return profile
#
# infor = user_profile('jie','lei',location = 'china',gender = 'male',color = 'yelllow')
#
# print(infor)
# 9-1
# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print('The name of this restaurant is: ' + self.restaurant_name.title() + '\nand the cuisine_type is: '
#               + self.cuisine_type.title())
#
#     def open_restaurant(self):
#         print('This restaurant ' + self.restaurant_name.title() + ' is opening')
#
#
# res = Restaurant('pizza town', 'pizza')
# print(res.restaurant_name)
# print(res.cuisine_type)
#
# res.describe_restaurant()
# res.open_restaurant()
#
# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print('The name of this restaurant is: ' + self.restaurant_name.title() + '\nand the cuisine_type is: '
#               + self.cuisine_type.title())
#
#     def open_restaurant(self):
#         print('This restaurant ' + self.restaurant_name.title() + ' is opening')
#
#
# res = Restaurant('pizza town', 'pizza')
# res2 = Restaurant('luck','chinese')
# res3 = Restaurant ('mid town','american')
# # print(res.restaurant_name)
# # print(res.cuisine_type)
#
# res.describe_restaurant()
# res.open_restaurant()
#
# res2.describe_restaurant()
# res2.open_restaurant()
# res3.describe_restaurant()
# res3.open_restaurant()

# class User():
#     def __init__(self, first_name, last_name, email, phone):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone = phone
#
#     def describe_user(self):
#         print('The name of this user is: ' + self.first_name.title() + self.last_name.title() +'\nEmail is: ' + self.email
#               + '\n phone number is:' + self.phone)
#     def greet_user(self):
#         print('Hi! ' +self.first_name.title() + self.last_name.title())
#
#
#
# user1 = User('jie','lei','123@gmail.com','110')
#
# user1.describe_user()
# user1.greet_user()


# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 1
#
#     def describe_restaurant(self):
#         print('The name of this restaurant is: ' + self.restaurant_name.title() + '\nand the cuisine_type is: '
#               + self.cuisine_type.title())
#
#     def open_restaurant(self):
#         print('This restaurant ' + self.restaurant_name.title() + ' is opening')
#
#     def num_served(self):
#         print('this res has: ' + str(self.number_served) )
#
#
# res = Restaurant('pizza town', 'pizza')
# # print(res.restaurant_name)
# # print(res.cuisine_type)
# #
# # res.describe_restaurant()
# # res.open_restaurant()
# res.number_served = 2 #change the value directly
# res.num_served()

# self.number_served = 1


# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print('The name of this restaurant is: ' + self.restaurant_name.title() + '\nand the cuisine_type is: '
#               + self.cuisine_type.title())
#
#     def open_restaurant(self):
#         print('This restaurant ' + self.restaurant_name.title() + ' is opening')
#
#     def num_served(self):
#         print('this res has: ' + str(self.number_served))
#
#     def set_num_served(self, set):
#         self.number_served = set
#
#     def increment_number_served(self, sett):
#         self.number_served += sett
#
#
# res = Restaurant('pizza town', 'pizza')
# # print(res.restaurant_name)
# # print(res.cuisine_type)
# #
# # res.describe_restaurant()
# # res.open_restaurant()
# res.set_num_served(2)
#
# res.increment_number_served(22)
#
# res.num_served()


# 9-5
# class User():
#     def __init__(self, first_name, last_name, email, phone):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone = phone
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(
#             'The name of this user is: ' + self.first_name.title() + self.last_name.title() + '\nEmail is: ' + self.email
#             + '\n phone number is:' + self.phone)
#
#     def greet_user(self):
#         print('Hi! ' + self.first_name.title() + self.last_name.title())
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         print(self.login_attempts)
#     def reset_login_attempts(self):
#         self.login_attempts =0
#         print(self.login_attempts)
# user1 = User('jie', 'lei', '123@gmail.com', '110')
#
# # user1.describe_user()
# # user1.greet_user()
#
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.reset_login_attempts()
# user1.increment_login_attempts()
# 9-6
# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print('The name of this restaurant is: ' + self.restaurant_name.title() + '\nand the cuisine_type is: '
#               + self.cuisine_type.title())
#
#     def open_restaurant(self):
#         print('This restaurant ' + self.restaurant_name.title() + ' is opening')
#
#
# class IceCreamStrand(Restaurant):
#
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = []
#     def show_flavors(self):
#         print('the flavor includes: ')
#         for flavor in self.flavors:
#             print(flavor)
#
#
# res = Restaurant('pizza town', 'pizza')
# print(res.restaurant_name)
# print(res.cuisine_type)
#
# res.describe_restaurant()
# res.open_restaurant()
#
# res_ice = IceCreamStrand('ice shop','ice' )
# res_ice.flavors = ['dick','pussy']
# res_ice.show_flavors()


# 9-7
# class User():
#     def __init__(self, first_name, last_name, email, phone):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone = phone
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(
#             'The name of this user is: ' + self.first_name.title() + self.last_name.title() + '\nEmail is: ' + self.email
#             + '\n phone number is:' + self.phone)
#
#     def greet_user(self):
#         print('Hi! ' + self.first_name.title() + self.last_name.title())
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         print(self.login_attempts)
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         print(self.login_attempts)
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, email, phone):
#         super().__init__(first_name, last_name, email, phone)
#         self.privileges = []
#
#     def show_privileges(self):
#         print('the priv are: ')
#         for priv in self.privileges:
#             print(priv)
#
#
# user1 = User('jie', 'lei', '123@gmail.com', '110')
#
# # user1.describe_user()
# # user1.greet_user()
#
# # user1.increment_login_attempts()
# # user1.increment_login_attempts()
# # user1.reset_login_attempts()
# # user1.increment_login_attempts()
#
# admin = Admin('eric', 'matthes', 'e_matthes@example.com', '111')
# admin.describe_user()
# admin.privileges = ['suck dick', 'or not suck dick']
#
# admin.show_privileges()


# 9-8 Answer for 9-8
# class User():
#     """Represent a simple user profile."""
#
#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the user."""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.location = location.title()
#         self.login_attempts = 0
#
#     def describe_user(self):
#         """Display a summary of the user's information."""
#         print("\n" + self.first_name + " " + self.last_name)
#         print("  Username: " + self.username)
#         print("  Email: " + self.email)
#         print("  Location: " + self.location)
#
#     def greet_user(self):
#         """Display a personalized greeting to the user."""
#         print("\nWelcome back, " + self.username + "!")
#
#     def increment_login_attempts(self):
#         """Increment the value of login_attempts."""
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         """Reset login_attempts to 0."""
#         self.login_attempts = 0
#
#
# class Admin(User):
#     """A user with administrative privileges."""
#
#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the admin."""
#         super().__init__(first_name, last_name, username, email, location)
#
#         # Initialize an empty set of privileges.
#         self.privileges = Privileges()
#
#
# class Privileges():
#     """A class to store an admin's privileges."""
#
#     def __init__(self, privileges=[]):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print("\nPrivileges:")
#         if self.privileges:
#             for privilege in self.privileges:
#                 print("- " + privilege)
#         else:
#             print("- This user has no privileges.")
#
#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
#
# eric.privileges.show_privileges()
#
# print("\nAdding privileges...")
# eric_privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
# ]
# eric.privileges.privileges = eric_privileges
# eric.privileges.show_privileges()
#9-9
# class Car():
#     """A simple attempt to represent a car."""
#
#     def __init__(self, manufacturer, model, year):
#         """Initialize attributes to describe a car."""
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
#
# class Battery():
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=61):
#         """Initialize the batteery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 60:
#             range = 140
#         elif self.battery_size == 85:
#             range = 185
#
#         message = "This car can go approximately " + str(range)
#         message += " miles on a full charge."
#         print(message)
#
#     def upgrade_battery(self):
#         """Upgrade the battery if possible."""
#         if self.battery_size == 60:
#             self.battery_size = 85
#             print("Upgraded the battery to 85 kWh.")
#         else:
#             print("The battery is already upgraded.")
#
#
# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""
#
#     def __init__(self, manufacturer, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(manufacturer, model, year)
#         self.battery = Battery()
#
#
# print("Make an electric car, and check the battery:")
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# my_tesla.battery.describe_battery()
#
# print("\nUpgrade the battery, and check it again:")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
#
# print("\nTry upgrading the battery a second time.")
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()

# from restaurant import Restaurant
