import pygame
import sys
from pygame.locals import*
from jiancai import jiancai
from fanyi import fanyi

pygame.init()
bg_size=width,height=650,975
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption('工具箱')
background=pygame.image.load('images/background.jpg').convert()

# 翻译模块
button_fanyi=pygame.image.load('images/fanyi_button.png')
button_fanyi=pygame.transform.scale(button_fanyi,(150,150))
button_fanyi_rect=button_fanyi.get_rect()
button_fanyi_rect.left,button_fanyi_rect.top=60,200

#剪裁模块
button_jiancai=pygame.image.load('images/jiancai_button.png')
button_jiancai=pygame.transform.scale(button_jiancai,(150,150))
button_jiancai_rect=button_jiancai.get_rect()
button_jiancai_rect.left,button_jiancai_rect.top=60,400









def main():
    #print("获取系统中所有可用字体",pygame.font.get_fonts())
    running=True
    clock=pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        if pygame.mouse.get_pressed()[0]:
            pos=pygame.mouse.get_pos()
            if button_fanyi_rect.left<pos[0]<button_fanyi_rect.right and \
                button_fanyi_rect.top<pos[1]<button_fanyi_rect.bottom:
                fanyi()
            if button_jiancai_rect.left<pos[0]<button_jiancai_rect.right and \
                button_jiancai_rect.top<pos[1]<button_jiancai_rect.bottom:
                jiancai()
        screen.blit(background,(0,0))
        screen.blit(button_fanyi,button_fanyi_rect)
        screen.blit(button_jiancai,button_jiancai_rect)
        pygame.display.flip()
        clock.tick(50)

main()