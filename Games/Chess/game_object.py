class GameObject():
    def __init__(self, pos=(0, 0), size=(0, 0), enabled=True, visible=True):
        self.pos = pos
        self.size = size
        self.enabled = enabled
        self.visible = visible
