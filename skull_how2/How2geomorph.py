from manim import *
from manim_slides import Slide

class How2geomorph(Slide):
    def update_canvas(self):
        self.counter += 1
        old_slide_number = self.canvas["slide_number"]
        new_slide_number = Text(f"{self.counter}").move_to(old_slide_number)
        self.play(Transform(old_slide_number, new_slide_number))

    def construct(self):
        title_0 = VGroup(
            Text("1 Getting Started with 1.6 Example datasets")
        ).arrange(DOWN)
        
        step_0 = VGroup(
            Text("Landmark data can be found as objects in 2 formats:")
#            Text("a 2D array or a 3D array(using (n) species = having (n) matrixes)")
        )
        step_1 = VGroup(
            Text("If you finish converting .png to .tps and performing plotting landmark,"),
            Text("you should read .tps file with readland.tps function"),
            Text("If you have curves in the file, you can use readcurves option and it will return curves as semiLM")
        ).arrange(DOWN)
        
        for step in [step_0, step_1]:
            step.scale(0.5).to_corner(UL)
        
        step = step_0
        
        self.play(FadeIn(title_0))
        
        self.next_slide()
        
        code_0 = Code(
            code = """
            data(plethodon)
            attributes(plethodon)
            """, 
            language = "R"
        )
        
        code_1 = Code(
            code = """
            readland.tps(file, specID = c("None", "ID", "imageID"), 
            readcurves = TRUE, warning = TRUE) 
            """,
            language = "R"
        )
        
        self.wipe(title_0, code_0)
        self.next_slide()
        
        self.play(FadeIn(step, shift=RIGHT))
        self.play(Transform(code_0, code_1))
        self.next_slide()
        
        self.play(Transform(step, step_1))
        self.play(Transform(code_0, code_1))
        self.next_slide()

'''
    def construct(self):
        title_2 = VGroup(
            Text("Landmark method", t2c={"Landmark": BLUE}),
        ).arrange(DOWN)
        
        step_1 = Text("1. To read landmark image, `readland.tps` is good.")
        
        
        
        for step in [step_1]:
            step.scale(0.5).to_corner(UL)
            
        step = step_1
        self.play(FadeIn(title_2))
        self.next_slide()
        
        code = Code(
            code = """
            readland.tps(file, specID = c("None", "ID", "imageID"), 
            readcurves = TRUE, warning = TRUE) 
            """,
            language = "R"
        )
        
        code_step_1 = Code(
            code = """
            readland.tps(file, specID = c("None", "ID", "imageID"), 
            readcurves = TRUE, warning = TRUE)
            """,
            language = "R"
        )
        
        self.wipe(title_2, code)
        self.next_slide()
'''