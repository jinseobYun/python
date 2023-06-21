import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Collision Detection by @TokyoEdtech")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

shapes = ["wizard.gif", "goblin1.gif", "pacman1.gif","pacman2.gif", "cherry1.gif", "bar7.gif","1floor.gif", "ball.gif", "x.gif","bar3.gif","0.gif","1.gif","2.gif","3.gif","gameover.gif","clear.gif"]

for shape in shapes:
    wn.register_shape(shape)


class Sprite():

## 생성자: 스프라이트의 위치, 가로/세로 크기, 이미지 지정

    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.dir = 1

## 스프라이트 메서드

# 지정된 위치로 스프라이트 이동 후 도장 찍기
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.shapesize(10,10,20)
        pen.stamp()
# 충돌 감지 방법 1: 두 스프라이트의 중심이 일치할 때 충돌 발생
    def is_overlapping_collision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

# 충돌 감지 방법 2: 두 스프라이트 사이의 거리가 두 객체의 너비의 평균값 보다 작을 때 충돌 발생
    def is_distance_collision(self, other):
        distance = (((self.x-other.x) ** 2) + ((self.y-other.y) ** 2)) ** 0.5
        if distance < (self.width + other.width)/2.0:
            return True
        else:
            return False

# 충돌 감지 방법 3: 각각의 스프라이트를 둘러썬 경계상자가 겹칠 때 충돌 발생
# aabb: Axis Aligned Bounding Box
    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
    
    # 자동으로 움직임
    def moving(self,speed = 0.6):
        self.x = self.x + (speed) * self.dir

class Character(Sprite):
    def __init__(self, x, y, width, height, image,jump=False):
        super().__init__(x, y, width, height, image)
        self.jump = jump
        self.state = False # 점프 상태
        self.contact = True
        self.dir = 1
        
        
    def hop(self, distance=200):
        if self.jump == True and self.state == False:
            self.y += distance
            self.state = True
            
            
    def direction(self):
        if self.dir == 1:
            self.image = "pacman1.gif"
            
        else:
            self.image = "pacman2.gif"    
        
    def graviti(self):
        
            if self.contact:
                self.y -= 0.7
                
            # 1층 블록 충돌판정
            if ((self.x >=-832 and self.x <=64) and (self.y <= -290 and self.y >=-300)):
                self.state = False
                self.contact = False   
                 
            # 2층 블록 충돌판정
            elif (((self.x >=64 and self.x <=440) or self.x >= 580) and (self.y <= -140 and self.y >=-150)):
                self.state = False
                self.contact = False
            
            # 3층 블록 충돌판정
            elif ((self.x >=-832 and self.x <=64) and (self.y <= 10 and self.y >=0)):
                self.state = False
                self.contact = False
            # 4층 블록 충돌판정
            elif (((self.x >=-440 and self.x <=440) or self.x >= 580) and (self.y <= 160 and self.y >=150)):
                self.state = False
                self.contact = False
            # 5층 블록 충돌판정
            elif (((self.x >=-832 and self.x <=64)) and (self.y <= 310 and self.y >=300)):
                self.state = False
                self.contact = False
            else:
                self.contact = True




wizard = Character(-720, 360, 128, 128, "wizard.gif")
goblin = Sprite(128, 160, 54, 64, "goblin1.gif")

pacman = Character(0, 0, 32, 32, "pacman1.gif", jump=True)
cherry = Sprite(720, 160, 128, 128, "cherry1.gif")
cherry2 = Sprite(720, -140, 128, 128, "cherry1.gif")
cherry3 = Sprite(-128, 160, 128, 128, "cherry1.gif")
score = Sprite(720,320,64,64,"0.gif")
gameover = Sprite(0,0,500,500,"gameover.gif")
clear = Sprite(0,0,692,361,"clear.gif")
#1층 블록
bar = Sprite(-384, -300, 889, 12, "bar7.gif")

#2층 블록
bar21 = Sprite(512, -150, 889, 12, "bar3.gif")
# bar22 = Sprite(-512, -150, 384, 12, "bar3.gif")
bar23 = Sprite(1024, -150, 384, 12, "bar3.gif")

#3층 블록
bar31 = Sprite(-384, 0, 889, 12, "bar7.gif")

#4층 블록
bar41 = Sprite(0, 150, 889, 12, "bar7.gif")
bar42 = Sprite(1024, 150, 384, 12, "bar3.gif")

#5층 블록
bar51 = Sprite(-384, 300, 889, 24, "bar7.gif")
# 스프라이트 모음 리스트
sprites = [wizard, goblin, pacman, cherry,cherry2,cherry3]

blocks = [bar,bar21,bar23,bar31,bar41,bar42,bar51,score]


# 팩맨 이동
def left():
    pacman.x -= 30
    pacman.dir = -1

# 팩맨 이동
def right():
    pacman.x += 30
    pacman.dir = 1

# 팩맨 점프
def jump_pacman(distance=200):
    pacman.hop(distance)




# 이벤트 처리
wn.listen()
wn.onkeypress(left, "Left")  # 왼쪽 방향 화살표 입력
wn.onkeypress(right, "Right") # 오른쪽 방향 화살표 입력
wn.onkeypress(jump_pacman, "Up") # 스페이크 키 입력
# wn.onkeypress(shoot_ball, "space") # 스페이크 키 입력
count = 0
scores = ["0.gif","1.gif","2.gif","3.gif"]
while True:

    # 각 스프라이트 위치 이동 및 도장 찍기
    for sprite in sprites:
        sprite.render(pen)
    for block in blocks:
        block.render(pen)
    pacman.graviti()
    pacman.direction()
    # 고블린 움직이기
    goblin.moving()
    if goblin.x >=448:
        goblin.dir = -1
    elif goblin.x <= -448:
        goblin.dir = 1


    if pacman.is_distance_collision(cherry):
        cherry.x = 1800
        count += 1
        score.image = scores[count]
    if pacman.is_distance_collision(cherry2):
        cherry2.x = 1800
        count += 1
        score.image = scores[count]
    if pacman.is_distance_collision(cherry3):
        cherry3.x = 1800
        count += 1
        score.image = scores[count]


    if pacman.is_distance_collision(goblin) or pacman.y <= -320:
        sprites = []
        blocks = []
        sprites.append(gameover)

    if  count == 3 and pacman.is_aabb_collision(wizard):
        sprites = []
        blocks = []
        sprites.append(clear)

    wn.update() # 화면 업데이트
    pen.clear() # 스프라이트 이동흔적 삭제 

