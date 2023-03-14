import os

from PIL import Image


class ImageManipulator:
    def __init__(self):
        self.title = ''

    def select_image(self):
        """it method is for query path to image"""
        try:
            self.path_image_input = input('Please enter path your image:\n')
            self.path_image = Image.open(self.path_image_input)

        except ValueError:
            return 'incorrect path to image please check path'

    def create_folder(self,name_folder):
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)

    def resize_image(self):
        self.create_folder('new_image')

        self.select_image()
        try:
            self.new_size_image = map(int, input('Please enter width and height:\n').split(' '))
            self.new_name_image = input('Please new name image: \n')
            self.new_image = self.path_image.resize(size=tuple(self.new_size_image))
            self.new_image.save(f'new_image/{self.new_name_image}')

        except ValueError:
            print('Please enter correct dates')

    def create_image(self, mode: str = 'RGB', size: tuple = (100, 100), color='blue', name='image.jpg'):
        """this method is for created images"""
        self.create_folder('created_images')
        self.image = Image.new(mode=mode, size=size, color=color)
        self.image.save(f'created_images/{name}')

    def select_variance(self):
        self.variance = input('Please select variance: 1:[resize image] 2:[create image] 3:[exit program]\n')

        match self.variance:
            case '1':
                return self.resize_image()
            case '2':
                self.color_mode = input('Please enter color mode it can be RGB:\n')
                self.new_size = map(int, input('Please enter width and height:\n').split(' '))
                self.color = map(int, input('Please enter color:\n').split(' '))
                self.name = input('Please enter name:\n')
                self.create_image(mode=self.color_mode, size=tuple(self.new_size), color=tuple(self.color),
                                  name=self.name)
            case '3':
                self.exit_program()
            case _:
                print('variance not found')

    def exit_program(self):
        self.exit = input('Your’s want exit from program ? \n if yes enter (y) or enter (n) for continue program: ')
        while True:
            match self.exit:
                case 'y':
                    self.select_variance()
                case 'n':
                    break


if __name__ == '__main__':
    image_manipulator = ImageManipulator()
    image_manipulator.select_variance()
