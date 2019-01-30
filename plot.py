import matplotlib.pyplot as plot
import math
import numpy as np
f1=input("enter the first freqancy")
f2=input("enter the second freqancy")
a=1
a1=2
t=np.arange(0,0.1,0.0001)
x=a*(np.sin((2*(math.pi)*f1*t))
x1=a*(np.sin((2*(math.pi)*f2*t))
y=x+x1
plot.subplot(311)
plot.plot(t,x)
plot.subplot(312)
plot.plot(t,x1)
plot.subplot(313)
plot.plot(t,y)
plot.show()




