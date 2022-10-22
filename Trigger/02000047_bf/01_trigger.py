""" trigger/02000047_bf/01_trigger.xml """
from common import *
import state


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000084], state=1)
        set_interact_object(triggerIds=[10000085], state=1)
        set_mesh(triggerIds=[10,11,12,13,14,15,16,17], visible=False) # 다리안보임

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000084,10000085], arg2=0):
            return 다리생성1011()


class 다리생성1011(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10,11], visible=True) # 다리보임
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 다리생성1213()


class 다리생성1213(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[12,13], visible=True) # 다리보임
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 다리생성1415()


class 다리생성1415(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[14,15], visible=True) # 다리보임
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 다리생성1617()


class 다리생성1617(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[16,17], visible=True) # 다리보임
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 다리제거()


class 다리제거(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            set_mesh(triggerIds=[10,11,12,13,14,15,16,17], visible=False)
            return 트리거초기화2()


class 트리거초기화2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 반응대기()


