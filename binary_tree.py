import time
import random
import bisect


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class AVLTree:
    def __init__(self):
        self.root = None

    # Get height of a node
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Get balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        return x

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        return y

    # Insert node
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Perform in-order traversal
    def inorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)
        return result

    # Delete a node
    def delete(self, root, key):
        if not root:
            return root

        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find the node with the minimum value
    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    # Build the balanced BST
    def build_balanced_bst(self, array):
        array.sort()  # Sort the array before inserting into BST
        for value in array:
            self.root = self.insert(self.root, value)

    # Print tree structure (for debugging)
    def print_tree(self, root, level=0):
        if root is not None:
            self.print_tree(root.right, level + 1)
            print(' ' * 4 * level + '->', root.val)
            self.print_tree(root.left, level + 1)


def performance_analysis():
    n = 1000
    random_list = [random.randint(1, 10000) for _ in range(n)]
    start_time = time.time()
    tree = AVLTree()
    tree.build_balanced_bst(random_list)
    end_time = time.time()
    print(f"Time to build balanced BST for {n} elements: {end_time - start_time:.6f} seconds.")

    start_time = time.time()
    sorted_list = tree.inorder(tree.root)
    end_time = time.time()
    print(f"Time for in-order traversal: {end_time - start_time:.6f} seconds.")


def main():
    tree = AVLTree()
    while True:
        print("\nMenu:")
        print("1) Build Balanced BST")
        print("2) In-Order Traversal")
        print("3) Display Sorted Array")
        print("4) Search and Delete")
        print("5) Performance Analysis")
        print("6) Exit from the program")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr = list(map(int, input("Enter an integer array (,-separated): ").split(',')))
            tree.build_balanced_bst(arr)
            print("Balanced BST built successfully.")

        elif choice == "2":
            if tree.root:
                result = tree.inorder(tree.root)
                print("In-Order Traversal:", result)
            else:
                print("Tree is empty.")

        elif choice == "3":
            if tree.root:
                sorted_array = tree.inorder(tree.root)
                print("Sorted Array:", sorted_array)
            else:
                print("Tree is empty.")

        elif choice == "4":
            if tree.root:
                key = int(input("Enter the integer to delete: "))
                tree.root = tree.delete(tree.root, key)
                print(f"Node {key} deleted successfully.")
            else:
                print("Tree is empty.")

        elif choice == "5":
            performance_analysis()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
