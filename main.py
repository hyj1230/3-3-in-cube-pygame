#这个代码是我初期的代码风格，有那么亿点点乱，现在我自己都看不懂了
import pygame
import sys
from gamedata import gamedata
from game import *
import time

pygame.init()
width,height=1200,674
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('纸中立方 (3^3 in cube)')
levelindex = 1
leveldata = gamedata(levelindex)
cube = Cube(leveldata,(0,0))
n_down = False


def draw_alpha_rect(window, color, alpha, rect, border_radius):
    rect_surface = pygame.Surface((rect.width, rect.height), flags=pygame.SRCALPHA).convert_alpha()
    pygame.draw.rect(rect_surface, color, (0, 0, *rect.size), border_radius=border_radius)
    rect_surface.set_alpha(alpha)
    window.blit(rect_surface, (rect.x*2, rect.y*2))


def draw_alpha_rect_new(surface, color, rect: pygame.Rect, border_radius):
    rect_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(rect_surface, color, (0, 0, *rect.size), border_radius=border_radius)
    screen.blit(sf, rect.topleft)

def draw_circle_alpha():
    surface = pygame.Surface((600, 600), pygame.SRCALPHA)
    rect = surface.get_rect(center=(350, 350))
    surface.fill((63,0xbb,0xd0))
    # 在 Surface 对象上画一个白色的圆
    pygame.draw.circle(surface, pygame.Color("white"), (300, 300), 150)
    
    # 设置 Surface 对象中圆的部分为透明
    surface.set_colorkey(pygame.Color("white"))
    
    # 将 Surface 对象绘制到屏幕上
    screen.blit(surface, rect)
def draw_mb_alpha():
    surface1 = pygame.Surface((1200, 700), pygame.SRCALPHA)
    rect = surface1.get_rect(center=(350, 350))
    surface1.fill((29,83,0xbb))
    draw_alpha_rect(surface1,(63,0xbb,0xd0),100,pygame.Rect(153,28,600,600),30)
    pygame.draw.rect(surface1, pygame.Color("white"), pygame.Rect(300, 50,600,600),border_radius=30)
    surface1.set_colorkey(pygame.Color("white"))
    screen.blit(surface1, rect)

def draw_line_fill(p1,llong,color):
    p2=(p1[0]+llong,p1[1])
    p3=(p1[0]+llong,p1[1]+llong)
    p4=(p1[0],p1[1]+llong)
    pygame.draw.polygon(screen, color, [p1,p2,p3,p4])
    pygame.draw.aalines(screen, (0,0,0), True, [p1,p2,p3,p4])

