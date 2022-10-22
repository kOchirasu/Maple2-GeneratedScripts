""" trigger/02000352_bf/lever_check.xml """
from common import *
import state


class 레버체크(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000823], state=0)
        set_interact_object(triggerIds=[10000824], state=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000823], arg2=1):
            return 레버체크2()
        if object_interacted(interactIds=[10000824], arg2=1):
            return 레버체크2()


class 레버체크2(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000823], arg2=0):
            return 레버체크3_1개()
        if object_interacted(interactIds=[10000824], arg2=0):
            return 레버체크4_1개()


class 레버체크3_1개(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000824], arg2=0):
            return 레버체크완료()


class 레버체크4_1개(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000823], arg2=0):
            return 레버체크완료()


class 레버체크완료(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 열림()


class 열림(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_mesh(triggerIds=[6054,6055,6056], visible=False, arg4=200, arg5=15) # 빨간선 사라지게
        set_mesh(triggerIds=[6154,6155,6156], visible=True, arg4=200, arg5=0) # 파란선 나타나게
        set_effect(triggerIds=[9000005], visible=True) # Sound EFfect on

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 열림_끝()

    def on_exit(self):
        set_mesh(triggerIds=[6003], visible=False, arg4=0, arg5=10) # 벽 해제


class 열림_끝(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=113, textId=40011) # 다음 지역으로 이동하세요
        select_camera(triggerId=8002, enable=False) # 연출 카메라
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=113)


class 종료(state.State):
    pass


