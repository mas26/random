import cv2  #OpenCVのインポート
import numpy as np #numpyをnpという名前でインポート
import random #randomをインポート

#400要素X600要素X3要素で全要素の値が0の3次元配列を生成しオブジェクトimgに代入
img=np.zeros((1024, 1980, 3), np.uint8)

for i in range(100): #以下のインデント行を10回繰り返す
    x=int(random.uniform(10,1970)) #10以上590以下の乱数(浮動小数点型)を発生し、intで整数に変換、xとする
    y=int(random.uniform(10,1014)) #10以上390以下の乱数(浮動小数点型)を発生し、intで整数に変換、yとする　
    cv2.circle(img, (x, y), 10, (255, 255, 255), -1) #中心がx,y半径が10の水色の塗りつぶした円を描画


cv2.imshow("random_circle",img) #別ウィンドウを開き(ウィンドウ名 "random_circle")オブジェクトimgを表示
cv2.imwrite("random_circle.png",img) #画像をファイル名random_circle.pngで保存

cv2.waitKey(0) #キー入力待ち
cv2.destroyAllWindows() #ウインドウを閉じる