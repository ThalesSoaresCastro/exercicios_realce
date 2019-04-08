#   Equalizacao de histograma
import cv2
import numpy as np

def main():

    #img = cv2.imread('img.png')
    img = cv2.imread('contrast01.jpg')
    
    cv2.imshow('imagem Original', img)
    cv2.imshow('equalizacao', equalizacao(img)) 
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def equalizacao(img):

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    
    equalizacao_hist = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return equalizacao_hist


if __name__ == "__main__":
    main()
