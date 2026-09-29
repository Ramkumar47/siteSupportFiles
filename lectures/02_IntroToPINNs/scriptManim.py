#!/bin/python3
"""============================================================================
manim script for PINN introduction

Ramkumar
Fri Sep 25 02:40:45 PM IST 2026
============================================================================"""

# importing needed modules
from manim import *

#==============================================================================

# setting catppuccin colors
background_color = "#dce0e8"
text_color       = "#4c4f69"
red_color        = "#d20f39"
blue_color       = "#1e66f5"
green_color      = "#40a02b"
yellow_color     = "#df8e1d"

config.background_color = background_color

# axes range setting
xrange = [-2,3]
yrange = [0,3]

# creating axis scene
class AxesCreation(Scene):
    def construct(self):
        # Create axes
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

class AddComplexSineCurve(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)
        self.play(Create(complex_sine_curve))
        self.wait(1)

class ScalingPlotToTopLeft(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)

        self.add(axes, x_label, y_label, complex_sine_curve)

        # Scale down the axes and curve
        self.play(axes.animate.scale(0.5).to_edge(UL),
                  complex_sine_curve.animate.scale(0.5).to_edge(UL),
                  x_label.animate.move_to(axes.get_right() + LEFT * 7.5+UP*0.4).scale(0.75),
                  y_label.animate.move_to(axes.get_top() + LEFT * 4.5).scale(0.75))

        self.wait(1)

class AddingComponentsOnRight(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)

        # scale down the axes and curve
        axes.scale(0.5).to_edge(UL)
        complex_sine_curve.scale(0.5).to_edge(UL)
        x_label.move_to(LEFT).scale(0.75)
        y_label.move_to(UP*3+LEFT*4.5).scale(0.75)

        self.add(axes, x_label, y_label, complex_sine_curve)

        # writing equal sign
        equal_sign = MathTex("=").scale(1.5).next_to(axes, RIGHT, buff=1.5)
        equal_sign.set_color(text_color)

        # writing plus symbols below each axes
        plus_sign1 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-1.5*UP, buff=0.5)
        plus_sign1.set_color(text_color)
        plus_sign2 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-5.0*UP, buff=0.5)
        plus_sign2.set_color(text_color)
        plus_sign3 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-9.0*UP, buff=0.5)
        plus_sign3.set_color(text_color)

        # writing fourier series text
        fourier_series_text = MathTex(r"f(x) = \sum_{n=1}^{\infty} w_n^{(2)} \sin(w_n^{(1)} x + b_n^{(1)})").scale(0.75).next_to(axes, DOWN, buff=1.0)
        fourier_series_text.set_color(text_color)
        fourier_series_label = Text("Fourier Series Representation", font_size=24).next_to(fourier_series_text, DOWN, buff=0.5)
        fourier_series_label.set_color(text_color)

        # drawing new axes on the right with a new sine wave
        new_axes1 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes1.next_to(axes, 0.5*RIGHT-2.75*UP, buff=-2).scale(0.25)
        new_axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes2.next_to(new_axes1, DOWN, buff=-2).scale(0.25)
        new_axes3 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes3.next_to(new_axes2, DOWN, buff=-2).scale(0.25)
        new_axes4 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes4.next_to(new_axes3, DOWN, buff=-2).scale(0.25)

        sineCurve1 = new_axes1.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x), color=green_color)
        sineCurve2 = new_axes2.plot(lambda x: 1.5+0.4*np.sin(2*np.pi*2.3*x+0.5), color=green_color)
        sineCurve3 = new_axes3.plot(lambda x: 1.5+0.3*np.sin(2*np.pi*4.7*x+1.2), color=green_color)
        sineCurve4 = new_axes4.plot(lambda x: 1.5+0.2*np.sin(2*np.pi*7*x), color=green_color)

        self.play(Write(equal_sign))

        self.play(Create(new_axes1), Create(sineCurve1),
                  Create(new_axes2), Create(sineCurve2),
                  Create(new_axes3), Create(sineCurve3),
                  Create(new_axes4), Create(sineCurve4),
                  Write(plus_sign1), Write(plus_sign2),
                  Write(plus_sign3))

        self.play(Write(fourier_series_text), Write(fourier_series_label))

        self.wait(1)

