class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def set_width(self, w):
    self.width = w
  def set_height(self,h):
    self.height = h
  def get_area(self):
    return (self.width * self.height)
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      str = ''
      element = '*' * int(self.width)
      for i in range(int(self.height)):
        str += element + '\n'
      return str
    

    
  def get_amount_inside(self, rect):
    fit = int(self.get_area()/rect.get_area())
    return fit

  def __str__(self):
    return 'Rectangle'+'('+'width='+str(self.width)+', '\
    +'height='+str(self.height)+')'

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
  def set_side(self, s):
    self.width = s
    self.height = s
  def __str__(self):
    return 'Square'+'('+'side='+str(self.width)+')'
  def set_width(self, w):
    self.width = w
    self.height = w
  def set_height(self, h):
    self.width = h
    self.height = h
  
