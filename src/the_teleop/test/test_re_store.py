from writebag import *
from readbag import *

ls=["/odom","1",genpy.Time(1,0),String()]
ls2=["/odom","2",genpy.Time(2,0),String()]
ls3=["/odom","3",genpy.Time(3,0),String()]
ls4=["/odom","4",genpy.Time(4,0),String()]
ls5=["/odom","5",genpy.Time(5,0),String()]
store_dict=dict([("1",ls),("2",ls2),("3",ls3),("4",ls4),("5",ls5)])
store(store_dict, "test")
r=restore()
if r==store_dict:
	print "ok"
else:
	print "wroghtsasd"
print r
print store_dict