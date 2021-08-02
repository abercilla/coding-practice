"""ASCII Art Graphics Library"""

#standard output = print (with Python)

#notes: 
## library is a bunch of code and instructions
## just add method name + paramters and docstring with requirements
## we can store one shape on the canvas like a row in a database
## use x and y to index into canvas and populate with character, e.g. data[y][x] = el.fill_char

class Canvas:
    """Intantiate a canvas with specificied height and width"""

    def __init__(self, height, width):
    
        #NEW self.elements = [] to store the shapes
        self.height = height
        self.width = width

    def render(self): 
        """Render the canvas"""

        inner_space = self.width - 2
        sides = inner_space * (" ")

        #print the body of the canvas
        for line in range(0, self.height):
            print(sides)

        #print bottom of canvas same as top
        bottom = self.width * ("^")
        print(bottom)

    def clear(self):
        """Clear all contents from canvas"""
        
        #NEW self.elements = [] => reset list to 0 
        self.render()

    #NEW add shape method within Canvas class
    #       def add(self, shape):
    ##         """Add shape to canvas"

class Shape(Canvas):

    def __init__(self, canvas_height, canvas_width, start_x, start_y, end_x, end_y, fill_char):
        """Create a shape within the confines of the canvas"""

        #inherit the height and width of the canvas so we can refer to it
        super().__init__(height = canvas_height, width = canvas_width)
        
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.start_x = start_x
        self.start_y = start_y 
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def add_shape(self): 
        
        #get shape height based on y-coords
        shape_height = self.start_y - self.end_y
        
        #get shape width based on x-coords
        shape_width = self.end_x - self.start_x
     
        #do not even add shape to canvas if it's out of bounds
        if shape_height > self.canvas_height:
            raise ValueError("Rectangle too tall for canvas.")
        if shape_width > self.canvas_width:
            raise ValueError("Rectangle too wide for canvas.")
    
        #figure out how much space between top of rectangle and canvas max height
        top_padding = self.canvas_height - self.start_y

        #print padding between shape and top of canvas height
        for line in range(0, top_padding):
            print(" ")

        #calculate space from left border of canvas to first side of shape
        left_padding = self.start_x * " "

        #print top of shape 
        top = shape_width * self.fill_char
        print(left_padding + top)

        #print the body of the canvas
        inner_spaces = shape_width - 2
        sides = left_padding + self.fill_char + inner_spaces * (" ") + self.fill_char

        for line in range(0, shape_height):
            print(sides)

        #print bottom of shape
        bottom = top
        print(left_padding + top)

        for line in range(0, self.end_y):
            print(" ")
        
        #print end of canvas
        print(self.canvas_width * "^")


    def change_fill(self, char): #I got this! 
        """Change the character to fill pre-existing rectangle"""

        self.fill_char = char

    def translate(self, axis, num): #I got this!
        """Move rectangle num spaces on the axis axis"""
        """Shape will go as far as outer bounds of canvas""" 
        
        """e.g. translate(x, 6)"""

        if axis == "x": 
            self.start_x += num
            self.end_x += num
        elif axis == "y": 
            self.start_y += num
            self.end_y += num


#TO-DO: How to add multiple shapes to canvas in the way the instructions describe
