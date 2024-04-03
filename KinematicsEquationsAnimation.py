from manim import *

class KinematicsDerivations(Scene):
    def construct(self):
        eqs = [
            MathTex("\\frac{dv}{dt} = a", font_size=60),
            MathTex("dv = a \, dt", font_size=60),
            MathTex("\\int_{v_0}^{v} dv = \int_{t_0}^{t} a \, dt", font_size=60),
            MathTex("v-v_0 = a(t-t_0)", font_size=60),
            MathTex("v-v_0= at", font_size=60),
            MathTex("v = v_0 + at", font_size=60),
            MathTex("\\frac{dx}{dt}=v", font_size=60),
            MathTex("dx=v \, dt", font_size=60),
            MathTex("\\int_{x_0}^{x} dx=\\int_{t_0}^{t} v \, dt", font_size=60),
            MathTex("\\int_{x_0}^{x} dx=\\int_{t_0}^{t} (v_0 + at) \, dt", font_size=60),
            MathTex("x\\bigg|_{x_0}^{x}= (v_0t+\\frac{1}{2}at^2)\\bigg|_{t_0}^{t}", font_size=60),
            MathTex("x-x_0= v_0(t-t_0)+\\frac{1}{2}a(t^2-t_0^2)", font_size=60),
            MathTex("x-x_0= v_0t +\\frac{1}{2}at^2", font_size=60),
            MathTex("x= x_0+ v_0t +\\frac{1}{2}at^2", font_size=60),
        ]
        notes = [MathTex("t_0 = 0", font_size=40, color=BLUE), MathTex("v = v_0 + at", font_size=40, color=BLUE)]
        notes[0].shift(DOWN)
        notes[1].shift(DOWN)
        for i in range(len(eqs)-1):
            if i == 5:
                self.play(Write(eqs[i+1]))
                continue
            if i == 3 or i == 11: self.play(TransformMatchingShapes(eqs[i], eqs[i+1]),FadeOut(notes[0]))
            elif i == 8: self.play(TransformMatchingShapes(eqs[i], eqs[i+1]),FadeOut(notes[1]))
            else: self.play(TransformMatchingShapes(eqs[i], eqs[i+1]))
            self.wait(0.5)
            if i == 2 or i == 10:
                self.play(Write(notes[0]))
                self.wait(1)
            elif i == 4:
                self.play(eqs[i+1].animate.shift(UP*3))
            elif i == 7:
                self.play(Write(notes[1]))
                self.wait(1)
        self.wait(1)