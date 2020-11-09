"Manejo de imagenes"
import cv2

class ProcesamientoImagenes(object):
    "Implementar casos"

    @classmethod
    def procesamiento(cls):
        "Se realiza el procesamiento de las imágenes"
        img = cv2.imread("img/animales.jpg")

        height, width = img.shape[0:2]

        return cls.updateimages(img, height, width)

    @classmethod
    def updateimages(cls, img, height, width):
        "Se realizan las validaciones"

        start_row = int(height*.15)
        start_col = int(width*.15)
        end_row = int(height*.85)
        end_col = int(width*.85)

        if height < width:
            orientation = "Vertical"
            if height > 796:
                cropped_image = img[start_row:end_row, start_col:end_col]

                cv2.imshow('Cropped Image', cropped_image)
                cv2.waitKey(0)

        elif height > width:
            orientation = "Horizontal"
            if width > 1123:
                cropped_image = img[start_row:end_row, start_col:end_col]

                cv2.imshow('Cropped Image', cropped_image)
                cv2.waitKey(0)

        elif height <= 796 and width > 1123:
            new_img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
            cv2.imshow('Resized Image', new_img)
            cv2.waitKey(0)

        print(orientation, cropped_image.shape[0:2])