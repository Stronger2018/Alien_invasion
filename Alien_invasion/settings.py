class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_limit = 3

        #子弹设置 创建宽３像素　高１５像素的深灰色子弹。子弹的速度比飞船稍低。
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #设置fleet_drop_speed指定了有外星人撞到屏幕边缘时，外星人向下移动的速度。
        self.fleet_drop_speed = 10

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5
        #初始化随游戏进行而变化的属性
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

         #记分
        self.alien_points = 50
        
        #fleet_direction为１表示向右;为－１表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor *= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)




