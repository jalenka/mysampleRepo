
#test header
# test on site

def testApp(a):
    a=a+2+1+3 #create conflict by adding +3 in login
    return a
a=1
a=a+1
a=testApp(5)
print(a)

#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
