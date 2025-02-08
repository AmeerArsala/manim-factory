from manim import *

# The demo one
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class DrawCircle(Scene):
    def construct(self):
        # Create a vertical bar
        bar = Rectangle(height=3, width=0.1, color=GREEN)
        bar.set_fill(GREEN, opacity=1)
        
        # Create a large dot that will fill counter-clockwise
        circle = Dot(radius=1.5, color=GREEN)
        circle.rotate(PI/2)  # Rotate circle to start drawing from the top
        
        # Animate the bar rotating and the circle filling counter-clockwise
        self.play(
            Rotate(bar, angle=2*PI, run_time=4, rate_func=linear),
            Create(circle, run_time=4, rate_func=smooth),
        )
        self.wait()

class DrawPieChart(Scene):
    def construct(self):
        # Use a ValueTracker to control the angle of the Sector dynamically.
        angle_tracker = ValueTracker(0)
        
        pie = Sector(
            radius=2.0,
            angle=angle_tracker.get_value(),
            start_angle=PI/2
        )
        pie.set_color(BLUE)
        pie.set_stroke(width=0)
        
        # Add an updater that resets the Sector based on the current angle value.
        pie.add_updater(lambda m: m.become(
            Sector(radius=2.0, angle=angle_tracker.get_value(), start_angle=PI/2)
        ))

        self.add(pie)
        self.play(
            angle_tracker.animate.set_value(2*PI),
            run_time=6,
            rate_func=linear
        )
        self.wait()