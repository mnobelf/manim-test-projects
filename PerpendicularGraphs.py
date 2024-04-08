from manim import *

class PerpendicularGraphs(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 15, 1],
            y_range=[-1, 12, 1],
            x_length=9,
            y_length=6.75,
            axis_config={"include_tip": True},
        )

        labels = axes.get_axis_labels()
        axes.shift(UP*3)

        # Define the functions
        func1 = lambda x: 2*x - 3
        func2 = lambda x: -0.5*x + 5

        # Create the graphs
        graph1 = axes.plot(func1, x_range=[1,7.5], color = BLUE)
        graph2 = axes.plot(func2, x_range=[-1,12], color = RED)

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

        opposite_vector1 = Arrow(intersection_point, axes.c2p(x_intersection - 4, func1(x_intersection - 4)), buff=0)
        opposite_vector2 = Arrow(intersection_point, axes.c2p(x_intersection - 8, func2(x_intersection - 8)), buff=0)

        right_angle = RightAngle(opposite_vector1, opposite_vector2, length=0.3)

        # Set the colors
        vector1.set_color(YELLOW)
        vector2.set_color(GREEN)


        # Create the horizontal line
        horizontal_line = DashedLine(start=axes.c2p(x_intersection - 10, y_intersection), end=axes.c2p(x_intersection + 10, y_intersection), dashed_ratio=0.2)

        label_vector1 = MathTex("\\vec{A}").next_to(vector1, UP).shift(DOWN*2+LEFT*0.3).set_color(YELLOW)
        label_vector2 = MathTex("\\vec{B}").next_to(vector2, DOWN).shift(UP*1.5+LEFT*0.8).set_color(GREEN)

        # Create the angle indicators
        angle_alpha = Angle(horizontal_line, vector1, radius=1, other_angle=False)
        angle_beta = Angle(horizontal_line, vector2, radius=1.5, other_angle=True)

        # Add labels for the angles
        label_alpha = MathTex("\\alpha").next_to(angle_alpha, RIGHT).shift(UP*0.3+LEFT*0.2)
        label_beta = MathTex("\\beta").next_to(angle_beta, RIGHT).shift(DOWN*0.15)

        # Create the x and y components of each vector
        vector1_x = Arrow(intersection_point, axes.c2p(x_intersection + 4, y_intersection), buff=0, stroke_width=3)
        vector1_y = Arrow(axes.c2p(x_intersection + 4, y_intersection), axes.c2p(x_intersection + 4, func1(x_intersection + 4)), buff=0, stroke_width=3)
        vector2_x = Arrow(intersection_point, axes.c2p(x_intersection + 8, y_intersection), buff=0, stroke_width=3)
        vector2_y = Arrow(axes.c2p(x_intersection + 8, y_intersection), axes.c2p(x_intersection + 8, func2(x_intersection + 8)), buff=0, stroke_width=3)

        vector1_x.set_color(YELLOW)
        vector1_y.set_color(YELLOW)
        vector2_x.set_color(GREEN)
        vector2_y.set_color(GREEN)

        vector1_y.shift(RIGHT*0.1)

        self.play(Create(axes))
        self.play(Create(graph1))
        self.play(Create(graph2))
        self.play(Create(vector1), Write(label_vector1))
        self.play(Create(vector2), Write(label_vector2))
        self.play(Create(right_angle))
        self.play(Create(horizontal_line))
        self.play(Create(angle_alpha), Write(label_alpha))
        self.play(Create(angle_beta), Write(label_beta))
        self.play(Create(vector2_x), Create(vector2_y))
        self.play(Create(vector1_x), Create(vector1_y))
        self.wait(1)

        # Define your equations
        equation1 = MathTex("\\|\\vec{A_x}\\| = \\|\\vec{A}\\| \\cos\\alpha").scale(0.8)
        equation2 = MathTex("\\|\\vec{A_y}\\| = \\|\\vec{A}\\| \\sin\\alpha").scale(0.8)
        equation3 = MathTex("\\|\\vec{B_x}\\| = \\|\\vec{B}\\| \\cos\\beta").scale(0.8)
        equation4 = MathTex("\\|\\vec{B_y}\\| = \\|\\vec{B}\\| \\sin\\beta").scale(0.8)
        equation5 = MathTex("\\vec{A} \\cdot \\vec{B}= \\|\\vec{A_x}\\|\\|\\vec{B_x}\\| + \\|\\vec{A_y}\\|\\|\\vec{B_y}\\|").scale(0.8)
        equation6 = MathTex("\\vec{A} \\cdot \\vec{B}= \\|\\vec{A}\\| \\cos\\alpha \\|\\vec{B}\\| \\cos\\beta + \\|\\vec{A}\\| \\sin\\alpha \\|\\vec{B}\\| \\sin\\beta").scale(0.8)
        equation7 = MathTex("\\vec{A} \\cdot \\vec{B}= \\|\\vec{A}\\| \\|\\vec{B}\\| \\cos 90^\\circ").scale(0.8)
        equation8 = MathTex("\\vec{A} \\cdot \\vec{B}= \\|\\vec{A}\\| \\|\\vec{B}\\| (0)").scale(0.8)
        equation9 = MathTex("\\vec{A} \\cdot \\vec{B}= 0").scale(0.8)
        equation10 = MathTex("\\|\\vec{A}\\| \\cos\\alpha \\|\\vec{B}\\| \\cos\\beta + \\|\\vec{A}\\| \\sin\\alpha \\|\\vec{B}\\| \\sin\\beta = 0").scale(0.8)
        equation11 = MathTex("\\|\\vec{A}\\| \\|\\vec{B}\\| ( \\cos\\alpha \\cos\\beta + \\sin\\alpha \\sin\\beta ) = 0").scale(0.8)
        equation12 = MathTex("\\cos\\alpha \\cos\\beta + \\sin\\alpha \\sin\\beta = 0").scale(0.8)
        equation13 = MathTex("1 + \\frac{\\sin\\alpha}{\\cos\\alpha} \\frac{\\sin\\beta}{\\cos\\beta} = 0").scale(0.8)
        equation14 = MathTex("1 + \\tan\\alpha \\tan\\beta = 0").scale(0.8)
        equation15 = MathTex("\\tan\\alpha \\tan\\beta = -1").scale(0.8)

        # Position your equations
        equation1.next_to(axes, DOWN*1.5).shift(LEFT*2)
        equation2.next_to(axes, DOWN*1.5).shift(RIGHT*2)
        equation3.next_to(equation1, DOWN*1.5)
        equation4.next_to(equation2, DOWN*1.5)
        equation5.next_to(equation3, DOWN*1.5).shift(RIGHT*2)
        equation6.next_to(equation3, DOWN*1.5).shift(RIGHT*2)
        equation7.next_to(equation6, DOWN*1.5)
        equation8.next_to(equation6, DOWN*1.5)
        equation9.next_to(equation6, DOWN*1.5)
        equation10.next_to(equation9, DOWN*1.5)
        equation11.next_to(equation9, DOWN*1.5)
        equation12.next_to(equation9, DOWN*1.5)
        equation13.next_to(equation9, DOWN*1.5)
        equation14.next_to(equation9, DOWN*1.5)
        equation15.next_to(equation9, DOWN*1.5)

        # Add your equations to the scene
        self.play(Write(equation1))
        self.play(Write(equation2))
        self.play(Write(equation3))
        self.play(Write(equation4))
        self.play(Write(equation5))
        self.wait(0.5)
        self.play(TransformMatchingShapes(equation5,equation6))
        self.wait(0.5)
        self.play(Write(equation7))
        self.wait(0.5)
        self.play(TransformMatchingShapes(equation7,equation8))
        self.wait(0.5)
        self.play(TransformMatchingShapes(equation8,equation9))
        self.wait(0.5)
        self.play(Write(equation10))
        self.wait(0.5)
        self.play(TransformMatchingShapes(equation10,equation11))
        self.wait(0.5)
        self.play(TransformMatchingShapes(equation11,equation12))
        self.wait(0.5)
        self.play(TransformMatchingShapes(equation12,equation13))
        self.wait(0.5)
        self.play(TransformMatchingShapes(equation13,equation14))
        self.wait(0.5)
        self.play(TransformMatchingShapes(equation14,equation15))
        self.wait(3)
