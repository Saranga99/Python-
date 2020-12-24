import cv2
import numpy as np
from pyzbar.pyzbar import decode
import xlrd
from xlwt import Workbook

# img = cv2.imread('2.png')
fileLocation = ("output.xlsx")
capture = cv2.VideoCapture(0)
cv2.namedWindow("cam")
capture.set(3, 480)
capture.set(4, 480)
counter = 0
wb = Workbook()
sheet1 = wb.add_sheet("sheet1")
while True:
    success, img = capture.read()

    for barcode in decode(img):
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape(-1, 1, 2)
        points2 = barcode.rect
        cv2.polylines(img, [points], True, (0, 0, 255), 3)
        print(barcode.data)
        myData = barcode.data.decode("utf-8")
        print(myData)
        print(img)
        sheet1.write(counter, 0, myData)
        counter = counter + 1
        print(counter)
        print(sheet1)
        wb.save('output.xls')

    cv2.imshow("Result", img)
    cv2.waitKey(1)
