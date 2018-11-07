class CameraSensob(Sensob):

    def __init__(self):
        camera = Camera(128, 30)
        super(CameraSensob, self).__init__(camera)

    def update(self):
        super().update()
        self.interpret_image()

    def interpret_image(self):
        camera = self.sensors
        image = camera.value # the matrix of pixels
        occurrence_array = [0 for i in range(128)]

        for h in range(camera.img_height):
            for w in range(camera.img_width):
                pixel = image.getpixel(w,h)
                r,g,b = pixel[0], pixel[1], pixel[2]
                if (r >= 180 and g < 45 and b < 45):
                    occurrence_array[w] += 1

        return (CameraSensob.max_index(occurrence_array) - camera.img_width)/camera.img_width #returns a value between -1 and 1

    @staticmethod
    def max_index(list):
        highest_index = 0
        for i in range(1, len(list)):
            if list[i] > list[highest_index]:
                highest_index = i
        return highest_index
