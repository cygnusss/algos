class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def insert(self, value):
    current = self
    
    while True:
      if current.value < value:
        if not current.right:
          break
        else:
          current = current.right
      elif current.value > value:
        if not current.left:
          break
        else:
          current = current.left
    
    if current.value < value:
      current.right = BinaryTree(value)
    elif current.value > value:
      current.left = BinaryTree(value)


if __name__ == "__main__":
  tree = BinaryTree(5)
  tree.insert(4)
  tree.insert(2)
  print("value is",  tree.value, "left left is", tree.left.left.value, "right is", tree.right)