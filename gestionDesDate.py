#coding: utf-8

import datetime

d1 =datetime.datetime(2018,10,31)
d2 =datetime.datetime(2018,10,30)

if d1 < d2:
	print("d1 est plus ancien que d2")

else:
	print("d1 est plus recent que d2")
