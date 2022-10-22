""" trigger/82000001_survival/08_raremob.xml """
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
        start_combine_spawn(groupId=[160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195], isStart=True)

    def on_tick(self) -> state.State:
        if user_value(key='RareMobOff', value=1):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195], isStart=False)


