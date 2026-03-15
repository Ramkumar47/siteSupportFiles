from manim import *


# setting catppuccin colors
background_color = "#dce0e8"
text_color = "#4c4f69"
red_color = "#d20f39"
blue_color = "#1e66f5"
green_color = "#40a02b"
yellow_color = "#df8e1d"

config.background_color = background_color

# axes range setting
xrange = [0,3]
yrange = [0,3]

class AxesCreation(Scene):
    def construct(self):
        # Create axes at the bottom left corner of the scene
        axes = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(text_color)
        y_label.set_color(text_color)

        # Add the axes and graph to the scene
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

class CreateX1mark(Scene):
    def construct(self):
        # Create axes at the bottom left corner of the scene
        axes = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(text_color)
        y_label.set_color(text_color)

        self.add(axes, x_label, y_label)

        # create a red cross mark at (2,2) and scale it to be smaller
        cross_mark = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(2, 2))
        self.play(Create(cross_mark))
        self.wait(1)

class CreateX1markLabel(Scene):
    def construct(self):
        # Create axes at the bottom left corner of the scene
        axes = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(text_color)
        y_label.set_color(text_color)

        # create a red cross mark at (2,2) and scale it to be smaller
        cross_mark = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(2, 2))

        self.add(axes, x_label, y_label, cross_mark)

        # add label for the cross mark
        cross_label = MathTex("A = 250", color=text_color).next_to(cross_mark, UP)
        self.play(Write(cross_label))
        self.wait(1)


class CreateX2mark(Scene):
    def construct(self):
        # Create axes at the bottom left corner of the scene
        axes = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(text_color)
        y_label.set_color(text_color)

        # create a red cross mark at (2,2) and scale it to be smaller
        cross_mark = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(2, 2))

        # add label for the cross mark
        cross_label = MathTex("A = 250", color=text_color).next_to(cross_mark, UP)

        self.add(axes, x_label, y_label, cross_mark, cross_label)

        # create another cross mark at (1,1) and scale it to be smaller
        cross_mark2 = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(1, 1))
        self.play(Create(cross_mark2))
        self.wait(1)


class CreateX2markLabel(Scene):
    def construct(self):
        # Create axes at the bottom left corner of the scene
        axes = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(text_color)
        y_label.set_color(text_color)

        # create a red cross mark at (2,2) and scale it to be smaller
        cross_mark = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(2, 2))

        # add label for the cross mark
        cross_label = MathTex("A = 250", color=text_color).next_to(cross_mark, UP)

        # create another cross mark at (1,1) and scale it to be smaller
        cross_mark2 = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(1, 1))

        self.add(axes, x_label, y_label, cross_mark, cross_label, cross_mark2)

        # add label for the second cross mark
        cross_label2 = MathTex("B = 200", color=text_color).next_to(cross_mark2, UP)
        self.play(Write(cross_label2))


class CreateX3mark(Scene):
    def construct(self):
        # Create axes at the bottom left corner of the scene
        axes = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(text_color)
        y_label.set_color(text_color)

        # create a red cross mark at (2,2) and scale it to be smaller
        cross_mark = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(2, 2))

        # add label for the cross mark
        cross_label = MathTex("A = 250", color=text_color).next_to(cross_mark, UP)

        # create another cross mark at (1,1) and scale it to be smaller
        cross_mark2 = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(1, 1))

        # add label for the second cross mark
        cross_label2 = MathTex("B = 200", color=text_color).next_to(cross_mark2, UP)

        self.add(axes, x_label, y_label, cross_mark, cross_label, cross_mark2, cross_label2)

        # create another cross mark at (1,2) and scale it to be smaller
        cross_mark3 = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(1.75, 0.5))
        self.play(Create(cross_mark3))
        self.wait(1)

