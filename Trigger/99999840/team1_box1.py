""" trigger/99999840/team1_box1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        dungeon_variable(varId=901, value=0)
        set_interact_object(triggerIds=[10002175], state=0, arg3=False)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='911', value=1):
            return 종료()
        if dungeon_variable(varID='912', value=1):
            return 종료()
        if dungeon_variable(varID='913', value=1):
            return 종료()
        if user_value(key='Start', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002175], state=1, arg3=False)
        set_interact_object(triggerIds=[10002176], state=1, arg3=False)
        set_interact_object(triggerIds=[10002177], state=1, arg3=False)
        set_interact_object(triggerIds=[10002178], state=1, arg3=False)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='911', value=1):
            return 종료()
        if dungeon_variable(varID='912', value=1):
            return 종료()
        if dungeon_variable(varID='913', value=1):
            return 종료()
        if object_interacted(interactIds=[10002175], arg2=0):
            return 애디셔널_중첩1()


class 애디셔널_중첩1(state.State):
    def on_enter(self):
        dungeon_variable(varId=901, value=1)
        add_buff(boxIds=[9001], skillId=70002511, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='911', value=1):
            return 종료()
        if dungeon_variable(varID='912', value=1):
            return 종료()
        if dungeon_variable(varID='913', value=1):
            return 종료()
        if wait_tick(waitTick=100):
            return 애디셔널_중첩2()


class 애디셔널_중첩2(state.State):
    def on_enter(self):
        add_buff(boxIds=[9001], skillId=70002511, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 애디셔널_중첩3()


class 애디셔널_중첩3(state.State):
    def on_enter(self):
        add_buff(boxIds=[9001], skillId=70002511, level=1, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


class 종료(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002175], state=0, arg3=False)

    def on_tick(self) -> state.State:
        if user_value(key='BadMob', value=1):
            return 대기()


