from utils.dispatcher import EventType, event
from utils.adb_utils import screen_capture, create_dir
from predict.predict import process
import config


def check_event(pic_type) -> callable:
    """判断当前是在什么事件"""
    print(event)
    if pic_type == EventType.Common:
        return event.get(EventType.Common)
    elif pic_type == EventType.NewWarship:
        return event.get(EventType.NewWarship)
    elif pic_type == EventType.NextFight:
        return event.get(EventType.NextFight)
    else:
        None


def run():
    """
    程序入口，循环事件，每个循环都会进行一次截图，
    对截图进行判断事件类型，根据事件类型执行相应的处理脚本
    """
    create_dir()
    while True:
        screen_capture(config.ScreenShotPath)
        event_type = process(config.ModelPath, config.ScreenShotPath)
        action = check_event(event_type)
        if action:
            action()


if __name__ == "__main__":
    run()
