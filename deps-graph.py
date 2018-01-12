#!/usr/bin/python

import sys

class NodeNotFound(Exception):
    """Couldn't find the node"""

class IgnoreLine(Exception):
    """Cannot create a node with this line"""


def main():
    print_deps_graph(sys.stdin)
    sys.stderr.write('\nCopy and paste the above into http://www.nomnoml.com\n')


def print_deps_graph(f):
    root = None
    parent = None
    for line in f.readlines():
        try:
            if parent is None:
                # First node
                parent = Node(line)
                if root is None:
                    root = parent
                continue
            current = Node(line)
            while current.indent <= parent.indent:
                parent = parent.parent
                if parent is None:
                    # We've reached the root of the tree, so this must be the
                    # start of a new tree.
                    #
                    # If the root of this tree appears in our existing tree,
                    # then we build _this_ tree on that existing node.
                    parent = root.find_node(current)
                    parent.indent = current.indent
                    break
            if parent == current:
                continue
            parent.add_child(current)
            parent = current
        except IgnoreLine:
            continue
        except:
            sys.stderr.write("Error handling line [%s]\n" % line)
            raise


class Node:
    def __init__(self, line, parent=None):
        if line.strip() == '':
            # Blank line
            raise IgnoreLine()
        if line.strip().startswith('#'):
            # Comment
            raise IgnoreLine()
        self.line = line
        self.name = line.strip()
        self.indent = len(line) - len(line.lstrip())
        self.parent=parent
        self.children = []

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def add_child(self, node):
        print '[%s] <- [%s]' % (self, node)
        self.children.append(node)
        node.parent = self

    def find_node(self, node):
        if self == node:
            return self
        for c in self.children:
            try:
                return c.find_node(node)
            except NodeNotFound:
                pass
        raise NodeNotFound("Could not find %s in %s" % (node, self))


if __name__ == '__main__':
    main()
