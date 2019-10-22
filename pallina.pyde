x=10
a=80
b=25
y=10
verx=1
very=1
ingrx=20
ingry=20
xrac=250     #("posizione racchetta 1")
yrac=250     #("posizione racchetta 2")

def keyPressed():
    global xrac,yrac
    if keyCode==LEFT:
        xrac=xrac-5
    if keyCode==RIGHT:
        xrac=xrac+5
    if xrac<0:
        xrac=xrac+5
    if xrac>width-80:
        xrac=xrac-5
    if key=="a":
        yrac=yrac-5
    if key=="d":
        yrac=yrac+5
    if yrac<0:
        yrac=yrac+5
    if yrac>width-80:
        yrac=yrac-5       

def setup():
    size(600,400)
    
def draw():
    global x,y,verx,very,ingrx,ingry
    background(0,0,100)
    ellipse(x,y,ingrx,ingry)
    rect(xrac,(height)-25,a,b)
    rect(yrac,(height)-400,a,b)
    x=x+2*verx
    y=y+2*very 
    
    if x>width or x<0:
        verx*=-1
        fill(random (255),random (255),random (255))
        
        
    
    if y>height or y<0:
        very*=-1
        fill(random (255),random (255),random (255))
        
    if y+ingry/2>(height)-25 and x+ingrx/2>xrac and x-ingrx/2<xrac+a:
        very=-1
        
    if y-ingry/2>b and x+ingrx/2>xrac and x-ingrx/2<xrac+a:      # ("la racchetta sopra non funziona")     
        very=-1     
