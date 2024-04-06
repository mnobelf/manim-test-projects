from manim import *

class PolygonToCircle(Scene):
    def construct(self):
        # Start with a triangle
        points = [[np.cos(2*np.pi*i/3), np.sin(2*np.pi*i/3), 0] for i in range(3)]
        waiting_time = 3
        polygon = Polygon(*points)
        self.add(polygon)

        # Calculate the interior angle of the triangle
        interior_angle = (180 * (3 - 2) / 3) * DEGREES

        # Create the angle bisectors
        for i in range(3):
            start_point = points[i]
            end_point = points[(i + 1) % 3]
            line = Line(start_point, end_point)
            bisector = line.copy()
            bisector.rotate(interior_angle / 2, about_point=start_point)
            bisector.scale(np.cos(interior_angle/2), about_point=start_point)
            self.play(Create(bisector), run_time=1)
            self.wait(0.5)

        self.wait(waiting_time)

        # Gradually increase the number of vertices
        for n in range(4, 100):
            new_polygon = Polygon(*[[np.cos(2*np.pi*i/n), np.sin(2*np.pi*i/n), 0] for i in range(n)])
            waiting_time = waiting_time * 0.9
            self.play(Transform(polygon, new_polygon), run_time=waiting_time)

        self.wait()
