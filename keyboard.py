from button import Button


class Keyboard:

    def __init__(self, window):
        self.window = window
        self.buttons = []

    def create(self):
        # keyboard top row
        letters = 'QWERTYUIOP'
        offset_left = 10
        offset_top = self.window.get_height() - 50 - (10 * 2) - (30 * 3)
        for ltr in letters:
            self.buttons.append(Button(self.window, ltr, 0, offset_left,
                                       offset_top, 20, 30, 16))
            offset_left += 25

        # keyboard mid row
        letters = 'ASDFGHJKL'
        offset_left = 25
        offset_top += 40
        for ltr in letters:
            self.buttons.append(Button(self.window, ltr, 0, offset_left,
                                       offset_top, 20, 30, 16))
            offset_left += 25

        # keyboard bottom row
        offset_left = 15
        offset_top += 40
        enter_button = Button(self.window, 'Enter', 0,
                              offset_left, offset_top, 30, 30, 10)
        offset_left += 35
        self.buttons.append(enter_button)

        letters = 'ZXCVBNM'
        for ltr in letters:
            self.buttons.append(Button(self.window, ltr, 0, offset_left,
                                       offset_top, 20, 30, 16))
            offset_left += 25

        back_button = Button(self.window, 'Back', 0,
                             offset_left, offset_top, 30, 30, 10)
        self.buttons.append(back_button)

    def render(self):
        for btn in self.buttons:
            btn.render()

    def find_button(self, pos):
        for btn in self.buttons:
            command = btn.check_click(pos)
            if command:
                return command

    def apply_themes(self, letter_themes):
        for btn in self.buttons:
            char = btn.get_text()
            if char in letter_themes:
                btn.set_theme(letter_themes[char])
