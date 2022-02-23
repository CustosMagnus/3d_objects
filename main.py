import cv2 as cv
import numpy as np
import math

class main():
    def __init__(self):
        # Canvas
        self.x_shape = 500
        self.y_shape = 500
        # Circle -> (x-M_x)**2 + (y-M_y)**2 + (z)**2 = radius**2 -> M_z == 0
        self.M_x = 250
        self.M_y = 250
        self.M_z = 0
        self.radius = 100
        # light source
        self.ls_M_x = 400
        self.ls_M_y = 0
        self.ls_M_z = -100
    def processed(self, img):
        # where is the circle
        for x in range(len(img)):
            for y in range(len(img[x])):
                if math.sqrt((abs(x - self.M_x))**2+(abs(y - self.M_y))**2) < self.radius:
                    img[x][y] = [255, 255, 255]
                    z = math.sqrt(self.radius ** 2 - (y - self.M_y) ** 2 - (x - self.M_x) ** 2)
                    # perpendicular line = [x-self.M_x, y-self.M_y, z-self.M_z]*t+[x, y, z]
                    # light ray line = [x-self.ls_M_x, y-self.ls_M_y, z-self.ls_M_z]*t+[self.ls_M_x, self.ls_M_y, self.ls_M_z]
                    # folgende formel rechnet den einfallswinkel bzw ausfallswinkel des lichtstrahls auf die Kugeloberfläche aus
                    # alpha ist in radians gemessen
                    # https://www.mathe-online.at/materialien/Andreas.Pester/files/Vectors/winkel_zwischen_vektoren.htm
                    alpha = math.acos(((x - self.M_x) * (x - self.ls_M_x) + (y - self.M_y) * (y - self.ls_M_y) + (z-self.M_z) * (z - self.ls_M_z)) / (math.sqrt((x-self.M_x)**2+(y-self.M_y)**2+(z-self.M_z)**2)*math.sqrt((x-self.ls_M_x)**2+(y-self.ls_M_y)**2+(z-self.ls_M_z)**2)))
                    # die brechungsgerade schaffe ich nicht zu berechnen siehe das Bild im repo

        return img

    def show(self):
        img = np.zeros(shape=[self.x_shape, self.y_shape, 3], dtype=np.uint8)
        img = self.processed(img)
        cv.namedWindow('image')
        cv.imshow('image', img)
        k = cv.waitKey(0) & 0xFF

        cv.destroyAllWindows()

if __name__ == '__main__':
    a = main()
    a.show()