""" trigger/52100002_qd/wave01.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='wave01', value=1):
            return 소환()
        if user_value(key='EndDungeon', value=1):
            return 종료()


class 소환(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[1901,1902,1903,1904,1905,1906,1907,1908,1909], isAutoTargeting=True, randomPickCount=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 대기()
        if user_value(key='EndDungeon', value=1):
            return 종료()


class 종료(state.State):
    pass


