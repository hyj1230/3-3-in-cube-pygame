import pygame


class FontManager:
    def __init__(self):
        self.font_cache = {}
    
    def Font(self, name, size):
        if name in self.font_cache and size in self.font_cache[name]:
            return self.font_cache[name][size]
        if name not in self.font_cache:
            self.font_cache[name] = {}
        _font = pygame.font.Font(name, size)
        self.font_cache[name] = {}
        self.font_cache[name][size] = _font
        return _font



font_manager = FontManager()
def show_text(screen, text, color=(0, 0, 0), pos=(0, 0), size=30):
    screen.blit(font_manager.Font('方正达利体.ttf', size).render(text, True, color), pos)


def convert_sf(sf):   # sf -> surface
    return {
        'front': 1,
        'behind': 2,
        'left': 3,
        'right': 4,
        'on': 5,
        'under': 6,
    }[sf]


def calc_Block_number(x, y, surface):  # 计算格子的编号
    tens_place = (x*(surface+2) + y*(surface)) % 10  # 十位
    ones_place = (x*(surface) + y*(surface+2)) % 10  # 个位
    return str(tens_place) + str(ones_place)


class Block:  # 格子类（单个格子），这个功能很单一，可以简单理解为c++结构体的替代
    def __init__(self, x, y, sf, mode):  # x,y:当前格子xy, sf:当前格子在哪个面上 mode:当前格子类型
        self.position = {
            'x': x+1,
            'y': y+1,
            'surface': convert_sf(sf),  # 把字母形式的面（如right）转为数字形式面存储
        }
        self.number = calc_Block_number(self.position['x'], self.position['y'], self.position['surface'])
        self.mode = mode
        self.info = ''  # 储存传送门的传送地点
        self.wh = 200  # 宽高
        
        # 当格子是传送门时，mode 是 “goto-方向” 如 goto-left
        if '-' in self.mode:  # 如果这个格子是传送门
            tmp = self.mode.split('-')
            self.mode = tmp[0]  # 分割mode
            print(tmp[1])
            self.info = eval(tmp[1])  # 把最终方向保存进info里
        self.color = {  # 保存当前格子的颜色
            'normal': (127,255,212),
            'goto': (255,250,205),
            'finish': (255,228,225),
        } [self.mode]
        self.rect = pygame.Rect(250, 250, self.wh, self.wh)  # 保存当前格子的矩形
    def draw(self,pos,screen,tox,toy):#绘制
        fx={
            'center':[0,0],
            'left':[-1,0],
            'right':[1,0],
            'up':[0,-1],
            'down':[0,1],
            'upleft':[-1,-1],
            'upright':[1,-1],
            'downleft':[-1,1],
            'downright':[1,1],
        }
        self.rect.x+=((fx[pos][0]*self.wh)+tox)
        self.rect.y+=((fx[pos][1]*self.wh)+toy)
        pygame.draw.rect(screen,self.color,self.rect,0)#填充颜色
        pygame.draw.rect(screen,(88,88,91),self.rect,1)#绘制矩形边框
        show_text(screen,self.number,pos=(self.rect.centerx-35,self.rect.centery-30),size=60)#显示数字
        self.rect.x-=((fx[pos][0]*self.wh)+tox)
        self.rect.y-=((fx[pos][1]*self.wh)+toy)

