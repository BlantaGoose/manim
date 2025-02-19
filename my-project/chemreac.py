from manim import *

class WaterFormation(Scene):
    def construct(self):
        h2 = VGroup(Circle(radius=0.2, color=BLUE).shift(LEFT*0.3),
                    Circle(radius=0.2, color=BLUE).shift(RIGHT*0.3))
        o2 = VGroup(Circle(radius=0.3, color=RED).shift(LEFT*0.5),
                    Circle(radius=0.3, color=RED).shift(RIGHT*0.5))

        h2.move_to(LEFT*3)
        o2.move_to(RIGHT*3)

        arrow = MathTex(r"\rightarrow").move_to(ORIGIN)

        h2o = VGroup(Circle(radius=0.3, color=RED),
                     Circle(radius=0.2, color=BLUE).shift(LEFT*0.4 + DOWN*0.3),
                     Circle(radius=0.2, color=BLUE).shift(RIGHT*0.4 + DOWN*0.3))
        h2o.move_to(RIGHT*3)

        self.play(FadeIn(h2, o2))
        self.wait(1)
        self.play(Write(arrow))
        self.wait(1)
        self.play(Transform(VGroup(h2, o2), h2o))  # 分子の変化
        self.wait(2)
