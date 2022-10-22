""" trigger/02000352_bf/lever_start.xml """
from common import *
import state


class 작동(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6201], visible=False, arg4=0, arg5=0) # 파란 선 안보이게
        set_interact_object(triggerIds=[10000821], state=1)
        set_mesh(triggerIds=[6150,6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163], visible=True, arg4=0, arg5=0) # 빨간 선 보이게
        set_mesh(triggerIds=[6150,6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163], visible=False, arg4=0, arg5=0) # 파란 선 안보이게

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000821], arg2=0):
            return 열림상태()


class 열림상태(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[9000001], visible=True) # Sound EFfect on
        set_mesh(triggerIds=[6211], visible=False, arg4=200, arg5=15) # 빨간 선 안보이게
        set_mesh(triggerIds=[6201], visible=True, arg4=200, arg5=15) # 파란 선 보이게

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 열림()


class 열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6001], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 열림_끝()


class 열림_끝(state.State):
    pass


