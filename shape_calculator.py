class Rectangle:
    def __init__(self, width, height=None):
        if height == None:
            self.width = width
            self.height = width
        else:
            self.width = width
            self.height = height

    def __repr__(self):
        string = f"Rectangle(width={self.width}, height={self.height})"
        width = self.width
        height = self.height
        return string

    def set_width(self, newwidth):
        if self.width == self.height:
            self.width = newwidth
            self.height = newwidth
        else:
            self.width = newwidth

    def get_width(self):
        return self.width

    def set_height(self, newheight):
        if self.height == self.width:
            self.height = newheight
            self.width = newheight
        else:
            self.height = newheight

    def get_height(self):
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        width_str = "*" * self.width
        picture = ""
        for i in range(self.height):
            picture += width_str + "\n"

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return picture

    def get_amount_inside(self, shape):
        width_out = self.width
        height_out = self.height

        width_in = shape.get_width()
        height_in = shape.get_height()

        amount_width = width_out // width_in
        # print(amount_width)
        amount_height = height_out // height_in
        # print(amount_height)

        if amount_width >= 1 and amount_height >= 1:
            amount_inside = amount_width * amount_height
        else:
            amount_inside = 0

        return amount_inside


class Square(Rectangle):
    def __repr__(self):
        string = f"Square(side={self.width})"
        return string

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side


rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

rect2 = Rectangle(4, 8)
print(rect2.get_amount_inside(rect))

rect.set_height(10)
rect.set_width(15)
print(rect.get_amount_inside(sq))
