class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def Add(self, child):
         child.parent = self
         self.children.append(child)

    def print_tree(self):
        char  = ' '* self.get_level();
        prefix =  char + "|--"  if self.parent else ""
        print(prefix + self.data);
        if self.children:
            for v in self.children:
                v.print_tree()

    def get_level(self):
        p = self.parent
        quant = 0
        while p:
            quant = quant + 1
            p = p.parent
        return quant