class CreateX3markLabel(Scene):
    def construct(self):
        # Create axes at the bottom left corner of the scene
        axes = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(text_color)
        y_label.set_color(text_color)

        # create a red cross mark at (2,2) and scale it to be smaller
        cross_mark = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(2, 2))

        # add label for the cross mark
        cross_label = MathTex("A = 250", color=text_color).next_to(cross_mark, UP)

        # create another cross mark at (1,1) and scale it to be smaller
        cross_mark2 = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(1, 1))

        # add label for the second cross mark
        cross_label2 = MathTex("B = 200", color=text_color).next_to(cross_mark2, UP)

        # create another cross mark at (1,2) and scale it to be smaller
        cross_mark3 = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(1.75, 0.5))
        self.add(axes, x_label, y_label, cross_mark, cross_label, cross_mark2, cross_label2, cross_mark3)

        cross_label3 = MathTex("C = 150", color=text_color).next_to(cross_mark3, UP)
        self.play(Write(cross_label3))
        self.wait(1)


class BulletPoint1(Scene):
    def construct(self):
        # Create axes at the bottom left corner of the scene
        axes = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        x_label.set_color(text_color)
        y_label.set_color(text_color)

        # create a red cross mark at (2,2) and scale it to be smaller
        cross_mark = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(2, 2))

        # add label for the cross mark
        cross_label = MathTex("A = 250", color=text_color).next_to(cross_mark, UP)

        # create another cross mark at (1,1) and scale it to be smaller
        cross_mark2 = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(1, 1))

        # add label for the second cross mark
        cross_label2 = MathTex("B = 200", color=text_color).next_to(cross_mark2, UP)

        # create another cross mark at (1,2) and scale it to be smaller
        cross_mark3 = Cross(color=red_color, scale_factor=0.2).move_to(axes.c2p(1.75, 0.5))
        cross_label3 = MathTex("C = 150", color=text_color).next_to(cross_mark3, UP)
        self.add(axes, x_label, y_label, cross_mark, cross_label, cross_mark2, cross_label2, cross_mark3, cross_label3)

        # fade all the elements
        self.play(
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(cross_mark),
            FadeOut(cross_label),
            FadeOut(cross_mark2),
            FadeOut(cross_label2),
            FadeOut(cross_mark3),
            FadeOut(cross_label3)
        )
        self.wait(1)

        # add a bullet point text
        bullet_point = Text("City - design space", color=text_color)
        self.play(Write(bullet_point))
        self.wait(1)

class BulletPoint2(Scene):
    def construct(self):

        bullet_point = Text("City - design space", color=text_color)

        self.add(bullet_point)

        # add another bullet point text below the first one and move first text up a bit
        bullet_point2 = Text("x,y - design variables", color=text_color).next_to(bullet_point, DOWN)   
        self.play(bullet_point.animate.shift(UP), Write(bullet_point2))
        self.wait(1)

class BulletPoint3(Scene):
    def construct(self):

        bullet_point = Text("City - design space", color=text_color)
        bullet_point.shift(UP)
        bullet_point2 = Text("x,y - design variables", color=text_color).next_to(bullet_point, DOWN)   
        self.add(bullet_point, bullet_point2)

        # add a bullet point with math tex in it 
        bullet_point3 = Text("Cost - objective function", color=text_color).next_to(bullet_point2, DOWN)
        bullet_pointMath3 = MathTex("f_{obj}(x,y)", color=text_color).next_to(bullet_point3, RIGHT)

        # add another bullet point text below the first one and move first text up a bit
        self.play(bullet_point.animate.shift(UP), bullet_point2.animate.shift(UP), Write(bullet_point3))
        self.play( Write(bullet_pointMath3))
        self.wait(1)

