from manim import *

class TwoBallsCollision(Scene):
    def construct(self):
        # Create two balls
        ball1 = Circle(radius=0.5, color=BLUE, fill_opacity=1)
        ball2 = Circle(radius=0.5, color=RED, fill_opacity=1)
        ball1.shift(LEFT*2)
        ball2.shift(RIGHT*2)

        # Set initial velocities
        v1_initial = 2  # Initial velocity of ball 1
        v2_initial = 1  # Initial velocity of ball 2

        # Animate the balls
        self.play(Create(ball1), Create(ball2))
        self.wait(1)
        self.play(ball1.animate.shift(RIGHT * v1_initial), ball2.animate.shift(LEFT * v2_initial))
        self.wait(1)

        # Simulate the collision (elastic)
        v1_final = ((ball1.radius - ball2.radius) * v1_initial + 2 * ball2.radius * v2_initial) / (ball1.radius + ball2.radius)
        v2_final = ((ball2.radius - ball1.radius) * v2_initial + 2 * ball1.radius * v1_initial) / (ball1.radius + ball2.radius)

        self.play(ball1.animate.shift(RIGHT * v1_final), ball2.animate.shift(LEFT * v2_final))
        self.wait(1)

        # Add labels
        label1 = MathTex("v_1", color=WHITE).next_to(ball1, DOWN)
        label2 = MathTex("v_2", color=WHITE).next_to(ball2, DOWN)
        self.play(Create(label1), Create(label2))
        self.wait(1)

        # Show final velocities
        self.play(Transform(label1, MathTex(f"v_1' = {v1_final:.2f}", color=WHITE).next_to(ball1, DOWN)),
                  Transform(label2, MathTex(f"v_2' = {v2_final:.2f}", color=WHITE).next_to(ball2, DOWN)))
        self.wait(2)

        # Clean up
        self.play(FadeOut(ball1), FadeOut(ball2), FadeOut(label1), FadeOut(label2))

if __name__ == "__main__":
    # To render the animation, run: manim -p -ql ElasticCollision.py ElasticCollision
    pass
