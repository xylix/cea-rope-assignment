# FIXME: Some specifications for a Rope say that _only_ the leaf nodes should contain text, not the upper nodes. Upper nodes should _only_ contain the size, if we are following such a spec
class Rope:
  # Note: depending on your implementation, you may want to to change this constructor
  def __init__(self, text, size = None, left = None, right = None):
    self.text = text
    if size:
      self.size = size
    else:
      if text:
        self.size = len(text)
      if left:
        self.size = len(left.text)
    self.left = left
    self.right = right

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
  rope = Rope(map.get('text'), map.get('size'))
  if 'left' in map: 
    rope.left = create_rope_from_map(map['left'])
  if 'right' in map: 
    rope.right = create_rope_from_map(map['right'])
  return rope

# This is an internal API. You can implement it however you want. 
# (E.g. you can choose to mutate the input rope or not)
def split_at(rope, position):
  if position <= rope.size:
    if rope.right:
      return split_at(rope.right(position - rope.size))
    else:
      string = rope.to_string()
      left = string[:position]
      right = string[position:]
      return (Rope(left), Rope(right)) 
  else:
    if rope.left:
      return split_at(rope.left, position)
    else:
      string = rope.to_string()
      left = string[:position]
      right = string[position:]
      return (Rope(left), Rope(right))

def delete_range(rope, start, end):
  left, _ = split_at(rope, start)
  _, right = split_at(rope, end)
  return concat(left, right)

def insert(rope, text, location): 
  left, right = split_at(rope, location)
  return concat(concat(left, Rope(text)), right)

def rebalance(rope):
  if rope.is_balanced():
    return rope
  else:
    if not rope.right:
      return rebalance(rotate_left(rope))
    if not rope.left:
      return rebalance(rotate_right(rope))
    left = rebalance(left)
    right = rebalance(right)
    return concat(left, right)

# Concat is useful for implementing other operations
def concat(left, right):
  return Rope('', None, left, right)

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
