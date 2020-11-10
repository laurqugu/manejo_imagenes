"Manejo de imagenes"
import cv2
import imutils

class ProcesamientoImagenes(object):
    "Implementar casos"

    @classmethod
    def procesamiento(cls, image:str):
        "Se realiza el procesamiento de las imágenes"
        img = cv2.imread(f"uploads/{image}")

        height, width = img.shape[0:2]

        return cls.updateimages(img, height, width)

    @classmethod
    def updateimages(cls, img, height, width):
        "Se realizan las validaciones"

        info = [
           { 
               'Ancho Original': width,
               'Alto Original': height
            }
        ]

        start_row = int(height*.15)
        start_col = int(width*.15)
        end_row = int(height*.85)
        end_col = int(width*.85)

        if height > width:
            orientacion = "Vertical"

            if height > 1123 and width > 796:
                new_image = img[start_row:end_row, start_col:end_col]
            elif height > 1123:
                print("Redimensionar")
                new_image = imutils.resize(img, height=1123)
            else:
                new_image = img
                
        else:
            orientacion = "Horizontal"

            if height > 796 and width > 1123:
                new_image = img[start_row:end_row, start_col:end_col]
            elif width > 1123:
                print("Redimensionar")
                new_image = imutils.resize(img, width=1123)
            else:
                new_image = img
        
        new_med = new_image.shape[0:2]
        
        info.append({'nuevo Alto': new_med[0], 'nuevo Ancho': new_med[1], 'orientacion': orientacion})


        print(info)

if __name__ == '__main__':
    ProcesamientoImagenes.procesamiento()
