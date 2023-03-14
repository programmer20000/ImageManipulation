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

    def resize_image(self):
        if not os.path.exists('new_image'):
            os.mkdir('new_image')

        self.select_image()
        try:
            self.size = map(int,input('Please enter width and height:\n').split(' '))
            self.new_name_image = input('Please new name image: \n')
            self.new_image = self.path_image.resize(size=tuple(self.size))
            self.new_image.save(f'new_image/{self.new_name_image}')

        except ValueError:
            print('Please enter correct dates')

    def create_image(self, mode: str = 'RGB', size: tuple = (100, 100), color='blue', name='image.jpg'):
        """this inputs are for  query user  parameters for create image"""
        self.image = Image.new(mode=mode, size=size, color=color)
        self.image.save(name)

    def select_variance(self):
        self.variance = input('Please select variance: 1:[resize image] 2:[create image] 3:[exit program]\n')

        match self.variance:
            case '1':
                return self.resize_image()
            case '2':
                ...
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
