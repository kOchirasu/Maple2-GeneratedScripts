""" trigger/02000351_bf/lever_03.xml """
from common import *
import state


class 닫힘상태(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000820], state=0)
        set_mesh(triggerIds=[6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162], visible=True, arg4=0, arg5=0) # 빨간 선 보이게
        set_mesh(triggerIds=[6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192], visible=False, arg4=0, arg5=0) # 파란 선 안보이게

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000820], arg2=1):
            return 작동()


class 작동(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000820], arg2=0):
            return 열림상태()


class 열림상태(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[9000004], visible=True) # Object_Electricity_On_01
        set_mesh(triggerIds=[6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162], visible=False, arg4=200, arg5=15) # 빨간선 사라지게
        set_mesh(triggerIds=[6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192], visible=True, arg4=200, arg5=0) # 파란선 나타나게

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 열림()


class 열림(state.State):
    pass


