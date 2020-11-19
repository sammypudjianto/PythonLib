import unittest

from asset_loader import AssetLoader


class TestAssetLoader(unittest.TestCase):

    def setUp(self):
        self.loader = AssetLoader()

    def test_is_singleton(self):
        loader2 = AssetLoader()
        self.assertEqual(self.loader, loader2)

    def test_walk_left_sprites(self):
        walk_left_animation = self.loader.load_walk_left_sprites()
        self.assertEqual(9, len(walk_left_animation))

    def test_walk_right_sprites(self):
        walk_right_animation = self.loader.load_walk_right_sprites()
        self.assertEqual(9, len(walk_right_animation))

    def test_walk_left_enemy_sprites(self):
        walk_left_animation = self.loader.load_enemy_walk_left_sprites()
        self.assertEqual(11, len(walk_left_animation))

    def test_walk_right_enemy_sprites(self):
        walk_right_animation = self.loader.load_enemy_walk_right_sprites()
        self.assertEqual(11, len(walk_right_animation))

    # def test_background_load(self):
    #     bg = self.loader.load_background()
    #     self.assertEqual(1, len(bg))


if __name__ == '__main__':
    unittest.main()
