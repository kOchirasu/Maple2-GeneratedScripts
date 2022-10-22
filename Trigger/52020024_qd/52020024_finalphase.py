""" trigger/52020024_qd/52020024_finalphase.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='FinalPhase', value=1):
            return 스폰()


class 스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[131,132,133,134,135,136], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return 스폰()
        if monster_dead(boxIds=[131,132,133,134,135,136]):
            return 스폰()
        if user_value(key='FinalPhase', value=2):
            return 종료()


class 종료(state.State):
    pass


