# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root: return []

#         sequence, deque = "", collections.deque([root])
#         while deque:

#             node = deque.popleft()
#             if node: 
#                 sequence += str(node.val) + ','
#                 deque.append(node.left)
#                 deque.append(node.right)
#             else:
#                 sequence += 'null,'
#         sequence_list = sequence[:-1].split(',')
#         while sequence_list[-1] == 'null':
#             sequence_list.pop()
#         seq = ','.join(sequence_list)
#         result  = '[' + seq + ']'      
#         print(result)   
#         return result     


#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNodei
#         """
#         if data == '[]' or data == '[null]': return 
#         values, i = data[1:-1].split(','), 1
#         root = TreeNode(int(values[0]))
#         deque = collections.deque([root])
#         while deque:
#             node = deque.popleft()
#             if values[i] != 'null':
#                 node.left = TreeNode(int(values[i]))
#             i += 1
#             if values[i] != 'null':
#                 node.right = TreeNode(int(values[i]))
#             i += 1
#         return root

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        seq = []
        if not root: return seq
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                seq.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                seq.append(None)
        while seq[-1] is None:
            seq.pop()
        return seq

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        root = TreeNode(data.pop(0))
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            left, right = None, None
            if data:
                item = data.pop(0)
                if item is not None:
                    left = TreeNode(item)
                    node.left = left
                    queue.append(left)
            if data:
                item = data.pop(0)
                if item is not None:
                    right = TreeNode(item)
                    node.right = right
                    queue.append(right)
            
        return root
