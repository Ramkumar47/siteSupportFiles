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
        plus_sign1 = MathTex("+").scale(0.5).next_to(equal_sign, 3.5*RIGHT+1*UP, buff=0.5)
        plus_sign1.set_color(text_color)
        plus_sign2 = MathTex("+").scale(0.5).next_to(equal_sign, 3.5*RIGHT-1.4*UP, buff=0.5)
        plus_sign2.set_color(text_color)
        plus_sign3 = MathTex("+").scale(0.5).next_to(equal_sign, 3.5*RIGHT-4.5*UP, buff=0.5)
        plus_sign3.set_color(text_color)
        plus_sign4 = MathTex("+").scale(0.5).next_to(equal_sign, 3.5*RIGHT-7.75*UP, buff=0.5)
        plus_sign4.set_color(text_color)

        # writing fourier series text
        fourier_series_text = MathTex(r"f(x) = \sum_{n=1}^{\infty} a_n \sin(n x + \phi_n)").scale(0.75).next_to(axes, DOWN, buff=0.5)
        fourier_series_text.set_color(text_color)
        fourier_series_label = Text("Fourier Series Representation", font_size=24).next_to(fourier_series_text, DOWN, buff=0.1)
        fourier_series_label.set_color(text_color)

        # drawing new axes on the right with a new sine wave
        new_axes1 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes1.next_to(axes, RIGHT-3*UP, buff=-2).scale(0.15)
        new_axes2 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes2.next_to(new_axes1, DOWN, buff=-2).scale(0.15)
        new_axes3 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes3.next_to(new_axes2, DOWN, buff=-2).scale(0.15)
        new_axes4 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes4.next_to(new_axes3, DOWN, buff=-2).scale(0.15)
        new_axes5 = Axes(
            x_range=xrange,
            y_range=yrange,
            axis_config={"color": blue_color},
        )
        new_axes5.next_to(new_axes4, DOWN, buff=-2).scale(0.15)

        sineCurve1 = new_axes1.plot(lambda x: 1.5+0.6*np.sin(2*np.pi*x), color=green_color)
        sineCurve2 = new_axes2.plot(lambda x: 1.5+0.4*np.sin(2*np.pi*2.3*x+0.5), color=green_color)
        sineCurve3 = new_axes3.plot(lambda x: 1.5+0.3*np.sin(2*np.pi*4.7*x+1.2), color=green_color)
        sineCurve4 = new_axes4.plot(lambda x: 1.5+0.3*np.sin(2*np.pi*4.7*x+1.2), color=green_color)
        sineCurve5 = new_axes5.plot(lambda x: 1.5+0.2*np.sin(2*np.pi*7*x), color=green_color)

        self.play(Write(equal_sign))

        self.play(Create(new_axes1), Create(sineCurve1),
                  Create(new_axes2), Create(sineCurve2),
                  Create(new_axes3), Create(sineCurve3),
                  Create(new_axes4), Create(sineCurve4),
                  Create(new_axes5), Create(sineCurve5),
                  Write(plus_sign1), Write(plus_sign2),
                  Write(plus_sign3), Write(plus_sign4))

        self.play(Write(fourier_series_text), Write(fourier_series_label))

        self.wait(1)

#==============================================================================
