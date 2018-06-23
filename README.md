# Alien_invasion

在 Linux 系统中安装 Pygame
如果你使用的是 Python 2.7 
$ sudo apt-get install python-pygame
如果你使用的是 Python 3 ，就需要执行两个步骤：安装 Pygame 依赖的库；下载并安装 Pygame 。
依赖的库（如果你开始终端会话时使用的是命令 python3.5 ，请将 python3-dev 替换为 python3.5-dev ）：
$ sudo apt-get install python3-dev mercurial
$ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
如果你要启用 Pygame 的一些高级功能，如添加声音的功能，可安装下面这些额外的库：
$ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
$ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
$ sudo apt-get install python-numpy
接下来，执行下面的命令来安装 Pygame （如有必要，将 pip 替换为 pip3 ）：
$ pip install --user hg+http://bitbucket.org/pygame/pygame


1. alien_invasion.py
主文件 alien_invasion.py 创建一系列整个游戏都要用到的对象：存储在 ai_settings 中的设置、存储在 screen 中的主显示 surface 以及一个飞船实例。文件 alien_invasion.py 还包含游戏的主循环，这是一个调用 check_events() 、 ship.update() 和 update_screen() 的 while 循环。
要玩游戏《外星人入侵》，只需运行文件 alien_invasion.py 。其他文件（ settings.py 、 game_functions.py 、 ship.py ）包含的代码被直接或间接地导入到这个文件中。
2. settings.py
文件 settings.py 包含 Settings 类，这个类只包含方法 __init__() ，它初始化控制游戏外观和飞船速度的属性。
3. game_functions.py
文件 game_functions.py 包含一系列函数，游戏的大部分工作都是由它们完成的。函数 check_events() 检测相关的事件，如按键和松开，并使用辅助函
数 check_keydown_events() 和 check_keyup_events() 来处理这些事件。就目前而言，这些函数管理飞船的移动。模块 game_functions 还包含函
数 update_screen() ，它用于在每次执行主循环时都重绘屏幕。
4. ship.py
文件 ship.py 包含 Ship 类，这个类包含方法 __init__() 、管理飞船位置的方法 update() 以及在屏幕上绘制飞船的方法 blitme() 。表示飞船的图像存储在文件夹 images 下的文件 ship.bmp 中。

