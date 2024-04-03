from manim import *

class EquationTransformation(Scene):
    def construct(self):
        # List of equations
        equations = [
            ["F = \\frac{dp}{dt}", "F = \\frac{d(mv)}{dt}", "F = m\\frac{dv}{dt}", "F = ma"],
            [1.5, 1.5, 1.5, 1.5]
        ]

        # Create the initial equation
        equation1 = MathTex(equations[0][0])
        equation1.scale(equations[1][1])
        self.play(Write(equation1))

        pmv = MathTex("P = mv").set_color(BLUE)
        pmv.next_to(equation1, DOWN)
        self.play(Write(pmv))
        self.play(FadeOut(pmv))

        # Transform the equation into F = ma
        self.animate_equations(equation1, equations)

    def animate_equations(self, eq, eq_data):
        for i, (text, scale) in enumerate(zip(eq_data[0][1:], eq_data[1][1:])):
            new_equation = MathTex(text)
            new_equation.scale(scale)
            self.play(TransformMatchingShapes(eq, new_equation))
            eq = new_equation

            # Add "m constant" if the current equation matches
            if text == eq_data[0][1]:
                note = Text("m konstan", font_size=30, color=BLUE)
                note.next_to(eq, DOWN, buff=SMALL_BUFF)
                self.play(Write(note))
                self.play(FadeOut(note))

            elif text == eq_data[0][2]:
                note = MathTex("a = \\frac{dv}{dt}").set_color(BLUE)
                note.next_to(eq, DOWN)
                self.play(Write(note))
                self.play(FadeOut(note))

            self.wait(1)