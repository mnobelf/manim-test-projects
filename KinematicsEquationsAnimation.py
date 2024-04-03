from manim import *

class KinematicsDerivations(Scene):
    def construct(self):
        eq1 = MathTex("\\frac{dv}{dt} = a", font_size=60)
        eq2 = MathTex("dv = a \\thinspace dt", font_size=60)
        eq3 = MathTex("\int_{v_0}^{v} dv = \int_{t_0}^{t} a \, dt", font_size=60)
        eq4 = MathTex("v-v_0 = a(t-t_0)", font_size=60)
        eq5 = MathTex("v-v_0= at", font_size=60)
        eq6 = MathTex("v = at + v_0", font_size=60)
        note1 = MathTex("t_0 = 0", font_size=40, color=BLUE)
        note1.next_to(eq4, DOWN)
        self.play(Write(eq1))
        self.wait(1)
        self.play(TransformMatchingShapes(eq1,eq2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq2,eq3))
        self.wait(1)
        self.play(TransformMatchingShapes(eq3,eq4),Write(note1))
        self.wait(1)
        self.play(TransformMatchingShapes(eq4,eq5),FadeOut(note1))
        self.wait(1)
        self.play(TransformMatchingShapes(eq5,eq6))
        self.wait(1)