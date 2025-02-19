from manim import *
from manim_chemistry import ChemicalEquation

class DrawPOrbital(Scene):
    def construct(self):
        orbital = Orbital(l=1, m=-1)
        self.add(orbital)

class DrawBohrDiagram(Scene):
    def construct(self):
        diagram = BohrAtom(e=14, p=14, n=10)
        self.add(diagram)
        

class ChemicalReaction(Scene):
    def construct(self):
        equation = ChemicalEquation(
            "2H2 + O2 -> 2H2O"
        )
        self.play(Write(equation))
        self.wait(2)
