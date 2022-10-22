""" trigger/02000351_bf/lever_02.xml """
from common import *
import state


class 닫힘상태(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000819], state=0)
        set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062], visible=True, arg4=0, arg5=0) # 빨간 선 보이게
        set_mesh(triggerIds=[6081,6082,6083,6084,6085,6086,6087,6088,6089,6090,6091,6092], visible=False, arg4=0, arg5=0) # 파란 선 안보이게

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000819], arg2=1):
            return 작동()


class 작동(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000819], arg2=0):
            return 열림상태()


class 열림상태(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[9000003], visible=True) # Object_Electricity_On_01
        set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062], visible=False, arg4=200, arg5=15) # 빨간선 사라지게
        set_mesh(triggerIds=[6081,6082,6083,6084,6085,6086,6087,6088,6089,6090,6091,6092], visible=True, arg4=200, arg5=15) # 파란선 나타나게

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 열림()


class 열림(state.State):
    pass


