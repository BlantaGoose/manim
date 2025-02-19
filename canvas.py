from manim import *
from manim_slides import Slide

class CanvasExample(Slide):
    def update_canvas(self):
        self.counter += 1
        old_slide_number = self.canvas["slide_number"]
        new_slide_number = Text(f"{self.counter}").move_to(old_slide_number)
        self.play(Transform(old_slide_number, new_slide_number))

    def construct(self):
        title = Text("My Title").to_corner(UL)

        self.counter = 1
        slide_number = Text("1").to_corner(DL)

        self.add_to_canvas(title=title, slide_number=slide_number)

        self.play(FadeIn(title), FadeIn(slide_number))
        self.next_slide()

        circle = Circle(radius=2)
        dot = Dot()

        self.update_canvas()
        self.play(Create(circle))
        self.play(MoveAlongPath(dot, circle))

        self.next_slide()
        self.update_canvas()

        square = Square()

        self.wipe(self.mobjects_without_canvas, square)
        self.next_slide()

        self.update_canvas()
        self.play(
            Transform(
                self.canvas["title"],
                Text("New Title").to_corner(UL)
            )
        )
        self.next_slide()

        self.remove_from_canvas("title", "slide_number")
        self.wipe(self.mobjects_without_canvas, [])

#####
class NextSlideExample(Slide):
    def construct(self):
        text = Text("Hello World!")

        self.play(FadeIn(text))

        self.next_slide()
        self.play(FadeOut(text))


class LoopExample(Slide):
    def construct(self):
        dot = Dot(color=BLUE, radius=1)

        self.play(FadeIn(dot))

        self.next_slide(loop=True)

        self.play(Indicate(dot, scale_factor=2))

        self.next_slide()

        self.play(FadeOut(dot))
        
class AutoNextExample(Slide):
    def construct(self):
        square = Square(color=RED, side_length=2)

        self.play(GrowFromCenter(square))

        self.next_slide(auto_next=True)

        self.play(Wiggle(square))

        self.next_slide()

        self.wipe(square)
        
class SpeakerNotesExample(Slide):
    def construct(self):
        self.next_slide(notes="Some introduction")
        square = Square(color=GREEN, side_length=2)

        self.play(GrowFromCenter(square))

        self.next_slide(notes="We now rotate the slide")

        self.play(Rotate(square, PI / 2))

        self.next_slide(notes="Bye bye")

        self.zoom(square)
        
##アニメーションウィンドウとは別に、スピーカービューが表示される。