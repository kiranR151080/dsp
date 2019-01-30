import matplotlib.pyplot as plot
import math
import numpy as np
f1=input("enter the first freqancy")
f2=input("enter the second freqancy")
if(f1>f2):
    fs=2*f1
else:
    fs=2*f2
p=0
p1=0
a=input("enter the amplitude of sine wave")
a1=input("enter the amplitud of cos wave")
t=np.arange(0,0.1,0.0001)
x=a*(np.sin(((2*(math.pi)*f1*t)/fs)+p))
y=a1*(np.cos(((2*(math.pi)*f2*t)/fs)+p1))
z=x+y
plot.subplot(311)
plot.xlabel("frequancy")
plot.ylabel("amplitude")
plot.plot(t,x)
plot.subplot(312)
plot.xlabel("frequancy")
plot.ylabel("amplitude")
plot.plot(t,y)
plot.subplot(313)
plot.xlabel("frequancy")
plot.ylabel("amplitude")
plot.plot(t,z)
plot.show()




