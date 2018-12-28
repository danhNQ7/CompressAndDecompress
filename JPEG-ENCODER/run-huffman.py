from encoder import encoder
from decoder import decoder
import cv2
import pickle
from huffman import HuffmanCoding
import time
DIR = 'TMP/'
def MSE(img1, img2):
  _sum = 0
  for i in range(img1.shape[0]):
    for j in range(img2.shape[2]):
      _sum += (img1[i, j] - img2[i, j]) ** 2
  return _sum / img1.shape[0] / img1.shape[1]

if __name__ == '__main__':
  begin = time.time()
  _encoder = encoder('./assets/flower_foveon.ppm')
  _decoder = decoder()
  img_y, img_cb, img_cr = _encoder.encode()
  #huffman coding 
  print(len(img_y))
  h1 = HuffmanCoding('a.txt')
  h2 = HuffmanCoding('a.txt')
  h3 = HuffmanCoding('a.txt')
  img_y = h1.compress( img_y,0)
  
  img_cb = h2.compress(img_cb,1)
  img_cr = h3.compress(img_cr,2)
  print(type(img_y))
  with open("Huffman/huffman.pkl", "wb") as fp:   #Pickling
    pickle.dump([img_y,img_cb,img_cr], fp)
  input()
  with open("Huffman/huffman.pkl", "rb") as fp:
    [img_y,img_cb,img_cr] = pickle.load(fp)
    with open(DIR+"huffman{}.bin".format(0), 'wb') as output:
      output.write(bytes(img_y))
    with open(DIR+"huffman{}.bin".format(1), 'wb') as output:
      output.write(bytes(img_cb))
    with open(DIR+"huffman{}.bin".format(2), 'wb') as output:
      output.write(bytes(img_cr))
  print(type(img_y))
  # with open("test.txt", "wb") as fp:   #Pickling
  #   pickle.dump([img_y,img_cb,img_cr], fp)
  # print(len(img_y),_encoder.width,_encoder.height)
  # input()
  #decode 
  img_y = h1.decompress(0)
  img_cb = h2.decompress(1)
  img_cr = h3.decompress(2)

  # input()
  img,dims = _decoder.decode(img_y, img_cb, img_cr)
  sup_width ,sup_height = dims
  #cv2.imshow('result', img[0:img.shape[0]-_encoder.sup_height, 0:img.shape[1]-_encoder.sup_width])
  #cv2.waitKey(0)
  #cv2.destroyAllWindows()
  #print(MSE(_encoder.origin_img, img[0:img.shape[0]-_encoder.sup_height, 0:img.shape[1]-_encoder.sup_width]))
  cv2.imwrite('./result/animal-cartoon-huffman.jpg', img[0:img.shape[0]-sup_height, 0:img.shape[1]-sup_width])
  print('Time: {} s'.format(time.time()-begin))
