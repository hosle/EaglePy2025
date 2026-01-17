from tree_construction_and_traverse import construct_tree
from tree_traverse_vertical import verticalOrder

def test_case():
    tree = construct_tree([3,9,8,4,0,1,7])
    
    assert verticalOrder(tree) == [[4],[9],[3,0,1],[8],[7]]
