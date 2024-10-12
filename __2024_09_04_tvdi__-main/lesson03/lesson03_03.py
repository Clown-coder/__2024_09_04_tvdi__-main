import tools

print(tools.SUN)
print("==============================")
p1 =tools.Person(name = "Ken", age=20)
print(p1)


#輸入時出現板手就表示 property
#只有method 要記得加上 括號

s1 = tools.Student('Ken',20,98,97,99)

print(f'Chinese: {s1.chinese}\nEnglish: {s1.english}\nMath: {s1.math}\nTotal: {s1.total}\nAvg: {s1.average()}')

print("==============================")
p2 = tools.get_person('Didigo',45)
print(p2,type(p2))

print('========================')

s2 = tools.get_student('Otani',20)
print(type(s2))
print(f'Chinese: {s2.chinese}\nEnglish: {s2.english}\nMath: {s2.math}\nTotal: {s2.total}\nAvg: {s2.average()}')