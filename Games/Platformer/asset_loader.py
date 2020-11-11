import os

import pygame as p


class AssetLoader():
    """
    Scan asset folders and import images
    """
    ASSETSPATH = './Assets/'
    PNGEXT = '.png'

    def __init__(self):
        if os.path.exists(AssetLoader.ASSETSPATH):
            self.files = os.listdir(AssetLoader.ASSETSPATH)
        else:
            raise OSError('unable to find ' + AssetLoader.ASSETSPATH)

    def __load_sprites(self, ext_filter, name_filter):
        player_sprites = []
        for file in self.files:
            name, ext = os.path.splitext(file)
            file_relpath = AssetLoader.ASSETSPATH + file
            if name_filter != '':
                if (
                    ext == ext_filter and
                    name[len(name_filter) - 1] == name_filter
                    ):
                    player_sprites.append(p.image.load(file_relpath))
            elif ext == ext_filter:
                player_sprites.append(p.image.load(file_relpath))
        return player_sprites

    def load_walk_left_sprites(self):
        return self.__load_sprites('.png', 'L')

    def load_walk_right_sprites(self):
        return self.__load_sprites('.png', 'R')

    def load_background(self):
        return self.__load_sprites('.png', 'bg')


l = AssetLoader()
x = l.load_walk_left_sprites()
print(x)
