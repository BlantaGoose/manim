from manim import *
from manim_slides import Slide
#from manim_slides import ThreeDSlide
from manim_slides.slide.animation import Wipe

class AprTwelve(Slide): 
    def update_canvas(self):
        self.counter += 1
        old_slide_number = self.canvas["slide_number"]
        new_slide_number = Text(f"{self.counter}").move_to(old_slide_number)
        self.play(Transform(old_slide_number, new_slide_number))
    
    def construct(self):
        title = Text("Team Evolutionary Ecology", t2c = {"Team Evolutionary Ecology": BLUE})
        progress = Text("Progress").to_corner(UL)
        plan = Text("Plan")
        
        self.counter = 1
        slide_number = Text("1").to_corner(DR)
        
        self.add_to_canvas(title = title, slide_number = slide_number)
        
        self.play(FadeIn(title), FadeIn(slide_number))
        self.next_slide()
        
#       self.update_canvas()
#        self.wipe(title, progress)
#        self.next_slide()
        
        mob = RoundedRectangle(width = 8, corner_radius=0.5, color= YELLOW) 
        text2 = Text("Learn how to use \nImageJ & MorphoJ")
        text2.move_to(mob.get_center())
        
        self.update_canvas()
        self.wipe(title, progress)
        self.play(FadeIn(mob))
        self.play(Write(text2))
        self.play(ApplyMethod(Group(text2, mob).to_edge, UP))
        
        image_path_mj = "../Desktop/Pictures/MorphoJ_logo.jpg"
        image_path_ij = "../Desktop/Pictures/imagej_logo.png"
        
        image_mj = ImageMobject(image_path_mj)
        image_ij = ImageMobject(image_path_ij)
        image_gp = Group(image_mj, image_ij).arrange(LEFT)
        self.play(FadeIn(image_gp))
        self.next_slide()
        
        self.update_canvas()
        text3 = Text("The phenome10K might be good \nto manipulate skull shape of birds!")
        text3.move_to(mob.get_center())
        
        text_phe = Text("Phenome10K seeks to advance the field of phenomics \nby providing free 3-D image data to the academic and educational (non-commercial) community.", 
                        t2c = {"3-D image data": BLUE}).scale(0.5)
        
        self.play(Wipe(Group(text2, mob, image_gp), Group(text3, mob, text_phe)))