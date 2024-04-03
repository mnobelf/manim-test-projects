from manim import *

class KinematicsDerivations(Scene):
    def construct(self):
        eq1 = MathTex("\\frac{dv}{dt} = a", font_size=60)
        eq2 = MathTex("dv = a \, dt", font_size=60)
        eq3 = MathTex("\int_{v_0}^{v} dv = \int_{t_0}^{t} a \, dt", font_size=60)
        eq4 = MathTex("v-v_0 = a(t-t_0)", font_size=60)
        eq5 = MathTex("v-v_0= at", font_size=60)
        eq6 = MathTex("v = v_0 + at", font_size=60)
        eq7 = MathTex("\\frac{dx}{dt}=v", font_size=60)
        eq8 = MathTex("dx=v \, dt", font_size=60)
        eq9 = MathTex("\int_{x_0}^{x} dx=\int_{t_0}^{t} v \, dt", font_size=60)
        eq10 = MathTex("\int_{x_0}^{x} dx=\int_{t_0}^{t} (v_0 + at) \, dt", font_size=60)
        eq11 = MathTex("x\\bigg|_{x_0}^{x}= (v_0t+\\frac{1}{2}at^2)\\bigg|_{t_0}^{t}", font_size=60)
        eq11b = MathTex("x-x_0= v_0(t-t_0)+\\frac{1}{2}a(t^2-t_0^2)", font_size=60)
        eq12 = MathTex("x-x_0= v_0t +\\frac{1}{2}at^2", font_size=60)
        eq13 = MathTex("x= x_0+ v_0t +\\frac{1}{2}at^2", font_size=60)
        note1 = MathTex("t_0 = 0", font_size=40, color=BLUE)
        note2 = MathTex("v = v_0 + at", font_size=40, color=BLUE)
        note1.shift(DOWN)
        note2.shift(DOWN)
        self.play(Write(eq1))
        self.wait(1)
        self.play(TransformMatchingShapes(eq1,eq2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq2,eq3))
        self.wait(1)
        self.play(TransformMatchingShapes(eq3,eq4))
        self.wait(0.25)
        self.play(Write(note1))
        self.wait(0.75)
        self.play(TransformMatchingShapes(eq4,eq5),FadeOut(note1))
        self.wait(1)
        self.play(TransformMatchingShapes(eq5,eq6))
        self.wait(1)
        self.play(eq6.animate.shift(UP*3))
        self.wait(0.25)
        self.play(Write(eq7))
        self.wait(1)
        self.play(TransformMatchingShapes(eq7,eq8))
        self.wait(1)
        self.play(TransformMatchingShapes(eq8,eq9))
        self.wait(0.25)
        self.play(Write(note2))
        self.wait(0.75)
        self.play(TransformMatchingShapes(eq9,eq10),FadeOut(note2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq10,eq11))
        self.wait(1)
        self.play(TransformMatchingShapes(eq11,eq11b))
        self.wait(0.25)
        self.play(Write(note1))
        self.wait(0.75)
        self.play(TransformMatchingShapes(eq11b,eq12),FadeOut(note1))
        self.wait(1)
        self.play(TransformMatchingShapes(eq12,eq13))
        self.wait(1)