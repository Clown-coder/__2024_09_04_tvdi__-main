import widget
#import 進來的方法不用 括號
from widget import get_person,get_student


#引用常數
print(widget.MON)

#因為是從 widget import 進來所以不用 在打widget.get_person()
#如下

s1 = get_student("Helen",18)
print(s1)
print(s1.total)
print(s1.average())