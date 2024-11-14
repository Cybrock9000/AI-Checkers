import pygame
from .constants import *

class Board:
  def __init__(self):
    self.board = []
    self.selected_piece = None
    self.red_left = self.white_left = 12
    self.red_kings = self.white_kings = 0

def draw_cubes(self, win):
  win.fill(BLACK)