class Cube:#立方体类
    def __init__(self,cubedata,startpos):#cubedata:当前关卡数据 startpos:起始位置
        self.data = cubedata.copy()#先拷贝一下关卡数据
        for sf in cubedata:#获取每个面
            for y in range(len(cubedata[sf])):#获取sf面的格子
                for x in range(len(cubedata[sf][y])):
                    self.data[sf][y][x] = Block(x,y,sf,cubedata[sf][y][x])
        self.x = startpos[0]#起始位置
        self.y = startpos[1]
    def move(self,to):#to:移动方向；这个函数是移动位置，这是最麻烦的部分
        if to == 'left':#向左移动
            self.x -= 1#x坐标减一
        elif to == 'right':#向右移动
            self.x += 1#x坐标加一
        elif to == 'up':#向上移动
            self.y -= 1#y坐标减一（这里和平面直角坐标系不一样，原点在左上角，向下为y轴正半轴
        else:#向下移动
            self.y += 1#y坐标加一
        if self.y >= len(self.data['front']):#当移到下边边缘，要换面
            self.rotate3d(to)#换面
            self.y = 0#将y坐标设为0(最顶上)
        if self.y < 0:#移到上边边缘
            self.rotate3d(to)#换面
            self.y = len(self.data['front']) - 1#y坐标设为长度-1(最下面)
        if self.x >= len(self.data['front'][self.y]):#移到右边边缘
            self.rotate3d(to)
            self.x = 0#把x坐标设为0（最左边）
        if self.x < 0:#移到左边边缘
            self.rotate3d(to)
            self.x = len(self.data['front'][self.y]) - 1#把x坐标设为长度-1（最右边）
    def rotate_array(self,matrix,isshun):
        if isshun:
            matrix = [list(row) for row in zip(*matrix)]
            for i in range(len(matrix)):
                matrix[i] = matrix[i][::-1]
        else:
            matrix = [list(row) for row in zip(*matrix[::-1])]
            matrix.reverse()
            for i in range(len(matrix)):
                matrix[i].reverse()
        return matrix
    def rotate3d(self,to):#改变立方体的面
        rotate_array=self.rotate_array
        if to == 'left':#往左移动，整体向右旋转，让正面替换左面，其他面以此类推
            self.data['right'], self.data['front'], self.data['left'], self.data['behind'] = \
            self.data['front'], self.data['left'], self.data['behind'], self.data['right']
            self.data['on']=rotate_array(self.data['on'],0)
            self.data['under']=rotate_array(self.data['under'],1)
        elif to == 'right':#往右移动，向左旋转
            self.data['front'], self.data['left'], self.data['behind'], self.data['right'] = \
            self.data['right'], self.data['front'], self.data['left'], self.data['behind']
            self.data['on']=rotate_array(self.data['on'],1)
            self.data['under']=rotate_array(self.data['under'],0)
        elif to == 'up':#往上移动，向下旋转
            self.data['front'], self.data['on'], self.data['behind'], self.data['under'] = \
            self.data['on'], self.data['behind'], self.data['under'], self.data['front']
            self.data['left']=rotate_array(self.data['left'],1)
            self.data['right']=rotate_array(self.data['right'],0)
        else:#往下移动，向上旋转
            self.data['on'], self.data['behind'], self.data['under'], self.data['front'] = \
            self.data['front'], self.data['on'], self.data['behind'], self.data['under']
            self.data['left']=rotate_array(self.data['left'],0)
            self.data['right']=rotate_array(self.data['right'],1)
    def get_mode(self):#获取当前格子的模式
        return self.data['front'][self.y][self.x].mode
    def get_data(self):#获取当前格子的模式
        return self.data['front'][self.y][self.x]
    def show(self,screen,tox,toy):#显示当前格子
        self.data['front'][self.y][self.x].draw('center',screen,tox,toy)
        self.move('left')
        self.data['front'][self.y][self.x].draw('left',screen,tox,toy)
        self.move('up')
        self.data['front'][self.y][self.x].draw('upleft',screen,tox,toy)
        self.move('down')
        self.move('down')
        self.data['front'][self.y][self.x].draw('downleft',screen,tox,toy)
        self.move('up')
        self.move('right')
        
        self.move('right')
        self.data['front'][self.y][self.x].draw('right',screen,tox,toy)
        self.move('up')
        self.data['front'][self.y][self.x].draw('upright',screen,tox,toy)
        self.move('down')
        self.move('down')
        self.data['front'][self.y][self.x].draw('downright',screen,tox,toy)
        self.move('up')
        self.move('left')
        
        self.move('up')
        self.data['front'][self.y][self.x].draw('up',screen,tox,toy)
        self.move('down')
        
        self.move('down')
        self.data['front'][self.y][self.x].draw('down',screen,tox,toy)
        self.move('up')