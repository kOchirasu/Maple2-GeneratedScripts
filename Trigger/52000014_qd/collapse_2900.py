""" trigger/52000014_qd/collapse_2900.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[2900,2901,2902,2903,2904,2905], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[12900], visible=False) # Vibrate Short
        set_effect(triggerIds=[22900], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12901], visible=False) # Vibrate Short
        set_effect(triggerIds=[22901], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12902], visible=False) # Vibrate Short
        set_effect(triggerIds=[22902], visible=False) # Vibrate Sound

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 로딩딜레이()


class 로딩딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 무너짐01()


class 무너짐01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[12900], visible=True) # Vibrate Short
        set_effect(triggerIds=[22900], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2900,2901,2902,2903,2904,2905], visible=False, meshCount=6, arg4=100, delay=200)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 카메라연출01()


class 카메라연출01(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=2)
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 카메라연출02()


class 카메라연출02(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$52000014_QD__COLLAPSE_2900__0$')
        set_skip(state=카메라연출03)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 카메라연출03()


class 카메라연출03(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=3)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=601, enable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 무너짐02()


class 무너짐02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__1$', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 무너짐03()


class 무너짐03(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=5)
        set_effect(triggerIds=[12901], visible=True) # Vibrate Short
        set_effect(triggerIds=[22901], visible=True) # Vibrate Sound

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 무너짐04()


class 무너짐04(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 무너짐05()


class 무너짐05(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return 반응안내01()


class 반응안내01(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=4)
        set_effect(triggerIds=[12902], visible=True) # Vibrate Short
        set_effect(triggerIds=[22902], visible=True) # Vibrate Sound
        set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__2$', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 줍기안내01()


class 줍기안내01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__3$', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9004], questIds=[50001250], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001251], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001252], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001253], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001254], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001255], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001256], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001257], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001258], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001259], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001370], questStates=[2]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001371], questStates=[2]): # 완료 유저
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001250], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001251], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001252], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001253], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001254], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001255], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001256], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001257], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001258], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001259], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001370], questStates=[3]):
            return 포털생성01()
        if quest_user_detected(boxIds=[9004], questIds=[50001371], questStates=[3]):
            return 포털생성01()


class 포털생성01(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12900], visible=False) # Vibrate Short
        set_effect(triggerIds=[22900], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12901], visible=False) # Vibrate Short
        set_effect(triggerIds=[22901], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12902], visible=False) # Vibrate Short
        set_effect(triggerIds=[22902], visible=False) # Vibrate Sound


