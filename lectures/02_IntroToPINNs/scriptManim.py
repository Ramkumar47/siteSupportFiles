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
mauvre_color     = "#8839ef"

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

class WhyNotSine1(Scene):
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

        box.move_to(UP*2.0)
        eqnGroup.move_to(UP*2.0)
        theoremStatement.move_to(UP*0.5)
        authorName.move_to(UP*0)

        existingElemGroup = VGroup(eqnGroup,box,theoremStatement,authorName,
                 sigmoidFunction1, sigmoidStatement1, sigmoidFunction2)

        self.add(existingElemGroup)

        self.play(Unwrite(sigmoidFunction1), Unwrite(sigmoidStatement1), Unwrite(sigmoidFunction2),
                  Unwrite(theoremStatement), Unwrite(authorName), Uncreate(box), Unwrite(eqnGroup))

        text = Text("Why not use fourier series instead of neural networks?", font_size=34)
        text.set_color(blue_color)

        self.play(Write(text))

        # self.play(box.animate.move_to(UP*2.0), eqnGroup.animate.move_to(UP*2.0),
        #           theoremStatement.animate.move_to(UP*0.5),
        #           authorName.animate.move_to(UP*0))
        # self.play(Write(sigmoidFunction1))
        # self.play(Write(sigmoidStatement1))
        # self.play(Write(sigmoidFunction2))

        self.wait(1)

class WhyNotSine2(Scene):
    def construct(self):

        text = Text("Why not use fourier series instead of neural networks?", font_size=34)
        text.set_color(blue_color)

        self.add(text)

        label1Dexample = Text("1D case:", font_size=34)
        label1Dexample.set_color(red_color)
        label1Dexample.move_to(UP*1.75+LEFT*4.5)
        label1DmathDef = MathTex(r"x \to y").scale(1)
        label1DmathDef.set_color(text_color).move_to(UP*1.75)

        fourier1Dlabel = Text("Fourier series:", font_size=28)
        fourier1Dlabel.set_color(text_color)
        fourier1Dlabel.move_to(UP*0.5+LEFT*5.5)
        fourier1DmathDef = MathTex(r"f(x) \approx  \sum_{n=1}^{N} w_n^{(2)} \sin(w_n^{(1)}x+b_n^{(1)})").scale(1)
        fourier1DmathDef.set_color(text_color).move_to(UP*0.5)

        nn1Dlabel = Text("Neural network:", font_size=28)
        nn1Dlabel.set_color(text_color)
        nn1Dlabel.move_to(LEFT*5.5+DOWN*1.5)
        nn1DmathDef = MathTex(r"f(x) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_n^{(1)}x+b_n^{(1)})").scale(1)
        nn1DmathDef.set_color(text_color).move_to(DOWN*1.5)

        self.play(text.animate.move_to(UP*3.0))
        self.play(Write(label1Dexample))
        self.wait(1)
        self.play(Write(label1DmathDef))
        self.wait(2)
        self.play(Write(fourier1Dlabel))
        self.play(Write(fourier1DmathDef))
        self.wait(2)
        self.play(Write(nn1Dlabel))
        self.play(Write(nn1DmathDef))

        # self.play(box.animate.move_to(UP*2.0), eqnGroup.animate.move_to(UP*2.0),
        #           theoremStatement.animate.move_to(UP*0.5),
        #           authorName.animate.move_to(UP*0))
        # self.play(Write(sigmoidFunction1))
        # self.play(Write(sigmoidStatement1))
        # self.play(Write(sigmoidFunction2))

        self.wait(1)

class WhyNotSine3(Scene):
    def construct(self):

        text = Text("Why not use fourier series instead of neural networks?", font_size=34)
        text.set_color(blue_color)

        self.add(text)

        label1Dexample = Text("1D case:", font_size=34)
        label1Dexample.set_color(red_color)
        label1Dexample.move_to(UP*1.75+LEFT*4.5)
        label1DmathDef = MathTex(r"x \to y").scale(1)
        label1DmathDef.set_color(text_color).move_to(UP*1.75)

        fourier1Dlabel = Text("Fourier series:", font_size=28)
        fourier1Dlabel.set_color(text_color)
        fourier1Dlabel.move_to(UP*0.5+LEFT*5.5)
        fourier1DmathDef = MathTex(r"f(x) \approx  \sum_{n=1}^{N} w_n^{(2)} \sin(w_n^{(1)}x+b_n^{(1)})").scale(1)
        fourier1DmathDef.set_color(text_color).move_to(UP*0.5)

        nn1Dlabel = Text("Neural network:", font_size=28)
        nn1Dlabel.set_color(text_color)
        nn1Dlabel.move_to(LEFT*5.5+DOWN*1.5)
        nn1DmathDef = MathTex(r"f(x) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_n^{(1)}x+b_n^{(1)})").scale(1)
        nn1DmathDef.set_color(text_color).move_to(DOWN*1.5)

        text.move_to(UP*3.0)

        group1D = VGroup(label1Dexample, label1DmathDef, fourier1Dlabel,
                         fourier1DmathDef, nn1Dlabel, nn1DmathDef)

        self.add(text, group1D)

        label2Dexample = Text("2D case:", font_size=34)
        label2Dexample.set_color(red_color)
        label2Dexample.move_to(UP*2.+LEFT*4.5)
        label2DmathDef = MathTex(r"(x,y) \to z").scale(1)
        label2DmathDef.set_color(text_color).move_to(UP*2)

        self.play(Unwrite(label1Dexample), Unwrite(label1DmathDef),
                  Unwrite(fourier1Dlabel), Unwrite(fourier1DmathDef),
                  Unwrite(nn1Dlabel), Unwrite(nn1DmathDef))
        self.wait(1)

        self.play(Write(label2Dexample))
        self.play(Write(label2DmathDef))

        self.wait(1)

class WhyNotSine4(Scene):
    def construct(self):

        text = Text("Why not use fourier series instead of neural networks?", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        self.add(text)

        label2Dexample = Text("2D case:", font_size=34)
        label2Dexample.set_color(red_color)
        label2Dexample.move_to(UP*2.+LEFT*4.5)
        label2DmathDef = MathTex(r"(x,y) \to z").scale(1)
        label2DmathDef.set_color(text_color).move_to(UP*2.)

        self.add(label2Dexample, label2DmathDef)

        fourier2Dlabel = Text("Fourier series:", font_size=28)
        fourier2Dlabel.set_color(text_color)
        fourier2Dlabel.move_to(UP*0.75+LEFT*5.5)
        fourier2DmathDef = MathTex(r"f(x,y) \approx  \sum_{m=1}^M\sum_{n=1}^NB_{mn}\sin(\frac{n\pi x}{L_x})\sin(\frac{n\pi y}{L_y})").scale(1)
        fourier2DmathDef2 = MathTex(r"B_{mn} = \frac{4}{L_xL_y}\int_0^{L_x}\int_0^{L_y}f(x,y)\sin(\frac{m\pi x}{L_x})\sin(\frac{n\pi y}{L_y})dxdy").scale(1)
        fourier2DmathDef.set_color(text_color).move_to(UP*0.75+RIGHT*0.5)
        fourier2DmathDef2.set_color(text_color).move_to(DOWN*0.75)

        self.play(Write(fourier2Dlabel))
        self.play(Write(fourier2DmathDef))
        self.play(Write(fourier2DmathDef2))


        self.wait(1)

class WhyNotSine5(Scene):
    def construct(self):

        text = Text("Why not use fourier series instead of neural networks?", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        self.add(text)

        label2Dexample = Text("2D case:", font_size=34)
        label2Dexample.set_color(red_color)
        label2Dexample.move_to(UP*2.+LEFT*4.5)
        label2DmathDef = MathTex(r"(x,y) \to z").scale(1)
        label2DmathDef.set_color(text_color).move_to(UP*2.)

        self.add(label2Dexample, label2DmathDef)

        fourier2Dlabel = Text("Fourier series:", font_size=28)
        fourier2Dlabel.set_color(text_color)
        fourier2Dlabel.move_to(UP*0.75+LEFT*5.5)
        fourier2DmathDef = MathTex(r"f(x,y) \approx  \sum_{m=1}^M\sum_{n=1}^NB_{mn}\sin(\frac{n\pi x}{L_x})\sin(\frac{n\pi y}{L_y})").scale(1)
        fourier2DmathDef2 = MathTex(r"B_{mn} = \frac{4}{L_xL_y}\int_0^{L_x}\int_0^{L_y}f(x,y)\sin(\frac{m\pi x}{L_x})\sin(\frac{n\pi y}{L_y})dxdy").scale(1)
        fourier2DmathDef.set_color(text_color).move_to(UP*0.75+RIGHT*0.5)
        fourier2DmathDef2.set_color(text_color).move_to(DOWN*0.75)

        self.add(fourier2Dlabel, fourier2DmathDef, fourier2DmathDef2)

        nn2Dlabel = Text("Neural network:", font_size=28)
        nn2Dlabel.set_color(text_color)
        nn2Dlabel.move_to(LEFT*5.5+DOWN*2.5)
        nn2DmathDef = MathTex(r"f(x) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_{n,1}^{(1)}x + w_{n,2}^{(1)}y +b_n^{(1)})").scale(1)
        nn2DmathDef.set_color(text_color).move_to(DOWN*2.5+RIGHT)

        # drawing box around nn2DmathDef
        box = SurroundingRectangle(nn2DmathDef, color=blue_color, buff=0.2)
        box.move_to(DOWN*2.5+RIGHT)

        self.play(Write(nn2Dlabel))
        self.play(Write(nn2DmathDef))
        self.play(Create(box))


        self.wait(1)

class WhyNotSine6(Scene):
    def construct(self):

        text = Text("Why not use fourier series instead of neural networks?", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        self.add(text)

        label2Dexample = Text("2D case:", font_size=34)
        label2Dexample.set_color(red_color)
        label2Dexample.move_to(UP*2.+LEFT*4.5)
        label2DmathDef = MathTex(r"(x,y) \to z").scale(1)
        label2DmathDef.set_color(text_color).move_to(UP*2.)

        self.add(label2Dexample, label2DmathDef)

        fourier2Dlabel = Text("Fourier series:", font_size=28)
        fourier2Dlabel.set_color(text_color)
        fourier2Dlabel.move_to(UP*0.75+LEFT*5.5)
        fourier2DmathDef = MathTex(r"f(x,y) \approx  \sum_{m=1}^M\sum_{n=1}^NB_{mn}\sin(\frac{n\pi x}{L_x})\sin(\frac{n\pi y}{L_y})").scale(1)
        fourier2DmathDef2 = MathTex(r"B_{mn} = \frac{4}{L_xL_y}\int_0^{L_x}\int_0^{L_y}f(x,y)\sin(\frac{m\pi x}{L_x})\sin(\frac{n\pi y}{L_y})dxdy").scale(1)
        fourier2DmathDef.set_color(text_color).move_to(UP*0.75+RIGHT*0.5)
        fourier2DmathDef2.set_color(text_color).move_to(DOWN*0.75)

        self.add(fourier2Dlabel, fourier2DmathDef, fourier2DmathDef2)

        nn2Dlabel = Text("Neural network:", font_size=28)
        nn2Dlabel.set_color(text_color)
        nn2Dlabel.move_to(LEFT*5.5+DOWN*2.5)
        nn2DmathDef = MathTex(r"f(x) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_{n,1}^{(1)}x + w_{n,2}^{(1)}y +b_n^{(1)})").scale(1)
        nn2DmathDef.set_color(text_color).move_to(DOWN*2.5+RIGHT)

        # drawing box around nn2DmathDef
        box = SurroundingRectangle(nn2DmathDef, color=blue_color, buff=0.2)
        box.move_to(DOWN*2.5+RIGHT)

        self.add(nn2Dlabel, nn2DmathDef, box)

        self.play(Unwrite(fourier2Dlabel), Unwrite(fourier2DmathDef),
                  Unwrite(fourier2DmathDef2), Unwrite(label2Dexample),
                  Unwrite(label2DmathDef), Unwrite(nn2Dlabel),
                  Unwrite(nn2DmathDef), Uncreate(box))

        HighDimexample = Text("Higher dimensional cases:", font_size=34)
        HighDimexample.set_color(red_color)
        HighDimexample.move_to(UP*2.+LEFT*4.0)
        HighDimText = Text("Fourier series becomes more complex", font_size=28)
        HighDimText.set_color(text_color).move_to(UP*2.+RIGHT*3)

        self.play(Write(HighDimexample))
        self.wait(1)
        self.play(Write(HighDimText))

        self.wait(1)

class WhyNotSine7(Scene):
    def construct(self):

        text = Text("Why not use fourier series instead of neural networks?", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        self.add(text)

        HighDimexample = Text("Higher dimensional cases:", font_size=34)
        HighDimexample.set_color(red_color)
        HighDimexample.move_to(UP*2.+LEFT*4.0)
        HighDimText = Text("Fourier series becomes more complex", font_size=28)
        HighDimText.set_color(text_color).move_to(UP*2.+RIGHT*3)

        self.add(HighDimexample, HighDimText)

        NNText = Text("Neural networks can handle higher dimensions easily", font_size=28)
        NNText.set_color(text_color).move_to(DOWN*1.5)

        NN1DExpression = MathTex(r"f(x) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_n^{(1)}x+b_n^{(1)})").scale(1)
        NN1DExpression.set_color(text_color).move_to(UP*0.5+LEFT*1.5)
        NN2DExpression = MathTex(r"f(x,y) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_{n,1}^{(1)}x + w_{n,2}^{(1)}y +b_n^{(1)})").scale(1)
        NN2DExpression.set_color(text_color).move_to(DOWN*1.+LEFT*0.75)
        NN3DExpression = MathTex(r"f(x,y,z) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_{n,1}^{(1)}x + w_{n,2}^{(1)}y + w_{n,3}^{(1)}z +b_n^{(1)})").scale(1)
        NN3DExpression.set_color(text_color).move_to(DOWN*2.5)

        NNEndText = Text("and so on ...", font_size=28)
        NNEndText.set_color(text_color).move_to(DOWN*3.5)

        self.play(Write(NNText))
        self.play(NNText.animate.move_to(UP*1.5))
        self.play(Write(NN1DExpression))
        self.play(Write(NN2DExpression))
        self.play(Write(NN3DExpression))
        self.play(Write(NNEndText))

        self.wait(1)

class DiagramaticRepresentation1(Scene):
    def construct(self):

        text = Text("Why not use fourier series instead of neural networks?", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        self.add(text)

        HighDimexample = Text("Higher dimensional cases:", font_size=34)
        HighDimexample.set_color(red_color)
        HighDimexample.move_to(UP*2.+LEFT*4.0)
        HighDimText = Text("Fourier series becomes more complex", font_size=28)
        HighDimText.set_color(text_color).move_to(UP*2.+RIGHT*3)

        self.add(HighDimexample, HighDimText)

        NNText = Text("Neural networks can handle higher dimensions easily", font_size=28)
        NNText.set_color(text_color).move_to(DOWN*1.5)

        NN1DExpression = MathTex(r"f(x) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_n^{(1)}x+b_n^{(1)})").scale(1)
        NN1DExpression.set_color(text_color).move_to(UP*0.5+LEFT*1.5)
        NN2DExpression = MathTex(r"f(x,y) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_{n,1}^{(1)}x + w_{n,2}^{(1)}y +b_n^{(1)})").scale(1)
        NN2DExpression.set_color(text_color).move_to(DOWN*1.+LEFT*0.75)
        NN3DExpression = MathTex(r"f(x,y,z) \approx  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_{n,1}^{(1)}x + w_{n,2}^{(1)}y + w_{n,3}^{(1)}z +b_n^{(1)})").scale(1)
        NN3DExpression.set_color(text_color).move_to(DOWN*2.5)

        NNEndText = Text("and so on ...", font_size=28)
        NNEndText.set_color(text_color).move_to(DOWN*3.5)

        NNText.move_to(UP*1.5)

        self.add(NNText, NN1DExpression, NN2DExpression, NN3DExpression, NNEndText)

        # unwrite all the text and equations
        self.play(Unwrite(NNText), Unwrite(NN1DExpression),
                  Unwrite(NN2DExpression), Unwrite(NN3DExpression),
                  Unwrite(NNEndText),Unwrite(text), Unwrite(HighDimexample),
                  Unwrite(HighDimText))

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        self.play(Write(text))

        self.wait(1)

class DiagramaticRepresentation2(Scene):
    def construct(self):

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        self.add(text)

        text2D = Text("2D expression", font_size=24)
        text2D.set_color(red_color)
        text2D.move_to(UP*2.+LEFT*4.0)

        NN2DExpression = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_{n,1}^{(1)}x + w_{n,2}^{(1)}y +b_n^{(1)})").scale(1)
        NN2DExpression.set_color(text_color).move_to(UP*1.+LEFT*0.75)

        self.play(Write(text2D),Write(NN2DExpression))

        self.wait(1)


class DiagramaticRepresentation3(Scene):
    def construct(self):

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        text2D = Text("2D expression", font_size=24)
        text2D.set_color(red_color)
        text2D.move_to(UP*2.+LEFT*4.0)

        NN2DExpression = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  \sum_{n=1}^{N} w_n^{(2)} \sigma(w_{n,1}^{(1)}x + w_{n,2}^{(1)}y +b_n^{(1)})").scale(1)
        NN2DExpression.set_color(text_color).move_to(UP*1.+LEFT*0.75)

        self.add(text,text2D,NN2DExpression)

        text2Da = Text("Taking N = 3", font_size=24)
        text2Da.set_color(red_color).move_to(UP*2.+LEFT*4.0)

        NN2DExpressionN3_1 = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  w_1^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)

        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_2^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.75)

        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_3^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*3.25)

        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)

        self.play(Transform(text2D,text2Da))
        self.wait(2)
        self.play(Transform(NN2DExpression,NN2DExpressionN3))



        self.wait(1)

