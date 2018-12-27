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
  _encoder = encoder('./assets/something.bmp')
  _decoder = decoder()
  img_y, img_cb, img_cr = _encoder.encode()
  #LZW(Dictionary-BAsed Codeing)
  img_y = LZW.compress1(img_y)
  img_cb = LZW.compress1(img_cb)
  img_cr = LZW.compress1(img_cr)

  print(len(img_y) +len(img_cb)+len(img_cr))
  with open("LWZ/lwz.pkl", "wb") as fp:   #Pickling
    pickle.dump([img_y,img_cb,img_cr], fp)
  # print(len(img_y),_encoder.width,_encoder.height)
  # input()
  #decode 
  img_y = LZW.decompress1(img_y)
  img_cb = LZW.decompress1(img_cb)
  img_cr = LZW.decompress1(img_cr)
  img = _decoder.decode(img_y, img_cb, img_cr, _encoder.width, _encoder.height)
  #cv2.imshow('result', img[0:img.shape[0]-_encoder.sup_height, 0:img.shape[1]-_encoder.sup_width])
  #cv2.waitKey(0)
  #cv2.destroyAllWindows()
  #print(MSE(_encoder.origin_img, img[0:img.shape[0]-_encoder.sup_height, 0:img.shape[1]-_encoder.sup_width]))
  cv2.imwrite('./result/something-lzw.bmp', img[0:img.shape[0]-_encoder.sup_height, 0:img.shape[1]-_encoder.sup_width])
  print('Time: {} s'.format(time.time()-begin))
