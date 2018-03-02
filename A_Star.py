from Queue import PriorityQueue

class State(object):
  def __init__(self, value, parent, start = 0, goal = 0, solver = 0):
    