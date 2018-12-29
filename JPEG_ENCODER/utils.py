from encoder import encoder
from decoder import decoder
import LZW
from huffman import HuffmanCoding
import lossless_LZW
import pickle
import time
import cv2
import os
import arithmetic_compress
import arithmetic_decompress
dict_Alg={0:"JPEG encoder with Huffman Coding",1:"JPEG encoder LZW Coding",
            2: "JPEG encoder Arithmetic Coding",3:"LZW Lossless Coding"}
def info_img(path,flag_alg):
    img = cv2.imread(path)

    try: 
        if img == None:
            output_info = "Please choose file image"
            return output_info
    except:
       
        h,w = img.shape[:2]
        size_img= os.path.getsize(path)/1000
        output_info = "Algorithm : {} \n".format(dict_Alg[flag_alg])
        output_info += "================================\n"
        output_info += "Info Image:\nPath: {} \nSize: {} KB \nWidthxHeight:{}x{}".format(path,size_img,w,h)
        return output_info
def compress(path,flag_alg):
    dir_folder = path[:path.rfind('.')]
    begin = time.time()
    result=''
    if flag_alg ==3: 
        result += lossless_LZW.compress(path,dir_folder)
    else:
        #JPEG-ENCODING
        _encoder = encoder(path)
        _decoder = decoder()
        img_y, img_cb, img_cr,result  = _encoder.encode()
        #Choose Algo
        result+=_encoder.get_time() + '[INFO] Entropy Encoder\n'
        #Huffman
        if flag_alg==0:
            print(len(img_y))
            h1 = HuffmanCoding('a.txt')
            h2 = HuffmanCoding('a.txt')
            h3 = HuffmanCoding('a.txt')
            img_y = h1.compress( img_y,0)
            
            img_cb = h2.compress(img_cb,1)
            img_cr = h3.compress(img_cr,2)
            print(type(img_y))
            
            with open(dir_folder+".pkl", "wb") as fp:   #Pickling
                pickle.dump([h1,h2,h3,img_y,img_cb,img_cr], fp)
        #LZW
        elif flag_alg ==1:
            img_y = LZW.compress1(img_y)
            img_cb = LZW.compress1(img_cb)
            img_cr = LZW.compress1(img_cr)

            print(len(img_y) +len(img_cb)+len(img_cr))
            with open(dir_folder+".pkl", "wb") as fp:   #Pickling
                pickle.dump([img_y,img_cb,img_cr], fp)
        #Arithmetic 
        elif flag_alg == 2:
            img_y = arithmetic_compress.arith_compress(img_y)
            img_cb = arithmetic_compress.arith_compress(img_cb)
            img_cr = arithmetic_compress.arith_compress(img_cr)
            with open(dir_folder+".pkl", "wb") as fp:   #Pickling
                pickle.dump([img_y,img_cb,img_cr], fp)
        result+=_encoder.get_time() + 'Done\n'
        
    result = "Compresssion Task\n==============================\n"+ result
    result += ('Time Total: {} s \n'.format(time.time()-begin))
    return result
def decompress(path,flag_alg):
    begin = time.time()
    dir_folder = path[:path.rfind('.')]
    result=''
    if flag_alg ==3:
        #LZW
        img_path = lossless_LZW.decompressImg(path,dir_folder)
        result="\nDecompresssion Task\n==============================\nDone! Decompressed file\n" 
        result+='Time: {} s'.format(time.time()-begin)
        return img_path,result
    else:
        #JPEG_DECODER
        #LZW 
        _decoder = decoder()
        result_tmp=_decoder.get_time() + '[INFO] Entropy Decoder\n'
        if flag_alg ==1:
            with open(path, "rb") as fp:   #Pickling
                [img_y,img_cb,img_cr]=pickle.load(fp)
            # print(len(img_y),_encoder.width,_encoder.height)
            # input()
            #decode
            img_y = LZW.decompress1(img_y)
            img_cb = LZW.decompress1(img_cb)
            img_cr = LZW.decompress1(img_cr)
        elif flag_alg ==0:
            DIR = os.path.dirname(os.path.realpath(__file__))+'/TMP/'
            # h1 = HuffmanCoding('a.txt')
            # h2 = HuffmanCoding('a.txt')
            # h3 = HuffmanCoding('a.txt')
            with open(path, "rb") as fp:
                [h1,h2,h3,img_y,img_cb,img_cr] = pickle.load(fp)
            
                with open(DIR+"huffman{}.bin".format(0), 'wb') as output:
                    output.write(bytes(img_y))
                with open(DIR+"huffman{}.bin".format(1), 'wb') as output:
                    output.write(bytes(img_cb))
                with open(DIR+"huffman{}.bin".format(2), 'wb') as output:
                    output.write(bytes(img_cr))
            img_y = h1.decompress(0)
            img_cb = h2.decompress(1)
            img_cr = h3.decompress(2)
        # Arithmetic
        elif flag_alg ==2:
            print("Arithmetic Decode")
            with open(path, "rb") as fp:   #Pickling
                [img_y,img_cb,img_cr]=pickle.load(fp)
            #decode
            img_y = arithmetic_decompress.arith_decompress(img_y)
            img_cb = arithmetic_decompress.arith_decompress(img_cb)
            img_cr = arithmetic_decompress.arith_decompress(img_cr)
        result_tmp+=_decoder.get_time() + 'Done\n'
        #decode
        img,dims,tail_f,result = _decoder.decode(img_y, img_cb, img_cr)
        sup_width ,sup_height = dims
        cv2.imwrite(dir_folder+'_restored.{}'.format(tail_f), img[0:img.shape[0]-sup_height, 0:img.shape[1]-sup_width])
        print('Time: {} s'.format(time.time()-begin))
        result="\nDecompresssion Task\n ==============================\n"+ result_tmp + result
        result+='Time Total: {} s'.format(time.time()-begin)
        return dir_folder+'_restored.{}'.format(tail_f),result
if __name__ =='__main__':
    # compress('assets/flower_foveon.ppm',0)
    decompress('assets/flower_foveon.pkl',0)