import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    
    imgLinear = cv2.imread('Linear.jpg',0)
    imgLogaritmo = cv2.imread('Logaritmo.jpg',0)
    imgQuadrado = cv2.imread('Quadrado.jpg',0)
    imgRaiz = cv2.imread('Raiz_Quadrada.jpg', 0)
    imgExp = cv2.imread('Exponencial.jpg', 0)
    
    
    print('##############################################################')
    print('HISTOGRAMA - TRANSFORMACAO LINEAR')
    plt.hist(imgLinear.ravel(), 256, [0,256]);plt.show()
    print('##############################################################')

    print('HISTOGRAMA - TRANSFORMACAO LOGARITMO')
    plt.hist(imgLogaritmo.ravel(), 256, [0,256]);plt.show()
    print('##############################################################')

    print('HISTOGRAMA - TRANSFORMACAO QUADRADO')
    plt.hist(imgQuadrado.ravel(), 256, [0,256]);plt.show()
    print('##############################################################')
    
    print('HISTOGRAMA - TRANSFORMACAO RAIZ QUADRADA')
    plt.hist(imgRaiz.ravel(), 256, [0,256]);plt.show()
    print('##############################################################')

    print('HISTOGRAMA - TRANSFORMACAO EXPONENCIAL')
    plt.hist(imgExp.ravel(), 256, [0,256]);plt.show()
    print('##############################################################')

###############################################################################
if __name__ == "__main__":
    main()
