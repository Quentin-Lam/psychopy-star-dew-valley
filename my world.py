#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author: Quentin Lam
# date: 2022.03.21
# 用Psychopy呈现花里胡哨的刺激

from psychopy import visual, core, event, monitors, sound
import os
from psychopy.hardware import keyboard

try:
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
except:
    print('工作路径出错，请粘贴exp_code文件位置至path变量后，或更改路径中的“\\”为“/”')
else:
    print('本程序开始运行……')

# Set up the monitor parameters, so we can use 'deg' as the screen units
# 呈现动态的psychopy图标
testMonitor = monitors.Monitor("HUAWEI", distance=57.0, width=32.0)
testMonitor.setSizePix([1280, 800])
# Open a window
win = visual.Window([800, 600],monitor=testMonitor, color = (-1,-1,-1), units="deg")
myMouse = event.Mouse()
# sound.Sound.backend_ptb.SoundPTB() 

# 0.1 加载游戏（呈现3D的部分hhh）
# Prepare a Gabor in memory
gabor = visual.GratingStim(win, tex="sin", mask="gauss", size=7.0, ori=45.0)
pre_text = visual.TextStim(win=win, text=u"游戏加载中，请稍候……", pos = (0, -5))
pre_text2 = visual.TextStim(win=win, text=u"游戏已加载完毕，按任意键开始游戏", pos = (-1, -5))
dtimer = core.CountdownTimer(2)
while not event.getKeys():
# Draw the Gabor on screen
# 加载游戏部分（degug阶段暂时注释掉）
    while dtimer.getTime()>0:
        # text_2.text = str(int(dtimer.getTime()))
        gabor.draw()
        pre_text.draw()
        # Update the phase following each screen refresh
        gabor.phase += 0.05
        win.flip()
    pre_text2.draw()
    gabor.draw()
    win.flip()


# 0.9 游戏开始，播放音乐
bgm = sound.Sound('Pelican Town.wav')
bgm.play()



# 1.0 选择性别
pic_male = visual.ImageStim(win, image = 'male2.png', size=(20,40),pos=(-380, -280), units='pix')
pic_female = visual.ImageStim(win, image = 'female2.png', size=(20,40),pos=(-380, -280), units='pix')
pic_bkg = visual.ImageStim(win, image = '星露谷.png', size = (800,600), units='pix')
gender_text = visual.TextStim(win=win, text=u"欢迎来到星露谷，请选择你的性别\n\nF             M",font='SourceHanSansCN-Normal-2.otf', pos = (0, 0), bold=True, color=[0.20,0.043, 0.055], colorSpace='rgb')
# gender_text.fontfile = ['C:/Windows/Fonts/HarmonyOS_Sans_SC_Regular.ttf']
# gender_text.font = 'HarmonyOS_Sans_SC_Regular.ttf'
pic_bkg.draw()
gender_text.draw()
win.flip()

gender_list = event.waitKeys(keyList = ['f','m'])
female_text = visual.TextStim(win=win, text=u'OK，这是你，Lucia，不知道你看到了没，你在屏幕的左下角，\n这里风景很好，想不想到处走走？试试按键盘上的方向键',height=0.7, bold=True,  pos = (-2, 1), color=[0.20,0.043, 0.055], colorSpace='rgb')
male_text = visual.TextStim(win=win, text=u'OK，这是你，Roger，不知道你看到了没，你在屏幕的左下角，\n这里风景很好，想不想到处走走？试试按键盘上的方向键',height=0.7, bold=True,  pos = (-2, 1), color=[0.20,0.043, 0.055], colorSpace='rgb')
if gender_list[0] == 'f':
    you = pic_female
    intro_text = female_text
if gender_list[0] == 'm': 
    you = pic_male  
    intro_text = male_text

pic_bkg.draw()
you.draw()
intro_text.draw()
win.flip()

