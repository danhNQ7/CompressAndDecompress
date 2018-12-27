from encoder import encoder
from decoder import decoder
import cv2
import pickle
import LZW
import time
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
  # #LZW(Dictionary-BAsed Codeing)
  # img_y = LZW.compress(img_y)
  # img_cb = LZW.compress(img_cb)
  # img_cr = LZW.compress(img_cr)
  #print(img_y)
  print(len(img_y))

  # print(img_y)
  with open("test.txt", "w") as fp:   #Pickling
    fp.write(img_y)
  # # print(len(img_y),_encoder.width,_encoder.height)
  # input()
  # #decode 
  # img_y = LZW.decompress(img_y)
  # img_cb = LZW.decompress(img_cb)
  # img_cr = LZW.decompress(img_cr)
  img = _decoder.decode(img_y, img_cb, img_cr, _encoder.width, _encoder.height)
  #cv2.imshow('result', img[0:img.shape[0]-_encoder.sup_height, 0:img.shape[1]-_encoder.sup_width])
  #cv2.waitKey(0)
  #cv2.destroyAllWindows()
  print(MSE(_encoder.origin_img, img[0:img.shape[0]-_encoder.sup_height, 0:img.shape[1]-_encoder.sup_width]))
  cv2.imwrite('./result/animal-cartoon.jpg', img[0:img.shape[0]-_encoder.sup_height, 0:img.shape[1]-_encoder.sup_width])
  print('Time: {} s'.format(time.time()-begin))
