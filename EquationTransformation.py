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

        # Transform the equation into F = ma
        self.animate_equations(equation1, equations)

    def animate_equations(self, eq, eq_data):
        for i, (text, scale) in enumerate(zip(eq_data[0][1:], eq_data[1][1:])):
            new_equation = MathTex(text)
            new_equation.scale(scale)

            # Add "m constant" if the current equation matches
            if text == eq_data[0][1]:
                note = MathTex("P = mv").set_color(BLUE)
                note.next_to(eq, RIGHT)
                self.play(Write(note))
                self.wait(1)
                self.play(FadeOut(note),TransformMatchingShapes(eq, new_equation))
            if text == eq_data[0][2]:
                note = Text("m konstan", font_size=30, color=BLUE)
                note.next_to(eq, RIGHT, buff=SMALL_BUFF)
                self.play(Write(note))
                self.wait(1)
                self.play(FadeOut(note),TransformMatchingShapes(eq, new_equation))
            elif text == eq_data[0][3]:
                note = MathTex("a = \\frac{dv}{dt}").set_color(BLUE)
                note.next_to(eq, RIGHT)
                self.play(Write(note))
                self.wait(1)
                self.play(FadeOut(note),TransformMatchingShapes(eq, new_equation))

            eq = new_equation