class DiagramaticRepresentation4(Scene):
    def construct(self):

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        self.add(text)

        text2Da = Text("Taking N = 3", font_size=24)
        text2Da.set_color(red_color).move_to(UP*2.+LEFT*4.0)

        NN2DExpressionN3_1 = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  w_1^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)

        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_2^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.75)

        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_3^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*3.25)

        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)

        self.add(text2Da, NN2DExpressionN3)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        self.play(Unwrite(text2Da))
        self.play(NN2DExpressionN3.animate.move_to(UP*1.5))

        self.play(Write(inpGroup))

        self.wait(1)

class DiagramaticRepresentation5(Scene):
    def construct(self):

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        NN2DExpressionN3_1 = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  w_1^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)

        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_2^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.75)

        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_3^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*3.25)

        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(UP*1.5)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        self.add(text,NN2DExpressionN3,inpGroup)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underline = Underline(NN2DExpressionN3_1, color=blue_color)
        underline.stretch_to_fit_width(NN2DExpressionN3_1.get_width()*0.5)
        underline.shift(RIGHT*1.9)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # draw arrows from input to the first layer of the NN2DExpressionN3
        arrow1_1 = Arrow(start=xInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_2 = Arrow(start=yInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_3 = Arrow(start=cInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1Group = VGroup(arrow1_1, arrow1_2, arrow1_3)

        # adding weights on top of the arrows
        weight1_1 = MathTex(r"w_{1,1}^{(1)}").scale(0.5).move_to(arrow1_1.get_center()+UP*0.3)
        weight1_1.set_color(text_color)
        weight1_2 = MathTex(r"w_{1,2}^{(1)}").scale(0.5).move_to(arrow1_2.get_center()+UP*0.3)
        weight1_2.set_color(text_color)
        weight1_3 = MathTex(r"b_1^{(1)}").scale(0.5).move_to(arrow1_3.get_center()+UP*0.3)
        weight1_3.set_color(text_color)
        weight1Group = VGroup(weight1_1, weight1_2, weight1_3)

        self.play(Create(underline))
        self.play(Create(neuron1Circle))
        self.wait(1)
        self.play(Create(arrow1Group))
        self.play(Write(weight1Group))

        self.wait(1)


class DiagramaticRepresentation6(Scene):
    def construct(self):

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        NN2DExpressionN3_1 = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  w_1^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)

        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_2^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.75)

        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_3^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*3.25)

        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(UP*1.5)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underline = Underline(NN2DExpressionN3_1, color=blue_color)
        underline.stretch_to_fit_width(NN2DExpressionN3_1.get_width()*0.5)
        underline.shift(RIGHT*1.9)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # draw arrows from input to the first layer of the NN2DExpressionN3
        arrow1_1 = Arrow(start=xInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_2 = Arrow(start=yInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_3 = Arrow(start=cInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1Group = VGroup(arrow1_1, arrow1_2, arrow1_3)

        # adding weights on top of the arrows
        weight1_1 = MathTex(r"w_{1,1}^{(1)}").scale(0.5).move_to(arrow1_1.get_center()+UP*0.3)
        weight1_1.set_color(text_color)
        weight1_2 = MathTex(r"w_{1,2}^{(1)}").scale(0.5).move_to(arrow1_2.get_center()+UP*0.3)
        weight1_2.set_color(text_color)
        weight1_3 = MathTex(r"b_1^{(1)}").scale(0.5).move_to(arrow1_3.get_center()+UP*0.3)
        weight1_3.set_color(text_color)
        weight1Group = VGroup(weight1_1, weight1_2, weight1_3)

        self.add(text,NN2DExpressionN3,inpGroup, underline,
                 neuron1Circle, arrow1Group, weight1Group)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underlineNew = Underline(NN2DExpressionN3_2, color=blue_color)
        underlineNew.stretch_to_fit_width(NN2DExpressionN3_2.get_width()*0.7)
        underlineNew.shift(RIGHT*0.5)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # draw arrows from input to the second layer of the NN2DExpressionN3
        arrow2_1 = Arrow(start=xInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_2 = Arrow(start=yInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_3 = Arrow(start=cInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2Group = VGroup(arrow2_1, arrow2_2, arrow2_3)

        # adding weights on top of the arrows
        weight2_1 = MathTex(r"w_{2,1}^{(1)}").scale(0.5).move_to(arrow2_1.get_center()+UP*0.3)
        weight2_1.set_color(text_color)
        weight2_2 = MathTex(r"w_{2,2}^{(1)}").scale(0.5).move_to(arrow2_2.get_center()+UP*0.3)
        weight2_2.set_color(text_color)
        weight2_3 = MathTex(r"b_2^{(1)}").scale(0.5).move_to(arrow2_3.get_center()+UP*0.3)
        weight2_3.set_color(text_color)
        weight2Group = VGroup(weight2_1, weight2_2, weight2_3)

        self.play(Uncreate(underline))
        self.play(Create(underlineNew))
        self.play(Create(neuron2Circle))
        # reducing opacity of arrow1Group and weight1Group to show that they are not active
        self.play(arrow1Group.animate.set_opacity(0.2), weight1Group.animate.set_opacity(0.2))
        self.wait(1)
        self.play(Create(arrow2Group))
        self.play(Write(weight2Group))

        self.wait(1)

class DiagramaticRepresentation7(Scene):
    def construct(self):

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        NN2DExpressionN3_1 = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  w_1^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)

        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_2^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.75)

        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_3^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*3.25)

        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(UP*1.5)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underline = Underline(NN2DExpressionN3_2, color=blue_color)
        underline.stretch_to_fit_width(NN2DExpressionN3_2.get_width()*0.7)
        underline.shift(RIGHT*0.5)

        # draw arrows from input to the first layer of the NN2DExpressionN3
        arrow1_1 = Arrow(start=xInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_2 = Arrow(start=yInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_3 = Arrow(start=cInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1Group = VGroup(arrow1_1, arrow1_2, arrow1_3)

        # adding weights on top of the arrows
        weight1_1 = MathTex(r"w_{1,1}^{(1)}").scale(0.5).move_to(arrow1_1.get_center()+UP*0.3)
        weight1_1.set_color(text_color)
        weight1_2 = MathTex(r"w_{1,2}^{(1)}").scale(0.5).move_to(arrow1_2.get_center()+UP*0.3)
        weight1_2.set_color(text_color)
        weight1_3 = MathTex(r"b_1^{(1)}").scale(0.5).move_to(arrow1_3.get_center()+UP*0.3)
        weight1_3.set_color(text_color)
        weight1Group = VGroup(weight1_1, weight1_2, weight1_3)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # draw arrows from input to the second layer of the NN2DExpressionN3
        arrow2_1 = Arrow(start=xInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_2 = Arrow(start=yInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_3 = Arrow(start=cInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2Group = VGroup(arrow2_1, arrow2_2, arrow2_3)

        # adding weights on top of the arrows
        weight2_1 = MathTex(r"w_{2,1}^{(1)}").scale(0.5).move_to(arrow2_1.get_center()+UP*0.3)
        weight2_1.set_color(text_color)
        weight2_2 = MathTex(r"w_{2,2}^{(1)}").scale(0.5).move_to(arrow2_2.get_center()+UP*0.3)
        weight2_2.set_color(text_color)
        weight2_3 = MathTex(r"b_2^{(1)}").scale(0.5).move_to(arrow2_3.get_center()+UP*0.3)
        weight2_3.set_color(text_color)
        weight2Group = VGroup(weight2_1, weight2_2, weight2_3)

        arrow1Group.set_opacity(0.2)
        weight1Group.set_opacity(0.2)

        self.add(text,NN2DExpressionN3,inpGroup, underline,
                 neuron1Circle, arrow1Group, weight1Group,
                 arrow2Group,weight2Group,neuron2Circle)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underlineNew = Underline(NN2DExpressionN3_3, color=blue_color)
        underlineNew.stretch_to_fit_width(NN2DExpressionN3_3.get_width()*0.7)
        underlineNew.shift(RIGHT*0.5)

        # creating third neuron circle for the third layer of the NN2DExpressionN3
        neuron3Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron3Circle.move_to(inpGroup.get_right()+RIGHT*2.5+DOWN*1.5)

        # creating arrows from input to the third layer of the NN2DExpressionN3
        arrow3_1 = Arrow(start=xInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_2 = Arrow(start=yInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_3 = Arrow(start=cInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3Group = VGroup(arrow3_1, arrow3_2, arrow3_3)

        # creating weights on top of the arrows
        weight3_1 = MathTex(r"w_{3,1}^{(1)}").scale(0.5).move_to(arrow3_1.get_center()+UP*0.3)
        weight3_1.set_color(text_color)
        weight3_2 = MathTex(r"w_{3,2}^{(1)}").scale(0.5).move_to(arrow3_2.get_center()+UP*0.3)
        weight3_2.set_color(text_color)
        weight3_3 = MathTex(r"b_3^{(1)}").scale(0.5).move_to(arrow3_3.get_center()+UP*0.3)
        weight3_3.set_color(text_color)
        weight3Group = VGroup(weight3_1, weight3_2, weight3_3)

        self.play(Uncreate(underline))
        self.play(Create(underlineNew))
        self.play(Create(neuron3Circle))
        # reducing opacity of arrow1Group and weight1Group to show that they are not active
        self.play(arrow2Group.animate.set_opacity(0.2), weight2Group.animate.set_opacity(0.2))
        self.wait(1)
        self.play(Create(arrow3Group))
        self.play(Write(weight3Group))

        self.wait(1)

class DiagramaticRepresentation8(Scene):
    def construct(self):

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        NN2DExpressionN3_1 = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  w_1^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)

        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_2^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.75)

        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_3^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*3.25)

        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(UP*1.5)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underline = Underline(NN2DExpressionN3_3, color=blue_color)
        underline.stretch_to_fit_width(NN2DExpressionN3_3.get_width()*0.7)
        underline.shift(RIGHT*0.5)


        # draw arrows from input to the first layer of the NN2DExpressionN3
        arrow1_1 = Arrow(start=xInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_2 = Arrow(start=yInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_3 = Arrow(start=cInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1Group = VGroup(arrow1_1, arrow1_2, arrow1_3)

        # adding weights on top of the arrows
        weight1_1 = MathTex(r"w_{1,1}^{(1)}").scale(0.5).move_to(arrow1_1.get_center()+UP*0.3)
        weight1_1.set_color(text_color)
        weight1_2 = MathTex(r"w_{1,2}^{(1)}").scale(0.5).move_to(arrow1_2.get_center()+UP*0.3)
        weight1_2.set_color(text_color)
        weight1_3 = MathTex(r"b_1^{(1)}").scale(0.5).move_to(arrow1_3.get_center()+UP*0.3)
        weight1_3.set_color(text_color)
        weight1Group = VGroup(weight1_1, weight1_2, weight1_3)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # draw arrows from input to the second layer of the NN2DExpressionN3
        arrow2_1 = Arrow(start=xInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_2 = Arrow(start=yInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_3 = Arrow(start=cInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2Group = VGroup(arrow2_1, arrow2_2, arrow2_3)

        # adding weights on top of the arrows
        weight2_1 = MathTex(r"w_{2,1}^{(1)}").scale(0.5).move_to(arrow2_1.get_center()+UP*0.3)
        weight2_1.set_color(text_color)
        weight2_2 = MathTex(r"w_{2,2}^{(1)}").scale(0.5).move_to(arrow2_2.get_center()+UP*0.3)
        weight2_2.set_color(text_color)
        weight2_3 = MathTex(r"b_2^{(1)}").scale(0.5).move_to(arrow2_3.get_center()+UP*0.3)
        weight2_3.set_color(text_color)
        weight2Group = VGroup(weight2_1, weight2_2, weight2_3)

        arrow1Group.set_opacity(0.2)
        weight1Group.set_opacity(0.2)

        # creating third neuron circle for the third layer of the NN2DExpressionN3
        neuron3Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron3Circle.move_to(inpGroup.get_right()+RIGHT*2.5+DOWN*1.5)

        # creating arrows from input to the third layer of the NN2DExpressionN3
        arrow3_1 = Arrow(start=xInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_2 = Arrow(start=yInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_3 = Arrow(start=cInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3Group = VGroup(arrow3_1, arrow3_2, arrow3_3)

        # creating weights on top of the arrows
        weight3_1 = MathTex(r"w_{3,1}^{(1)}").scale(0.5).move_to(arrow3_1.get_center()+UP*0.3)
        weight3_1.set_color(text_color)
        weight3_2 = MathTex(r"w_{3,2}^{(1)}").scale(0.5).move_to(arrow3_2.get_center()+UP*0.3)
        weight3_2.set_color(text_color)
        weight3_3 = MathTex(r"b_3^{(1)}").scale(0.5).move_to(arrow3_3.get_center()+UP*0.3)
        weight3_3.set_color(text_color)
        weight3Group = VGroup(weight3_1, weight3_2, weight3_3)

        arrow2Group.set_opacity(0.2)
        weight2Group.set_opacity(0.2)

        self.add(text,NN2DExpressionN3,inpGroup, underline,
                 neuron1Circle, arrow1Group, weight1Group,
                 arrow2Group,weight2Group,neuron2Circle,
                 arrow3Group,weight3Group,neuron3Circle)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underline1 = Underline(NN2DExpressionN3_1, color=blue_color)
        underline1.stretch_to_fit_width(NN2DExpressionN3_1.get_width()*0.1)
        underline1.shift(LEFT*0.4)
        underline2 = Underline(NN2DExpressionN3_2, color=blue_color)
        underline2.stretch_to_fit_width(NN2DExpressionN3_2.get_width()*0.1)
        underline2.shift(LEFT*1.7)
        underline3 = Underline(NN2DExpressionN3_3, color=blue_color)
        underline3.stretch_to_fit_width(NN2DExpressionN3_3.get_width()*0.1)
        underline3.shift(LEFT*1.7)

        # creating a circle representing neuron of the output layer of the NN2DExpressionN3
        neuron4Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron4Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5)

        # drawing arrows from the first layer neurons to the output layer neuron
        arrow4_1 = Arrow(start=neuron1Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4_2 = Arrow(start=neuron2Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4_3 = Arrow(start=neuron3Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4Group = VGroup(arrow4_1, arrow4_2, arrow4_3)

        # adding weights on top of the arrows
        weight4_1 = MathTex(r"w_{1}^{(2)}").scale(0.5).move_to(arrow4_1.get_center()+UP*0.3)
        weight4_1.set_color(text_color)
        weight4_2 = MathTex(r"w_{2}^{(2)}").scale(0.5).move_to(arrow4_2.get_center()+UP*0.3)
        weight4_2.set_color(text_color)
        weight4_3 = MathTex(r"w_{3}^{(2)}").scale(0.5).move_to(arrow4_3.get_center()+UP*0.3)
        weight4_3.set_color(text_color)
        weight4Group = VGroup(weight4_1, weight4_2, weight4_3)

        # drawing output variable
        outputVar = MathTex(r"\hat{f}(x,y)").scale(1).move_to(neuron4Circle.get_right()+RIGHT*1.5)
        outputVar.set_color(text_color)

        # drawing arrow to output variable
        arrow5 = Arrow(start=neuron4Circle.get_right(), end=outputVar.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        self.play(Uncreate(underline))
        self.play(Create(underline1), Create(underline2), Create(underline3))
        self.play(Create(neuron4Circle))
        # reducing opacity of arrow1Group and weight1Group to show that they are not active
        self.play(arrow3Group.animate.set_opacity(0.2), weight3Group.animate.set_opacity(0.2))
        self.wait(1)
        self.play(Create(arrow4Group))
        self.play(Write(weight4Group))
        self.wait(1)
        self.play(Create(arrow5))
        self.play(Write(outputVar))

        self.wait(1)

class DiagramaticRepresentation9(Scene):
    def construct(self):

        text = Text("Diagramatic representation", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        NN2DExpressionN3_1 = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  w_1^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)

        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_2^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.75)

        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_3^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*3.25)

        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(UP*1.5)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underline = Underline(NN2DExpressionN3_3, color=blue_color)
        underline.stretch_to_fit_width(NN2DExpressionN3_3.get_width()*0.7)
        underline.shift(RIGHT*0.5)


        # draw arrows from input to the first layer of the NN2DExpressionN3
        arrow1_1 = Arrow(start=xInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_2 = Arrow(start=yInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_3 = Arrow(start=cInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1Group = VGroup(arrow1_1, arrow1_2, arrow1_3)

        # adding weights on top of the arrows
        weight1_1 = MathTex(r"w_{1,1}^{(1)}").scale(0.5).move_to(arrow1_1.get_center()+UP*0.3)
        weight1_1.set_color(text_color)
        weight1_2 = MathTex(r"w_{1,2}^{(1)}").scale(0.5).move_to(arrow1_2.get_center()+UP*0.3)
        weight1_2.set_color(text_color)
        weight1_3 = MathTex(r"b_1^{(1)}").scale(0.5).move_to(arrow1_3.get_center()+UP*0.3)
        weight1_3.set_color(text_color)
        weight1Group = VGroup(weight1_1, weight1_2, weight1_3)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # draw arrows from input to the second layer of the NN2DExpressionN3
        arrow2_1 = Arrow(start=xInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_2 = Arrow(start=yInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_3 = Arrow(start=cInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2Group = VGroup(arrow2_1, arrow2_2, arrow2_3)

        # adding weights on top of the arrows
        weight2_1 = MathTex(r"w_{2,1}^{(1)}").scale(0.5).move_to(arrow2_1.get_center()+UP*0.3)
        weight2_1.set_color(text_color)
        weight2_2 = MathTex(r"w_{2,2}^{(1)}").scale(0.5).move_to(arrow2_2.get_center()+UP*0.3)
        weight2_2.set_color(text_color)
        weight2_3 = MathTex(r"b_2^{(1)}").scale(0.5).move_to(arrow2_3.get_center()+UP*0.3)
        weight2_3.set_color(text_color)
        weight2Group = VGroup(weight2_1, weight2_2, weight2_3)

        arrow1Group.set_opacity(0.2)
        weight1Group.set_opacity(0.2)

        # creating third neuron circle for the third layer of the NN2DExpressionN3
        neuron3Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron3Circle.move_to(inpGroup.get_right()+RIGHT*2.5+DOWN*1.5)

        # creating arrows from input to the third layer of the NN2DExpressionN3
        arrow3_1 = Arrow(start=xInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_2 = Arrow(start=yInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_3 = Arrow(start=cInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3Group = VGroup(arrow3_1, arrow3_2, arrow3_3)

        # creating weights on top of the arrows
        weight3_1 = MathTex(r"w_{3,1}^{(1)}").scale(0.5).move_to(arrow3_1.get_center()+UP*0.3)
        weight3_1.set_color(text_color)
        weight3_2 = MathTex(r"w_{3,2}^{(1)}").scale(0.5).move_to(arrow3_2.get_center()+UP*0.3)
        weight3_2.set_color(text_color)
        weight3_3 = MathTex(r"b_3^{(1)}").scale(0.5).move_to(arrow3_3.get_center()+UP*0.3)
        weight3_3.set_color(text_color)
        weight3Group = VGroup(weight3_1, weight3_2, weight3_3)

        arrow2Group.set_opacity(0.2)
        weight2Group.set_opacity(0.2)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underline1 = Underline(NN2DExpressionN3_1, color=blue_color)
        underline1.stretch_to_fit_width(NN2DExpressionN3_1.get_width()*0.1)
        underline1.shift(LEFT*0.4)
        underline2 = Underline(NN2DExpressionN3_2, color=blue_color)
        underline2.stretch_to_fit_width(NN2DExpressionN3_2.get_width()*0.1)
        underline2.shift(LEFT*1.7)
        underline3 = Underline(NN2DExpressionN3_3, color=blue_color)
        underline3.stretch_to_fit_width(NN2DExpressionN3_3.get_width()*0.1)
        underline3.shift(LEFT*1.7)

        # creating a circle representing neuron of the output layer of the NN2DExpressionN3
        neuron4Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron4Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5)

        # drawing arrows from the first layer neurons to the output layer neuron
        arrow4_1 = Arrow(start=neuron1Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4_2 = Arrow(start=neuron2Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4_3 = Arrow(start=neuron3Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4Group = VGroup(arrow4_1, arrow4_2, arrow4_3)

        # adding weights on top of the arrows
        weight4_1 = MathTex(r"w_{1}^{(2)}").scale(0.5).move_to(arrow4_1.get_center()+UP*0.3)
        weight4_1.set_color(text_color)
        weight4_2 = MathTex(r"w_{2}^{(2)}").scale(0.5).move_to(arrow4_2.get_center()+UP*0.3)
        weight4_2.set_color(text_color)
        weight4_3 = MathTex(r"w_{3}^{(2)}").scale(0.5).move_to(arrow4_3.get_center()+UP*0.3)
        weight4_3.set_color(text_color)
        weight4Group = VGroup(weight4_1, weight4_2, weight4_3)

        # drawing output variable
        outputVar = MathTex(r"\hat{f}(x,y)").scale(1).move_to(neuron4Circle.get_right()+RIGHT*1.5)
        outputVar.set_color(text_color)

        # drawing arrow to output variable
        arrow5 = Arrow(start=neuron4Circle.get_right(), end=outputVar.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        arrow3Group.set_opacity(0.2)
        weight3Group.set_opacity(0.2)

        self.add(text,NN2DExpressionN3,inpGroup,
                 neuron1Circle, arrow1Group, weight1Group,
                 arrow2Group,weight2Group,neuron2Circle,
                 arrow3Group,weight3Group,neuron3Circle,
                 arrow4Group,weight4Group,neuron4Circle,
                 arrow5,outputVar, underline1, underline2, underline3)

        textNew = Text("Neural Network", font_size=34)
        textNew.set_color(blue_color)
        textNew.move_to(UP*3.0)

        self.play(Uncreate(underline1), Uncreate(underline2), Uncreate(underline3),
                  Unwrite(NN2DExpressionN3_1), Unwrite(NN2DExpressionN3_2), Unwrite(NN2DExpressionN3_3))

        # shifting to the center all the arrows weights and neurons
        self.play(inpGroup.animate.shift(UP+RIGHT*1.5),
                  neuron1Circle.animate.shift(UP+RIGHT*1.5),
                  neuron2Circle.animate.shift(UP+RIGHT*1.5),
                  neuron3Circle.animate.shift(UP+RIGHT*1.5),
                  neuron4Circle.animate.shift(UP+RIGHT*1.5),
                  arrow1Group.animate.shift(UP+RIGHT*1.5).set_opacity(1),
                  arrow2Group.animate.shift(UP+RIGHT*1.5).set_opacity(1),
                  arrow3Group.animate.shift(UP+RIGHT*1.5).set_opacity(1),
                  arrow4Group.animate.shift(UP+RIGHT*1.5),
                  arrow5.animate.shift(UP+RIGHT*1.5),
                  weight1Group.animate.shift(UP+RIGHT*1.5),
                  weight2Group.animate.shift(UP+RIGHT*1.5),
                  weight3Group.animate.shift(UP+RIGHT*1.5),
                  weight4Group.animate.shift(UP+RIGHT*1.5).set_opacity(0.2),
                  outputVar.animate.shift(UP+RIGHT*1.5))

        self.play(Unwrite(text))
        self.play(Write(textNew))

        self.wait(1)

class DiagramaticRepresentation10(Scene):
    def construct(self):

        text = Text("Neural Network", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # draw arrows from input to the first layer of the NN2DExpressionN3
        arrow1_1 = Arrow(start=xInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_2 = Arrow(start=yInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_3 = Arrow(start=cInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1Group = VGroup(arrow1_1, arrow1_2, arrow1_3)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # draw arrows from input to the second layer of the NN2DExpressionN3
        arrow2_1 = Arrow(start=xInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_2 = Arrow(start=yInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_3 = Arrow(start=cInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2Group = VGroup(arrow2_1, arrow2_2, arrow2_3)

        arrow1Group.set_opacity(1)

        # creating third neuron circle for the third layer of the NN2DExpressionN3
        neuron3Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron3Circle.move_to(inpGroup.get_right()+RIGHT*2.5+DOWN*1.5)

        # creating arrows from input to the third layer of the NN2DExpressionN3
        arrow3_1 = Arrow(start=xInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_2 = Arrow(start=yInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_3 = Arrow(start=cInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3Group = VGroup(arrow3_1, arrow3_2, arrow3_3)

        arrow2Group.set_opacity(1)

        # creating a circle representing neuron of the output layer of the NN2DExpressionN3
        neuron4Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron4Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5)

        # drawing arrows from the first layer neurons to the output layer neuron
        arrow4_1 = Arrow(start=neuron1Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4_2 = Arrow(start=neuron2Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4_3 = Arrow(start=neuron3Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4Group = VGroup(arrow4_1, arrow4_2, arrow4_3)

        # drawing output variable
        outputVar = MathTex(r"\hat{f}(x,y)").scale(1).move_to(neuron4Circle.get_right()+RIGHT*1.5)
        outputVar.set_color(text_color)

        # drawing arrow to output variable
        arrow5 = Arrow(start=neuron4Circle.get_right(), end=outputVar.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        arrow3Group.set_opacity(1)

        inpGroup.shift(UP+RIGHT*1.5)
        neuron1Circle.shift(UP+RIGHT*1.5)
        neuron2Circle.shift(UP+RIGHT*1.5)
        neuron3Circle.shift(UP+RIGHT*1.5)
        neuron4Circle.shift(UP+RIGHT*1.5)
        arrow1Group.shift(UP+RIGHT*1.5)
        arrow2Group.shift(UP+RIGHT*1.5)
        arrow3Group.shift(UP+RIGHT*1.5)
        arrow4Group.shift(UP+RIGHT*1.5)
        arrow5.shift(UP+RIGHT*1.5)
        outputVar.shift(UP+RIGHT*1.5)

        self.add(text,inpGroup,
                 neuron1Circle, arrow1Group,
                 arrow2Group,neuron2Circle,
                 arrow3Group,neuron3Circle,
                 arrow4Group,neuron4Circle,
                 arrow5,outputVar)

        neuronsText = Text("Neurons", font_size=24)
        neuronsText.set_color(text_color)
        neuronsText.move_to(UP*2.0+RIGHT*2.5)

        # arrow from neuronsText to the first layer of the NN2DExpressionN3
        arrowNeurons = Arrow(start=neuronsText.get_left(), end=neuron1Circle.get_top(),
                       buff=0.1, color=blue_color, stroke_width=1, tip_length=0.2)

        # layers labels
        inputLayerText = Text("Input layer", font_size=24)
        inputLayerText.set_color(text_color)
        inputLayerText.move_to(inpGroup.get_bottom()+DOWN*0.5+LEFT)
        hiddenLayerText = Text("Hidden layer", font_size=24)
        hiddenLayerText.set_color(text_color)
        hiddenLayerText.move_to(neuron3Circle.get_bottom()+DOWN*0.5)
        outputLayerText = Text("Output layer", font_size=24)
        outputLayerText.set_color(text_color)
        outputLayerText.move_to(neuron4Circle.get_bottom()+DOWN*0.5+RIGHT)

        self.play(Write(neuronsText),Create(arrowNeurons))
        self.wait(4)
        self.play(Write(inputLayerText))
        self.play(Write(hiddenLayerText))
        self.play(Write(outputLayerText))

        self.wait(1)

class VectorFunctions1(Scene):
    def construct(self):

        text = Text("Neural Network", font_size=34)
        text.set_color(blue_color)
        text.move_to(UP*3.0)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # draw arrows from input to the first layer of the NN2DExpressionN3
        arrow1_1 = Arrow(start=xInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_2 = Arrow(start=yInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1_3 = Arrow(start=cInp.get_right(), end=neuron1Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow1Group = VGroup(arrow1_1, arrow1_2, arrow1_3)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # draw arrows from input to the second layer of the NN2DExpressionN3
        arrow2_1 = Arrow(start=xInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_2 = Arrow(start=yInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2_3 = Arrow(start=cInp.get_right(), end=neuron2Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow2Group = VGroup(arrow2_1, arrow2_2, arrow2_3)

        arrow1Group.set_opacity(1)

        # creating third neuron circle for the third layer of the NN2DExpressionN3
        neuron3Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron3Circle.move_to(inpGroup.get_right()+RIGHT*2.5+DOWN*1.5)

        # creating arrows from input to the third layer of the NN2DExpressionN3
        arrow3_1 = Arrow(start=xInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_2 = Arrow(start=yInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3_3 = Arrow(start=cInp.get_right(), end=neuron3Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow3Group = VGroup(arrow3_1, arrow3_2, arrow3_3)

        arrow2Group.set_opacity(1)

        # creating a circle representing neuron of the output layer of the NN2DExpressionN3
        neuron4Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron4Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5)

        # drawing arrows from the first layer neurons to the output layer neuron
        arrow4_1 = Arrow(start=neuron1Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4_2 = Arrow(start=neuron2Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4_3 = Arrow(start=neuron3Circle.get_right(), end=neuron4Circle.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)
        arrow4Group = VGroup(arrow4_1, arrow4_2, arrow4_3)

        # drawing output variable
        outputVar = MathTex(r"\hat{f}(x,y)").scale(1).move_to(neuron4Circle.get_right()+RIGHT*1.5)
        outputVar.set_color(text_color)

        # drawing arrow to output variable
        arrow5 = Arrow(start=neuron4Circle.get_right(), end=outputVar.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        arrow3Group.set_opacity(1)

        inpGroup.shift(UP+RIGHT*1.5)
        neuron1Circle.shift(UP+RIGHT*1.5)
        neuron2Circle.shift(UP+RIGHT*1.5)
        neuron3Circle.shift(UP+RIGHT*1.5)
        neuron4Circle.shift(UP+RIGHT*1.5)
        arrow1Group.shift(UP+RIGHT*1.5)
        arrow2Group.shift(UP+RIGHT*1.5)
        arrow3Group.shift(UP+RIGHT*1.5)
        arrow4Group.shift(UP+RIGHT*1.5)
        arrow5.shift(UP+RIGHT*1.5)
        outputVar.shift(UP+RIGHT*1.5)

        neuronsText = Text("Neurons", font_size=24)
        neuronsText.set_color(text_color)
        neuronsText.move_to(UP*2.0+RIGHT*2.5)
        # arrow from neuronsText to the first layer of the NN2DExpressionN3
        arrowNeurons = Arrow(start=neuronsText.get_left(), end=neuron1Circle.get_top(),
                       buff=0.1, color=blue_color, stroke_width=1, tip_length=0.2)

        # layers labels
        inputLayerText = Text("Input layer", font_size=24)
        inputLayerText.set_color(text_color)
        inputLayerText.move_to(inpGroup.get_bottom()+DOWN*0.5+LEFT)
        hiddenLayerText = Text("Hidden layer", font_size=24)
        hiddenLayerText.set_color(text_color)
        hiddenLayerText.move_to(neuron3Circle.get_bottom()+DOWN*0.5)
        outputLayerText = Text("Output layer", font_size=24)
        outputLayerText.set_color(text_color)
        outputLayerText.move_to(neuron4Circle.get_bottom()+DOWN*0.5+RIGHT)


        self.add(text,inpGroup,
                 neuron1Circle, arrow1Group,
                 arrow2Group,neuron2Circle,
                 arrow3Group,neuron3Circle,
                 arrow4Group,neuron4Circle,
                 arrow5,outputVar,
                 neuronsText, arrowNeurons,
                 inputLayerText, hiddenLayerText, outputLayerText)

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.play(Unwrite(text),Uncreate(arrowNeurons), Unwrite(neuronsText),
                  Unwrite(inputLayerText), Unwrite(hiddenLayerText),
                  Unwrite(outputLayerText), Uncreate(arrow1Group), Uncreate(arrow2Group), Uncreate(arrow3Group),
                  Uncreate(arrow4Group), Uncreate(arrow5), Unwrite(outputVar),
                  Uncreate(neuron1Circle), Uncreate(neuron2Circle), Uncreate(neuron3Circle), Uncreate(neuron4Circle), Uncreate(inpGroup))
        self.play(Write(titleText))


        self.wait(1)

class VectorFunctions2(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        definitionMath = MathTex(r"\mathbf{f}(x,y)").scale(1)
        definitionMath.set_color(text_color)
        definitionMath.move_to(UP*2.0)

        definitionText = Text("A function that takes a vector as input and produces a vector as output.", font_size=24)
        definitionText.set_color(text_color)
        definitionText.move_to(UP*1.0)

        exampleMath = MathTex(r"\mathbf{u}(x,y,z) = \begin{bmatrix} u(x,y,z) \\ v(x,y,z) \\ w(x,y,z) \end{bmatrix}").scale(1)
        exampleMath.set_color(text_color)
        exampleMath.move_to(DOWN*0.5+RIGHT*3.0)

        exampleText = Text("Example: ", font_size=24)
        exampleText.set_color(red_color)
        exampleText.move_to(DOWN*0.5+LEFT*5.0)
        exampleMathText = Text("3D Velocity vector field", font_size=24)
        exampleMathText.set_color(text_color)
        exampleMathText.move_to(DOWN*0.5+LEFT*2.0)

        self.play(Write(definitionMath))
        self.play(Write(definitionText))
        self.play(Write(exampleText),Write(exampleMathText),Write(exampleMath))

        self.wait(1)

class VectorFunctions3(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        definitionMath = MathTex(r"\mathbf{f}(x,y)").scale(1)
        definitionMath.set_color(text_color)
        definitionMath.move_to(UP*2.0)

        definitionText = Text("A function that takes a vector as input and produces a vector as output.", font_size=24)
        definitionText.set_color(text_color)
        definitionText.move_to(UP*1.0)

        exampleMath = MathTex(r"\mathbf{u}(x,y,z) = \begin{bmatrix} u(x,y,z) \\ v(x,y,z) \\ w(x,y,z) \end{bmatrix}").scale(1)
        exampleMath.set_color(text_color)
        exampleMath.move_to(DOWN*0.5+RIGHT*3.0)

        exampleText = Text("Example: ", font_size=24)
        exampleText.set_color(red_color)
        exampleText.move_to(DOWN*0.5+LEFT*5.0)
        exampleMathText = Text("3D Velocity vector field", font_size=24)
        exampleMathText.set_color(text_color)
        exampleMathText.move_to(DOWN*0.5+LEFT*2.0)

        self.add(definitionMath, definitionText, exampleText, exampleMathText,
                 exampleMath)
        self.play(Unwrite(definitionText), Unwrite(exampleText),
                  Unwrite(exampleMathText), Unwrite(exampleMath))

        scalarFunctionText = Text("For a scalar function: ", font_size=24)
        scalarFunctionText.set_color(red_color)
        scalarFunctionText.move_to(UP*1.0+LEFT*4.0)

        NN2DExpressionN3_1 = MathTex(r"f(x,y) \approx \hat{f}(x,y) =  w_{1,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)
        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_{1,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.75)
        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_{1,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*3.25)
        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(DOWN)

        self.play(Write(scalarFunctionText))
        self.play(Write(NN2DExpressionN3))

        self.wait(1)

class VectorFunctions4(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        definitionMath = MathTex(r"\mathbf{f}(x,y)").scale(1)
        definitionMath.set_color(text_color)
        definitionMath.move_to(UP*2.0)

        scalarFunctionText = Text("For a scalar function: ", font_size=24)
        scalarFunctionText.set_color(red_color)
        scalarFunctionText.move_to(UP*1.0+LEFT*4.0)

        NN2DExpressionN3_1 = MathTex(r"\hat{f}(x,y) =  w_{1,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)
        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_{1,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.)
        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_{1,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*2.5)
        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(DOWN)

        self.add(definitionMath, scalarFunctionText, NN2DExpressionN3)

        # draw an underline higlighting the first layer of the NN2DExpressionN3
        underline1 = Underline(NN2DExpressionN3_1, color=blue_color)
        underline1.stretch_to_fit_width(NN2DExpressionN3_1.get_width()*0.12)
        underline1.shift(LEFT*1.1)
        underline2 = Underline(NN2DExpressionN3_2, color=blue_color)
        underline2.stretch_to_fit_width(NN2DExpressionN3_2.get_width()*0.15)
        underline2.shift(LEFT*1.6)
        underline3 = Underline(NN2DExpressionN3_3, color=blue_color)
        underline3.stretch_to_fit_width(NN2DExpressionN3_3.get_width()*0.15)
        underline3.shift(LEFT*1.6)

        self.play(Create(underline1), Create(underline2), Create(underline3))
        self.wait(2)
        self.play(Uncreate(underline1), Uncreate(underline2), Uncreate(underline3))
        self.wait(1)

        self.wait(1)

class VectorFunctions5(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        definitionMath = MathTex(r"\mathbf{f}(x,y)").scale(1)
        definitionMath.set_color(text_color)
        definitionMath.move_to(UP*2.0)

        scalarFunctionText = Text("For a scalar function: ", font_size=24)
        scalarFunctionText.set_color(red_color)
        scalarFunctionText.move_to(UP*1.0+LEFT*4.0)

        NN2DExpressionN3_1 = MathTex(r"\hat{f}(x,y) =  w_{1,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)
        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_{1,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.)
        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_{1,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*2.5)
        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(DOWN)

        self.add(definitionMath, scalarFunctionText, NN2DExpressionN3)

        vectorFunctionText = Text("For a vector function: ", font_size=24)
        vectorFunctionText.set_color(red_color)
        vectorFunctionText.move_to(UP*2.0+LEFT*4.0)
        vectorFunctionMath = MathTex(r" = \begin{bmatrix} f(x,y) & g(x,y) \end{bmatrix}^T").scale(0.75)
        vectorFunctionMath.set_color(text_color)
        vectorFunctionMath.move_to(UP*2.0+RIGHT*2.5)

        self.play(FadeOut(scalarFunctionText),Write(vectorFunctionText))
        self.play(Write(vectorFunctionMath))

        self.wait(1)

class VectorFunctions6(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        definitionMath = MathTex(r"\mathbf{f}(x,y)").scale(1)
        definitionMath.set_color(text_color)
        definitionMath.move_to(UP*2.0)

        NN2DExpressionN3_1 = MathTex(r"\hat{f}(x,y) =  w_{1,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)
        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_{1,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.)
        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_{1,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*2.5)
        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(DOWN)

        vectorFunctionText = Text("For a vector function: ", font_size=24)
        vectorFunctionText.set_color(red_color)
        vectorFunctionText.move_to(UP*2.0+LEFT*4.0)
        vectorFunctionMath = MathTex(r" = \begin{bmatrix} f(x,y) & g(x,y) \end{bmatrix}^T").scale(0.75)
        vectorFunctionMath.set_color(text_color)
        vectorFunctionMath.move_to(UP*2.0+RIGHT*2.5)

        self.add(definitionMath, NN2DExpressionN3,
                 vectorFunctionText, vectorFunctionMath)

        NN2DExpressionN3V2_1 = MathTex(r"\hat{g}(x,y) =  w_{2,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3V2_1.set_color(text_color).move_to(DOWN*1+LEFT*2.75)
        NN2DExpressionN3V2_2 = MathTex(r"+ \ \ w_{2,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3V2_2.set_color(text_color).move_to(DOWN*1+RIGHT*3.)
        NN2DExpressionN3V2_3 = MathTex(r"+ \ \ w_{2,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3V2_3.set_color(text_color).move_to(DOWN*2.0+RIGHT*2.5)
        NN2DExpressionN3V2 = VGroup(NN2DExpressionN3V2_1, NN2DExpressionN3V2_2, NN2DExpressionN3V2_3)
        NN2DExpressionN3V2.move_to(DOWN*2.25)

        self.play(NN2DExpressionN3.animate.shift(UP*1.25))
        self.play(Write(NN2DExpressionN3V2))

        self.wait(1)

class VectorFunctions7(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        definitionMath = MathTex(r"\mathbf{f}(x,y)").scale(1)
        definitionMath.set_color(text_color)
        definitionMath.move_to(UP*2.0)

        NN2DExpressionN3_1 = MathTex(r"\hat{f}(x,y) =  w_{1,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)
        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_{1,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.)
        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_{1,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*2.5)
        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(DOWN)
        NN2DExpressionN3.shift(UP*1.25)

        vectorFunctionText = Text("For a vector function: ", font_size=24)
        vectorFunctionText.set_color(red_color)
        vectorFunctionText.move_to(UP*2.0+LEFT*4.0)
        vectorFunctionMath = MathTex(r" = \begin{bmatrix} f(x,y) & g(x,y) \end{bmatrix}^T").scale(0.75)
        vectorFunctionMath.set_color(text_color)
        vectorFunctionMath.move_to(UP*2.0+RIGHT*2.5)

        NN2DExpressionN3V2_1 = MathTex(r"\hat{g}(x,y) =  w_{2,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3V2_1.set_color(text_color).move_to(DOWN*1+LEFT*2.75)
        NN2DExpressionN3V2_2 = MathTex(r"+ \ \ w_{2,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3V2_2.set_color(text_color).move_to(DOWN*1+RIGHT*3.)
        NN2DExpressionN3V2_3 = MathTex(r"+ \ \ w_{2,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3V2_3.set_color(text_color).move_to(DOWN*2.0+RIGHT*2.5)
        NN2DExpressionN3V2 = VGroup(NN2DExpressionN3V2_1, NN2DExpressionN3V2_2, NN2DExpressionN3V2_3)
        NN2DExpressionN3V2.move_to(DOWN*2.25)

        self.add(definitionMath, NN2DExpressionN3,
                 vectorFunctionText, vectorFunctionMath,
                 NN2DExpressionN3V2)

        rewritingText = Text("Rewriting as", font_size=24)
        rewritingText.set_color(text_color)
        rewritingText.move_to(LEFT*4+DOWN*1)

        NNVectorForm1 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \begin{bmatrix} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) \\ \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)}) \\ \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)}) \end{bmatrix}").scale(0.75)
        NNVectorForm1.set_color(text_color)
        NNVectorForm1.move_to(DOWN*2.5)

        self.play(Unwrite(vectorFunctionText), Unwrite(vectorFunctionMath),
                  Unwrite(definitionMath))
        self.play(NN2DExpressionN3.animate.shift(UP*1.25), NN2DExpressionN3V2.animate.shift(UP*1.75))
        self.play(Write(rewritingText))
        self.wait(1)
        self.play(Write(NNVectorForm1))

        self.wait(1)

class VectorFunctions8(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        definitionMath = MathTex(r"\mathbf{f}(x,y)").scale(1)
        definitionMath.set_color(text_color)
        definitionMath.move_to(UP*2.0)

        NN2DExpressionN3_1 = MathTex(r"\hat{f}(x,y) =  w_{1,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3_1.set_color(text_color).move_to(UP*1.25+LEFT*2.75)
        NN2DExpressionN3_2 = MathTex(r"+ \ \ w_{1,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3_2.set_color(text_color).move_to(UP*1.25+RIGHT*3.)
        NN2DExpressionN3_3 = MathTex(r"+ \ \ w_{1,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3_3.set_color(text_color).move_to(UP*0.25+RIGHT*2.5)
        NN2DExpressionN3 = VGroup(NN2DExpressionN3_1, NN2DExpressionN3_2, NN2DExpressionN3_3)
        NN2DExpressionN3.move_to(DOWN)
        NN2DExpressionN3.shift(UP*1.25)

        vectorFunctionText = Text("For a vector function: ", font_size=24)
        vectorFunctionText.set_color(red_color)
        vectorFunctionText.move_to(UP*2.0+LEFT*4.0)
        vectorFunctionMath = MathTex(r" = \begin{bmatrix} f(x,y) & g(x,y) \end{bmatrix}^T").scale(0.75)
        vectorFunctionMath.set_color(text_color)
        vectorFunctionMath.move_to(UP*2.0+RIGHT*2.5)

        NN2DExpressionN3V2_1 = MathTex(r"\hat{g}(x,y) =  w_{2,1}^{(2)} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) ").scale(0.75)
        NN2DExpressionN3V2_1.set_color(text_color).move_to(DOWN*1+LEFT*2.75)
        NN2DExpressionN3V2_2 = MathTex(r"+ \ \ w_{2,2}^{(2)} \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)})").scale(0.75)
        NN2DExpressionN3V2_2.set_color(text_color).move_to(DOWN*1+RIGHT*3.)
        NN2DExpressionN3V2_3 = MathTex(r"+ \ \ w_{2,3}^{(2)} \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)})").scale(0.75)
        NN2DExpressionN3V2_3.set_color(text_color).move_to(DOWN*2.0+RIGHT*2.5)
        NN2DExpressionN3V2 = VGroup(NN2DExpressionN3V2_1, NN2DExpressionN3V2_2, NN2DExpressionN3V2_3)
        NN2DExpressionN3V2.move_to(DOWN*2.25)

        NN2DExpressionN3.shift(UP*1.25)
        NN2DExpressionN3V2.shift(UP*1.75)

        rewritingText = Text("Rewriting as", font_size=24)
        rewritingText.set_color(text_color)
        rewritingText.move_to(LEFT*4+DOWN*1)

        NNVectorForm1 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \begin{bmatrix} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) \\ \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)}) \\ \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)}) \end{bmatrix}").scale(0.75)
        NNVectorForm1.set_color(text_color)
        NNVectorForm1.move_to(DOWN*2.5)

        self.add(NN2DExpressionN3,
                 NN2DExpressionN3V2, rewritingText, NNVectorForm1)

        NNVectorForm2 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \sigma\left(\begin{bmatrix} w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)} \\ w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)} \\ w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)} \end{bmatrix}\right)").scale(0.75)
        NNVectorForm2.set_color(text_color)
        NNVectorForm2.move_to(DOWN*2.5)

        self.play(FadeOut(NN2DExpressionN3), FadeOut(NN2DExpressionN3V2))
        self.play(NNVectorForm1.animate.shift(UP*2.5))
        self.play(Write(NNVectorForm2))

        self.wait(1)

class VectorFunctions9(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        rewritingText = Text("Rewriting as", font_size=24)
        rewritingText.set_color(text_color)
        rewritingText.move_to(LEFT*4+DOWN*1)

        NNVectorForm1 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \begin{bmatrix} \sigma(w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)}) \\ \sigma(w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)}) \\ \sigma(w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)}) \end{bmatrix}").scale(0.75)
        NNVectorForm1.set_color(text_color)
        NNVectorForm1.move_to(DOWN*2.5)
        NNVectorForm1.shift(UP*2.5)

        NNVectorForm2 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \sigma\left(\begin{bmatrix} w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)} \\ w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)} \\ w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)} \end{bmatrix}\right)").scale(0.75)
        NNVectorForm2.set_color(text_color)
        NNVectorForm2.move_to(DOWN*2.5)

        self.add(rewritingText, NNVectorForm1, NNVectorForm2)

        NNVectorForm3 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \sigma\left(\begin{bmatrix} w_{1,1}^{(1)} & w_{1,2}^{(1)} \\ w_{2,1}^{(1)} & w_{2,2}^{(1)} \\ w_{3,1}^{(1)} & w_{3,2}^{(1)} \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} + \begin{bmatrix} b_1^{(1)} \\ b_2^{(1)} \\ b_3^{(1)}\end{bmatrix}\right)").scale(0.75)
        NNVectorForm3.set_color(text_color)
        NNVectorForm3.move_to(DOWN*2.5)

        self.play(FadeOut(NNVectorForm1))
        self.play(NNVectorForm2.animate.shift(UP*2.5))
        self.play(Write(NNVectorForm3))

        self.wait(1)

class VectorFunctions10(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        rewritingText = Text("Rewriting as", font_size=24)
        rewritingText.set_color(text_color)
        rewritingText.move_to(LEFT*4+DOWN*1)

        NNVectorForm2 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \sigma\left(\begin{bmatrix} w_{1,1}^{(1)}x + w_{1,2}^{(1)}y +b_1^{(1)} \\ w_{2,1}^{(1)}x + w_{2,2}^{(1)}y +b_2^{(1)} \\ w_{3,1}^{(1)}x + w_{3,2}^{(1)}y +b_3^{(1)} \end{bmatrix}\right)").scale(0.75)
        NNVectorForm2.set_color(text_color)
        NNVectorForm2.move_to(DOWN*2.5)
        NNVectorForm2.shift(UP*2.5)

        NNVectorForm3 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \sigma\left(\begin{bmatrix} w_{1,1}^{(1)} & w_{1,2}^{(1)} \\ w_{2,1}^{(1)} & w_{2,2}^{(1)} \\ w_{3,1}^{(1)} & w_{3,2}^{(1)} \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} + \begin{bmatrix} b_1^{(1)} \\ b_2^{(1)} \\ b_3^{(1)}\end{bmatrix}\right)").scale(0.75)
        NNVectorForm3.set_color(text_color)
        NNVectorForm3.move_to(DOWN*2.5)

        self.add(rewritingText, NNVectorForm2, NNVectorForm3)

        NNVectorForm4 = MathTex(r"\hat{\mathbf{f}}(x,y) = W^{(2)} \sigma\left(W^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right)").scale(1)
        NNVectorForm4.set_color(text_color)
        NNVectorForm4.move_to(DOWN*2.5)

        self.play(FadeOut(NNVectorForm2))
        self.play(NNVectorForm3.animate.shift(UP*2.5))
        self.play(Write(NNVectorForm4))

        self.wait(1)

class VectorFunctions11(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        rewritingText = Text("Rewriting as", font_size=24)
        rewritingText.set_color(text_color)
        rewritingText.move_to(LEFT*4+DOWN*1)

        NNVectorForm3 = MathTex(r"\begin{bmatrix} \hat{f}(x,y) \\ \hat{g}(x,y) \end{bmatrix} = \begin{bmatrix} w_{1,1}^{(2)} & w_{1,2}^{(2)} & w_{1,3}^{(2)} \\ w_{2,1}^{(2)} & w_{2,2}^{(2)} & w_{2,3}^{(2)} \end{bmatrix} \sigma\left(\begin{bmatrix} w_{1,1}^{(1)} & w_{1,2}^{(1)} \\ w_{2,1}^{(1)} & w_{2,2}^{(1)} \\ w_{3,1}^{(1)} & w_{3,2}^{(1)} \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} + \begin{bmatrix} b_1^{(1)} \\ b_2^{(1)} \\ b_3^{(1)}\end{bmatrix}\right)").scale(0.75)
        NNVectorForm3.set_color(text_color)
        NNVectorForm3.move_to(DOWN*2.5)
        NNVectorForm3.shift(UP*2.5)

        NNVectorForm4 = MathTex(r"\hat{\mathbf{f}}(x,y) = W^{(2)} \sigma\left(W^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right)").scale(1)
        NNVectorForm4.set_color(text_color)
        NNVectorForm4.move_to(DOWN*2.5)

        self.add(rewritingText, NNVectorForm3, NNVectorForm4)

        SLFNText = Text("Generic expression of Single Layer Neural Network", font_size=24)
        SLFNText.set_color(blue_color)
        SLFNText.move_to(UP*1.0)

        self.play(FadeOut(NNVectorForm3))
        self.play(NNVectorForm4.animate.shift(UP*4.5))
        self.play(Transform(rewritingText, SLFNText))

        self.wait(1)

class VectorFunctions12(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        NNVectorForm4 = MathTex(r"\hat{\mathbf{f}}(x,y) = W^{(2)} \sigma\left(W^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right)").scale(1)
        NNVectorForm4.set_color(text_color)
        NNVectorForm4.move_to(DOWN*2.5)
        NNVectorForm4.shift(UP*4.5)

        SLFNText = Text("Generic expression of Single Layer Neural Network", font_size=24)
        SLFNText.set_color(blue_color)
        SLFNText.move_to(UP*1.0)

        self.add(SLFNText, NNVectorForm4)

        graphicalText = Text("Graphically,", font_size=24)
        graphicalText.set_color(text_color)
        graphicalText.move_to(UP*1.0+LEFT*4.0)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # creating third neuron circle for the third layer of the NN2DExpressionN3
        neuron3Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron3Circle.move_to(inpGroup.get_right()+RIGHT*2.5+DOWN*1.5)

        # creating a circle representing neuron of the output layer of the NN2DExpressionN3
        neuron4Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron4Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5)

        # drawing output variable
        outputVar = MathTex(r"\hat{f}(x,y)").scale(1).move_to(neuron4Circle.get_right()+RIGHT*1.5)
        outputVar.set_color(text_color)

        # drawing arrow to output variable
        arrow5 = Arrow(start=neuron4Circle.get_right(), end=outputVar.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        # drawing connecting lines
        line1_1 = Line(xInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1_2 = Line(yInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1_3 = Line(cInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_1 = Line(xInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_2 = Line(yInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_3 = Line(cInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_1 = Line(xInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_2 = Line(yInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_3 = Line(cInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1Group = VGroup(line1_1, line1_2, line1_3, line2_1,
                            line2_2, line2_3, line3_1, line3_2, line3_3)

        line1_o = Line(neuron1Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line2_o = Line(neuron2Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line3_o = Line(neuron3Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line2Group = VGroup(line1_o, line2_o, line3_o)

        self.play(Unwrite(SLFNText))
        self.play(Write(graphicalText))
        self.wait(1)
        # drawing the network
        self.play(Write(inpGroup))
        self.play(Create(line1Group))
        self.play(Create(neuron1Circle), Create(neuron2Circle), Create(neuron3Circle))
        self.play(Create(line2Group))
        self.play(Create(neuron4Circle))
        self.play(Create(arrow5))
        self.play(Write(outputVar))

        self.wait(1)

class VectorFunctions13(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        NNVectorForm4 = MathTex(r"\hat{\mathbf{f}}(x,y) = W^{(2)} \sigma\left(W^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right)").scale(1)
        NNVectorForm4.set_color(text_color)
        NNVectorForm4.move_to(DOWN*2.5)
        NNVectorForm4.shift(UP*4.5)

        SLFNText = Text("Generic expression of Single Layer Neural Network", font_size=24)
        SLFNText.set_color(blue_color)
        SLFNText.move_to(UP*1.0)

        graphicalText = Text("Graphically,", font_size=24)
        graphicalText.set_color(text_color)
        graphicalText.move_to(UP*1.0+LEFT*4.0)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # creating third neuron circle for the third layer of the NN2DExpressionN3
        neuron3Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron3Circle.move_to(inpGroup.get_right()+RIGHT*2.5+DOWN*1.5)

        # creating a circle representing neuron of the output layer of the NN2DExpressionN3
        neuron4Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron4Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5)

        # drawing output variable
        outputVar = MathTex(r"\hat{f}(x,y)").scale(1).move_to(neuron4Circle.get_right()+RIGHT*1.5)
        outputVar.set_color(text_color)

        # drawing arrow to output variable
        arrow5 = Arrow(start=neuron4Circle.get_right(), end=outputVar.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        # drawing connecting lines
        line1_1 = Line(xInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1_2 = Line(yInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1_3 = Line(cInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_1 = Line(xInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_2 = Line(yInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_3 = Line(cInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_1 = Line(xInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_2 = Line(yInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_3 = Line(cInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1Group = VGroup(line1_1, line1_2, line1_3, line2_1,
                            line2_2, line2_3, line3_1, line3_2, line3_3)

        line1_o = Line(neuron1Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line2_o = Line(neuron2Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line3_o = Line(neuron3Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line2Group = VGroup(line1_o, line2_o, line3_o)

        self.add(NNVectorForm4,graphicalText, inpGroup, neuron1Circle,
                 neuron2Circle, neuron3Circle, neuron4Circle, outputVar,
                 arrow5, line1Group, line2Group)
        neuron5Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron5Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5+DOWN*0.75)
        outputVar2 = MathTex(r"\hat{g}(x,y)").scale(1).move_to(neuron5Circle.get_right()+RIGHT*1.5)
        outputVar2.set_color(text_color)
        arrow6 = Arrow(start=neuron5Circle.get_right(), end=outputVar2.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        line4_o = Line(neuron1Circle.get_right(), neuron5Circle.get_left(),
                       color=text_color, stroke_width=1)
        line5_o = Line(neuron2Circle.get_right(), neuron5Circle.get_left(),
                       color=text_color, stroke_width=1)
        line6_o = Line(neuron3Circle.get_right(), neuron5Circle.get_left(),
                       color=text_color, stroke_width=1)
        line3Group = VGroup(line4_o, line5_o, line6_o)

        hiddenDot = Dot(point=neuron4Circle.get_left()+RIGHT*0.1+UP*0.75, color=blue_color)

        line7_o = Line(neuron1Circle.get_right(), hiddenDot.get_left(),
                       color=text_color, stroke_width=1)
        line8_o = Line(neuron2Circle.get_right(), hiddenDot.get_left(),
                       color=text_color, stroke_width=1)
        line9_o = Line(neuron3Circle.get_right(), hiddenDot.get_left(),
                       color=text_color, stroke_width=1)
        line4Group = VGroup(line7_o, line8_o, line9_o)

        self.play(neuron4Circle.animate.shift(UP*0.75), FadeOut(line2Group),
                  outputVar.animate.shift(UP*0.75), arrow5.animate.shift(UP*0.75))
        self.play(Create(neuron5Circle), Create(arrow6), Write(outputVar2))
        self.play(Create(line4Group),Create(line3Group))

        self.wait(1)

class DeepNetworks1(Scene):
    def construct(self):

        titleText = Text("Vector Functions", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        NNVectorForm4 = MathTex(r"\hat{\mathbf{f}}(x,y) = W^{(2)} \sigma\left(W^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right)").scale(1)
        NNVectorForm4.set_color(text_color)
        NNVectorForm4.move_to(DOWN*2.5)
        NNVectorForm4.shift(UP*4.5)

        SLFNText = Text("Generic expression of Single Layer Neural Network", font_size=24)
        SLFNText.set_color(blue_color)
        SLFNText.move_to(UP*1.0)

        graphicalText = Text("Graphically,", font_size=24)
        graphicalText.set_color(text_color)
        graphicalText.move_to(UP*1.0+LEFT*4.0)

        # input elements
        xInp = MathTex(r"x").scale(1)
        xInp.set_color(text_color).move_to(LEFT*4.5+DOWN*0.5)
        yInp = MathTex(r"y").scale(1)
        yInp.set_color(text_color).move_to(LEFT*4.5+DOWN*1.5)
        cInp = MathTex(r"1").scale(1)
        cInp.set_color(text_color).move_to(LEFT*4.5+DOWN*2.5)
        inpGroup = VGroup(xInp, yInp, cInp)

        # creating a circle representing neuron of the first layer of the NN2DExpressionN3
        neuron1Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron1Circle.move_to(inpGroup.get_right()+RIGHT*2.5+UP*1.5)

        # creating second neuron circle for the second layer of the NN2DExpressionN3
        neuron2Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron2Circle.move_to(inpGroup.get_right()+RIGHT*2.5)

        # creating third neuron circle for the third layer of the NN2DExpressionN3
        neuron3Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron3Circle.move_to(inpGroup.get_right()+RIGHT*2.5+DOWN*1.5)

        # creating a circle representing neuron of the output layer of the NN2DExpressionN3
        neuron4Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron4Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5)

        # drawing output variable
        outputVar = MathTex(r"\hat{f}(x,y)").scale(1).move_to(neuron4Circle.get_right()+RIGHT*1.5)
        outputVar.set_color(text_color)

        # drawing arrow to output variable
        arrow5 = Arrow(start=neuron4Circle.get_right(), end=outputVar.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        # drawing connecting lines
        line1_1 = Line(xInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1_2 = Line(yInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1_3 = Line(cInp.get_right(), neuron1Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_1 = Line(xInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_2 = Line(yInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line2_3 = Line(cInp.get_right(), neuron2Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_1 = Line(xInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_2 = Line(yInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line3_3 = Line(cInp.get_right(), neuron3Circle.get_left(),
                        color=text_color, stroke_width=1)
        line1Group = VGroup(line1_1, line1_2, line1_3, line2_1,
                            line2_2, line2_3, line3_1, line3_2, line3_3)

        line1_o = Line(neuron1Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line2_o = Line(neuron2Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line3_o = Line(neuron3Circle.get_right(), neuron4Circle.get_left(),
                       color=text_color, stroke_width=1)
        line2Group = VGroup(line1_o, line2_o, line3_o)

        neuron5Circle = Circle(radius=0.2, color=blue_color,
                              fill_opacity=0.5, stroke_width=2)
        neuron5Circle.move_to(neuron2Circle.get_right()+RIGHT*2.5+DOWN*0.75)
        outputVar2 = MathTex(r"\hat{g}(x,y)").scale(1).move_to(neuron5Circle.get_right()+RIGHT*1.5)
        outputVar2.set_color(text_color)
        arrow6 = Arrow(start=neuron5Circle.get_right(), end=outputVar2.get_left(),
                       buff=0.1, color=text_color, stroke_width=1, tip_length=0.2)

        line4_o = Line(neuron1Circle.get_right(), neuron5Circle.get_left(),
                       color=text_color, stroke_width=1)
        line5_o = Line(neuron2Circle.get_right(), neuron5Circle.get_left(),
                       color=text_color, stroke_width=1)
        line6_o = Line(neuron3Circle.get_right(), neuron5Circle.get_left(),
                       color=text_color, stroke_width=1)
        line3Group = VGroup(line4_o, line5_o, line6_o)

        hiddenDot = Dot(point=neuron4Circle.get_left()+RIGHT*0.1+UP*0.75, color=blue_color)

        line7_o = Line(neuron1Circle.get_right(), hiddenDot.get_left(),
                       color=text_color, stroke_width=1)
        line8_o = Line(neuron2Circle.get_right(), hiddenDot.get_left(),
                       color=text_color, stroke_width=1)
        line9_o = Line(neuron3Circle.get_right(), hiddenDot.get_left(),
                       color=text_color, stroke_width=1)
        line4Group = VGroup(line7_o, line8_o, line9_o)

        neuron4Circle.shift(UP*0.75)
        outputVar.shift(UP*0.75)
        arrow5.shift(UP*0.75)

        self.add(NNVectorForm4,graphicalText, inpGroup, neuron1Circle,
                 neuron2Circle, neuron3Circle, neuron4Circle, outputVar,
                 arrow5, line1Group, line2Group, neuron5Circle, outputVar2, arrow6, line3Group, line4Group)

        titleText2 = Text("Deep Networks", font_size=34)
        titleText2.set_color(blue_color)
        titleText2.move_to(UP*3.0)

        self.play(FadeOut(NNVectorForm4),
                  FadeOut(graphicalText), FadeOut(inpGroup),
                  FadeOut(neuron1Circle), FadeOut(neuron2Circle),
                  FadeOut(neuron3Circle), FadeOut(neuron4Circle),
                  FadeOut(outputVar), FadeOut(arrow5), FadeOut(line1Group),
                  FadeOut(line2Group), FadeOut(neuron5Circle),
                  FadeOut(outputVar2), FadeOut(arrow6), FadeOut(line3Group),
                  FadeOut(line4Group))
        self.play(Transform(titleText, titleText2))

        self.wait(1)

class DeepNetworks2(Scene):
    def construct(self):

        titleText = Text("Deep Networks", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

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

        sineCurveGroup = VGroup(axes, complex_sine_curve, x_label, y_label)

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

        mathExp = MathTex(r"\hat{f}(x,y) = \sum_{i=1}^{4} w_i \sigma\left(a_i x + b_i y + c_i\right)").scale(0.75)
        mathExp.set_color(text_color)
        mathExp.move_to(LEFT*3+DOWN*1.5)

        # scaling and moving down a bit
        sineCurveGroup.scale(0.75).shift(DOWN*0.5)

        self.play(Create(sineCurveGroup),
                  Write(equal_sign), Write(plus_sign1), Write(plus_sign2),
                  Write(plus_sign3), Create(new_axes1), Create(new_axes2),
                  Create(new_axes3), Create(new_axes4), Create(sigmoidCurve1),
                  Create(sigmoidCurve2), Create(sigmoidCurve3), Create(sigmoidCurve4),
                  Write(mathExp))

        self.wait(1)

class DeepNetworks3(Scene):
    def construct(self):

        titleText = Text("Deep Networks", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

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

        sineCurveGroup = VGroup(axes, complex_sine_curve, x_label, y_label)

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

        mathExp = MathTex(r"\hat{f}(x,y) = \sum_{i=1}^{4} w_i \sigma\left(a_i x + b_i y + c_i\right)").scale(0.75)
        mathExp.set_color(text_color)
        mathExp.move_to(LEFT*3+DOWN*1.5)

        # scaling and moving down a bit
        sineCurveGroup.scale(0.75).shift(DOWN*0.5)

        # creating more complex sine curve
        newAxes = Axes(
            x_range=[-2,3],
            y_range=[0,3],
            axis_config={"color": blue_color},
        )

        complex_sine_curve2 = newAxes.plot(lambda x: 1.5+0.5*np.sin(11*np.pi*x+1)+1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=mauvre_color)

        x_label2 = newAxes.get_x_axis_label("x")
        y_label2 = newAxes.get_y_axis_label("y")
        x_label2.set_color(text_color)
        y_label2.set_color(text_color)
        newAxes.scale(0.5).to_edge(UL)
        complex_sine_curve2.scale(0.5).to_edge(UL)
        x_label2.move_to(LEFT).scale(0.75)
        y_label2.move_to(UP*3+LEFT*4.5).scale(0.75)

        sineCurveGroup2 = VGroup(newAxes,complex_sine_curve2,x_label2,y_label2)
        sineCurveGroup2.scale(0.75).shift(DOWN*0.5)

        self.add(sineCurveGroup, equal_sign, plus_sign1, plus_sign2, plus_sign3,
                 new_axes1, new_axes2, new_axes3, new_axes4,
                 sigmoidCurve1, sigmoidCurve2, sigmoidCurve3, sigmoidCurve4,
                 mathExp)

        self.play(FadeOut(mathExp),
                  sineCurveGroup.animate.shift(DOWN*3.5).scale(0.75))
        self.play(Create(sineCurveGroup2))

        self.wait(1)

class DeepNetworks4(Scene):
    def construct(self):

        titleText = Text("Deep Networks", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

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

        sineCurveGroup = VGroup(axes, complex_sine_curve, x_label, y_label)

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

        # scaling and moving down a bit
        sineCurveGroup.scale(0.75).shift(DOWN*0.5)

        # creating more complex sine curve
        newAxes = Axes(
            x_range=[-2,3],
            y_range=[0,3],
            axis_config={"color": blue_color},
        )

        complex_sine_curve2 = newAxes.plot(lambda x: 1.5+0.5*np.sin(11*np.pi*x+1)+1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=mauvre_color)

        x_label2 = newAxes.get_x_axis_label("x")
        y_label2 = newAxes.get_y_axis_label("y")
        x_label2.set_color(text_color)
        y_label2.set_color(text_color)
        newAxes.scale(0.5).to_edge(UL)
        complex_sine_curve2.scale(0.5).to_edge(UL)
        x_label2.move_to(LEFT).scale(0.75)
        y_label2.move_to(UP*3+LEFT*4.5).scale(0.75)

        sineCurveGroup2 = VGroup(newAxes,complex_sine_curve2,x_label2,y_label2)
        sineCurveGroup2.scale(0.75).shift(DOWN*0.5)

        sineCurveGroup.shift(DOWN*3.5).scale(0.75)

        self.add(sineCurveGroup, equal_sign, plus_sign1, plus_sign2, plus_sign3,
                 new_axes1, new_axes2, new_axes3, new_axes4,
                 sigmoidCurve1, sigmoidCurve2, sigmoidCurve3, sigmoidCurve4,
                 sineCurveGroup2)

        textSigmoid = Text("With more no. of sigmoidal bases", font_size=24)
        textSigmoid.set_color(text_color)
        textSigmoid.move_to(DOWN*0.75+LEFT*3.0)

        self.play(Write(textSigmoid))

        self.wait(1)

class DeepNetworks5(Scene):
    def construct(self):

        titleText = Text("Deep Networks", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

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

        sineCurveGroup = VGroup(axes, complex_sine_curve, x_label, y_label)

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

        # scaling and moving down a bit
        sineCurveGroup.scale(0.75).shift(DOWN*0.5)

        # creating more complex sine curve
        newAxes = Axes(
            x_range=[-2,3],
            y_range=[0,3],
            axis_config={"color": blue_color},
        )

        complex_sine_curve2 = newAxes.plot(lambda x: 1.5+0.5*np.sin(11*np.pi*x+1)+1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=mauvre_color)

        x_label2 = newAxes.get_x_axis_label("x")
        y_label2 = newAxes.get_y_axis_label("y")
        x_label2.set_color(text_color)
        y_label2.set_color(text_color)
        newAxes.scale(0.5).to_edge(UL)
        complex_sine_curve2.scale(0.5).to_edge(UL)
        x_label2.move_to(LEFT).scale(0.75)
        y_label2.move_to(UP*3+LEFT*4.5).scale(0.75)

        sineCurveGroup2 = VGroup(newAxes,complex_sine_curve2,x_label2,y_label2)
        sineCurveGroup2.scale(0.75).shift(DOWN*0.5)

        # Create axes
        axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label_3 = axes2.get_x_axis_label("x")
        y_label_3 = axes2.get_y_axis_label("y")
        x_label_3.set_color(text_color)
        y_label_3.set_color(text_color)

        # drawing a complex sine curve
        complex_sine_curve3 = axes2.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x+2)+0.4*np.sin(2*np.pi*2.3*x+0.5+2)+0.3*np.sin(2*np.pi*4.7*x+1.2+2)+0.2*np.sin(2*np.pi*7*x+2), color=red_color)

        # scale down the axes and curve
        axes2.scale(0.5).to_edge(UL)
        complex_sine_curve3.scale(0.5).to_edge(UL)
        x_label_3.move_to(LEFT).scale(0.75)
        y_label_3.move_to(UP*3+LEFT*4.5).scale(0.75)

        sineCurveGroup3 = VGroup(axes2, complex_sine_curve3, x_label_3, y_label_3)
        sineCurveGroup3.shift(DOWN*3.5).scale(0.75)
        sineCurveGroup3.shift(UP*3+RIGHT*8).scale(0.75)
        sineCurveGroup3.shift(DOWN*3)

        sineCurveGroup.shift(DOWN*3.5).scale(0.75)

        textSigmoid = Text("With more no. of sigmoidal bases", font_size=24)
        textSigmoid.set_color(text_color)
        textSigmoid.move_to(DOWN*0.75+LEFT*3.0)

        self.add(sineCurveGroup, equal_sign, plus_sign1, plus_sign2, plus_sign3,
                 new_axes1, new_axes2, new_axes3, new_axes4,
                 sigmoidCurve1, sigmoidCurve2, sigmoidCurve3, sigmoidCurve4,
                 sineCurveGroup2, textSigmoid)

        textFeatures = Text("With less no. of basis functions", font_size=24)
        textFeatures.set_color(text_color)
        textFeatures.move_to(DOWN*0.75+LEFT*3.0)


        self.play(FadeOut(textSigmoid),
                  FadeOut(new_axes1), FadeOut(new_axes2), FadeOut(new_axes3), FadeOut(new_axes4),
                  FadeOut(sigmoidCurve1), FadeOut(sigmoidCurve2), FadeOut(sigmoidCurve3), FadeOut(sigmoidCurve4),
                  FadeOut(plus_sign1),FadeOut(plus_sign3))
        self.play(sineCurveGroup.animate.shift(UP*3+RIGHT*8),
                  equal_sign.animate.shift(DOWN*1.5))
        self.play(Create(sineCurveGroup3))
        self.wait(1)
        self.play(Write(textFeatures))

        self.wait(1)

class DeepNetworks6(Scene):
    def construct(self):

        titleText = Text("Deep Networks", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

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

        sineCurveGroup = VGroup(axes, complex_sine_curve, x_label, y_label)

        # writing equal sign
        equal_sign = MathTex("=").scale(1.5).next_to(axes, RIGHT, buff=1.5)
        equal_sign.set_color(text_color)

        # writing plus symbols below each axes
        plus_sign2 = MathTex("+").scale(1.0).next_to(equal_sign, 1.5*RIGHT-5.0*UP, buff=0.5)
        plus_sign2.set_color(text_color)

        # scaling and moving down a bit
        sineCurveGroup.scale(0.75).shift(DOWN*0.5)

        # creating more complex sine curve
        newAxes = Axes(
            x_range=[-2,3],
            y_range=[0,3],
            axis_config={"color": blue_color},
        )

        complex_sine_curve2 = newAxes.plot(lambda x: 1.5+0.5*np.sin(11*np.pi*x+1)+1.5+0.6*np.sin(2*np.pi*x)+0.4*np.sin(2*np.pi*2.3*x+0.5)+0.3*np.sin(2*np.pi*4.7*x+1.2)+0.2*np.sin(2*np.pi*7*x), color=mauvre_color)

        x_label2 = newAxes.get_x_axis_label("x")
        y_label2 = newAxes.get_y_axis_label("y")
        x_label2.set_color(text_color)
        y_label2.set_color(text_color)
        newAxes.scale(0.5).to_edge(UL)
        complex_sine_curve2.scale(0.5).to_edge(UL)
        x_label2.move_to(LEFT).scale(0.75)
        y_label2.move_to(UP*3+LEFT*4.5).scale(0.75)

        sineCurveGroup2 = VGroup(newAxes,complex_sine_curve2,x_label2,y_label2)
        sineCurveGroup2.scale(0.75).shift(DOWN*0.5)

        # Create axes
        axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )

        # Create labels for the axes
        x_label_3 = axes2.get_x_axis_label("x")
        y_label_3 = axes2.get_y_axis_label("y")
        x_label_3.set_color(text_color)
        y_label_3.set_color(text_color)

        # drawing a complex sine curve
        complex_sine_curve3 = axes2.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x+2)+0.4*np.sin(2*np.pi*2.3*x+0.5+2)+0.3*np.sin(2*np.pi*4.7*x+1.2+2)+0.2*np.sin(2*np.pi*7*x+2), color=red_color)

        # scale down the axes and curve
        axes2.scale(0.5).to_edge(UL)
        complex_sine_curve3.scale(0.5).to_edge(UL)
        x_label_3.move_to(LEFT).scale(0.75)
        y_label_3.move_to(UP*3+LEFT*4.5).scale(0.75)

        sineCurveGroup3 = VGroup(axes2, complex_sine_curve3, x_label_3, y_label_3)
        sineCurveGroup3.shift(DOWN*3.5).scale(0.75)
        sineCurveGroup3.shift(UP*3+RIGHT*8).scale(0.75)
        sineCurveGroup3.shift(DOWN*3)

        sineCurveGroup.shift(DOWN*3.5).scale(0.75)

        textFeatures = Text("With less no. of basis functions", font_size=24)
        textFeatures.set_color(text_color)
        textFeatures.move_to(DOWN*0.75+LEFT*3.0)

        sineCurveGroup.shift(UP*3+RIGHT*8)
        equal_sign.shift(DOWN*1.5)

        self.add(sineCurveGroup, equal_sign, plus_sign2,
                 sineCurveGroup2, textFeatures, sineCurveGroup3)

        self.play(FadeOut(textFeatures),
                  FadeOut(sineCurveGroup2),
                  FadeOut(plus_sign2),FadeOut(equal_sign),
                  FadeOut(sineCurveGroup3),FadeOut(sineCurveGroup))


        NNVectorForm4 = MathTex(r"\hat{\mathbf{f}}(\mathbf{x}) = \mathbf{W}^{(2)} \sigma\left(\mathbf{W}^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right)").scale(1)
        NNVectorForm4.set_color(text_color)

        self.play(Write(NNVectorForm4))

        self.wait(1)

class DeepNetworks7(Scene):
    def construct(self):

        titleText = Text("Deep Networks", font_size=34)
        titleText.set_color(blue_color)
        titleText.move_to(UP*3.0)

        self.add(titleText)

        NNVectorForm4 = MathTex(r"\hat{\mathbf{f}}(\mathbf{x}) = \mathbf{W}^{(2)} \sigma\left(\mathbf{W}^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right)").scale(1)
        NNVectorForm4.set_color(text_color)

        self.add(NNVectorForm4)

        NNVectorForm5 = MathTex(r"\hat{\mathbf{f}}(\mathbf{x}) = \mathbf{W}^{(3)}\sigma\left(\mathbf{W}^{(2)} \sigma\left(\mathbf{W}^{(1)} \mathbf{x} + \mathbf{b}^{(1)}\right) + \mathbf{b}^{(2)}\right)").scale(1)
        NNVectorForm5.set_color(text_color)
        NNVectorForm5.move_to(DOWN*1)

        self.play(NNVectorForm4.animate.shift(UP*1))
        self.play(Write(NNVectorForm5))

        self.wait(1)


"""
1. put graphical visualization
2. talk about hyper parameter tuning, wider network vs deep skinny network
    """

#==============================================================================
