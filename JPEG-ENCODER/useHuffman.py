from huffman import HuffmanCoding
#import sys

path = "sample.txt"

h = HuffmanCoding('a.txt')
#with open('test.txt','r') as f:
 #   text = f.read()
text = 'Nguyen quoc danh'

text2 = 'sdadsa'
print(len(text))
output_path = h.compress(text,1)
print("Compressed file path: " + output_path)
output_path2 = h.compress(text2,2)

decom_path = h.decompress(1)
print(len(decom_path))
decom_path2 = h.decompress(2)

print("Decompressed file path: " + decom_path)
