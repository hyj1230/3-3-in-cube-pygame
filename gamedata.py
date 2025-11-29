'''
         -------
        / 上面 /|
       /      / |
      --------右|
      |      |面/
      | 正面 | /
      |      |/
      --------
在以下的列表里，是如下格式，代表立方体每一个面的格子
-------------------
|格子类型|格子类型|...
|格子类型|格子类型|...
...
-------------------
其中 normal表示普通格子
finish是终点的格子
goto是传送门格子，可以把你传送到某个面的对应点上
'''

def gamedata(levelindex):  # 获取地图数据
    leveltest = {  # 测试关
        'front': [['normal',],],  # 正面
        'behind': [['normal',],],  # 背面
        'left': [['normal',],],  # 左面
        'right': [['normal',],],  # 右面
        'on': [['normal',],],  # 上面
        'under': [['normal',],],  # 下面
    }
    level1 = {
        'front': [
            ['normal','normal','normal',],
            ['normal','normal','normal',],
        ],
        'behind': [
            ['normal','normal','normal',],
            ['normal','finish','normal',],
        ],
        'left': [
            ['normal',],
            ['normal',],
        ],
        'right': [
            ['normal',],
            ['normal',],
        ],
        'on': [
            ['normal','normal','normal',],
        ],
        'under': [
            ['normal','normal','normal',],
        ],
    }
    
    level2 = {
        'front': [
            ['normal','normal',],
            ['normal','normal',],
        ],
        'behind': [
            ['normal','normal',],
            ['normal','normal',],
        ],
        'left': [
            ['normal','normal',],
            ['normal','normal',],
        ],
        'right': [
            ['normal','finish',],
            ['normal','normal',],
        ],
        'on': [
            ['normal','normal',],
            ['normal','normal',],
        ],
        'under': [
            ['normal','normal',],
            ['normal','normal',],
        ],
    }
    level3 = {
        'front': [
            ['normal','normal',],
            ['normal',"goto-['behind',0,1]",],
        ],
        'behind': [
            ['normal','normal',],
            ['normal','finish',],
        ],
        'left': [
            ['normal','normal',],
            ['normal','normal',],
        ],
        'right': [
            ['normal','normal',],
            ['normal','normal',],
        ],
        'on': [
            ['normal','normal',],
            ['normal','normal',],
        ],
        'under': [
            ['normal','normal',],
            ['normal','normal',],
        ],
    }
    level4 = {
        'front': [
            ['normal','normal','normal',],
            ['normal','normal','normal',],
            ['normal',"goto-['behind',0,1]",'normal',],
        ],
        'behind': [
            ['normal','normal','normal',],
            ['normal','finish','normal',],
            ['normal','normal','normal',],
        ],
        'left': [
            ['normal','normal','normal',],
            ['normal','normal','normal',],
            ['normal','normal','normal',],
        ],
        'right': [
            ['normal','normal','normal',],
            ['normal','normal','normal',],
            ['normal','normal','normal',],
        ],
        'on': [
            ['normal','normal','normal',],
            ['normal','normal','normal',],
            ['normal','normal','normal',],
        ],
        'under': [
            ['normal','normal','normal',],
            ['normal','normal','normal',],
            ['normal','normal','normal',],
        ],
    }
    level5 = {
        'front': [
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal',"goto-['right',0,0]",'normal','normal','normal',],
            ['normal',"goto-['behind',0,1]",'normal','normal','normal',],
            ['normal',"goto-['up',0,0]",'normal','normal','normal',],
        ],
        'behind': [
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','finish','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
        ],
        'left': [
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
        ],
        'right': [
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
        ],
        'on': [
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
        ],
        'under': [
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
            ['normal','normal','normal','normal','normal',],
        ],
    }
    levels = [
        leveltest,
        level1,
        level2,
        level3,
        level4,
        level5,
    ]
    return levels[levelindex]