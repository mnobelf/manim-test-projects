from manim import *

class PerpendicularGraphs(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 15, 1],
            y_range=[-1, 15, 1],
            x_length=9,
            y_length=9,
            axis_config={"include_tip": True},
        )

        labels = axes.get_axis_labels()

        # Define the functions
        func1 = lambda x: 2*x - 3
        func2 = lambda x: -0.5*x + 5

        # Create the graphs
        graph1 = axes.plot(func1, color = BLUE)
        graph2 = axes.plot(func2, color = RED)

        # Set the colors
        graph1.set_color(BLUE)
        graph2.set_color(RED)

        # Calculate the intersection point
        x_intersection = (5 + 3) / (2 + 0.5)
        y_intersection = func1(x_intersection)
        intersection_point = axes.c2p(x_intersection, y_intersection)

        # Create the vectors
        vector1 = Arrow(intersection_point, axes.c2p(x_intersection + 4, func1(x_intersection + 4)), buff=0)
        vector2 = Arrow(intersection_point, axes.c2p(x_intersection + 8, func2(x_intersection + 8)), buff=0)

        # Set the colors
        vector1.set_color(YELLOW)
        vector2.set_color(GREEN)


        # Create the horizontal line
        horizontal_line = DashedLine(start=axes.c2p(x_intersection - 10, y_intersection), end=axes.c2p(x_intersection + 10, y_intersection))

        label_vector1 = MathTex("\\vec{A}").next_to(vector1, UP).shift(DOWN*2+LEFT*0.3).set_color(YELLOW)
        label_vector2 = MathTex("\\vec{B}").next_to(vector2, DOWN).shift(UP*1.5+LEFT*0.8).set_color(GREEN)

        # Create the angle indicators
        angle_alpha = Angle(horizontal_line, vector1, radius=1, other_angle=False)
        angle_beta = Angle(horizontal_line, vector2, radius=1.5, other_angle=True)

        # Add labels for the angles
        label_alpha = MathTex("\\alpha").next_to(angle_alpha, RIGHT).shift(UP*0.2+LEFT*0.3)
        label_beta = MathTex("\\beta").next_to(angle_beta, RIGHT).shift(DOWN*0.1)

        # Create the x and y components of each vector
        vector1_x = Arrow(intersection_point, axes.c2p(x_intersection + 4, y_intersection), buff=0, stroke_width=3)
        vector1_y = Arrow(intersection_point, axes.c2p(x_intersection + 4, func1(x_intersection + 4)), buff=0, stroke_width=3)
        vector2_x = Arrow(intersection_point, axes.c2p(x_intersection + 8, y_intersection), buff=0, stroke_width=3)
        vector2_y = Arrow(intersection_point, axes.c2p(x_intersection + 8, func2(x_intersection + 8)), buff=0, stroke_width=3)

        vector1_x.set_color(YELLOW)
        vector1_y.set_color(YELLOW)
        vector2_x.set_color(GREEN)
        vector2_y.set_color(GREEN)

        self.play(Create(axes))
        self.play(Create(graph1))
        self.play(Create(graph2))
        self.play(Create(vector1), Write(label_vector1))
        self.play(Create(vector2), Write(label_vector2))
        self.play(Create(horizontal_line))
        self.play(Create(angle_alpha), Write(label_alpha))
        self.play(Create(angle_beta), Write(label_beta))
        self.play(Create(vector2_x), Create(vector2_y))
        self.play(Create(vector1_x), Create(vector1_y))
        self.wait(3)