from manim import *

class EquationTransformation(Scene):
    def construct(self):
        # List of equations
        equations = [
            ["F = \\frac{dp}{dt}","F = \\frac{d(mv)}{dt}", "F = m\\frac{dv}{dt}", "F = ma"],
            [1.5, 1.5, 1.5, 1.5]
        ]

        # Create the initial equation
        equation1 = MathTex(equations[0][0])
        equation1.scale(equations[1][0])
        self.play(Write(equation1))

        # Transform the equation into F = ma
        self.animate_equations(equation1, equations)

    def animate_equations(self, eq, eq_data):
        for i, (text, scale) in enumerate(zip(eq_data[0][1:], eq_data[1][1:])):
            new_equation = MathTex(text)
            new_equation.scale(scale)
            self.play(TransformMatchingShapes(eq, new_equation))
            eq = new_equation
            self.wait(1)