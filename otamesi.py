from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Tex("Hello World !")
        self.add(text)