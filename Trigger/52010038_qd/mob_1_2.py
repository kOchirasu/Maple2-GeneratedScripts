""" trigger/52010038_qd/mob_1_2.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='WaveStart', value=1):
            return 생성()

    def on_exit(self):
        spawn_npc_range(rangeIds=[2005,2006,2007], isAutoTargeting=True)


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4000], arg2=False)
        spawn_npc_range(rangeIds=[2005,2006,2007], isAutoTargeting=True, randomPickCount=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 생성()
        if user_value(key='WaveEnd', value=1):
            return 종료()


class 종료(state.State):
    pass


