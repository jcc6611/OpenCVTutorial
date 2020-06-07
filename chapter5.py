import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")

width, height = 250, 350
pts1King = np.float32([[170, 105], [325, 70], [215, 316], [368, 286]])
pts2King = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrixKing = cv2.getPerspectiveTransform(pts1King, pts2King)
imgOutputKing = cv2.warpPerspective(img, matrixKing,(width, height))

pts1Queen = np.float32([[519, 109],[643,203],[390, 277],[518, 365]])
matrixQueen = cv2.getPerspectiveTransform(pts1Queen, pts2King)
imgOutputQueen = cv2.warpPerspective(img, matrixQueen, (width, height))



cv2.imshow("Image", img)
cv2.imshow("Output King", imgOutputKing)
cv2.imshow("Output Queen", imgOutputQueen)

cv2.waitKey(0)
