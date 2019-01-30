import matplotlib.pyplot as plot
import math
import numpy as np
f1=input("enter the first freqancy")
f2=input("enter the second freqancy")
p1=0
p=0
a=input("enter the amplitude of sine wave")
a1=input("enter the amplitud of cos wave")
t=np.arange(0,0.1,0.0001)
x=a*(np.sin((2*(math.pi)*f1*t)+p))
y=a1*(np.sin((2*(math.pi)*f2*t)+p1))
z=x+y
plot.subplot(311)
plot.plot(t,x)
plot.subplot(312)
plot.plot(t,y)
plot.subplot(313)
plot.plot(t,z)
plot.show()




