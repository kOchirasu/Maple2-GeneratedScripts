""" trigger/52100031_qd/boss_recall.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[2099]):
            return 발신()


class 발신(state.State):
    def on_enter(self):
        set_ai_extra_data(key='recall', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()


class 종료(state.State):
    pass


