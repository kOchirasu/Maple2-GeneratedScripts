""" trigger/02000352_bf/lever_01.xml """
from common import *
import state


class 닫힘상태(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6111], visible=True, arg4=0, arg5=0) # 벽
        set_mesh(triggerIds=[6101], visible=False, arg4=0, arg5=0) # 벽

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000822], arg2=1):
            return 작동()


class 작동(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=111, textId=20000080) # 스위치를 정지하세요

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000822], arg2=0):
            return 열림상태()

    def on_exit(self):
        hide_guide_summary(entityId=111)


class 열림상태(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[9000002], visible=True) # Sound EFfect on
        set_mesh(triggerIds=[6111], visible=False, arg4=200, arg5=15) # 벽 해제
        set_mesh(triggerIds=[6101], visible=True, arg4=200, arg5=15) # 벽 해제

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 열림()


class 열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6002], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 열림_끝()


class 열림_끝(state.State):
    def on_enter(self):
        show_guide_summary(entityId=113, textId=40011) # 스위치를 정지하세요
        select_camera(triggerId=8001, enable=False) # 연출 카메라


