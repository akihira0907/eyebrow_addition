# -*- coding: <utf-8> -*-
import cv2
import sys
import numpy as np
import csv

def main(img_path, landmark_path):
    # $B2hA|FI$_9~$_(B
    img = cv2.imread(img_path)
    if img is None:
        print("Failed to load image.")

    # Landmark$BFI$_9~$_(B
    csv_file = open(landmark_path)
    reader = csv.reader(csv_file)
    l = [row for row in reader]
    # str$B$+$i(Bfloat$B$X(B,float$B$+$i(Bint$B$X(B
    landmarks_x = list(map(float, l[1][296:364]))
    landmarks_y = list(map(float, l[1][364:432]))
    landmarks_x = list(map(int, landmarks_x))
    landmarks_y = list(map(int, landmarks_y))

    # $BH}LS$N%i%s%I%^!<%/<hF@(B
    eyebrows_landmarks = []
    for i in range(17, 27):
        eyebrows_landmarks.append((landmarks_x[i], landmarks_y[i]))
    print(eyebrows_landmarks)

    # $B;XDj$5$l$?%T%/%;%k$N<~0O$r9u$/$9$k(B(3ch$B$"$k$3$H$KCm0U(B)
    size = 20
    for x, y in eyebrows_landmarks:
        img[y-size:y+size, x-size:x+size, :] = 0

    # $B2hA|=q$-=P$7(B
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

