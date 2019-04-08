import cv2
import numpy as np
import math as m
def main():
    
    #img = cv2.imread('lenna_low_contrast.png')
    #img = cv2.imread('contrast01.jpg')
    img = cv2.imread('helena.jpg',0)

    #cv2.imwrite('Linear.jpg' ,linear(img, [40, 150]))
    #cv2.imwrite('Logaritmo.jpg', logaritmo(img))
    cv2.imwrite('Exponencial.jpg', exponencial(img))
    #cv2.imwrite('Quadrado.jpg', quadrado(img))
    #cv2.imwrite('Raiz_Quadrada.jpg', raiz_quadrada(img))

###############################################################################

def linear(f,new_interval):
    
    #plt.imshow(f, cmap='gray', vmin=0, vmax=255)
    #plt.pause(0.2)
    #plt.hist(np.ndarray.flatten(f),256,range=(0,255));
    
    
    size = f.shape
    g = np.zeros(size)
    
    f_max = np.amax(f)
    f_min = np.amin(f)
    
    g_min = new_interval[0]
    g_max = new_interval[1]
    
    a = (g_max-g_min)/(f_max-f_min)
    
    for i in range(size[0]):
        for j in range(size[1]):
            g[i,j] = a*(f[i,j]-f_min)+g_min
            
    #plt.pause(0.2)
    #plt.imshow(g, cmap='gray', vmin=0, vmax=255)
    #plt.pause(0.2)
    #plt.hist(np.ndarray.flatten(g),256,range=(0,255));
    return g

###############################################################################

def logaritmo(f):
    
    
    size = f.shape
    g = np.zeros(size)
    
    f_max = np.amax(f)
    
    a = 255/(np.log(1+f_max))
    
    for i in range(size[0]):
        for j in range(size[1]):
            g[i, j] = a*np.log(f[i,j]+1)


    return g

###############################################################################

def exponencial(f):
    
    size = f.shape
    g = np.zeros(size)

    f_max = np.amax(f)
    
    a=255/(np.log(1+f_max))
    
    #a=1
    
    for i in range(size[0]):
        for j in range(size[1]):
            #g[i, j] = a*( np.exp(f[i, j]) -1)
            g[i, j] = a*( m.exp(f[i, j]) -1)

    return g

###############################################################################

def quadrado(f):
    size = f.shape
    g = np.zeros(size)

    f_max = np.amax(f)
    
    a=255/(np.log(1+f_max))
    
    for i in range(size[0]):
        for j in range(size[1]):
            g[i, j] = a*(np.power(f[i,j],2))

    return g    
    
###############################################################################

def raiz_quadrada(f):
    size = f.shape
    g = np.zeros(size)

    f_max = np.amax(f)
    
    a=255/(np.log(1+f_max))
    
    for i in range(size[0]):
        for j in range(size[1]):
            g[i, j] = a*(np.power(f[i,j],(1/2)))

    return g    

###############################################################################
if __name__ == "__main__":
    main()
