# import time
# from datetime import datetime
# ep = time.time()
# print(ep)
#
# s =time.ctime(ep)
# print(s)
# s =datetime.now()
# print(s)
from datetime import datetime
# from datetime import *
# import time
# # x = int(input('Enter Your Value Here:'))
#
# # str = datetime.strptime(x,'%Y/%m/%d %H:%M:%S')
# xh = time.ctime()
# x = datetime(xh - timedelta(hours=2))
# print(x)



l =[1,32,3,4,5,6,3,7,8]
f = list(map(lambda x:x*x,l))
print(f)