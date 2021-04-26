class Rope:
  # Note: depending on your implementation, you may want to to change this constructor
  def __init__(self, text, size):
    self.text = text
    self.size = size
    self.left = None
    self.right = None

  # just prints the stored text
  # note that you may want to change this, depending on your implementation  
  def to_string(self):
    leftText =  self.left.to_string() if self.left else  ''
    rightText = self.right.to_string() if self.right else  ''
    return leftText + self.text + rightText

  # how deep the tree is (I.e. the maximum depth of children)
  def depth(self):
    return 1 + max(self.left_depth(), self.right_depth())

  # Whether the rope is balanced, i.e. whether any subtrees have branches
  # which differ by more than one in depth. 
  def is_balanced(self): 
    leftBalanced =  self.left.is_balanced() if self.left else True
    rightBalanced = self.right.is_balanced() if self.right else True

    return leftBalanced and rightBalanced and abs(self.left_depth() - self.right_depth()) < 2

  def left_depth(self): 
    if (not self.left): 
      return 0
    return self.left.depth()

  def right_depth(self): 
    if (not self.right): 
      return 0
    return self.right.depth()

  # Helper method which converts the rope into an associative array
  # 
  # Only used for debugging, this has no functional purpose
  def to_dictionary(self):
    mapVersion = {
      'text': self.text,
      'size': self.size
    }
    if (self.right):
      mapVersion['right'] = self.right.to_dictionary()
    if (self.left):
      mapVersion['left'] = self.left.to_dictionary()
    return mapVersion

def create_rope_from_map(map): 
  rope = Rope(map['text'], map['size'])
  if 'left' in map: 
    rope.left = create_rope_from_map(map['left'])
  if 'right' in map: 
    rope.right = create_rope_from_map(map['right'])
  return rope

# This is an internal API. You can implement it however you want. 
# (E.g. you can choose to mutate the input rope or not)
def split_at(rope, position):
  # TODO
  pass

def delete_range(rope, start, end):
  # TODO
  pass

def insert(rope, text, location): 
  # TODO
  pass

def rebalance(rope):
  # TODO
  pass

'''
 Rotates a tree: used for rebalancing.

 Turns:
    b
  /  \
  a   c

  Into:
     c
    /
   b
  /
a
'''
def rotate_left(rope):
  newParent = rope.right
  newLeft = rope
  newLeft.right = newParent.left
  newParent.left = newLeft
  return newParent

'''
/*
 Rotates a tree: used for rebalancing.

 Turns:
    b
  /  \
  a   c

  Into:
     a
      \
       b
        \
         c 
'''
def rotate_right(rope):
  newParent = rope.left
  newRight = rope
  newRight.left = newParent.right
  newParent.right = newRight
  return newParent
