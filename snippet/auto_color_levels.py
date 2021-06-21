import numpy as np
import cv2

'''
    Algorithm of Brightness Contrast transformation
    The formula is:
        y = [x - 127.5 * (1 - B)] * k + 127.5 * (1 + B);
        x is the input pixel value
        y is the output pixel value
        B is brightness, value range is [-1,1]
        k is used to adjust contrast
            k = tan( (45 + 44 * c) / 180 * PI );
            c is contrast, value range is [-1,1]
'''

def auto_color_levels(imgfile):
    img = cv2.imread(imgfile)
    cv2.imshow('src', img)

    inBlack = np.array([0,0,0], dtype=np.float32)
    inWhite = np.array([255, 255, 255], dtype=np.float32)
    inGama = np.array([1.0, 1.0, 1.0], dtype=np.float32)

    outBlack = np.array([0, 0, 0], dtype=np.float32)
    outWhite = np.array([200, 200, 200], dtype=np.float32)

    img = np.clip((img - inBlack) / (inWhite - inBlack), 0, 255)
    img = (img ** (1/inGama)) * (outWhite - outBlack) + outBlack
    img = np.clip(img, 0, 255).astype(np.uint8)
    cv2.imshow('result', img)
    cv2.waitKey()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    auto_color_levels('E:/Media/images/sand2.jpg')

