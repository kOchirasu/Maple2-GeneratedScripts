""" trigger/02000351_bf/lever_01.xml """
from common import *
import state


class 닫힘상태(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6001,6002], visible=True, arg4=0, arg5=0) # 벽
        set_mesh(triggerIds=[6020,6021,6022,6023,6024,6025,6026], visible=False, arg4=0, arg5=0) # 벽

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000818], arg2=1):
            return 작동()


class 작동(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=111, textId=20000080) # 스위치를 정지하세요

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000818], arg2=0):
            return 열림상태()

    def on_exit(self):
        hide_guide_summary(entityId=111)


class 열림상태(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_mesh(triggerIds=[6010,6011,6012,6013,6014,6015,6016], visible=False, arg4=200, arg5=15) # 벽 해제
        set_mesh(triggerIds=[6020,6021,6022,6023,6024,6025,6026], visible=True, arg4=200, arg5=15) # 벽 해제
        set_effect(triggerIds=[9000002], visible=True) # Object_Electricity_On_01

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 열림()


class 열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6001,6002], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 열림_끝()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class 열림_끝(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=False) # 연출 카메라


