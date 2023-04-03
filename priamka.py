from PIL import Image

pic = Image.new("RGB", (300,300), 'white')
pixels = pic.load()
A = (10, 150)
B = (10, 15)

#ak to je zvislá čiara
if A[0]==B[0] and A[1]<B[1]:
    for y in range(A[1],B[1]):
        x = A[0]
        pixels[x, y] = (0, 0, 0)

if A[0]==B[0] and A[1]>B[1]:
    for y in range(B[1],A[1]):
        x = A[0]
        pixels[x, y] = (0, 0, 0)

if A[0]==B[0] and A[1]==B[1]:
        x = A[0]
        y = A[1]
        pixels[x, y] = (0, 0, 0)

#ak to ide z ľava do prava
elif A[0]<B[0]:
    k = (B[1]-A[1])/(B[0]-A[0])
    q = A[1]-k*A[0]
    for x in range(A[0],B[0]):
        y = int(k*x+q)
        pixels[x, y]=(0,0,0)

#ak to ide z prava do ľava
elif A[0]>B[0]:
    k = (A[1] - B[1]) / (A[0] - B[0])
    q = B[1] - k * B[0]
    for x in range(B[0], A[0]):
        y = int(k * x + q)
        pixels[x, y] = (0, 0, 0)

pic.show()
