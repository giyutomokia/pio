# rule.py
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left            # Reference to left child
        self.right = right          # Reference to right child (for operators)
        self.value = value          # Value for operand nodes

def create_rule(rule_string):
    # A simple parser that creates an AST from the rule string
    # This function needs to be implemented for your specific rule parsing logic
    # For simplicity, we are returning a placeholder
    return Node("root", value=rule_string)  # Placeholder AST

def evaluate_rule(node, data):
    # Recursive function to evaluate the AST against the data
    if node.node_type == "operand":
        # Compare the value with the corresponding data attribute
        attr, op, value = node.value
        if op == '>':
            return data[attr] > value
        elif op == '<':
            return data[attr] < value
        elif op == '=':
            return data[attr] == value
    elif node.node_type == "operator":
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)
        if node.value == "AND":
            return left_result and right_result
        elif node.value == "OR":
            return left_result or right_result
    return False  # Default case if no condition matches
