import pygame.font 
from pygame.sprite import Group
from ship import Ship 

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats 

        #显示得分信息使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #准备包含最高得分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)

        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.ai_settings.bg_color)

        #将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(str(self.stats.level), True,
            self.text_color, self.ai_settings.bg_color)

        #将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """显示还剩余多少飞船"""
        #创建一个空编组 self.ships ，用于存储飞船实例
        self.ships = Group()
        #为填充这个编组，根据玩家还有多少艘飞船运行一个循环相应的次数
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            #设置其 x  坐标，让整个飞船编组都位于屏幕左边，且每艘飞船的左边距都为 10 像素
            ship.rect.x = 10 + ship_number * ship.rect.width
            # y  坐标设置为离屏幕上边缘 10 像素
            ship.rect.y = 10
            #将每艘新飞船都添加到编组 ships 中
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分和最高得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #绘制飞船
        self.ships.draw(self.screen)


