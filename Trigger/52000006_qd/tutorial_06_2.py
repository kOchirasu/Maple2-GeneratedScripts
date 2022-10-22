""" trigger/52000006_qd/tutorial_06_2.xml """
from common import *
import state


class 엔터대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 오픈대기중()


class 오픈대기중(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000016]):
            return 화면효과()


class 화면효과(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 화면효과2()


class 화면효과2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_2__0$')
        set_effect(triggerIds=[401], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 화면효과3()


class 화면효과3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        select_camera(triggerId=303, enable=True)
        set_effect(triggerIds=[402], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 맵이동()


class 맵이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        move_user(mapId=52000007, portalId=1)