class BulletPoint4(Scene):
    def construct(self):

        bullet_point = Text("City - design space", color=text_color)
        bullet_point.shift(UP)
        bullet_point2 = Text("x,y - design variables", color=text_color).next_to(bullet_point, DOWN)   
        # add a bullet point with math tex in it 
        bullet_point3 = Text("Cost - objective function", color=text_color).next_to(bullet_point2, DOWN)
        bullet_pointMath3 = MathTex("f_{obj}(x,y)", color=text_color).next_to(bullet_point3, RIGHT)

        self.add(bullet_point, bullet_point2, bullet_point3, bullet_pointMath3)

        # add another bullet point text below the first one and move first text up a bit
        bullet_point4 = Text("Objective - find shop with lowest cost", color=text_color).next_to(bullet_point3, DOWN)
        bullet_pointMath4 = MathTex(r"\underset{x,y}{minimize} \ \ f_{obj}(x,y)", color=text_color).next_to(bullet_point4, DOWN)
        self.play(bullet_point.animate.shift(UP), bullet_point2.animate.shift(UP),
                  bullet_point3.animate.shift(UP), bullet_pointMath3.animate.shift(UP))
        self.play(Write(bullet_point4), Write(bullet_pointMath4))
        self.wait(1)

class BulletPoint5(Scene):
    def construct(self):

        bullet_point = Text("City - design space", color=text_color)
        bullet_point.shift(UP)
        bullet_point2 = Text("x,y - design variables", color=text_color).next_to(bullet_point, DOWN)   
        # add a bullet point with math tex in it 
        bullet_point3 = Text("Cost - objective function", color=text_color).next_to(bullet_point2, DOWN)
        bullet_pointMath3 = MathTex("f_{obj}(x,y)", color=text_color).next_to(bullet_point3, RIGHT)
        bullet_point4 = Text("Objective - find shop with lowest cost", color=text_color).next_to(bullet_point3, DOWN)
        bullet_pointMath4 = MathTex(r"\underset{x,y}{minimize} \ \ f_{obj}(x,y)", color=text_color).next_to(bullet_point4, DOWN)

        self.add(bullet_point, bullet_point2, bullet_point3, bullet_pointMath3, bullet_point4, bullet_pointMath4)

        bullet_point5 = Text("A,B,C - particles ", color=text_color).next_to(bullet_point4, DOWN)  

        # add another bullet point text below the first one and move first text up a bit
        self.play(bullet_point.animate.shift(UP), bullet_point2.animate.shift(UP),
                  bullet_point3.animate.shift(UP), bullet_pointMath3.animate.shift(UP),
                  bullet_point4.animate.shift(UP), bullet_pointMath4.animate.shift(UP))
        self.play(Write(bullet_point5))
        self.wait(1)

class BulletPoint6(Scene):
    def construct(self):

        bullet_point = Text("City - design space", color=text_color)
        bullet_point.shift(UP)
        bullet_point2 = Text("x,y - design variables", color=text_color).next_to(bullet_point, DOWN)   
        # add a bullet point with math tex in it 
        bullet_point3 = Text("Cost - objective function", color=text_color).next_to(bullet_point2, DOWN)
        bullet_pointMath3 = MathTex("f_{obj}(x,y)", color=text_color).next_to(bullet_point3, RIGHT)
        bullet_point4 = Text("Objective - find shop with lowest cost", color=text_color).next_to(bullet_point3, DOWN)
        bullet_pointMath4 = MathTex(r"\underset{x,y}{minimize} \ \ f_{obj}(x,y)", color=text_color).next_to(bullet_point4, DOWN)
        bullet_point5 = Text("A,B,C - particles ", color=text_color).next_to(bullet_pointMath4, DOWN)  


        self.add(bullet_point, bullet_point2, bullet_point3, bullet_pointMath3, bullet_point4, bullet_pointMath4, bullet_point5)

        bullet_point6 = Text("PSO mostly gives approximate global minima!", color=text_color).next_to(bullet_point5, DOWN)

        # reducing font size and changing color to blue for the last bullet point
        bullet_point6.set_color(blue_color)
        bullet_point6.set_font_size(32)

        # add another bullet point text below the first one and move first text up a bit
        self.play(bullet_point.animate.shift(2*UP), bullet_point2.animate.shift(2*UP),
                  bullet_point3.animate.shift(2*UP), bullet_pointMath3.animate.shift(2*UP),
                  bullet_point4.animate.shift(2*UP), bullet_pointMath4.animate.shift(2*UP),
                  bullet_point5.animate.shift(2*UP))
        bullet_point6.shift(1.5*UP)

        self.play(Write(bullet_point6))

        self.wait(1)

