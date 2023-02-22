#!/usr/bin/env python

import cairo

#width and height of the image
width= 500 
height = 400

#surface variable with the specified width and height
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height) #cairo.FORMAT_RGB24 did not work but cairo.FORMAT_ARGB32 did so yay

#this creates a new context; we then use the methods of the context to 'draw' on the surface i.e., drawing lines and shapes
context = cairo.Context(surface)

#this is for getting rid of the black and white boxes but doesnt seem to have worked
context.set_antialias(cairo.ANTIALIAS_NONE)

#specifying the width of the line
context.set_line_width(6)

#we specifiy a line drawn from (50, 50) to (400, 400)
context.move_to(50, 50)
context.line_to(400, 400)
context.stroke()

#we specify a rectangle starting at the top left corner at (100, 100) and has a width of 300 and a height of 200
context.rectangle(100, 100, 300, 200)
context.stroke() #basically a command to make the rectangle from the set parameters

#output the image to a png file
surface.write_to_png('shape_with_line.png')

############################
