import time

from utils import adb_utils


class Task:

    def _wait(self, seconds):
        time.sleep(seconds)

    def task_run(self):
        raise NotImplementedError


class NewBattleShipsTask(Task):

    def __init__(self):
        self.label1 = (522, 1539)  # 新战舰看视频坐标点
        self.label2 = (975, 212)  # 新战舰视频结束x坐标点
        self.adv_wait = 50  # 新战舰视频等待事件

    def task_run(self):
        adb_utils.click(*self.label1)
        self._wait(self.adv_wait)
        adb_utils.click(*self.label2)
