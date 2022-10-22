""" trigger/02000375_bf/1123000.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3400], visible=True, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_off')

    def on_tick(self) -> state.State:
        if user_value(key='SecondPhaseEnd', value=1):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3400], visible=False, arg3=0, arg4=0, arg5=0)
        set_actor(triggerId=201, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_on')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 종료(state.State):
    pass