class UndrawingComponentGraphs(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)

        # scale down the axes and curve
        axes.scale(0.5).to_edge(UL)
        complex_sine_curve.scale(0.5).to_edge(UL)
        x_label.move_to(LEFT).scale(0.75)
        y_label.move_to(UP*3+LEFT*4.5).scale(0.75)

        # writing equal sign
        equal_sign = MathTex("=").scale(1.5).next_to(axes, RIGHT, buff=1.5)
        equal_sign.set_color(text_color)

        # writing plus symbols below each axes
        plus_sign1 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-1.5*UP, buff=0.5)
        plus_sign1.set_color(text_color)
        plus_sign2 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-5.0*UP, buff=0.5)
        plus_sign2.set_color(text_color)
        plus_sign3 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-9.0*UP, buff=0.5)
        plus_sign3.set_color(text_color)

        # writing fourier series text
        fourier_series_text = MathTex(r"f(x) = \sum_{n=1}^{\infty} w_n^{(2)} \sin(w_n^{(1)} x + b_n^{(1)})").scale(0.75).next_to(axes, DOWN, buff=1.0)
        fourier_series_text.set_color(text_color)
        fourier_series_label = Text("Fourier Series Representation", font_size=24).next_to(fourier_series_text, DOWN, buff=0.5)
        fourier_series_label.set_color(text_color)

        # drawing new axes on the right with a new sine wave
        new_axes1 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes1.next_to(axes, 0.5*RIGHT-2.75*UP, buff=-2).scale(0.25)
        new_axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes2.next_to(new_axes1, DOWN, buff=-2).scale(0.25)
        new_axes3 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes3.next_to(new_axes2, DOWN, buff=-2).scale(0.25)
        new_axes4 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes4.next_to(new_axes3, DOWN, buff=-2).scale(0.25)

        sineCurve1 = new_axes1.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x), color=green_color)
        sineCurve2 = new_axes2.plot(lambda x: 1.5+0.4*np.sin(2*np.pi*2.3*x+0.5), color=green_color)
        sineCurve3 = new_axes3.plot(lambda x: 1.5+0.3*np.sin(2*np.pi*4.7*x+1.2), color=green_color)
        sineCurve4 = new_axes4.plot(lambda x: 1.5+0.2*np.sin(2*np.pi*7*x), color=green_color)

        self.add(axes, x_label, y_label, complex_sine_curve,equal_sign,
                 plus_sign1, plus_sign2, plus_sign3, new_axes1, new_axes2, new_axes3, new_axes4,
                 sineCurve1, sineCurve2, sineCurve3, sineCurve4,
                 fourier_series_text, fourier_series_label)

        # undrawing the component graphs and plus signs
        self.play(Uncreate(sineCurve1), Uncreate(sineCurve2),
                  Uncreate(sineCurve3), Uncreate(sineCurve4),
                  Unwrite(fourier_series_text), Unwrite(fourier_series_label))

        self.wait(1)

