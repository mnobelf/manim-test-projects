from manim import *

class KinematicsDerivations(Scene):
    CONFIG = {
        "camera_config": {
            "frame_shape": (9, 16),  # Ratio of width to height (e.g., 16:9)
            }
        }
    def construct(self):
        f_size = 60*0.8
        n_size = 40*0.8
        wait_t = 0.75
        eqs = [
            MathTex("\\frac{dv}{dt} = a", font_size=f_size),
            MathTex("dv = a \, dt", font_size=f_size),
            MathTex("\\int_{v_0}^{v} dv = \int_{t_0}^{t} a \, dt", font_size=f_size),
            MathTex("v-v_0 = a(t-t_0)", font_size=f_size),
            MathTex("v-v_0= at", font_size=f_size),
            MathTex("v = v_0 + at", font_size=f_size),
            MathTex("\\frac{dx}{dt}=v", font_size=f_size),
            MathTex("dx=v \, dt", font_size=f_size),
            MathTex("\\int_{x_0}^{x} dx=\\int_{t_0}^{t} v \, dt", font_size=f_size),
            MathTex("\\int_{x_0}^{x} dx=\\int_{t_0}^{t} (v_0 + at) \, dt", font_size=f_size),
            MathTex("x\\bigg|_{x_0}^{x}= (v_0t+\\frac{1}{2}at^2)\\bigg|_{t_0}^{t}", font_size=f_size),
            MathTex("x-x_0= v_0(t-t_0)+\\frac{1}{2}a(t^2-t_0^2)", font_size=f_size),
            MathTex("x-x_0= v_0t +\\frac{1}{2}at^2", font_size=f_size),
            MathTex("x= x_0+ v_0t +\\frac{1}{2}at^2", font_size=f_size),
            MathTex("\\frac{dv}{dt} = a", font_size=f_size),
            MathTex("\\frac{dx}{dx} \\frac{dv}{dt} = a", font_size=f_size),
            MathTex("\\frac{dx}{dt} \\frac{dv}{dx} = a", font_size=f_size),
            MathTex("\\frac{dx}{dt} dv = a \, dx", font_size=f_size),
            MathTex("v \, dv = a \, dx", font_size=f_size),
            MathTex("\\int_{v_0}^{v} v \, dv = \\int_{x_0}^{x} a \, dx", font_size=f_size),
            MathTex("\\frac{1}{2} v^2\\bigg|_{v_0}^{v} = ax\\bigg|_{x_0}^{x}", font_size=f_size),
            MathTex("\\frac{1}{2}(v^2-v_0^2) = a(x-x_0)", font_size=f_size),
            MathTex("v^2-v_0^2 = 2a(x-x_0)", font_size=f_size),
            MathTex("v^2 = v_0^2+2a(x-x_0)", font_size=f_size),
        ]
        notes = [MathTex("t_0 = 0", font_size=n_size, color=BLUE), MathTex("v = v_0 + at", font_size=n_size, color=BLUE),MathTex("v = \\frac{dx}{dt}", font_size=n_size, color=BLUE)
                 ,MathTex("\\frac{dx}{dx}=1", font_size=n_size, color=BLUE)]
        self.play(Write(eqs[0]))
        notes[0].shift(DOWN*1.5)
        notes[1].shift(DOWN*1.5)
        notes[2].shift(DOWN*1.5)
        notes[3].shift(DOWN*1.5)
        for i in range(len(eqs)-1):
            if i == 5:
                self.play(Write(eqs[i+1]))
                continue
            elif i == 13:
                self.play(Write(eqs[i+1]))
                self.wait(wait_t)
                self.play(Write(notes[3]))
                continue
            if i == 3 or i == 11: self.play(TransformMatchingShapes(eqs[i], eqs[i+1]),FadeOut(notes[0]))
            elif i == 8: self.play(TransformMatchingShapes(eqs[i], eqs[i+1]),FadeOut(notes[1]))
            elif i == 14: self.play(TransformMatchingTex(eqs[i], eqs[i+1]),FadeOut(notes[3]))
            elif i == 17: self.play(TransformMatchingTex(eqs[i], eqs[i+1]),FadeOut(notes[2]))
            else: self.play(TransformMatchingShapes(eqs[i], eqs[i+1]))
            self.wait(wait_t)
            if i == 2 or i == 10:
                self.play(Write(notes[0]))
                self.wait(wait_t)
            elif i == 4:
                self.play(eqs[i+1].animate.shift(UP*4))
            elif i == 12:
                self.play(eqs[i+1].animate.shift(DOWN*4))
            elif i == 7:
                self.play(Write(notes[1]))
                self.wait(wait_t)
            elif i == 16:
                self.play(Write(notes[2]))
                self.wait(wait_t)
        self.wait(3)