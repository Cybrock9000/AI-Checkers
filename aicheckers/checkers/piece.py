from .constance import *
class Piece:
  PADDING = 10
  OUTLINE = 2
  def __intit__(self, row, col, color):
    self.row = row
    self.col = col
    self.color = color
    self.king = False

    if self.color == RED:
      self.direction = -1
    else:
      self.direction = 1
  self.x = 0
  self.y = 0

def cal_pos(self):
  self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
  self/.y =  SQUARE_SIZE * self.row + SQUARE_SIZE // 2

def make_King(self):
  self.king = True

def draw(self, win):
  radius = SQUARE_SIZE//2 - self.PADDING
  pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
  pygame.draw.circle(win, GREY, (self.x, self.y), radius)

def __repr___(self):
   return str(self.color)

