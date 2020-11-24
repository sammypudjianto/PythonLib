import os
import re

import pygame as p


class AssetLoader():
    """
    Scan asset folders and import images
    """
    ASSETSPATH = './Assets/'
    PNGEXT = '.png'
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AssetLoader, cls).__new__(cls)
            if os.path.exists(AssetLoader.ASSETSPATH):
                cls._instance.files = os.listdir(AssetLoader.ASSETSPATH)
            else:
                raise OSError('unable to find ' + AssetLoader.ASSETSPATH)
        return cls._instance

    def __load_sprites(self, file_filter):
        player_sprites = {}
        regex = re.compile(file_filter)
        filtered_files = list(filter(regex.search, self.files))

        for file in filtered_files:
            file_relpath = self.ASSETSPATH + file
            try:
                player_sprites[file[1]] = p.image.load(file_relpath)
            except p.error as message:
                print('cannot load image:', file_relpath)
                raise SystemExit(message)

        return player_sprites

    def load_white_pieces(self):
        return self.__load_sprites('^w(.{1}).png$')

    def load_black_pieces(self):
        return self.__load_sprites('^b(.{1}).png$')
