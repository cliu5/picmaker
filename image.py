import random as r

def image ():

    f = open('image.ppm','w')
    f.write('P3 500 500 255 ')

    for i in range(500):
        for j in range (500):
             f.write("%d %d %d " % (i%256,j%256, ((i+j)*5)%256))

    f.close()

if __name__  == "__main__":
    image()
