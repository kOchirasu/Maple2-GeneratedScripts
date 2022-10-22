""" trigger/82000006_survival/08_raremob.xml """
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
        start_combine_spawn(groupId=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], isStart=True)

    def on_tick(self) -> state.State:
        if user_value(key='RareMobOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36], isStart=False)