rect1=visual.Rect(win, pos=(0,0),width=20,height=15, lineColor=None, fillColor=None, opacity = 0) # 侦测鼠标点击的透明背景板    




# 2 控制人物移动
# move_list = event.waitKeys(keyList = [38, 40, 37, 39])# 上下左右
kb = keyboard.Keyboard()
kb.start()
keylist = ['left', 'right', 'up', 'down']
# 一些地点的坐标
barrier = (0,-150)
berry = (-260, -170)
Mary = (-150,-230)
house = (20, 0)
door = (70, -230)
Bartlett = (150, -240)
crystal = (-180, -40)
hatchet = (-60, 140)
house_pic = visual.ImageStim(win, image = 'house.png', size=(700,700),pos=(0,0), units='pix')
rect1=visual.Rect(win, pos=(0,0),width=20,height=15, lineColor=None, fillColor=None, opacity = 0) # 侦测鼠标点击的透明背景板
global in_house
in_house = 0

berry_num = 0
key_num = 0
# key_num = 1 # debug阶段开钥匙
hatchet_num = 0



while -300 < you.pos[1] < 300 and -400 < you.pos[0] < 400:
    # while you.pos[0] != berry[0] or you.pos[1] != berry[1]:
    keys = kb.waitKeys(keyList=keylist)
    if you.size[0] != 40:
        for key in keys:
            if key.name == 'up':
                you.pos += (0,10)
                # print(you.pos)
            if key.name == 'down':
                you.pos += (0,-10)
                # print(you.pos)
            if key.name == 'left':
                you.pos += (-10,0)
                # print(you.pos)
            if key.name == 'right':
                you.pos += (10,0)
                # print(you.pos)  
            pic_bkg.draw()
            you.draw()
            win.flip()   
    else:         
        for key in keys:
            if key.name == 'up':
                you.pos += (0,20)
                # print(you.pos)
            if key.name == 'down':
                you.pos += (0,-20)
                # print(you.pos)
            if key.name == 'left':
                you.pos += (-20,0)
                # print(you.pos)
            if key.name == 'right':
                you.pos += (20,0)
                # print(you.pos)  
            house_pic.draw()
            you.draw()
            win.flip()
