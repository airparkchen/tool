#random radius noise
import cv2
import numpy as np
import random
import time

def noisy(img, color_pick, num_noises ):
    height, width, _ = img.shape

    for _ in range(num_noises):
    # 隨機選擇半徑和圓心
        radius = random.randint(5, 20)
        center = (random.randint(0, width-1), random.randint(0, height-1))
    
    # 隨機選擇顏色 (白色或黑色)
        if color_pick == 1:
            color = [(0,0,0), (255,255,255)][random.randint(1,1)]
        if color_pick == 0:
            color = [(0,0,0), (255,255,255)][random.randint(0,0)]
        if color_pick == 2:
            color = [(0,0,0), (255,255,255)][random.randint(0,1)]
        # 在影像上繪製圓形
        cv2.circle(img, center, radius, color, -1)
    return img

random.seed(time.time())
img_path = '01.jpg'
# 讀取影像
img = cv2.imread(img_path)

# 取得影像的高度和寬度
height, width, _ = img.shape

# 定義添加噪點的數量
num_noises = 100

img = noisy(img, 1, num_noises)

# 顯示和保存結果影像
# cv2.imshow('Noisy Image', img)
cv2.imwrite(f'noisy_{img_path}.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
