x=500          #("lunghezza pallina spawn")
a=80           #("lunghezza racchetta")
b=25           #("spessore racchetta")
y=100          #("altezza pallina spawn")
verx=1          #("verso pallina lunghezza")
very=1          #("verso pallina altezza")
ingrx=20
ingry=20
xrac=300         #("posizione racchetta 1")
yrac=300        #("posizione racchetta 2")
score1=0        #("punteggio 1")
score2=0        #("punteggio 2")
start=0         #("timer")
 
## Prof.: Da qui in poi nessun commento: scarsa leggibilità
def setup():
    start = millis()
            
def keyPressed():
    global xrac,yrac
    if keyCode==LEFT:
        xrac=xrac-5
    if keyCode==RIGHT:
        xrac=xrac+5
## Prof.: sposta la racchetta solo se non tocca i bordi e il comando è quello corretto
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
    size(800,600)
    
def draw():
    global x,y,verx,very,ingrx,ingry,score1,score2
    background(100,100,100)
    ellipse(x,y,ingrx,ingry)
    rect(xrac,(height)-25,a,b)
    rect(yrac,(height)-600,a,b)
    x=x+2*verx
    y=y+2*very 
    text("SCORE 1:",10,(height)-25)
    text("SCORE 2:",10,40) 
    text(score2,70,(height)-25)
    text(score1,70,40)
    stroke(255)
    line(800,300,0,300)
    timer = millis () - start
    text (timer, 10,290);
    if timer>=100000:
     textSize(50)
     text("GAME OVER",300,400)
    
   
    if x>=width or x<=0:
        verx*=-1
        fill(random (255),random (255),random (255))
   
        
    if y>=height or y<=0:
        very*=-1
        fill(random (255),random (255),random (255))
        
    if y+ingry/2>(height)-25 and x+ingrx/2>xrac and x-ingrx/2<xrac+a:
        very=-1
        
    if y-ingry/2<=(height)-575 and x+ingrx/2>=yrac and x-ingrx/2<=yrac+a:
        very*=-1 
        
        
    if y==height:
       score1+=1
        
    if y==0:
        score2+=1
        
## Prof.: Cosa è questa funzione???        
    def keyPressed():
     if key=="r":
      return
    