def draw_rect(cube, llong, x, y):
    data=cube.data
    for i in range(len(data['front'])):
        for j in range(len(data['front'][0])):
            draw_line_fill((y+j*llong,x+i*llong), llong, data['front'][i][j].color)
            show_text(screen,str(data['front'][i][j].number),pos=((y+j*llong+((llong-35)//2)) ,(x+i*llong+((llong-30)//2))),size=30)
            if i==cube.y and j==cube.x:
                pygame.draw.rect(screen,(29,83,0xbb),pygame.Rect(y+j*llong+20,x+i*llong+20,llong-40,llong-40))

def gethelp():
    npc=[]
    for i in range(1,10):
        npc.append(pygame.image.load('npc'+str(i)+'.png'))
    alpha_pic=255
    pic_num=0
    isalpha=0
    alpha_out=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_alpha_rect(screen,(29,83,0xbb),255,pygame.Rect(0,0,1200,674),0)
        draw_alpha_rect(screen,(0,0,0),20,pygame.Rect(0,150,1200,200),0)
        show_text(screen,'纸中立方',pos=(300,60),color=(255,255,255),size=150)
        screen.blit(next_level,(1000,360))
        next_rect=pygame.Rect(1000,350,75,75)
        show_text(screen,'点击跳过',(255,255,255),(1000,350+75+10),20)
        pos=pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if next_rect.collidepoint(pos[0],pos[1]):
                return
        if alpha_out:
            pygame.time.delay(20)
            alpha_out=0
            pic_num+=1
            isalpha=0
            alpha_pic=255
            if pic_num==9:
                return
        if isalpha and not alpha_out:
            alpha_pic-=8
            npc[pic_num].set_alpha(alpha_pic)
            screen.blit(npc[pic_num],(250,330))
            npc[pic_num].set_alpha(255)
            if alpha_pic-8<0:
                pygame.display.update()
                pygame.time.delay(10)
                alpha_out=1
            pygame.time.delay(10)
        if not isalpha:
            screen.blit(npc[pic_num],(250,330))
            if pygame.mouse.get_pressed()[0]:
                isalpha=1
        pygame.display.update()
def gethelp1():
    npc=[]
    for i in [1,2,3,4,5,8,9]:
        npc.append(pygame.image.load('npc'+str(i)+'.png'))
    alpha_pic=255
    pic_num=0
    isalpha=0
    alpha_out=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_alpha_rect(screen,(29,83,0xbb),255,pygame.Rect(0,0,1200,674),0)
        draw_alpha_rect(screen,(0,0,0),20,pygame.Rect(0,150,1200,200),0)
        next_level=pygame.image.load('next.png').convert_alpha()
        show_text(screen,'纸中立方',pos=(300,60),color=(255,255,255),size=150)
        screen.blit(next_level,(1000,360))
        next_rect=pygame.Rect(1000,350,75,75)
        show_text(screen,'点击跳过',(255,255,255),(1000,350+75+10),20)
        pos=pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if next_rect.collidepoint(pos[0],pos[1]):
                return
        if alpha_out:
            pygame.time.delay(20)
            alpha_out=0
            pic_num+=1
            isalpha=0
            alpha_pic=255
            if pic_num==7:
                return
        if isalpha and not alpha_out:
            alpha_pic-=8
            npc[pic_num].set_alpha(alpha_pic)
            screen.blit(npc[pic_num],(250,330))
            npc[pic_num].set_alpha(255)
            if alpha_pic-8<0:
                pygame.display.update()
                pygame.time.delay(10)
                alpha_out=1
            pygame.time.delay(10)
        if not isalpha:
            screen.blit(npc[pic_num],(250,330))
            if pygame.mouse.get_pressed()[0]:
                isalpha=1
        pygame.display.update()
def getlevel(level,canzb):
    leveldata = gamedata(level)
    '''if level==0:
        cube=Cube(leveldata,(0,0))'''
    cube=Cube(leveldata,(0,0))
    move_block=None
    move_num=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and move_block==None:
                if event.key == pygame.K_LEFT:
                    move_block='left'
                elif event.key == pygame.K_RIGHT:
                    move_block='right'
                elif event.key == pygame.K_UP:
                    move_block='up'
                elif event.key == pygame.K_DOWN:
                    move_block='down'
                elif event.key == pygame.K_n:
                    if cube.get_mode()=='finish':
                        image=pygame.image.load('成功.png').convert_alpha()
                        draw_alpha_rect(screen,(0,0,0),180,pygame.Rect(100,50,800,400),30)
                        screen.blit(image,(200,15))
                        again=pygame.image.load('again.png').convert_alpha()
                        next_level=pygame.image.load('next.png').convert_alpha()
                        home=pygame.image.load('home.png').convert_alpha()
                        screen.blit(again,(800,150))
                        screen.blit(next_level,(800,270))
                        screen.blit(home,(800,270+120))
                        again_rect=pygame.Rect(800,150,75,75)
                        next_rect=pygame.Rect(800,270,75,75)
                        home_rect=pygame.Rect(800,270+120,75,75)
                        while 1:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            pos=pygame.mouse.get_pos()
                            if pygame.mouse.get_pressed()[0]:
                                if again_rect.collidepoint(pos[0],pos[1]):
                                    leveldata=gamedata(level)
                                    cube=Cube(leveldata,(0,0))
                                    break
                                elif next_rect.collidepoint(pos[0],pos[1]):
                                    try:
                                        level+=1
                                        leveldata=gamedata(level)
                                        cube=Cube(leveldata,(0,0))
                                        break
                                        #print(leveldata)
                                    except:
                                        return 
                                elif home_rect.collidepoint(pos[0],pos[1]):
                                    return
                            pygame.display.update()
                    elif cube.get_mode()=='goto':
                        info = cube.data['front'][cube.y][cube.x].info#获取格子传送位置
                        if info[0] == 'behind':#传送到背面（相对当前面）
                            cube.rotate3d('up')
                            cube.rotate3d('up')
                        elif info[0] in ['left','right','up','down']:#传送到其他面
                            cube.rotate3d(info[0])#直接换面
                        cube.x, cube.y = info[1], info[2]    
        draw_alpha_rect(screen,(29,83,0xbb),255,pygame.Rect(0,0,1200,674),0)
        if move_block!=None:
            move_num+=50
            if move_num==200:
                move_num=0
                move_block=None
            if move_block=='left':
                if move_num<100:
                    cube.show(screen,move_num,0)
                elif move_num==100:
                    cube.show(screen,move_num,0)
                    cube.move('left')
                else:
                    cube.show(screen,-(200-move_num),0)
            elif move_block=='right':
                if move_num<100:
                    cube.show(screen,-move_num,0)
                elif move_num==100:
                    cube.show(screen,-move_num,0)
                    cube.move('right')
                else:
                    cube.show(screen,200-move_num,0)
            elif move_block=='up':
                if move_num<100:
                    cube.show(screen,0,move_num)
                elif move_num==100:
                    cube.show(screen,0,move_num)
                    cube.move('up')
                else:
                    cube.show(screen,0,-(200-move_num))   
            else:
                if move_num<100:
                    cube.show(screen,0,-move_num)
                elif move_num==100:
                    cube.show(screen,0,-move_num)
                    cube.move('down')
                else:
                    cube.show(screen,0,200-move_num)  
        else:
            cube.show(screen,0,0)
        draw_circle_alpha()
        draw_mb_alpha()
        ch={
            'left':'左',
            'right':'右',
            'behind':'背',
            'up':'上',
            'down':'下',
        }
        if cube.get_mode()=='goto':
            show_text(screen,"提示：按N键可以传送到"+ch[cube.get_data().info[0]]+"面",(255,255,255),(60,550),40)
        if cube.get_mode()=='finish':
            show_text(screen,"提示：按N键进入下一关",(255,255,255),(60,550),48)
        show_text(screen,"第"+str(level)+'关',(255,255,255),(60,60),48)
        again=pygame.image.load('again.png').convert_alpha()
        next_level=pygame.image.load('next.png').convert_alpha()
        home=pygame.image.load('home.png').convert_alpha()
        draw_alpha_rect(screen,(0xfc,0xaf,0x7b),100,pygame.Rect(350+3,280+3,420,95),border_radius=30)
        draw_alpha_rect(screen,(0xfc,0xaf,0x7b),255,pygame.Rect(350,280,420,95),border_radius=30)
        
        screen.blit(again,(750,570))
        screen.blit(next_level,(870,570))
        screen.blit(home,(870+120,570))
        again_rect=pygame.Rect(750,570,75,75)
        next_rect=pygame.Rect(870,570,75,75)
        home_rect=pygame.Rect(870+120,570,75,75)
        draw_alpha_rect(screen,(0x3b,0xc4,0xb1),100,pygame.Rect(350+3,30+3,420,480),border_radius=30)
        draw_alpha_rect(screen,(0x3b,0xc4,0xb1),255,pygame.Rect(350,30,420,480),border_radius=30)
        if canzb:
            show_text(screen,'作弊模式专享：',color=(255,255,255),pos=(730,100),size=36)
            if level==5:
                draw_rect(cube,70,170,750)
            else:
                draw_rect(cube,100,190,760)
        else:
            show_text(screen,'当前不是作弊模式',color=(255,255,255),pos=(730,100),size=30)
            show_text(screen,'所以无法使用',color=(255,255,255),pos=(730,143),size=30)
            show_text(screen,'但是可以点个赞支持一下吗？',color=(255,255,255),pos=(730,143+43),size=30)
            show_text(screen,'原作者：',color=(255,255,255),pos=(730,143+43+43),size=30)
            head_xx=pygame.image.load('friend.png').convert_alpha()
            screen.blit(head_xx,(880,143+43+43))
            show_text(screen,'有思想的不定积分',color=(255,255,255),pos=(880,143+43+43+100+10),size=20)
            show_text(screen,'改编作者：',color=(255,255,255),pos=(730,143+43+43+100+40),size=30)
            show_text(screen,'hyj1230',color=(255,255,255),pos=(880+20,143+43+43+100+40+50+10),size=40)
            show_text(screen,'部分图片素材来源于共创世界POCO的《超阀》',color=(255,255,255),pos=(730,143+43+293+28),size=18)
        pos=pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if again_rect.collidepoint(pos[0],pos[1]):
                pygame.time.delay(100)
                leveldata=gamedata(level)
                cube=Cube(leveldata,(0,0))
            elif next_rect.collidepoint(pos[0],pos[1]):
                pygame.time.delay(100)
                try:
                    level+=1
                    leveldata=gamedata(level)
                    cube=Cube(leveldata,(0,0))
                except:
                    return
            elif home_rect.collidepoint(pos[0],pos[1]):
                return
        
        pygame.display.update()
        if move_block!=None:
            pygame.time.delay(10)

_start_time = time.time()
clock = pygame.time.Clock()
while True:
    if time.time() - _start_time >= 3:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    x = y = 10
    show_text(screen,'原作者：有思想的不定积分', color=(255, 255, 255), pos=(x, y), size=60)
    show_text(screen,'改编作者：hyj1230', color=(255, 255, 255), pos=(x, y+80), size=60)
    show_text(screen,'注：本作部分图片素材来自ccw的POCO的《超阀》', color=(255, 255, 255), pos=(x, y+2*80), size=45)
    show_text(screen,'如有侵权请告知删除', color=(255, 255, 255), pos=(x, y+3*80), size=45)
    pygame.display.update()
    clock.tick(30)


bg = pygame.image.load('./背景.png').convert_alpha()
title = pygame.image.load('./标题.png').convert_alpha()
next_level = pygame.image.load('next.png').convert_alpha()
level = None


class MaskSurface:
    def __init__(self):
        self.mask_surface = pygame.Surface((1200,674), pygame.SRCALPHA).convert_alpha()
        self.start_time = None
        self.active = False
    
    def start_anim(self):
        self.start_time = time.time()
        self.active = True
    
    def display(self, surface):
        current_time = time.time()
        if self.active and current_time - self.start_time > 2:
            self.active = False
            if level==0:
                gethelp()
                getlevel(1,1)
            else:
                gethelp1()
                getlevel(1,0)
            pygame.display.update()
            hover_button.active = True
        
        if self.active:
            self.mask_surface.fill((29, 83, 0xbb, int((current_time - self.start_time) / 2 * 255)))
            surface.blit(self.mask_surface, (0, 0))

class PopWindow:
    def __init__(self):
        self.active = False
        self.start_time = None
    
    def open(self):
        self.active = True
        self.start_time = time.time()
    
    def close(self):
        self.active = False
        self.start_time = None
        
    @property
    def open_anim_done(self):
        return self.active and (time.time() - self.start_time) * 2 * 255 > 180
    
    def display(self, screen):
        if not self.active:
            return 
        current_time = time.time()
        anim_progress = min((current_time - self.start_time) * 2, 1)
        alpha = int(anim_progress * 255)
        
        draw_alpha_rect(screen,(0,0,0),40,pygame.Rect(180+3,120+3,500,300),20)
        draw_alpha_rect(screen,(88,88,91),alpha,pygame.Rect(180,120,500,300),20)
        if alpha>=180:
            show_text(screen,'是否开启作弊',pos=(400,270),size=40)
            show_text(screen,'是',pos=(400,410),size=40)
            show_text(screen,'否',pos=(700,410),size=40)
            show_text(screen,'X',color=(255,0,0),pos=(800,270),size=20)
                    

class HoverButton:
    def __init__(self):
        self.button = pygame.image.load('./征途.png').convert_alpha()
        self.button_hover = pygame.image.load('./征途2.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.button)
        self.rect = self.button.get_rect(x=616, y=253)
        
        self.active = True
    
    def display(self, surface, mouse_x, mouse_y, offset_x, offset_y):
        if self.collidepoint(mouse_x, mouse_y):
            surface.blit(self.button_hover, (self.rect.x+offset_x-15, self.rect.y+offset_y-164))
        else:
            surface.blit(self.button, (self.rect.x+offset_x, self.rect.y+offset_y))

    def collidepoint(self, mouse_x, mouse_y):
        return self.active and self.rect.collidepoint(mouse_x, mouse_y) and self.mask.get_at((mouse_x-self.rect.x, mouse_y-self.rect.y))


bgx = bgy = 0
hover_button = HoverButton()
pop_window = PopWindow()
mask_surface = MaskSurface()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hover_button.collidepoint(*event.pos):
                hover_button.active = False
                pop_window.open()
            if pop_window.active and pop_window.open_anim_done:
                close_button = pygame.Rect(800,270,20,20)
                yes_button = pygame.Rect(400,410,40,40)
                no_button = pygame.Rect(700,410,40,40)
                if close_button.collidepoint(event.pos):
                    pop_window.close()
                    hover_button.active = True
                elif yes_button.collidepoint(event.pos):
                    pop_window.close()
                    hover_button.active = False
                    level=0
                    mask_surface.start_anim()
                elif no_button.collidepoint(event.pos):
                    pop_window.close()
                    hover_button.active = False
                    level=1
                    mask_surface.start_anim()
                

    mouse_x, mouse_y = pygame.mouse.get_pos()
    offset_x,offset_y = -(mouse_x-600)*0.03, -(mouse_y-674/2)*0.03
    screen.blit(bg, (-25+offset_x,-14+offset_y))
    screen.blit(title, (-56+offset_x,-75+offset_y))

    hover_button.display(screen, mouse_x, mouse_y, offset_x, offset_y)
    pop_window.display(screen)
    mask_surface.display(screen)
            
    clock.tick(100)
    pygame.display.update()
