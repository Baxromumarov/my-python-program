import random
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
# symbol = "[]{}!$%^&*()-_"
all = lower + upper + number
length = 8
password = "".join(random.sample(all,length))
print("The Password you Generated is : ",password)