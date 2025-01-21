import math
from collections import Counter

# Function to calculate entropy
def entropy(data):
    total = len(data)
    counts = Counter(row[-1] for row in data)  # Count class labels (last element)
    entropy_val = 0
    for count in counts.values():
        prob = count / total
        entropy_val -= prob * math.log2(prob)  # Entropy formula
    return entropy_val

# Function to calculate information gain
def information_gain(data, attribute_index):
    total_entropy = entropy(data)  # Entropy of the original dataset
    values = set(row[attribute_index] for row in data)  # Unique values for the attribute
    
    weighted_entropy = 0
    for value in values:
        subset = [row for row in data if row[attribute_index] == value]  # Subset based on value
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)  # Weighted entropy of the subset
    
    return total_entropy - weighted_entropy  # Information Gain

# Recursive function to build the decision tree
def build_tree(data, attributes):
    # If all instances have the same class label, return a leaf node
    if len(set([row[-1] for row in data])) == 1:
        return {"label": data[0][-1]}
    
    # If no attributes left, return a leaf node with the majority class
    if not attributes:
        majority_class = Counter([row[-1] for row in data]).most_common(1)[0][0]
        return {"label": majority_class}
    
    # Find the best attribute to split on based on information gain
    best_attribute = max(attributes, key=lambda attr: information_gain(data, attr))
    tree = {"attribute": best_attribute}
    
    # Get the values of the best attribute
    attribute_values = set(row[best_attribute] for row in data)
    
    # Create branches for each value of the attribute
    tree["branches"] = {}
    for value in attribute_values:
        # Create the subset of data for the given attribute value
        subset = [row for row in data if row[best_attribute] == value]
        # Recursively build the subtree for this subset
        new_attributes = [attr for attr in attributes if attr != best_attribute]
        tree["branches"][value] = build_tree(subset, new_attributes)
    
    return tree

# Function to print the decision tree in a readable way
def print_tree(tree, attribute_names, indent=""):
    if "label" in tree:
        print(indent + f"Class: {tree['label']}")
    else:
        print(indent + f"Attribute {attribute_names[tree['attribute']]}")
        for value, subtree in tree["branches"].items():
            print(indent + f"  Value {value}:")
            print_tree(subtree, attribute_names, indent + "    ")

# Example dataset
dataset = [
    [2.5, 3.4, 1.2, 0],
    [1.7, 2.3, 3.1, 0],
    [3.1, 2.9, 1.5, 1],
    [2.6, 3.1, 2.2, 1],
    [3.1, 3.6, 1.8, 0],
    [2.9, 2.4, 3.0, 1],
    [2.7, 3.2, 2.9, 0],
    [3.4, 2.7, 1.6, 1],
    [2.5, 3.5, 2.8, 0],
    [3.2, 2.8, 1.7, 1]
]

# Calculate and print entropy of the entire dataset
print(f"Entropy of the dataset: {entropy(dataset)}\n")

# Calculate information gain for each attribute
info_gains = []
for i in range(3):  # We only have 3 attributes A, B, C (index 0, 1, 2)
    info_gain = information_gain(dataset, i)
    info_gains.append(info_gain)
    print(f"Information Gain for Attribute {['A', 'B', 'C'][i]}: {info_gain}")

# Identify the best attribute to split on
best_attribute = ['A', 'B', 'C'][info_gains.index(max(info_gains))]
print(f"\nBest attribute to split on: {best_attribute}\n")

# Map column indices to attribute names
attribute_names = ['A', 'B', 'C']  # Names for attributes A, B, C

# Attributes correspond to the columns 0, 1, and 2 (i.e., A, B, and C)
attributes = [0, 1, 2]

# Build the decision tree
tree = build_tree(dataset, attributes)

# Print the decision tree
print_tree(tree, attribute_names)