
class Controls:

    def __init__(self, screen_attribute, paddle):

        self.window = screen_attribute
        self.paddle = paddle
        self.keys = {"w":False,"s":False,"Up":False,"Down":False}
        self.window_listen()
        self.move()

    def window_listen(self):
        """on screen listen"""
        self.window.listen()
        self.window.onkeypress(lambda: self.press_key("w"), "w")
        self.window.onkeyrelease(lambda: self.release_key("w"), "w")
        self.window.onkeypress(lambda: self.press_key("s"), "s")
        self.window.onkeyrelease(lambda: self.release_key("s"), "s")

        self.window.onkeypress(lambda: self.press_key("Up"), "Up")
        self.window.onkeyrelease(lambda: self.release_key("Up"), "Up")
        self.window.onkeypress(lambda: self.press_key("Down"), "Down")
        self.window.onkeyrelease(lambda: self.release_key("Down"), "Down")

    def press_key(self,key):
        self.keys[key] = True

    def release_key(self, key):
       self.keys[key] = False

    def move(self):

        if self.keys["w"]:
            self.paddle.left_up()
        if self.keys["s"]:
            self.paddle.left_down()
        if self.keys["Up"]:
            self.paddle.right_up()
        if self.keys["Down"]:
            self.paddle.right_down()

        self.window.update()
        self.window.ontimer(self.move, 50)