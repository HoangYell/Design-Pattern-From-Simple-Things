from abc import ABC, abstractmethod


class Component(ABC):
    _parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):  # noqa: B027
        pass

    def remove(self, component):  # noqa: B027
        pass

    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    """
    A leaf can't have any children.
    Leaf objects do the actual work.
    """

    def operation(self):
        return "🍁"


class Branch(Component):
    """
    A branch can have children(leaves or baby branches) .
    Branch objects do nothing but contain children
    """

    def __init__(self):
        self._children = []

    def add(self, component):
        component.parent = self
        self._children.append(component)

    def remove(self, component):
        component.parent = None
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return results


if __name__ == "__main__":
    branch_1 = Branch()
    branch_1.add(Leaf())
    branch_1.add(Leaf())

    branch_2 = Branch()
    branch_2.add(Leaf())

    wormy_leaf = Leaf()

    tree = Branch()
    tree.add(branch_1)
    tree.add(Leaf())
    tree.add(wormy_leaf)
    tree.add(branch_2)
    tree.remove(wormy_leaf)

    print(tree.operation())
