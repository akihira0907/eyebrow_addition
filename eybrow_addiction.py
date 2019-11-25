# -*- coding: <utf-8> -*-
import cv2
import sys
import numpy as np
import csv

def main(img_path, landmark_path):
    # 画像読み込み
    img = cv2.imread(img_path)
    if img is None:
        print("Failed to load image.")

    # Landmark読み込み
    csv_file = open(landmark_path)
    reader = csv.reader(csv_file)
    l = [row for row in reader]
    # strからfloatへ,floatからintへ
    landmarks_x = list(map(float, l[1][296:364]))
    landmarks_y = list(map(float, l[1][364:432]))
    landmarks_x = list(map(int, landmarks_x))
    landmarks_y = list(map(int, landmarks_y))

    # 眉毛のランドマーク取得
    eyebrows_landmarks = []
    for i in range(17, 27):
        eyebrows_landmarks.append((landmarks_x[i], landmarks_y[i]))
    print(eyebrows_landmarks)

    # 指定されたピクセルの周囲を黒くする(3chあることに注意)
    size = 20
    for x, y in eyebrows_landmarks:
        img[y-size:y+size, x-size:x+size, :] = 0

    # 画像書き出し
    output_filename = "output.jpg"
    ret = cv2.imwrite(output_filename, img)
    if not ret:
        print("Failed to write image.")
    
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print("Invalid syntax.")
        sys.exit()
    img_path = args[1]
    landmark_path = args[2]
    main(img_path, landmark_path)