class DrawingSigmoidComponents(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)

        # scale down the axes and curve
        axes.scale(0.5).to_edge(UL)
        complex_sine_curve.scale(0.5).to_edge(UL)
        x_label.move_to(LEFT).scale(0.75)
        y_label.move_to(UP*3+LEFT*4.5).scale(0.75)

        # writing equal sign
        equal_sign = MathTex("=").scale(1.5).next_to(axes, RIGHT, buff=1.5)
        equal_sign.set_color(text_color)

        # writing plus symbols below each axes
        plus_sign1 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-1.5*UP, buff=0.5)
        plus_sign1.set_color(text_color)
        plus_sign2 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-5.0*UP, buff=0.5)
        plus_sign2.set_color(text_color)
        plus_sign3 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-9.0*UP, buff=0.5)
        plus_sign3.set_color(text_color)

        # drawing new axes on the right with a new sine wave
        new_axes1 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes1.next_to(axes, 0.5*RIGHT-2.75*UP, buff=-2).scale(0.25)
        new_axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes2.next_to(new_axes1, DOWN, buff=-2).scale(0.25)
        new_axes3 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes3.next_to(new_axes2, DOWN, buff=-2).scale(0.25)
        new_axes4 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes4.next_to(new_axes3, DOWN, buff=-2).scale(0.25)

        sigmoidCurve1 = new_axes1.plot(lambda x: 0.5+1/(1+np.exp(-2*x)), color=green_color)
        sigmoidCurve2 = new_axes2.plot(lambda x: 0.5+1/(1+np.exp(-4*x)), color=green_color)
        sigmoidCurve3 = new_axes3.plot(lambda x: 0.5+1-1/(1+np.exp(-5.5*x)), color=green_color)
        sigmoidCurve4 = new_axes4.plot(lambda x: 0.5+1-1/(1+np.exp(-10*x+4)), color=green_color)

        text1 = Text("Weighted sum of non-periodic functions?", font_size=24).next_to(axes, DOWN, buff=2.5)
        text1.set_color(text_color)

        self.add(axes, x_label, y_label, complex_sine_curve,equal_sign,
                 plus_sign1, plus_sign2, plus_sign3, new_axes1, new_axes2,
                 new_axes3, new_axes4)

        # drawing sigmoid curve on all axes
        self.play(Create(sigmoidCurve1), Create(sigmoidCurve2),
                  Create(sigmoidCurve3), Create(sigmoidCurve4))
        self.play(Write(text1))

        self.wait(1)

class DrawingSigmoidComponents2(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)

        # scale down the axes and curve
        axes.scale(0.5).to_edge(UL)
        complex_sine_curve.scale(0.5).to_edge(UL)
        x_label.move_to(LEFT).scale(0.75)
        y_label.move_to(UP*3+LEFT*4.5).scale(0.75)

        # writing equal sign
        equal_sign = MathTex("=").scale(1.5).next_to(axes, RIGHT, buff=1.5)
        equal_sign.set_color(text_color)

        # writing plus symbols below each axes
        plus_sign1 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-1.5*UP, buff=0.5)
        plus_sign1.set_color(text_color)
        plus_sign2 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-5.0*UP, buff=0.5)
        plus_sign2.set_color(text_color)
        plus_sign3 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-9.0*UP, buff=0.5)
        plus_sign3.set_color(text_color)

        # drawing new axes on the right with a new sine wave
        new_axes1 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes1.next_to(axes, 0.5*RIGHT-2.75*UP, buff=-2).scale(0.25)
        new_axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes2.next_to(new_axes1, DOWN, buff=-2).scale(0.25)
        new_axes3 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes3.next_to(new_axes2, DOWN, buff=-2).scale(0.25)
        new_axes4 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes4.next_to(new_axes3, DOWN, buff=-2).scale(0.25)

        sigmoidCurve1 = new_axes1.plot(lambda x: 0.5+1/(1+np.exp(-2*x)), color=green_color)
        sigmoidCurve2 = new_axes2.plot(lambda x: 0.5+1/(1+np.exp(-4*x)), color=green_color)
        sigmoidCurve3 = new_axes3.plot(lambda x: 0.5+1-1/(1+np.exp(-5.5*x)), color=green_color)
        sigmoidCurve4 = new_axes4.plot(lambda x: 0.5+1-1/(1+np.exp(-10*x+4)), color=green_color)

        text1 = Text("Weighted sum of non-periodic functions?", font_size=24).next_to(axes, DOWN, buff=2.5)
        text1.set_color(text_color)

        text2 = Text("Yes! with more components", font_size=24).next_to(axes, DOWN, buff=2.5)
        text2.set_color(blue_color)

        self.add(axes, x_label, y_label, complex_sine_curve,equal_sign,
                 plus_sign1, plus_sign2, plus_sign3, new_axes1, new_axes2,
                 new_axes3, new_axes4,text1,
                 sigmoidCurve1, sigmoidCurve2, sigmoidCurve3, sigmoidCurve4)

        # moving text1 slightly up and writing text2
        self.play(text1.animate.shift(UP*0.5))
        self.play(Write(text2))

        self.wait(1)

