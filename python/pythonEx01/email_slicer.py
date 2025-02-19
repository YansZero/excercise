# Email字串分析

email = "abc.test@demo.com"
index = email.index("@")
print("@位置在:", index)
print("email帳號為:",email[:index])
print("email網域為:",email[index+1:])