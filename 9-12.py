from restaurant import Restaurant
from user import Admin

my_res = Restaurant('x','y')
my_res.describe_restaurant()

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()