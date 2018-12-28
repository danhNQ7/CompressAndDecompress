import cv2
import numpy as np
# from huffman import huffman, dehuffman, inverse

class decoder():
  def __init__(self):
    pass
  
  # def huffman_decode(self, img):
  #   origin = []
  #   for i in range(len(img)):
  #     tmp = []
  #     for j in range(len(img[i])):
  #       key = dehuffman(img[i][j][0]).split('/')
  #       zeros, size = map(lambda x: int(x, 16), key)
  #       if zeros == 0 and size == 0 and j == len(img[i]) - 1:
  #         tmp.append('EOB')
  #       else:
  #         binary = ''
  #         flag = 1
  #         if img[i][j][1] == '':
  #           binary = '0'
  #         elif img[i][j][1][0] == '0' and len(img[i][j][1]) >= 1:
  #           binary = inverse(img[i][j][1])
  #           flag = -1
  #         else:
  #           binary = img[i][j][1]
        
  #         tmp.append((zeros, flag * int(binary, 2)))
  #     origin.append(tmp)
  #   return origin
  
  def deRLE(self, img):
    num_blocks=0
    tmp_dc = img[0][1]
    dc = [tmp_dc]
    for i in range(1,len(img)):
      if img[i][0] ==0: 
        num_blocks = i+1
        dc.append(dc[i-1]+img[i][1])
      else: break
    da =''
    # print(num_blocks)
    # print('done dc')

    for i in range(num_blocks-1,len(img)):
      da = da +img[i][0]*(str(img[i][1])+' ')
    

    da = list(map(int,da.strip().split(' ')))
    # print('done da')
    col = len(da)//num_blocks
    da = np.array(da).reshape(num_blocks,col)
    # print(da,dc)
    # print('done reshape')
    result = np.insert(da,0,dc,axis =1)
    # print(result)
    return result
      

  def inverse_scan(self, img, z, height, width):
    origin = np.zeros([height, width], dtype=int)
    for i in range(len(img)):
      tmp = np.zeros(len(img[i]))
      for j in range(len(img[i])):
        tmp[z[j]] = img[i][j]
      tmp = tmp.reshape([8, 8])
      row, col = i // (width // 8), i % (width // 8)
      row = row * 8
      col = col * 8
      origin[row:row+8, col:col+8] = tmp
  
    return origin
  
  def idct(self, img, dct_kernel):
    origin = np.zeros(img.shape)
    for i in range(0, img.shape[0], 8):
      for j in range(0, img.shape[1], 8):
        temp = img[i:i+8, j:j+8]
        t1 = np.dot(np.transpose(dct_kernel), temp)
        origin[i:i+8, j:j+8] = np.dot(t1, dct_kernel)
    return origin

  def inverse_quantization(self, img, q):
    origin = np.zeros(img.shape)
    for i in range(0, img.shape[0], 8):
      for j in range(0, img.shape[1], 8):
        temp = img[i:i+8, j:j+8]
        origin[i:i+8, j:j+8] = temp * q
    return origin

  def inverse_subsampling(self, img_cb, img_cr, height, width):
    origin_cb, origin_cr = np.zeros([height, width]), np.zeros([height, width])
    for i in range(img_cb.shape[0]):
      for j in range(img_cb.shape[1]):
        tmp1, tmp2 = img_cb[i][j], img_cr[i][j]
        origin_cb[i*2:i*2+2, j*2:j*2+2] = np.array([tmp1, tmp1, tmp1, tmp1]).reshape([2, 2])
        origin_cr[i*2:i*2+2, j*2:j*2+2] = np.array([tmp2, tmp2, tmp2, tmp2]).reshape([2, 2])
    return origin_cb, origin_cr
  
  def rgb_convert(self, img, origin_cb, origin_cr, img_y):
    img[:,:,0] = img_y
    img[:,:,1] = origin_cb
    img[:,:,2] = origin_cr
    img = cv2.cvtColor(img,cv2.COLOR_YUV2BGR)
    # for i in range(img.shape[0]):
    #   for j in range(img.shape[1]):
    #     y = img_y[i, j]
    #     cb = origin_cb[i, j]
    #     cr = origin_cr[i, j]
    #     img[i, j, 2] = min(255, max(0, round(1.402 * (cr - 128) + y)))
    #     img[i, j, 1] = min(255, max(0, round(-0.344136 * (cb - 128) - 0.714136 * (cr - 128) + y)))
    #     img[i, j, 0] = min(255, max(0, round(1.772 * (cb - 128) + y)))
    return img
  def string_to_tuple(self,string,flag =0):
    img = list(map(int,string.split(' ')))
    dims =[]
    if flag == 1:
      dims = img[:4]
      img = img[4:]
    tmp = len(img)-1
    return [tuple([img[i],img[i+1]]) for i in range(0,tmp,2)],dims
  def decode(self, img_y, img_cb, img_cr):
    qy = [16,11,10,16,24,40,51,61,
12,12,14,19,26,58,60,55,
14,13,16,24,40,57,69,56,
14,17,22,29,51,87,80,62,
18,22,37,56,68,109,103,77,
24,35,55,64,81,104,113,92,
49,64,78,87,103,121,120,101,
72,92,95,98,112,100,103,99]

    qy = np.array(qy)
    qy = qy.reshape([8, 8])

    qc = [17,18,24,47,99,99,99,99,
18,21,26,66,99,99,99,99,
24,26,56,99,99,99,99,99,
47,66,99,99,99,99,99,99,
99,99,99,99,99,99,99,99,
99,99,99,99,99,99,99,99,
99,99,99,99,99,99,99,99,
99,99,99,99,99,99,99,99]

    qc = np.array(qc)
    qc = qc.reshape([8, 8])

    z = [0,1,5,6,14,15,27,28,
2,4,7,13,16,26,29,42,
3,8,12,17,25,30,41,43,
9,11,18,24,31,40,44,53,
10,19,23,32,39,45,52,54,
20,22,33,38,46,51,55,60,
21,34,37,47,50,56,59,61,
35,36,48,49,57,58,62,63]
    dct_kernel = np.zeros([8, 8])
    dct_kernel[0, :] = 1 / np.sqrt(8)
    for i in range(1, 8):
      for j in range(8):
        dct_kernel[i, j] = np.cos(np.pi * i * (2 * j + 1) / 16) * np.sqrt(2 / 8)
    # decode
    # img_y = self.huffman_decode(img_y)
    # img_cb = self.huffman_decode(img_cb)
    # img_cr = self.huffman_decode(img_cr)
    #string to tuple 
    print('[Info] De String to tuple:')
    img_y,dims= self.string_to_tuple(img_y,1)
    width ,height = dims[:2]
    img_cb,_=self.string_to_tuple(img_cb)
    img_cr,_=self.string_to_tuple(img_cr)
    print('Done\n[Info] DeRLE')
    #
    img_y = self.deRLE(img_y)
    img_cb = self.deRLE(img_cb)
    img_cr = self.deRLE(img_cr)
    print('Done\n[Info] Inverse-z-scan')
    # inverse-z-scan
    img_y = self.inverse_scan(img_y, z, height, width)
    img_cb = self.inverse_scan(img_cb, z, height // 2, width // 2)
    img_cr = self.inverse_scan(img_cr, z, height // 2, width // 2)
    print('Done\n[Info] Inverse-quantization')
    # inverse-quantization
    img_y = self.inverse_quantization(img_y, qy)
    img_cb = self.inverse_quantization(img_cb, qc)
    img_cr = self.inverse_quantization(img_cr, qc)
    print('Done\n[Info] IDCT')
    # idct
    img_y = self.idct(img_y, dct_kernel)
    img_cb = self.idct(img_cb, dct_kernel)
    img_cr = self.idct(img_cr, dct_kernel)
    # inverse subsampling
    print('Done\n[INFO] Inverse_subsampling')
    origin_cb, origin_cr = self.inverse_subsampling(img_cb, img_cr, height, width)
    print('Done\n[INFO] rgb convert')
    img = np.zeros([height, width, 3], dtype=np.uint8)
    img = self.rgb_convert(img, origin_cb, origin_cr, img_y)
    print('Done')
    return img,dims[2:]
if __name__=='__main__':
  _decoder = decoder()
  a = _decoder.string_to_tuple('0 1 0 2 0 5 1 2 2 3 4 5')
  # _decoder.deRLE([(0, 93), (0, -70), (0, 1), (0, -18), (16, 0), (1, -1), (46, 0), (1, 43), (2, -3), (4, 0), (1, 34), (1, 0), (1, -2), (5, 0), (1, 10), (58, 0), (1, 25), (4, 0), (1, 40), (9, 0), (1, 12), (1, 0), (1, -5), (23, 0), (1, -1), (4, 0), (1, -3), (5, 0), (1, 11), (4, -1), (1, 1), (1, 0), (1, 9), (2, 0), (1, -1), (1, 6), (1, 2), (2, 0), (1, 3), (1, 10), (1, 0), (1, 9), (1, 3), (1, 0), (1, -1), (1, 0), (1, 13), (1, 3), (1, 5), (1, 3), (1, 0), (1, -1), (2, 0), (1, 8), (1, 2), (24, 0), (2, -1), (4, 0)])
  # a= np.array([1,2,3,4,5,6,7,8])
  # print(a.reshape(2,4))
  print(_decoder.decode([(0, 93), (0, -70), (0, 1), (0, -18), (16, 0), (1, -1), (46, 0), (1, 43), (2, -3), (4, 0), (1, 34), (1, 0), (1, -2), (5, 0), (1, 10), (58, 0), (1, 25), (4, 0), (1, 40), (9, 0), (1, 12), (1, 0), (1, -5), (23, 0), (1, -1), (4, 0), (1, -3), (5, 0), (1, 11), (4, -1), (1, 1), (1, 0), (1, 9), (2, 0), (1, -1), (1, 6), (1, 2), (2, 0), (1, 3), (1, 10), (1, 0), (1, 9), (1, 3), (1, 0), (1, -1), (1, 0), (1, 13), (1, 3), (1, 5), (1, 3), (1, 0), (1, -1), (2, 0), (1, 8), (1, 2), (24, 0), (2, -1), (4, 0)]))