""" trigger/02000064_tw_triatown02/massive_door_1.xml """
from common import *
import state


class 오픈대기중(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[11,12,13], visible=True)
        set_actor(triggerId=1, visible=True, initialSequence='Eff_MassiveEvent_Bridge_Opened')
        set_actor(triggerId=2, visible=True, initialSequence='Eff_MassiveEvent_Bridge_Opened')
        set_actor(triggerId=3, visible=True, initialSequence='Eff_MassiveEvent_Door_Closed')


class 오픈중1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 오픈중2()

    def on_exit(self):
        reset_timer(timerId='1')


class 오픈중2(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 클로즈대기중()

    def on_exit(self):
        reset_timer(timerId='2')
        set_actor(triggerId=3, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')


class 클로즈대기중(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=114)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 클로즈5초전()

    def on_exit(self):
        reset_timer(timerId='3')


class 클로즈5초전(state.State):
    def on_enter(self):
        notice(arg1=False, script='$02000064_TW_Triatown02__MASSIVE_DOOR_1__0$', arg3=True)
        set_timer(timerId='4', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 클로즈중1()

    def on_exit(self):
        reset_timer(timerId='4')
        set_actor(triggerId=3, visible=True, initialSequence='Eff_MassiveEvent_Door_Closed')


class 클로즈중1(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 클로즈중2()

    def on_exit(self):
        reset_timer(timerId='5')


class 클로즈중2(state.State):
    def on_enter(self):
        notice(arg1=False, script='$02000064_TW_Triatown02__MASSIVE_DOOR_1__1$', arg3=True)
        set_timer(timerId='6', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 오픈대기중()

    def on_exit(self):
        reset_timer(timerId='6')


