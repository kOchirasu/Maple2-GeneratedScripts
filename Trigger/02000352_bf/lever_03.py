""" trigger/02000352_bf/lever_03.xml """
from common import *
import state


class 닫힘상태(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000824], state=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000824], arg2=1):
            return 작동()


class 작동(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000824], arg2=0):
            return 열림상태()


class 열림상태(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[9000004], visible=True) # Sound EFfect on
        set_mesh(triggerIds=[6060,6061,6062,6063], visible=False, arg4=200, arg5=15) # 빨간선 사라지게
        set_mesh(triggerIds=[6160,6161,6162,6163], visible=True, arg4=200, arg5=0) # 파란선 나타나게

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 열림()


class 열림(state.State):
    pass


