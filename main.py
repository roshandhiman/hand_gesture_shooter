import cv2
import mediapipe as mp
import pygame
import random
import math
import time

pygame.init()

WIDTH=1000
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("AI Gesture Shooter ULTRA")

mp_hands=mp.solutions.hands

hands=mp_hands.Hands(
max_num_hands=1,
min_detection_confidence=0.8,
min_tracking_confidence=0.8
)

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

score=0

class Target:

    def __init__(self):

        self.x=random.randint(100,WIDTH-100)
        self.y=random.randint(100,HEIGHT-100)

        self.r=random.randint(25,40)

        self.dx=random.choice([-3,-2,2,3])
        self.dy=random.choice([-3,-2,2,3])

        self.color=random.choice([
        (255,80,80),
        (80,255,120),
        (80,160,255),
        (255,220,80),
        (255,80,200)
        ])

    def move(self):

        self.x+=self.dx
        self.y+=self.dy

        if self.x<0 or self.x>WIDTH:
            self.dx*=-1

        if self.y<0 or self.y>HEIGHT:
            self.dy*=-1

    def draw(self):

        pygame.draw.circle(screen,self.color,(int(self.x),int(self.y)),self.r)

targets=[Target() for _ in range(6)]

smooth_x=WIDTH//2
smooth_y=HEIGHT//2

crosshair_x=WIDTH//2
crosshair_y=HEIGHT//2

alpha=0.15
deadzone=4

prev_tip_y=0

last_shot=0
cooldown=0.2

clock=pygame.time.Clock()

def draw_crosshair(x,y,hit):

    color=(255,50,50) if hit else (255,255,255)

    pygame.draw.line(screen,color,(x-15,y),(x-5,y),2)
    pygame.draw.line(screen,color,(x+5,y),(x+15,y),2)

    pygame.draw.line(screen,color,(x,y-15),(x,y-5),2)
    pygame.draw.line(screen,color,(x,y+5),(x,y+15),2)

    pygame.draw.circle(screen,color,(x,y),3)

running=True

while running:

    ret,frame=cap.read()

    frame=cv2.flip(frame,1)

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results=hands.process(rgb)

    if results.multi_hand_landmarks:

        hand=results.multi_hand_landmarks[0]

        tip=hand.landmark[8]

        tx=tip.x*WIDTH
        ty=tip.y*HEIGHT

        smooth_x+=alpha*(tx-smooth_x)
        smooth_y+=alpha*(ty-smooth_y)

        if abs(tx-crosshair_x)>deadzone:
            crosshair_x=int(smooth_x)

        if abs(ty-crosshair_y)>deadzone:
            crosshair_y=int(smooth_y)

        velocity=prev_tip_y-tip.y

        now=time.time()

        if velocity>0.09 and now-last_shot>cooldown:

            last_shot=now

            for t in targets:

                dist=math.hypot(crosshair_x-t.x,crosshair_y-t.y)

                if dist<t.r:

                    score+=1
                    targets.remove(t)
                    targets.append(Target())
                    break

        prev_tip_y=tip.y

    screen.fill((15,15,30))

    hit=False

    for t in targets:

        t.move()
        t.draw()

        if math.hypot(crosshair_x-t.x,crosshair_y-t.y)<t.r:

            hit=True

    draw_crosshair(crosshair_x,crosshair_y,hit)

    font=pygame.font.SysFont("Arial",28)

    txt=font.render("Score: "+str(score),True,(255,255,255))

    screen.blit(txt,(20,20))

    pygame.display.update()

    for e in pygame.event.get():

        if e.type==pygame.QUIT:
            running=False

    clock.tick(60)

cap.release()
pygame.quit()
