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
                  x_label.animate.scale(0.5).next_to(axes, DOWN, buff=0.1),
                  y_label.animate.scale(0.5).next_to(axes, LEFT, buff=0.1))

        self.wait(1)

#==============================================================================
