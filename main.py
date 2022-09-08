import cv2
import numpy as np

def mostraImagem(titulo, img):
    cv2.imshow(titulo, img)
    cv2.waitkey(0)

img = cv2.imread("cores.png")
mostraImagem("Original", img)
b,g,r = cv2.split(img)

lin,col,dim = img.shape
img3=np.zeros([lin,col*3,])
img3[0:lin,0:col]=b[0:lin,0:col]
img3[0:lin,col:2*col]=g
img3[0:lin,2*col:3*col]=r
#juntar as imagens
imagem= cv2.merge([b,g,r])
mostraImagem("Bandas Unidas", imagem)

#convertendo para cinza
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
mostraImagem("Cinza", gray)

img = cv2.imread("ayrton-senna.jpg")
mostraImagem("Original", img)

flipped = cv2.flip(img, 1)
mostraImagem("Horizontalmente", flipped)

flipped = cv2.flip(img, -1)
mostraImagem("Verticalmente ", flipped)

image = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
# cv2.ROTATE_180, cv2.ROTATE_90_COUNTERCLOCKWISE
mostraImagem("rotacionada", image)

lin,col,dim - img.shape
(cX, cY) = (lin // 2, col // 2)

M = cv2.getRotationMatrix2D((cX,cY), 45, 1.0)
rotated = cv2.warpAffine(img, M, (lin,col))
mostraImagem("Rotated by 45 Degrees", rotated)

#pixel a pixel
imagem = cv2.imread("halteres.jpg")
[col,lin,dim] = imagem.shape;
imagem2 = imagem.copy()
print('Tipo da Imagem:', imagem.dtype)
print('Tamanho em pixels da Imagem:')
print("linha= ",lin,"col= ", col)

for j in range(0, col-1):
    for i in range(0, lin-1):
        (b,g,r) = imagem[j, i]
        #print (b,g,r)
        #print (j,i) #i=linhas
        if(b>110 and b<255) and (g>80 and g<120) and (r>30 and r<80):
            b=255
            g=0
            r=0
            imagem2[j,i,]=np.array([b,g,r])
        else:
            imagem2[j,i,]=np.array([0,0,0])
imagem = cv2.hconcat([imagem,imagem2])
mostraImagem("halteres Alterado", imagem)

#Abre video gravado em disco
camera = cv2.VideoCapture('videocanetas.mp4')
#Também é possivel abrir a webcam com
#camera = cv2.VideoCapture(0)
outputFile = 'saida.avi'
(sucesso, frame) = camera.read()
vid_writer = cv2.VideoWriter(outputFile, cv2.VideoWriter_fourcc('M','J','P','G'), 60, (frame.shape[1],frame.shape[0]))
numero=1
while True:
    #read() retorna 1 se houve sucesso e 2 o proprio frame
    (sucesso, frame) = camera.read()
    if not sucesso: #fim do video
        break
#grava frame como imagem
    cv2.imwrite('nome'+str(numero)+'.jpg', frame)
    numero=numero+1

#converte para L*a*b e vai gravando vídeo em disco
    lab = cv2.cvtColor(frame, cv2.COLOR_RGB2Lab)
    vid_writer.write((lab).astype(np.uint8))

    #converte para greyscale
    #frame_pb = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Exibindo video", frame)
    #cv2.waitKey(0)
    #Espera que a tecla 'S" seja pressionada para sair
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break
vid_writer.release()
cv2.destroyAllWindows()