# 3. 和浆果丛互动
    if you.pos[0] == berry[0] and you.pos[1] == berry[1]:
        berry_text = visual.TextStim(win=win, text=u'选项：[P]收集，[C]砍伐', pos = (0, -7), height=0.6)
        pic_bkg.draw()
        you.draw()
        berry_text.draw()
        win.flip()
        berry_list = ['left', 'right', 'up', 'down', 'p', 'c']
        
        while you.pos[0] == berry[0] and you.pos[1] == berry[1]:
            keys = kb.waitKeys(keyList=berry_list)
            for key in keys:
                if key.name == 'p':
                    berry_num += 1
                    berry_text2 = visual.TextStim(win=win, text=(f'已采摘树莓：{berry_num}' ), pos = (0, -7), height=0.6)
                    pic_bkg.draw()
                    you.draw()
                    berry_text2.draw()
                    win.flip()
                    core.wait(1)
                if key.name == 'c':
                    if hatchet_num == 0:
                        berry_text3 = visual.TextStim(win=win, text=u'缺乏道具：斧头', pos = (0, -7), height=0.6)
                        pic_bkg.draw()
                        you.draw()
                        berry_text3.draw()
                        win.flip()
                        core.wait(1)
                    if hatchet_num > 0:
                        berry_num += 10
                        berry_text3 = visual.TextStim(win=win, text=(f'已采摘树莓：{berry_num}'), pos = (0, -7), height=0.6)
                        pic_bkg.draw()
                        you.draw()
                        berry_text3.draw()
                        win.flip()
                        core.wait(1)
                if key.name == 'up':
                    you.pos += (0,10)
                    # print(you.pos)
                if key.name == 'down':
                    you.pos += (0,-10)
                    # print(you.pos)
                if key.name == 'left':
                    you.pos += (-10,0)
                    # print(you.pos)
                if key.name == 'right':
                    you.pos += (10,0)
                    # print(you.pos)  
                pic_bkg.draw()
                you.draw()
                win.flip() 

        # 4. 和玛丽互动
        
    elif you.pos[0] == Mary[0] and you.pos[1] == Mary[1]:
        Mary_list = ['left', 'right', 'up', 'down', 't', 'g']   
        dialog_pic = visual.ImageStim(win, image = '对话框.png', size=(700,320),pos=(-20, -200), units='pix')
        mary_pic = visual.ImageStim(win, image = 'mary2.png', size=(130,150),pos=(190, -155), units='pix')
        mary_name = visual.TextStim(win=win, text=u'玛丽',height=0.5, color=[0.20,0.043, 0.055], pos=(4.7, -6.6)) 
        next_text = visual.TextStim(win=win, text=u'点击鼠标继续', pos = (-1, -7), height=0.3)
        Mary_text1 = visual.TextStim(win=win, text=u'选项：[T]交谈，[G]交付', pos = (0, -7), height=0.6)
        Mary_text2 = visual.TextStim(win=win, text=u'选项：[T]交谈', pos = (0, -7), height=0.6)
        

        if berry_num > 0:
            pic_bkg.draw()
            you.draw()
            Mary_text1.draw()
            win.flip()
        else: 
            pic_bkg.draw()
            you.draw()
            Mary_text2.draw()
            win.flip()    
        while you.pos[0] == Mary[0] and you.pos[1] == Mary[1]:
            keys = kb.waitKeys(keyList=Mary_list)
            for key in keys:
                if key.name == 't':
                    # a, b= myMouse.getPressed(getTime=True)
                    # # print(a) [0, 0, 0]
                    while not myMouse.isPressedIn(rect1):
                        # # print(a, b)
                        t_text1 = visual.TextStim(win=win, text=u'你好，很抱歉现在不方便下来\n……噢？你是新来的农民吗！\n欢迎欢迎，我是这边的导游玛丽，\n一会儿我带你熟悉这边的环境吧。', pos = (-3.7, -3), height=0.6, color=[0.20,0.043, 0.055])
                        
                        pic_bkg.draw()
                        you.draw()
                        dialog_pic.draw()
                        mary_pic.draw()
                        mary_name.draw()
                        next_text.draw()
                        t_text1.draw()
                        win.flip()
                    
                    t_text2 = visual.TextStim(win=win, text=u'但首先，\n你能帮我摘些浆果喂马吗？\n浆果丛就在栅栏边，\n小心别掉出去了，\n在这片农场里,\n可要沉浸其中才好呀!', pos = (-3.2, -3.7), height=0.6, color=[0.20,0.043, 0.055]) 
                    # core.wait(1)
                    pic_bkg.draw()
                    you.draw()
                    dialog_pic.draw()
                    mary_pic.draw()
                    mary_name.draw()
                    # next_text.draw()
                    t_text2.draw()
                    win.flip()
                        # t_text2.draw()
                        # win.flip()
                    core.wait(5)
                if key.name == 'up':
                    you.pos += (0,10)
                    # print(you.pos)
                if key.name == 'down':
                    you.pos += (0,-10)
                    # print(you.pos)
                if key.name == 'left':
                    you.pos += (-10,0)
                    # print(you.pos)
                if key.name == 'right':
                    you.pos += (10,0)
                    # print(you.pos)  
                pic_bkg.draw()
                you.draw()
                win.flip()     
            if key.name == 'g':  
                berry_num = 0   
                Mary_text3 = visual.TextStim(win=win, text=u'获得:房门钥匙 × 1', pos = (0, -7), height=0.6)
                key_num += 1
                if berry_num >= 3:
                    while not myMouse.isPressedIn(rect1):
                        t_text3 = visual.TextStim(win=win, text=u'嗯,就是这些!\n看来你已经理解这个农场的意义了,\n这是路易斯爷爷留给你的钥匙,\n属于前面的房子,\n进去看看吧!', pos = (-4, -3.5), height=0.6, color=[0.20,0.043, 0.055])
                        pic_bkg.draw()
                        you.draw()
                        dialog_pic.draw()
                        mary_pic.draw()
                        mary_name.draw()
                        next_text.draw()
                        t_text3.draw()
                        win.flip()
                    pic_bkg.draw()
                    you.draw()
                    Mary_text3.draw()
                    win.flip()
                elif berry_num < 3:    
                    while not myMouse.isPressedIn(rect1):
                        t_text4 = visual.TextStim(win=win, text=u'嗯......\n看来你对这个农场的意义还有些不了解,\n不过不要紧,我相信你总会自己实践出来的,\n这是路易斯爷爷留给你的钥匙,\n属于前面的房子,\n进去看看吧!', pos = (-4, -3.5), height=0.5, color=[0.20,0.043, 0.055])
                        pic_bkg.draw()
                        you.draw()
                        dialog_pic.draw()
                        mary_pic.draw()
                        mary_name.draw()
                        next_text.draw()
                        t_text4.draw()
                        win.flip()
                    pic_bkg.draw()
                    you.draw()
                    Mary_text3.draw()
                    win.flip()    

    # 5. 和房门互动
    if you.pos[0] == door[0] and you.pos[1] == door[1]:
    
        door_list = ['o', 'b', 'left', 'right', 'up', 'down']
        door_list2 = ['b', 'left', 'right', 'up', 'down']
        door_text1 = visual.TextStim(win=win, text=u'选项：[O]开锁，[B]砸开', pos = (0, -7), height=0.6)
        door_text2 = visual.TextStim(win=win, text=u'选项：[B]砸开', pos = (0, -7), height=0.6)
        if key_num > 0:
            pic_bkg.draw()
            you.draw()
            door_text1.draw()
            win.flip()
        else:
            pic_bkg.draw()
            you.draw()
            door_text2.draw()
            win.flip()
        while you.pos[0] == door[0] and you.pos[1] == door[1]:
            if key_num > 0:
                keys = kb.waitKeys(keyList=door_list)
            else:    
                keys = kb.waitKeys(keyList=door_list2)
            for key in keys:
                if key.name == 'o':
                    in_house = 1
                    key_num -= 1
                    house_pic = visual.ImageStim(win, image = 'house.png', size=(700,700),pos=(0,0), units='pix')
                    house_pic.draw()
                    you.pos = (-160, -240)
                    you.size=(40, 80)
                    you.draw()
                    win.flip()
                    

                if key.name == 'b':
                    house_text0 = visual.TextStim(win=win, text=u'以你目前的体力，还砸不开哦！', pos = (0, -7), height=0.6)
                    pic_bkg.draw()
                    house_text0.draw()
                    you.draw()
                    win.flip()
                    core.wait(1)
                if key.name == 'up':
                    you.pos += (0,0)
                    pic_bkg.draw()
                    you.draw()
                    win.flip()  
                if key.name == 'down':
                    you.pos += (0,-10)
                    pic_bkg.draw()
                    you.draw()
                    win.flip() 
                if key.name == 'left':
                    you.pos += (-10,0)
                    pic_bkg.draw()
                    you.draw()
                    win.flip() 
                if key.name == 'right':
                    you.pos += (10,0)
                    pic_bkg.draw()
                    you.draw()
                    win.flip()   

    # 5. 1和水晶球互动  
    elif you.pos[0] == crystal[0] and you.pos[1] == crystal[1]:
        crystal_text = visual.TextStim(win=win, text=u'选项：[R]查看', pos = (0, -7), height=0.6)
        house_pic.draw()
        you.draw()
        crystal_text.draw()
        win.flip()
        crystal_list = ['r', 'left', 'right', 'up', 'down']
        while you.pos[0] == crystal[0] and you.pos[1] == crystal[1]:
            keys = kb.waitKeys(keyList=crystal_list)
            for key in keys:
                if key.name == 'r':
                    bgm.pause()
                    rect1=visual.Rect(win, pos=(0,0),width=20,height=15, lineColor=None, fillColor=None, opacity = 0)
                    while not myMouse.isPressedIn(rect1):
                        dialog_pic = visual.ImageStim(win, image = '对话框.png', size=(700,320),pos=(-20, -200), units='pix')
                    
                        if you == pic_female:
                            you_pic = visual.ImageStim(win, image = 'female_face2.png', size=(130,150),pos=(190, -155), units='pix')
                            you_name = visual.TextStim(win=win, text=u'露西亚',height=0.5, color=[0.20,0.043, 0.055], pos=(4.7, -6.6))
                        if you == pic_male:
                            you_pic = visual.ImageStim(win, image = 'male_face2.png', size=(130,150),pos=(190, -155), units='pix')
                            you_name = visual.TextStim(win=win, text=u'罗杰',height=0.5, color=[0.20,0.043, 0.055], pos=(4.7, -6.6))

                        you_text = visual.TextStim(win=win, text=u'这是……祖父留下来的AR投影仪？\n里面貌似还保留着一段视频，\n唔……能再看到祖父\n真好……', pos = (-3.5, -3.7), height=0.6, color=[0.20,0.043, 0.055]) 
                        next_text = visual.TextStim(win=win, text=u'点击鼠标继续', pos = (-1, -7), height=0.3)
                        house_pic.draw()
                        you.draw()
                        dialog_pic.draw()
                        you_pic.draw()
                        you_name.draw()
                        you_text.draw()
                        next_text.draw()
                        win.flip()
                    
                    video_text = visual.TextStim(win=win, text=u'按空格键跳过', pos = (7, -7), height=0.4)
                    if you == pic_female:
                        animate = visual.VlcMovieStim(win, 'girl.mp4', size=(800, 600), pos=(0,0),  units='pix')
                    if you == pic_male:
                        animate = visual.VlcMovieStim(win, 'boy.mp4', size=(800, 600), pos=(0,0), units='pix')  
                    while animate.status != visual.FINISHED:
                        animate.draw()
                        video_text.draw()
                        win.flip()
                        if event.getKeys(keyList = ['space']):            
                            animate.pause()
                            house_pic.draw()
                            you.draw()
                            win.flip()
                            break        
                                   
                if key.name == 'up':
                    you.pos += (0,20)
                    house_pic.draw()
                    you.draw()
                    win.flip()
                if key.name == 'down':
                    you.pos += (0,-20)
                    house_pic.draw()
                    you.draw()
                    win.flip()
                if key.name == 'left':
                    you.pos += (-20,0)
                    house_pic.draw()
                    you.draw()
                    win.flip()
                if key.name == 'right':
                    you.pos += (20,0)
                      
               

    # 5.2 和斧头互动            
    elif you.pos[0] == hatchet[0] and you.pos[1] == hatchet[1]:
        hatchet_text = visual.TextStim(win=win, text=u'选项：[P]收集', pos = (0, -7), height=0.6)
        house_pic.draw()
        you.draw()
        hatchet_text.draw()
        win.flip()
        hatchet_list = ['left', 'right', 'up', 'down', 'p']
        while you.pos[0] == hatchet[0] and you.pos[1] == hatchet[1]:
            keys = kb.waitKeys(keyList=hatchet_list)
            for key in keys:
                if key.name == 'p':
                    house_text = visual.TextStim(win=win, text=u'获得：斧头 × 1', pos = (0, -7), height=0.6)
                    hatchet_num += 1
                    house_pic.draw()
                    you.draw()
                    house_text.draw()
                    win.flip()
                    core.wait(1)
                if key.name == 'up':
                    you.pos += (0,0)
                    # print(you.pos)
                if key.name == 'down':
                    you.pos += (0,-20)
                    # print(you.pos)
                if key.name == 'left':
                    you.pos += (-20,0)
                    # print(you.pos)
                if key.name == 'right':
                    you.pos += (0,0)
                    # print(you.pos)  
                house_pic.draw()
                you.draw()
                win.flip()    
    # 5.3 退出房间
    elif you.pos[0] == -160 and you.pos[1] == -260:
        if in_house == 1:
            you.size = (20,40)
            you.pos[0] = door[0]
            you.pos[1] = door[1]
            pic_bkg.draw()
            you.draw()
            win.flip() 
        in_house = 0
    # 6. 和巴特雷特互动
    elif you.pos[0] == Bartlett[0] and you.pos[1] == Bartlett[1]:
        Bartlett_list = ['left', 'right', 'up', 'down']
        while you.pos[0] == Bartlett[0] and you.pos[1] == Bartlett[1]:
            dialog_pic = visual.ImageStim(win, image = '对话框.png', size=(700,320),pos=(-20, -200), units='pix')
            Bartlett_pic = visual.ImageStim(win, image = 'farmer2.png', size=(130,150),pos=(190, -155), units='pix')
            Bartlett_name = visual.TextStim(win=win, text=u'巴特利特',height=0.5, color=[0.20,0.043, 0.055], pos=(4.7, -6.6))
            Bartlett_text = visual.TextStim(win=win, text=u'噢噢噢噢！\n别挡着我，现在该收玉米了，\n你想干嘛？\n没事的话就别来烦我。', pos = (-3.2, -3.7), height=0.6, color=[0.20,0.043, 0.055]) 
            # next_text = visual.TextStim(win=win, text=u'点击鼠标继续', pos = (-1, -7), height=0.3)
            pic_bkg.draw()
            dialog_pic.draw()
            Bartlett_pic.draw()
            Bartlett_name.draw()
            Bartlett_text.draw()
            win.flip()
            core.wait(1)
            keys = kb.waitKeys(keyList=Bartlett_list)
            for key in keys:
                if key.name == 'up':
                    you.pos += (0,0)
                    # print(you.pos)
                if key.name == 'down':
                    you.pos += (0,-20)
                    # print(you.pos)
                if key.name == 'left':
                    you.pos += (-20,0)
                    # print(you.pos)
                if key.name == 'right':
                    you.pos += (0,0)
                    # print(you.pos)  
                pic_bkg.draw()
                you.draw()
                win.flip()    
        # hatchet_text = visual.TextStim(win=win, text=u'选项：[P]收集', pos = (0, -7), height=0.6)
    # 7. 和栅栏互动
    if you.pos[1] == barrier[1]:
        if in_house == 0:
            while you.pos[1] == barrier[1]:
                barrier_text = visual.TextStim(win=win, text=u'呜呜，在往前就要掉下去啦！快后退！', pos = (0, -7), height=0.6)
                pic_bkg.draw()
                you.draw()
                barrier_text.draw()
                win.flip()
                core.wait(1)
                barrier_list = ['left', 'right', 'up', 'down']
            
                keys = kb.waitKeys(keyList=barrier_list)
                for key in keys:
                    if key.name == 'up':
                        you.pos += (0,0)
                        # print(you.pos)
                    if key.name == 'down':
                        you.pos += (0,-10)
                        # print(you.pos)
                    if key.name == 'left':
                        you.pos += (-10,0)
                        # print(you.pos)
                    if key.name == 'right':
                        you.pos += (10,0)
                        # print(you.pos)

else:       
    frindge_text = visual.TextStim(win=win, text=u'你已经到边界啦，前面的区域，以后再来探索吧！', pos = (0, -7), height=0.6)
    pic_bkg.draw()
    you.draw()
    frindge_text.draw()
    win.flip()
    core.wait(3)

    # close the window and quit PsychoPy
    win.close()
    core.quit()




        
