def solution(nodeinfo):
    answer = []
    nodeinfo = sorted([[idx+1, node] for idx, node in enumerate(nodeinfo)], key=lambda x: x[1][1], reverse=True)
    root = Node(nodeinfo[0])

    tree = BinaryTree()
    tree.root = root

    for i in range(1, len(nodeinfo)):
        tree.insert(nodeinfo[i])

    answer.append(tree.preorder())
    answer.append(tree.postorder())

    return answer

class Node:
    def __init__(self, data):
        self.data = data[0]
        self.coordinate = data[1]
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, nodeinfo):
        self.current_node = self.root
        while True:
            if nodeinfo[1][0] < self.current_node.coordinate[0]:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(nodeinfo)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(nodeinfo)
                    break
    
    def preorder(self):
        pre_list = []
        def preorder(root):
            if root is None:
                pass
            else:
                pre_list.append(root.data)
                preorder(root.left)
                preorder(root.right)
        preorder(self.root)
        return pre_list
    
    def postorder(self):
        post_list = []
        def postorder(root):
            if root is None:
                pass
            else:
                postorder(root.left)
                postorder(root.right)
                post_list.append(root.data)
        postorder(self.root)
        return post_list
        

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))