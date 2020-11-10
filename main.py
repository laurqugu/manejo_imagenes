"Manejo de imagenes"
import cv2

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
               'Ancho Original': height,
               'Alto Original': width
            }
        ]

        start_row = int(height*.15)
        start_col = int(width*.15)
        end_row = int(height*.85)
        end_col = int(width*.85)

        if height > 796 and width >= 1123:
            new_image = img[start_row:end_row, start_col:end_col]

            if height < width:
                orientacion = "Vertical"
            else:
                orientacion = "Horizontal"
        else:
            print("Redimensionar")
            new_image = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

            if height < width:
                orientacion = "Vertical"
            else:
                orientacion = "Horizontal"
        
        new_med = new_image.shape[0:2]
        
        info.append({'nuevo Ancho': new_med[0], 'nuevo alto': new_med[1], 'orientacion': orientacion})


        print(info)

if __name__ == '__main__':
    ProcesamientoImagenes.procesamiento()
