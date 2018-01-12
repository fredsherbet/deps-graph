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
    parent = None
    for line in f.readlines():
        try:
            current = Node(line)
            while parent and current.indent <= parent.indent:
                # Hunting for the line that "wraps" this line.
                parent = parent.parent
            if parent is None:
                # Starting a new tree
                parent = current
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


if __name__ == '__main__':
    main()
