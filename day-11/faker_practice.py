import random
from faker import Faker
fake=Faker()
# print(fake.name())
# print(fake.email())
# print(fake.address())


# print(fake.first_name())
# print(fake.last_name())
# print(fake.phone_number())
# print(fake.date_of_birth())

# print(fake.address())
# print(fake.city())
# print(fake.state())
# print(fake.country())
# print(fake.postalcode())

# print(fake.user_name())
# print(fake.domain_name())
# print(fake.url())
# print(fake.ipv4())

# print(fake.job())
# print(fake.company())

# print(fake.random_int(min=1,max=100))
# print(fake.texts())
# print(fake.words())
# print(fake.sentence())


# user=[]
# for _ in range(3):
#     user.append({
#         "name":fake.name(),
#         "email":fake.email(),
#         "city":fake.city()
#     })
    
# print(user)

def invalid_ip():
    return f"{random.randint(256,999)}.{random.randint(256,999)}.{random.randint(256,999)}.{random.randint(256,999)}"