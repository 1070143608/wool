import functools
import logging

from utils.events import task

event = {}


class EventType:
    Common = "common"
    NewBattleShips = "new_battleships"
    StageClear = "stage_clear"
    


def iface(_id):
    def deco(func):
        event[_id] = func

        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        return inner

    return deco


@iface(EventType.Common)
def on_common():
    pass


@iface(EventType.StageClear)
def on_next_fight():
    pass


@iface(EventType.NewBattleShips)
def on_new_warship():
    logging.info("新战舰事件任务")
    task.NewBattleShipsTask().task_run()
