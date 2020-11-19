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
        player_sprites = []
        regex = re.compile(file_filter)
        filtered_files = list(filter(regex.search, self.files))

        if len(filtered_files) > 1:
            number_regex = re.compile(r'(\d+)')
            filtered_files = sorted(
                filtered_files,
                key=lambda x: int(number_regex.search(x)[0])
            )

        for file in filtered_files:
            file_relpath = self.ASSETSPATH + file
            try:
                player_sprites.append(p.image.load(file_relpath))
            except p.error as message:
                print('cannot load image:', file_relpath)
                raise SystemExit(message)

        return player_sprites

    def load_walk_left_sprites(self):
        return self.__load_sprites('L[0-9].png')

    def load_walk_right_sprites(self):
        return self.__load_sprites('R[0-9].png')

    def load_background(self):
        return self.__load_sprites('bg.jpg').pop()

    def load_character(self):
        return self.__load_sprites('standing.png')

    def load_enemy_walk_left_sprites(self):
        return self.__load_sprites('L[0-9]{1,2}E.png')

    def load_enemy_walk_right_sprites(self):
        return self.__load_sprites('R[0-9]{1,2}E.png')

    def load_bullet_sound(self):
        return p.mixer.Sound(self.ASSETSPATH + 'bullet.mp3')

    def load_hit_sound(self):
        return p.mixer.Sound(self.ASSETSPATH + 'hit.mp3')

    def load_music(self):
        return p.mixer.Sound(self.ASSETSPATH + 'music.mp3')
