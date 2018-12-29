import cv2
import LZW
import numpy as np
import pickle
import os
import time
from huffman import HuffmanCoding
import datetime
def get_time():
    now = datetime.datetime.now()
    return "[{}:{}:{}] - ".format(now.hour,now.minute, now.second)
def regenerate_the_image(code,myshape):
    print("Regenerating the compresed image:\n")
    pixelList = []
    for c in code:
        pixelList.append(ord(c))

    array = np.array(pixelList, dtype=np.uint8)

    return array.reshape(myshape)

def convertImg2Str(img):
    res = img.reshape(-1)

    convertedString = []
    realString = ""

    for f in res:
        convertedString.append(chr(f))

    for s in convertedString:
        realString +=str(s)
    return realString
def compress(path_img,filename):
    img = cv2.imread(path_img)
    st = time.time()
    myshape = img.shape
    result=''
    result+='Img shape: {}\n'.format(myshape)

    realString = convertImg2Str(img)

    result+='Lenght string : {}\n'.format(len(realString))
    ext = path_img.split('.')[-1]
    a = LZW.compress1(realString)
    # print(len(a))
    pickle.dump((a, myshape,ext), open("{}.pkl".format(filename),"wb"))
    result+="Done! Compressed file\n".format(filename)
    # result+='Time compressed: '.format(time.time() - st)
    return result
def decompressImg(com_path,dir_path):
    st = time.time()
    com, myshape ,ext= pickle.load(open(com_path,'rb'))
    b = LZW.decompress1(com)
    img = regenerate_the_image(b,myshape)
    cv2.imwrite(dir_path+'_restored.{}'.format(ext),img)
    return dir_path+'_restored.{}'.format(ext)
    #print("Done! the decompressed image file is {}".format(new_file))
    #print('Time decompress: ', time.time() - st)


def score(org_path,com_path):
    org = os.stat(org_path).st_size
    new = os.stat(com_path).st_size
    print(org)
    print(new)
    print('Compression Ratio: ',org/new)

# def compress(path_img,dir_path):
#     img = cv2.imread(path_img)
#     print(img.shape)


#     compressImg(img, dir_path)
    # decompressImg('somethingHieu.pkl', path_img)
    # score(path_img, 'somethingHieu.pkl')