class TransformingGraphsToEqns(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)

        # scale down the axes and curve
        axes.scale(0.5).to_edge(UL)
        complex_sine_curve.scale(0.5).to_edge(UL)
        x_label.move_to(LEFT).scale(0.75)
        y_label.move_to(UP*3+LEFT*4.5).scale(0.75)

        # writing equal sign
        equal_sign = MathTex("=").scale(1.5).next_to(axes, RIGHT, buff=1.5)
        equal_sign.set_color(text_color)

        # writing plus symbols below each axes
        plus_sign1 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-1.5*UP, buff=0.5)
        plus_sign1.set_color(text_color)
        plus_sign2 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-5.0*UP, buff=0.5)
        plus_sign2.set_color(text_color)
        plus_sign3 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-9.0*UP, buff=0.5)
        plus_sign3.set_color(text_color)

        # drawing new axes on the right with a new sine wave
        new_axes1 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes1.next_to(axes, 0.5*RIGHT-2.75*UP, buff=-2).scale(0.25)
        new_axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes2.next_to(new_axes1, DOWN, buff=-2).scale(0.25)
        new_axes3 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes3.next_to(new_axes2, DOWN, buff=-2).scale(0.25)
        new_axes4 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes4.next_to(new_axes3, DOWN, buff=-2).scale(0.25)

        sigmoidCurve1 = new_axes1.plot(lambda x: 0.5+1/(1+np.exp(-2*x)), color=green_color)
        sigmoidCurve2 = new_axes2.plot(lambda x: 0.5+1/(1+np.exp(-4*x)), color=green_color)
        sigmoidCurve3 = new_axes3.plot(lambda x: 0.5+1-1/(1+np.exp(-5.5*x)), color=green_color)
        sigmoidCurve4 = new_axes4.plot(lambda x: 0.5+1-1/(1+np.exp(-10*x+4)), color=green_color)

        text1 = Text("Weighted sum of non-periodic functions?", font_size=24).next_to(axes, DOWN, buff=2.5)
        text1.set_color(text_color)
        text1.shift(UP*0.5)

        text2 = Text("Yes! with more components", font_size=24).next_to(axes, DOWN, buff=2.5)
        text2.set_color(blue_color)

        self.add(axes, x_label, y_label, complex_sine_curve,equal_sign,
                 plus_sign1, plus_sign2, plus_sign3, new_axes1, new_axes2,
                 new_axes3, new_axes4,text1,text2,
                 sigmoidCurve1, sigmoidCurve2, sigmoidCurve3, sigmoidCurve4)

        fGroup = VGroup(axes, complex_sine_curve,x_label, y_label)
        fOfX = MathTex(r"f(x)").scale(1)
        fOfX.set_color(text_color).move_to(fGroup.get_center())

        s1Group = VGroup(new_axes1, sigmoidCurve1)
        sOfX1 = MathTex(r"\sigma(w_1^{(1)} x + b_1^{(1)})").scale(1)
        sOfX1.set_color(text_color).move_to(s1Group.get_center())
        s2Group = VGroup(new_axes2, sigmoidCurve2)
        sOfX2 = MathTex(r"\sigma(w_2^{(1)} x + b_2^{(1)})").scale(1)
        sOfX2.set_color(text_color).move_to(s2Group.get_center())
        s3Group = VGroup(new_axes3, sigmoidCurve3)
        sOfX3 = MathTex(r"\sigma(w_3^{(1)} x + b_3^{(1)})").scale(1)
        sOfX3.set_color(text_color).move_to(s3Group.get_center())
        s4Group = VGroup(new_axes4, sigmoidCurve4)
        sOfX4 = MathTex(r"\sigma(w_4^{(1)} x + b_4^{(1)})").scale(1)
        sOfX4.set_color(text_color).move_to(s4Group.get_center())

        # transforming the axes to f(x) equation and disappearing the complex sine curve
        self.play(ReplacementTransform(fGroup, fOfX))
        self.wait(1)
        self.play(ReplacementTransform(s1Group, sOfX1),
                  ReplacementTransform(s2Group, sOfX2),
                  ReplacementTransform(s3Group, sOfX3),
                  ReplacementTransform(s4Group, sOfX4))
        self.wait(1)

