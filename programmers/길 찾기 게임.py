import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    # 이진트리 구현
    class Node:
        def __init__(self, v, x, y):
            self.v = v
            self.x = x
            self.y = y
            self.left = None
            self.right = None
            
    class BST():
        def __init__(self):
            self.root = None
            
        def insert(self, nv, nx, ny):
            self.cur_node = self.root
            while True:
                # 왼쪽에 삽입
                if nx<self.cur_node.x:
                    # 왼쪽에 노드가 달려있다면 해당 노드와 비교
                    if self.cur_node.left is not None:
                        self.cur_node = self.cur_node.left
                    # 왼쪽에 노드가 없다면 노드 추가
                    else:
                        self.cur_node.left = Node(nv, nx, ny)
                        break
                # 오른쪽에 삽입
                else:
                    if self.cur_node.right is not None:
                        self.cur_node = self.cur_node.right
                    else:
                        self.cur_node.right = Node(nv, nx, ny)
                        break
                        
        def preorder(self):
            order=[]
            def _preorder(node):
                order.append(node.v)
                if node.left:
                    _preorder(node.left)
                if node.right:
                    _preorder(node.right)
            _preorder(self.root)
            return order
                      
        def postorder(self):
            order=[]
            def _postorder(node):
                if node.left:
                    _postorder(node.left)
                if node.right:
                    _postorder(node.right)
                order.append(node.v)

            _postorder(self.root)
            return order            
        
    for i, node in enumerate(nodeinfo):
        node.insert(0, i+1)

    nodeinfo.sort(key=lambda x:-x[2])

    tree = BST()
    tree.root=Node(*nodeinfo[0])
    nodeinfo.pop(0)
    
    for node in nodeinfo:
        tree.insert(*node)
        
    
    return [tree.preorder(), tree.postorder()]