import cv2

def procesamiento():
    img = cv2.imread("img/animales.jpg")

    height, width = img.shape[0:2]

    if height < width and height > 796:
        orientation = "Vertical"

        startRow = int(height*.15)
        startCol = int(width*.15)
        endRow = int(height*.85)
        endCol = int(width*.85)

        croppedImage = img[startRow:endRow, startCol:endCol]

        cv2.imshow('Original Image', img)
        cv2.imshow('Cropped Image', croppedImage)
        cv2.waitKey(0)

    elif height > width and width > 1123:
        orientation = "Horizontal"
        startRow = int(height*.15)
        startCol = int(width*.15)
        endRow = int(height*.85)
        endCol = int(width*.85)

        croppedImage = img[startRow:endRow, startCol:endCol]

        cv2.imshow('Original Image', img)
        cv2.imshow('Cropped Image', croppedImage)
        cv2.waitKey(0)
    
    print(orientation, croppedImage.shape[0:2])

if __name__ == '__main__':
    procesamiento()