class EqnsRearranging(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)

        # scale down the axes and curve
        axes.scale(0.5).to_edge(UL)
        complex_sine_curve.scale(0.5).to_edge(UL)
        x_label.move_to(LEFT).scale(0.75)
        y_label.move_to(UP*3+LEFT*4.5).scale(0.75)

        # writing equal sign
        equal_sign = MathTex("=").scale(1.5).next_to(axes, RIGHT, buff=1.5)
        equal_sign.set_color(text_color)

        # writing plus symbols below each axes
        plus_sign1 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-1.5*UP, buff=0.5)
        plus_sign1.set_color(text_color)
        plus_sign2 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-5.0*UP, buff=0.5)
        plus_sign2.set_color(text_color)
        plus_sign3 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-9.0*UP, buff=0.5)
        plus_sign3.set_color(text_color)

        # drawing new axes on the right with a new sine wave
        new_axes1 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes1.next_to(axes, 0.5*RIGHT-2.75*UP, buff=-2).scale(0.25)
        new_axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes2.next_to(new_axes1, DOWN, buff=-2).scale(0.25)
        new_axes3 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes3.next_to(new_axes2, DOWN, buff=-2).scale(0.25)
        new_axes4 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes4.next_to(new_axes3, DOWN, buff=-2).scale(0.25)

        sigmoidCurve1 = new_axes1.plot(lambda x: 0.5+1/(1+np.exp(-2*x)), color=green_color)
        sigmoidCurve2 = new_axes2.plot(lambda x: 0.5+1/(1+np.exp(-4*x)), color=green_color)
        sigmoidCurve3 = new_axes3.plot(lambda x: 0.5+1-1/(1+np.exp(-5.5*x)), color=green_color)
        sigmoidCurve4 = new_axes4.plot(lambda x: 0.5+1-1/(1+np.exp(-10*x+4)), color=green_color)

        text1 = Text("Weighted sum of non-periodic functions?", font_size=24).next_to(axes, DOWN, buff=2.5)
        text1.set_color(text_color)
        text1.shift(UP*0.5)

        text2 = Text("Yes! with more components", font_size=24).next_to(axes, DOWN, buff=2.5)
        text2.set_color(blue_color)

        fGroup = VGroup(axes, complex_sine_curve,x_label, y_label)
        fOfX = MathTex(r"f(x)").scale(1)
        fOfX.set_color(text_color).move_to(fGroup.get_center())

        s1Group = VGroup(new_axes1, sigmoidCurve1)
        sOfX1 = MathTex(r"\sigma(w_1^{(1)} x + b_1^{(1)})").scale(1)
        sOfX1.set_color(text_color).move_to(s1Group.get_center())
        s2Group = VGroup(new_axes2, sigmoidCurve2)
        sOfX2 = MathTex(r"\sigma(w_2^{(1)} x + b_2^{(1)})").scale(1)
        sOfX2.set_color(text_color).move_to(s2Group.get_center())
        s3Group = VGroup(new_axes3, sigmoidCurve3)
        sOfX3 = MathTex(r"\sigma(w_3^{(1)} x + b_3^{(1)})").scale(1)
        sOfX3.set_color(text_color).move_to(s3Group.get_center())
        s4Group = VGroup(new_axes4, sigmoidCurve4)
        sOfX4 = MathTex(r"\sigma(w_4^{(1)} x + b_4^{(1)})").scale(1)
        sOfX4.set_color(text_color).move_to(s4Group.get_center())

        plus_sign4 = MathTex("+").scale(1.0).set_color(text_color)
        dots = MathTex(r"\dots").scale(1).set_color(text_color)
        plus_sign4.move_to(RIGHT*5.5+DOWN)
        dots.move_to(RIGHT*6.0+DOWN)

        w21 = MathTex(r"w_1^{(2)}").scale(1).set_color(text_color).move_to(LEFT*2.5)
        w22 = MathTex(r"w_2^{(2)}").scale(1).set_color(text_color).move_to(RIGHT*2.25)
        w23 = MathTex(r"w_3^{(2)}").scale(1).set_color(text_color).move_to(LEFT*3.0+DOWN)
        w24 = MathTex(r"w_4^{(2)}").scale(1).set_color(text_color).move_to(RIGHT*1.6+DOWN)

        self.add(text1, text2, fOfX, sOfX1, sOfX2, sOfX3, sOfX4,
                 plus_sign1, plus_sign2, plus_sign3, equal_sign)

        # transforming the axes to f(x) equation and disappearing the complex sine curve
        self.play(Unwrite(text1), Unwrite(text2),
                  fOfX.animate.move_to(LEFT*4.5).scale(1),
                  equal_sign.animate.move_to(LEFT*3.5).scale(1),
                  Write(w21),
                  sOfX1.animate.move_to(LEFT*0.5).scale(1),
                  plus_sign1.animate.move_to(RIGHT*1.5).scale(1),
                  Write(w22),
                  sOfX2.animate.move_to(RIGHT*4.25).scale(1),
                  plus_sign2.animate.move_to(LEFT*3.7+DOWN).scale(1),
                  Write(w23),
                  sOfX3.animate.move_to(LEFT*1.0+DOWN).scale(1),
                  plus_sign3.animate.move_to(RIGHT*0.9+DOWN).scale(1),
                  Write(w24),
                  sOfX4.animate.move_to(RIGHT*3.6+DOWN).scale(1))
        self.play(Write(plus_sign4), Write(dots))

        self.wait(1)

