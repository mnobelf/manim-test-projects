from manim import *

class PolygonToCircle(Scene):
    def construct(self):
        # Start with a triangle
        waiting_time = 3
        polygon = Polygon(*[[np.cos(2*np.pi*i/3), np.sin(2*np.pi*i/3), 0] for i in range(3)])
        self.wait(waiting_time)

        self.add(polygon)

        # Gradually increase the number of vertices
        for n in range(4, 100):
            new_polygon = Polygon(*[[np.cos(2*np.pi*i/n), np.sin(2*np.pi*i/n), 0] for i in range(n)])
            waiting_time = waiting_time * 0.9
            self.play(Transform(polygon, new_polygon), run_time=waiting_time)

        self.wait()
