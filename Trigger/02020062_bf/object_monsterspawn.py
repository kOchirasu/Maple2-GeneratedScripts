""" trigger/02020062_bf/object_monsterspawn.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[494], isStart=False)

    def on_tick(self) -> state.State:
        if user_value(key='EliteSpawn', value=1):
            return 스폰()


class 스폰(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[494], isStart=True)

    def on_tick(self) -> state.State:
        if user_value(key='EliteSpawn', value=0):
            return 대기()
        if user_value(key='EliteSpawn', value=2):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[494], isStart=False)


