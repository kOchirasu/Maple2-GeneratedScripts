""" trigger/02000351_bf/lever_check.xml """
from common import *
import state


class 레버체크(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000819], state=0)
        set_interact_object(triggerIds=[10000820], state=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000819], arg2=1):
            return 레버체크2()
        if object_interacted(interactIds=[10000820], arg2=1):
            return 레버체크2()


class 레버체크2(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000820], arg2=0):
            return 레버체크3_1개()
        if object_interacted(interactIds=[10000819], arg2=0):
            return 레버체크4_1개()


class 레버체크3_1개(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000819], arg2=0):
            return 레버체크완료()


class 레버체크4_1개(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000820], arg2=0):
            return 레버체크완료()


class 레버체크완료(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 열림()


class 열림(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_mesh(triggerIds=[6005], visible=False, arg4=0, arg5=10) # 벽 해제

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 열림_끝()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class 열림_끝(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        # <action name="이벤트UI를설정한다" arg1="1" arg2="관문이 개방되었습니다. \n다음 지역으로 이동하십시오." arg3="3000"/>

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 종료()
        if count_users(boxId=704, boxId=1):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=113)


class 종료(state.State):
    pass