class EqnsRewriting(Scene):
    def construct(self):
        # Create axes
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

        # drawing a complex sine curve
        complex_sine_curve = axes.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=red_color)

        # scale down the axes and curve
        axes.scale(0.5).to_edge(UL)
        complex_sine_curve.scale(0.5).to_edge(UL)
        x_label.move_to(LEFT).scale(0.75)
        y_label.move_to(UP*3+LEFT*4.5).scale(0.75)

        # writing equal sign
        equal_sign = MathTex("=").scale(1.5).next_to(axes, RIGHT, buff=1.5)
        equal_sign.set_color(text_color)

        # writing plus symbols below each axes
        plus_sign1 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-1.5*UP, buff=0.5)
        plus_sign1.set_color(text_color)
        plus_sign2 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-5.0*UP, buff=0.5)
        plus_sign2.set_color(text_color)
        plus_sign3 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-9.0*UP, buff=0.5)
        plus_sign3.set_color(text_color)

        # drawing new axes on the right with a new sine wave
        new_axes1 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes1.next_to(axes, 0.5*RIGHT-2.75*UP, buff=-2).scale(0.25)
        new_axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes2.next_to(new_axes1, DOWN, buff=-2).scale(0.25)
        new_axes3 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes3.next_to(new_axes2, DOWN, buff=-2).scale(0.25)
        new_axes4 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes4.next_to(new_axes3, DOWN, buff=-2).scale(0.25)

        sigmoidCurve1 = new_axes1.plot(lambda x: 0.5+1/(1+np.exp(-2*x)), color=green_color)
        sigmoidCurve2 = new_axes2.plot(lambda x: 0.5+1/(1+np.exp(-4*x)), color=green_color)
        sigmoidCurve3 = new_axes3.plot(lambda x: 0.5+1-1/(1+np.exp(-5.5*x)), color=green_color)
        sigmoidCurve4 = new_axes4.plot(lambda x: 0.5+1-1/(1+np.exp(-10*x+4)), color=green_color)

        text1 = Text("Weighted sum of non-periodic functions?", font_size=24).next_to(axes, DOWN, buff=2.5)
        text1.set_color(text_color)
        text1.shift(UP*0.5)

        text2 = Text("Yes! with more components", font_size=24).next_to(axes, DOWN, buff=2.5)
        text2.set_color(blue_color)

        fGroup = VGroup(axes, complex_sine_curve,x_label, y_label)
        fOfX = MathTex(r"f(x)").scale(1)
        fOfX.set_color(text_color).move_to(fGroup.get_center())

        s1Group = VGroup(new_axes1, sigmoidCurve1)
        sOfX1 = MathTex(r"\sigma(w_1^{(1)} x + b_1^{(1)})").scale(1)
        sOfX1.set_color(text_color).move_to(s1Group.get_center())
        s2Group = VGroup(new_axes2, sigmoidCurve2)
        sOfX2 = MathTex(r"\sigma(w_2^{(1)} x + b_2^{(1)})").scale(1)
        sOfX2.set_color(text_color).move_to(s2Group.get_center())
        s3Group = VGroup(new_axes3, sigmoidCurve3)
        sOfX3 = MathTex(r"\sigma(w_3^{(1)} x + b_3^{(1)})").scale(1)
        sOfX3.set_color(text_color).move_to(s3Group.get_center())
        s4Group = VGroup(new_axes4, sigmoidCurve4)
        sOfX4 = MathTex(r"\sigma(w_4^{(1)} x + b_4^{(1)})").scale(1)
        sOfX4.set_color(text_color).move_to(s4Group.get_center())

        plus_sign4 = MathTex("+").scale(1.0).set_color(text_color)
        dots = MathTex(r"\dots").scale(1).set_color(text_color)
        plus_sign4.move_to(RIGHT*5.5+DOWN)
        dots.move_to(RIGHT*6.0+DOWN)

        w21 = MathTex(r"w_1^{(2)}").scale(1).set_color(text_color).move_to(LEFT*2.5)
        w22 = MathTex(r"w_2^{(2)}").scale(1).set_color(text_color).move_to(RIGHT*2.25)
        w23 = MathTex(r"w_3^{(2)}").scale(1).set_color(text_color).move_to(LEFT*3.0+DOWN)
        w24 = MathTex(r"w_4^{(2)}").scale(1).set_color(text_color).move_to(RIGHT*1.6+DOWN)

        # transforming the axes to f(x) equation and disappearing the complex sine curve
        fOfX.move_to(LEFT*4.5).scale(1)
        equal_sign.move_to(LEFT*3.5).scale(1)
        sOfX1.move_to(LEFT*0.5).scale(1)
        plus_sign1.move_to(RIGHT*1.5).scale(1)
        sOfX2.move_to(RIGHT*4.25).scale(1)
        plus_sign2.move_to(LEFT*3.7+DOWN).scale(1)
        sOfX3.move_to(LEFT*1.0+DOWN).scale(1)
        plus_sign3.move_to(RIGHT*0.9+DOWN).scale(1)
        sOfX4.move_to(RIGHT*3.6+DOWN).scale(1)

        eqnGroup = VGroup(sOfX1, sOfX2, sOfX3, sOfX4,w21, w22, w23, w24,
                      plus_sign1, plus_sign2, plus_sign3, plus_sign4, dots)

        sumEqn = MathTex(r"\sum_{n=1}^{N} w_n^{(2)} \sigma(w_n^{(1)} x + b_n^{(1)})").scale(1)
        sumEqn.set_color(text_color).move_to(UP*0.5+RIGHT*1.5)

        finiteText = Text("Rewriting with finite no. of terms...", font_size=24).move_to(UP*2)
        finiteText.set_color(text_color)

        approxSymbol = MathTex(r"\approx").scale(1.5).move_to(LEFT*1.5+UP*0.5)
        approxSymbol.set_color(text_color)

        self.add(fOfX, sOfX1, sOfX2, sOfX3, sOfX4,w21, w22, w23, w24,
                 plus_sign1, plus_sign2, plus_sign3, equal_sign, plus_sign4, dots)

        self.play(Write(finiteText))
        self.wait(1)
        self.play(ReplacementTransform(eqnGroup, sumEqn),
                  fOfX.animate.move_to(LEFT*2.5+UP*0.5).scale(1),
                  equal_sign.animate.move_to(LEFT*1.5+UP*0.5).scale(1))
        self.wait(1)
        self.play(ReplacementTransform(equal_sign, approxSymbol))

        self.wait(1)

