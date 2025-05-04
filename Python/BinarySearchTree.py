class Node:
  def __init__(self, value=None):
    self.val = value
    self.left_child = None
    self.right_child = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
    else:
      self._insert(self.root, value)

  def _insert(self, current, value):
    if value < current.val:
      if current.left_child is None:
        current.left_child = Node(value)
      else:
        self._insert(current.left_child, value)
    elif value > current.val:
      if current.right_child is None:
        current.right_child = Node(value)
      else:
        self._insert(current.right_child, value)
    # If value == current.val, do nothing (no duplicates)

  def search(self, value):
    return self._search(self.root, value)

  def _search(self, current, value):
    if current is None:
      return False
    if value == current.val:
      return True
    elif value < current.val:
      return self._search(current.left_child, value)
    else:
      return self._search(current.right_child, value)

  def delete(self, value):
    self.root = self._delete(self.root, value)

  def _delete(self, current, value):
    if current is None:
      return None
    if value < current.val:
      current.left_child = self._delete(current.left_child, value)
    elif value > current.val:
      current.right_child = self._delete(current.right_child, value)
    else:
      # Node with only one child or no child
      if current.left_child is None:
        return current.right_child
      elif current.right_child is None:
        return current.left_child
      # Node with two children: get the inorder successor
      min_larger_node = self._find_min(current.right_child)
      current.val = min_larger_node.val
      current.right_child = self._delete(current.right_child, min_larger_node.val)
    return current

  def inorder(self):
    result = []
    self._inorder(self.root, result)
    return result

  def _inorder(self, current, result):
    if current:
      self._inorder(current.left_child, result)
      result.append(current.val)
      self._inorder(current.right_child, result)

  def preorder(self):
    result = []
    self._preorder(self.root, result)
    return result

  def _preorder(self, current, result):
    if current:
      result.append(current.val)
      self._preorder(current.left_child, result)
      self._preorder(current.right_child, result)

  def postorder(self):
    result = []
    self._postorder(self.root, result)
    return result

  def _postorder(self, current, result):
    if current:
      self._postorder(current.left_child, result)
      self._postorder(current.right_child, result)
      result.append(current.val)

  def find_min(self):
    node = self._find_min(self.root)
    return node.val if node else None

  def _find_min(self, current):
    while current and current.left_child:
      current = current.left_child
    return current

  def find_max(self):
    node = self._find_max(self.root)
    return node.val if node else None

  def _find_max(self, current):
    while current and current.right_child:
      current = current.right_child
    return current