class Points1(Scene):
    def construct(self):

        bullet_point = Text("City - design space", color=text_color)
        bullet_point.shift(UP)
        bullet_point2 = Text("x,y - design variables", color=text_color).next_to(bullet_point, DOWN)   
        # add a bullet point with math tex in it 
        bullet_point3 = Text("Cost - objective function", color=text_color).next_to(bullet_point2, DOWN)
        bullet_pointMath3 = MathTex("f_{obj}(x,y)", color=text_color).next_to(bullet_point3, RIGHT)
        bullet_point4 = Text("Objective - find shop with lowest cost", color=text_color).next_to(bullet_point3, DOWN)
        bullet_pointMath4 = MathTex(r"\underset{x,y}{minimize} \ \ f_{obj}(x,y)", color=text_color).next_to(bullet_point4, DOWN)
        bullet_point5 = Text("A,B,C - particles ", color=text_color).next_to(bullet_pointMath4, DOWN)  

        bullet_point.shift(2*UP)
        bullet_point2.shift(2*UP)
        bullet_point3.shift(2*UP)
        bullet_pointMath3.shift(2*UP)
        bullet_point4.shift(2*UP)
        bullet_pointMath4.shift(2*UP)
        bullet_point5.shift(2*UP)

        # self.add(bullet_point, bullet_point2, bullet_point3, bullet_pointMath3, bullet_point4, bullet_pointMath4, bullet_point5)

        Point1 = Text("PSO gives global minima", color=text_color).shift(2*UP)

        # # add another bullet point text below the first one and move first text up a bit
        # self.play(FadeOut(bullet_point), FadeOut(bullet_point2), 
        #           FadeOut(bullet_point3), FadeOut(bullet_pointMath3),
        #           FadeOut(bullet_point4), FadeOut(bullet_pointMath4),
        #           FadeOut(bullet_point5))

        self.play(Write(Point1))

        self.wait(1)

class Points2(Scene):
    def construct(self):

        Point1 = Text("PSO gives global minima", color=text_color).shift(2*UP)

        self.add(Point1)

        Point2 = Text("Mostly an approximate one!", color=red_color).next_to(Point1, DOWN)

        self.play(Write(Point2))

        self.wait(1)

class Points3(Scene):
    def construct(self):

        Point1 = Text("PSO gives global minima", color=text_color).shift(2*UP)

        Point2 = Text("Mostly an approximate one!", color=red_color).next_to(Point1, DOWN)

        self.add(Point1, Point2)

        Point3 = Text("It is one of meta-heuristic algorithms", color=text_color)

        self.play(Write(Point3))

        self.wait(1)

class Points4(Scene):
    def construct(self):

        Point1 = Text("PSO gives global minima", color=text_color).shift(2*UP)

        Point2 = Text("Mostly an approximate one!", color=red_color).next_to(Point1, DOWN)

        Point3 = Text("It is one of meta-heuristic algorithms", color=text_color)

        self.add(Point1, Point2, Point3)

        Point4 = Text("Nature-inspired evolutionary algorithms", color=text_color).shift(DOWN)
        Point5 = Text("with strategies that guides the search process", color=text_color).shift(2*DOWN)

        self.play(Write(Point4))
        self.play(Write(Point5))

        self.wait(1)

class Points5(Scene):
    def construct(self):

        Point1 = Text("PSO gives global minima", color=text_color).shift(2*UP)

        Point2 = Text("Mostly an approximate one!", color=red_color).next_to(Point1, DOWN)

        Point3 = Text("It is one of meta-heuristic algorithms", color=text_color)

        Point4 = Text("Nature-inspired evolutionary algorithms", color=text_color).shift(DOWN)
        Point5 = Text("with strategies that guides the search process", color=text_color).shift(2*DOWN)

        self.add(Point1, Point2, Point3, Point4, Point5)

        Point6 = Text("We get quick, global but suboptimal solution", color=blue_color).shift(3*DOWN)

        self.play(Write(Point6))

        self.wait(1)