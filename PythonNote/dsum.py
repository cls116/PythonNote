# Param : name, age
# execution condition
# 10살 미만 : 안녕^^
# 10살 ~ 20살 미만 : 반가워^^
# 20살 이상 : "안녕하세요"

def sayhello(name, age):
    if age < 10:
        print("안녕^^ " + name)
    elif age > 9 and age < 20:
        print("반가워^^ " + name)
    elif age > 19 and age < 60:
        print("안녕하세요 " + name)
    else:
        print("안녕하시오니이까 " + name)

s = sayhello

s("현정", 4)
s("해식", 9)
s("희령", 22)
s("엄마님", 60)
