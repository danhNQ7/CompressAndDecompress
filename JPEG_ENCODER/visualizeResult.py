import matplotlib.pyplot as plt
import glob,os
import numpy as np
import argparse

def drawScore(data):
    N = len(data[0])
    ind = np.arange(N)  # the x locations for the groups
    width = 0.2       # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)
    hu = ax.bar(ind-width*3/2, data[1], width, color='blue')
    lz = ax.bar(ind - width/2, data[2], width, color='red')
    ar = ax.bar(ind+width/2, data[3], width, color='green')
    lo = ax.bar(ind+width*3/2, data[4], width, color='yellow')

    # add some
    ax.set_ylabel('Compression Ratio %')
    ax.set_title('Result')
    ax.set_xticks(ind)
    ax.set_xticklabels( data[0],rotation = 30, ha="right",position=(0,0.02))

    ax.legend((hu[0], lz[0], ar[0],lo[0]), ('JPEG_Huffman','JPEG_LZW','JPEG_Aff','Lossless_LZW') )

    plt.show()

def score(org_path,com_path):
    org = os.stat(org_path).st_size
    new = os.stat(com_path).st_size
    return round(org/new,2)

def getdata(path):
    list_img = glob.glob(os.path.join(path,'*.ppm'))
    flag = 0
    huff = []
    lzw = []
    ari = []
    loss = []

    filename = []
    isExist = []
    # list_img = ['artificial.ppm', 'flower_foveon.ppm', 'hdr.ppm', 'spider_web.ppm']
    for p in list_img:
        try:
            com_file = p.replace('.ppm', '_huffman.pkl')
            huff.append(score(p,com_file))

            com_file = p.replace('.ppm', '_lzw.pkl')
            lzw.append(score(p,com_file))

            com_file = p.replace('.ppm', '_arithmetic.pkl')
            ari.append(score(p,com_file))

            com_file = p.replace('.ppm', '_LWZLossless.pkl')
            loss.append(score(p,com_file))

            filename.append(os.path.basename(p))
        except:
            print("Skip: ",p)



    return (filename, huff, lzw, ari, loss)

if __name__ == '__main__':
    parser =argparse.ArgumentParser()
    parser.add_argument('-p','--path_data',help='Path dataset',required=True)
    args = parser.parse_args()
    a = getdata(args.path_data)
    drawScore(a)
    # exe()
    # print(a)
