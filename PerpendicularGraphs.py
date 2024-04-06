from manim import *

class PerpendicularGraphs(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length=10,
            y_length=10,
            axis_config={"include_tip": True},
        )

        labels = axes.get_axis_labels()

        # Define the functions
        func1 = lambda x: x
        func2 = lambda x: -x

        # Create the graphs
        graph1 = axes.plot(func1, color = BLUE)
        graph2 = axes.plot(func2, color = RED)

        # Set the colors
        graph1.set_color(BLUE)
        graph2.set_color(RED)

        self.play(Create(axes))
        self.play(Create(graph1))
        self.play(Create(graph2))
        self.wait(3)