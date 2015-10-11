__author__ = 'KolesnikG'

import numpy as np
import PIL.Image as Image
import os,sys,cv2
import matplotlib.pyplot as plt
import matplotlib.cm as cm

sys.path.append("..")

def read_images(path, sz = None):
    c = 0
    X,y = [],[]
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames :
            subject_path=os.path.join(dirname,subdirname)
            for filename in os.listdir(subject_path):
                try :
                    im=Image.open(os.path.join(subject_path,filename))
                    im=im.convert("L")
                    # resize to given size (if given )
                    if (sz is not None):
                        im=im.resize(sz, Image.ANTIALIAS)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError:
                    print("I/O error ({0}) : {1} ".format(errno, strerror))
                except:
                    print ("Unexpected error:", sys.exc_info()[0])
                    raise
            c = c +1
    return [X , y]

[X,y]=read_images("d:/3d/faces/")

def asRowMatrix(X) :
    if len(X)==0:
        return np.array([])
    mat=np.empty((0, X[0].size), dtype=X[0].dtype)
    for row in X:
        mat=np.vstack((mat, np.asarray(row).reshape(1, -1)))
    return mat

def pca(X, num_components=0):
    [n,d]=X.shape
    if ( num_components<=0) or (num_components>n):
        num_components=n
    mu=X.mean(axis=0)
    X=X-mu
    if n>d:
        C=np.dot(X.T,X)
        [eigenvalues, eigenvectors]=np.linalg.eigh(C)
    else:
        C=np.dot(X,X.T)
        [eigenvalues, eigenvectors]=np.linalg.eigh(C)
        eigenvectors=np.dot(X.T, eigenvectors)
        for i in range(n):
            eigenvectors[:,i]=eigenvectors[:,i]/np.linalg.norm(eigenvectors[:,i])
    idx = np. argsort (- eigenvalues )
    eigenvalues=eigenvalues[idx]
    eigenvectors=eigenvectors[:,idx]
    # select only num_components
    eigenvalues=eigenvalues[0:num_components].copy()
    eigenvectors=eigenvectors[:,0:num_components].copy()
    return [eigenvalues, eigenvectors, mu]

[D, W, mu]=pca(asRowMatrix(X))

def project(W, X, mu=None):
    if mu is None :
        return np.dot(X,W)
    return np.dot(X-mu, W)

def reconstruct(W, Y, mu=None):
    if mu is None :
        return np.dot(Y,W.T)
    return np.dot(Y, W.T)+mu

def normalize(X, low, high, dtype=None):
    X=np.asarray(X)
    minX , maxX = np.min(X), np.max(X)
    # normalize to [0...1].
    X=X-float(minX)
    X=X/float(( maxX - minX ))
    # scale to [ low ... high ].
    X=X*(high-low)
    X=X+low
    if dtype is None :
        return np.asarray(X)
    return np.asarray(X, dtype=dtype)

def create_font(fontname='Tahoma', fontsize=10):
    return {'fontname':fontname, 'fontsize':fontsize}

def subplot (title , images , rows , cols , sptitle ="subplot", sptitles =[] , colormap =cm.gray , ticks_visible =True , filename = None ):
    fig =plt.figure()
    # main title
    fig.text(.5,.95, title , horizontalalignment ='center')
    for i in range(len(images)):
        ax0=fig.add_subplot(rows,cols ,(i+1) )
        plt.setp(ax0.get_xticklabels(),visible = False )
        plt.setp(ax0.get_yticklabels(),visible = False )
        if len ( sptitles ) == len ( images ):
            plt.title ("%s #%s" % ( sptitle , str ( sptitles [i])), create_font ('Tahoma' ,10))
        else:
            plt.title ("%s #%d" % ( sptitle , (i +1)), create_font ('Tahoma' ,10))
        plt.imshow(np.asarray(images[i]), cmap=colormap)
    if filename is None :
        plt.show()
    else :
        fig.savefig(filename)


E = []
for i in range(min(len(X),16)):
    e = W[:,i].reshape(X[0].shape)
    E.append(normalize(e,0,255))
print(len(X))
#cv2.imwrite("s.jpg",E)
# plot them and store the plot to " python_eigenfaces .pdf"
subplot(title="Eigenfaces AT&T Facedatabase", images=E, rows=4, cols=4, sptitle ="Eigenvectors", sptitles="Eigenface", colormap=cm.jet, filename="python_pca_eigenfaces.png")
'''
steps=[i for i in range(10, min(len(X), 320), 20)]
E = []
for i in range(min(len(steps), 16)):
	numEvs = steps[i]
	P = project(W[:,0:numEvs], X[0].reshape(1,-1), mu)
	R = reconstruct(W[:,0:numEvs], P, mu)
	# reshape and append to plots
	R = R.reshape(X[0].shape)
	E.append(normalize(R,0,255))
# plot them and store the plot to "python_reconstruction.pdf"
subplot(title="Reconstruction AT&T Facedatabase", images=E, rows=4, cols=4, sptitle="Eigenvectors", sptitles=steps, colormap=cm.gray, filename="python_pca_reconstruction.pdf")'''