class TheoremIntro(Scene):
    def construct(self):

        fOfX = MathTex(r"f(x)").scale(1)
        fOfX.set_color(text_color)
        fOfX.move_to(LEFT*2.5+UP*0.5).scale(1)

        sumEqn = MathTex(r"\sum_{n=1}^{N} w_n^{(2)} \sigma(w_n^{(1)} x + b_n^{(1)})").scale(1)
        sumEqn.set_color(text_color).move_to(UP*0.5+RIGHT*1.5)

        finiteText = Text("Rewriting with finite no. of terms...", font_size=24).move_to(UP*2)
        finiteText.set_color(text_color)

        approxSymbol = MathTex(r"\approx").scale(1.5).move_to(LEFT*1.5+UP*0.5)
        approxSymbol.set_color(text_color)

        theoremStatement = Text("Universal Approximation Theorem", font_size=36)
        theoremStatement.set_color(blue_color)
        authorName = Text("Cybenko, 1989", font_size=24)
        authorName.set_color(text_color)
        authorName.move_to(DOWN*0.5)

        eqnGroup = VGroup(fOfX, sumEqn, approxSymbol)

        box = SurroundingRectangle(eqnGroup, color=blue_color, buff=0.2)
        box.move_to(UP*1.5)

        self.add(finiteText, sumEqn, approxSymbol,fOfX)

        self.play(Unwrite(finiteText))
        self.play(eqnGroup.animate.move_to(UP*1.5))
        self.play(Write(theoremStatement), Create(box))
        self.play(Write(authorName))


        self.wait(1)

