import h5py
import numpy as np
from numpy.core.fromnumeric import reshape
import open3d as o3d
import matplotlib.pyplot as plt
import six


#############################
# create time 2020.4.20
# 定义一个huffman节点类
#############################
class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def is_left(self):
        return self.father.left == self


#############################
# create time 2020.4.20
# 节点生成函数
#############################
def create_nodes(frequencies):
    return [Node(freq) for freq in frequencies]


#############################
# create time 2020.4.20
# huffman树生成函数
#############################
def create_huffman_tree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


###############################
# create time 2020.4.20
# 根据huffman树产生huffman编码
###############################
def huffman_encoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.is_left():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes


#############################################
# create time 2020.4.20
# 获取字符出现的频数
#############################################
def count_frequency(datas):
    # 用于存放字符
    char_store = []
    # 用于存放频数
    freq_store = []
    rows = datas.shape[0]
    cols = datas.shape[0]
    # 解析字符串
    for row in range(rows):
        for col in range(cols):
            data = datas[row][col]
            data1 = data.tolist()
            if char_store.count(data1) > 0:
                temp = int(freq_store[char_store.index(data1)])
                temp = temp + 1
                freq_store[char_store.index(data1)] = temp
            else:
                char_store.append(data1)
                freq_store.append(1)
    # 返回字符列表和频数列表
    print(1)
    return char_store, freq_store


############################
# create time 2020.4.20
# 获取字符、频数的列表
############################

def get_char_frequency(char_store=[], freq_store=[]):
    # 用于存放char_frequency
    char_frequency = []
    for item in zip(char_store, freq_store):
        temp = (item[0], item[1])
        char_frequency.append(temp)
    return char_frequency


################################
# create time 2020.4.20
# 编码转换
################################
def write_file(code):
    f = open("huffman_encoding.txt", "wb")
    out = 0
    while len(code) > 8:
        for x in range(8):
            out = out << 1
            if code[x] == "1":
                out = out | 1
        code = code[8:]
        f.write(six.int2byte(out))
        out = 0

    f.write(six.int2byte(len(code)))
    out = 0
    for i in range(len(code)):
        out = out << 1
        if code[i] == "1":
            out = out | 1

    for i in range(8 - len(code)):
        out = out << 1
    f.write(six.int2byte(out))
    f.close()
    return True


###############################
# create time 2020.4.20
# 将字符转换成huffman编码
###############################
def get_huffman_file(input_string, char_frequency, codes):
    # 逐个字符替换
    file_content = ''
    for index in range(len(input_string)):
        for item in zip(char_frequency, codes):
            if input_string[index] == item[0][0]:
                file_content = file_content + item[1]

    return file_content


##################################
# create time 2020.4.20
# 解码huffman编码文件
###################################
def decode_huffman(input_string, char_store, freq_store):
    encode = ''
    decode = ''
    for index in range(len(input_string)):
        encode = encode + input_string[index]
        for item in zip(char_store, freq_store):
            if encode == item[1]:
                decode = decode + item[0]
                encode = ''
    return decode


def load_h5(h5_filename):
    f = h5py.File(h5_filename)
    point_map = f['point_map'][:]
    intrinsics = f['intrinsics'][:]
    return (point_map, intrinsics)


datas, labels = load_h5("/Users/json/Documents/point_cloud_compression/point_cloud.h5")

# one block
points = datas[0][..., 0:3]
label = labels[0]

char_store, freq_store = count_frequency(datas)  # 字母出现次数统计
char_frequency = get_char_frequency(char_store, freq_store)  # 频段统计
nodes = create_nodes([i[1] for i in char_frequency])  # 节点生成
root = create_huffman_tree(nodes)  # 标记根结点
codes = huffman_encoding(nodes, root)  # 生成huffman树
save_file = get_huffman_file(input_string, char_frequency, codes)  # 根据生成的huffman树，生成huffman编码
write_file(save_file)  # 将01比特串按位写入文件
