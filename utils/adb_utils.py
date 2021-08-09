import os
from PyMacro import auto_bot


def execute_shell(command: str):
    process = os.popen(command)
    res = process.read()
    process.close()
    return res


def create_dir():
    """
    在手机上创建文件夹
    :return: None
    """
    print("create_dir 在手机上创建文件夹...")
    execute_shell('adb shell mkdir /sdcard/com.game.matrix_crazygame/plugin_pic/')
    print("create_dir finished")


def screen_capture(screen_capture_path) -> None:
    """
    截取手机当前屏幕
    :return: path  图片存储路径
    """
    print("保存截图...start..")
    pic_name = "current.jpg"
    command = f'adb shell /system/bin/screencap -p /sdcard/com.game.matrix_crazygame/plugin_pic/{pic_name}'
    execute_shell(command)
    command = f'adb pull /sdcard/com.game.matrix_crazygame/plugin_pic/{pic_name} {screen_capture_path}'
    # print("pic_path: ", command)
    execute_shell(command)
    print("保存截图...finished..")


def click(x, y):
    """模拟点击屏幕"""
    auto_bot.tap(x, y)
