""" trigger/82000002_survival/08_raremob.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_user_value(key='RareMobOnCount', value=0)
        set_user_value(key='RareMobOff', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RareMobOnCount', value=1):
            return Delay()


class Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return MobSpawn()
        if user_value(key='RareMobOff', value=1):
            return Quit()


class MobSpawn(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354], isStart=True)

    def on_tick(self) -> state.State:
        if user_value(key='RareMobOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354], isStart=False)


