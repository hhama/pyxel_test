import pyxel

class TextApp:
    def __init__(self):
        pyxel.init(160, 120, title="Mouse Checker")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(7)
        pyxel_table = [hex(x) for x in pyxel.colors.to_list()]
        y = 3
        for idx, color in enumerate(pyxel_table):
            pyxel.text(55, y, color, idx)
            y += 7

class ImageApp:
    def __init__(self):
        pyxel.init(160, 120, title="Hello Pyxel")
        pyxel.load("./hamada.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        old_colors = pyxel.colors.to_list()
        pyxel.colors[8] = old_colors[pyxel.frame_count % 16]
        x = (pyxel.frame_count * 2) % 160
        y = (int(pyxel.frame_count / 80) * 10) % 120
        pyxel.blt(x, y, 0, 0, 0, 16, 16)
        # pyxel.text(16, 40, f"{y}", 7)

# ImageApp()
TextApp()
