import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left, merged_node.right = left, right
        heapq.heappush(heap, merged_node)
    
    return heap[0]

def build_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return
    
    if root.char is not None:
        huffman_codes[root.char] = current_code
        return
    
    build_huffman_codes(root.left, current_code + "0", huffman_codes)
    build_huffman_codes(root.right, current_code + "1", huffman_codes)

def compress(data, huffman_codes):
    compressed_data = ""
    for char in data:
        compressed_data += huffman_codes[char]
    return compressed_data

def decompress(compressed_data, huffman_tree):
    decompressed_data = ""
    current_node = huffman_tree
    for bit in compressed_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decompressed_data += current_node.char
            current_node = huffman_tree
    
    return decompressed_data
