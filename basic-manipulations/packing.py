from datetime import date

new_date = (2013, 3, 15)
print(date(*new_date).year) # 2013
print(date(*new_date).month) # 3
print(date(*new_date).day) # 15

def new_user(active = False, admin = False):
    print(active)
    print(admin)

config = {'active': False, 'admin': True}

new_user(**config) # False True