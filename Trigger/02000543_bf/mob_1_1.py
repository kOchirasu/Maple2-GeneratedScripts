""" trigger/02000543_bf/mob_1_1.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='WaveStart', value=1):
            return 생성()

    def on_exit(self):
        create_monster(spawnIds=[101,102], arg2=True)


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 생성()
        if user_value(key='WaveEnd', value=1):
            return 종료()


class 종료(state.State):
    pass