class TheoremIntro2(Scene):
    def construct(self):

        fOfX = MathTex(r"f(x)").scale(1)
        fOfX.set_color(text_color)
        fOfX.move_to(LEFT*2.5+UP*0.5).scale(1)

        sumEqn = MathTex(r"\sum_{n=1}^{N} w_n^{(2)} \sigma(w_n^{(1)} x + b_n^{(1)})").scale(1)
        sumEqn.set_color(text_color).move_to(UP*0.5+RIGHT*1.5)

        approxSymbol = MathTex(r"\approx").scale(1.5).move_to(LEFT*1.5+UP*0.5)
        approxSymbol.set_color(text_color)

        theoremStatement = Text("Universal Approximation Theorem", font_size=36)
        theoremStatement.set_color(blue_color)
        authorName = Text("Cybenko, 1989", font_size=24)
        authorName.set_color(text_color)
        authorName.move_to(DOWN*0.5)

        eqnGroup = VGroup(fOfX, sumEqn, approxSymbol).move_to(UP*1.5)

        box = SurroundingRectangle(eqnGroup, color=blue_color, buff=0.2)
        box.move_to(UP*1.5)

        sigmoidFunction1 = MathTex(r"\sigma(w_n^{(1)}x+b_n^{(1)}) = ").scale(1)
        sigmoidFunction1.set_color(text_color)
        sigmoidStatement1 = Text("Sigmoid function ", font_size=24)
        sigmoidStatement1.set_color(text_color)
        sigmoidFunction2 = MathTex(r" = \frac{1}{1+e^{-(w_n^{(1)}x+b_n^{(1)})}").scale(1)
        sigmoidFunction2.set_color(text_color)
        sigmoidFunction1.move_to(2*DOWN+LEFT*4)
        sigmoidStatement1.next_to(sigmoidFunction1, RIGHT, buff=0.5)
        sigmoidFunction2.next_to(sigmoidStatement1, RIGHT, buff=0.5)

        self.add(eqnGroup,box,theoremStatement,authorName)

        self.play(box.animate.move_to(UP*2.0), eqnGroup.animate.move_to(UP*2.0),
                  theoremStatement.animate.move_to(UP*0.5),
                  authorName.animate.move_to(UP*0))
        self.play(Write(sigmoidFunction1))
        self.play(Write(sigmoidStatement1))
        self.play(Write(sigmoidFunction2))

        self.wait(1)


#==============================================================================
