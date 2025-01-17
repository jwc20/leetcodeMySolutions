from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    # result = []
    result = deque()
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        current_level = []
        for _ in range(len(queue)):
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        # result.append(current_level)
        result.appendleft(current_level)
    
    # new_result = []
    # for i in reversed(range(len(result))):
    #     new_result.append(result[i])


    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
