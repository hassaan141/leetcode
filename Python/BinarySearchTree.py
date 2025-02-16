class Node:
  def __init__(self, value=None):
    self.val = value
    self.left_child = None
    self.right_child = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, value):

    if self.root == None:
      self.root = Node(value)
    else:
      