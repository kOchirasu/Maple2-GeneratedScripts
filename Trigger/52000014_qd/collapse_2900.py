""" trigger/52000014_qd/collapse_2900.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[2900,2901,2902,2903,2904,2905], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[12900], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22900], visible=False) # Vibrate Sound
        self.set_effect(triggerIds=[12901], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22901], visible=False) # Vibrate Sound
        self.set_effect(triggerIds=[12902], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22902], visible=False) # Vibrate Sound

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 로딩딜레이(self.ctx)


class 로딩딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 무너짐01(self.ctx)


class 무너짐01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[12900], visible=True) # Vibrate Short
        self.set_effect(triggerIds=[22900], visible=True) # Vibrate Sound
        self.set_random_mesh(triggerIds=[2900,2901,2902,2903,2904,2905], visible=False, meshCount=6, arg4=100, delay=200)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 카메라연출01(self.ctx)


class 카메라연출01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=2)
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 카메라연출02(self.ctx)


class 카메라연출02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$52000014_QD__COLLAPSE_2900__0$')
        self.set_skip(state=카메라연출03)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='4'):
            return 카메라연출03(self.ctx)


class 카메라연출03(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=3)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=601, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 무너짐02(self.ctx)


class 무너짐02(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__1$', arg3='4000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9002]):
            return 무너짐03(self.ctx)


class 무너짐03(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=5)
        self.set_effect(triggerIds=[12901], visible=True) # Vibrate Short
        self.set_effect(triggerIds=[22901], visible=True) # Vibrate Sound

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 무너짐04(self.ctx)


class 무너짐04(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 무너짐05(self.ctx)


class 무너짐05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9003]):
            return 반응안내01(self.ctx)


class 반응안내01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=4)
        self.set_effect(triggerIds=[12902], visible=True) # Vibrate Short
        self.set_effect(triggerIds=[22902], visible=True) # Vibrate Sound
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__2$', arg3='4000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='20'):
            return 줍기안내01(self.ctx)


class 줍기안내01(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2900__3$', arg3='4000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9004], questIds=[50001250], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001251], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001252], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001253], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001254], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001255], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001256], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001257], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001258], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001259], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001370], questStates=[2]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001371], questStates=[2]): # 완료 유저
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001250], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001251], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001252], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001253], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001254], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001255], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001256], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001257], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001258], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001259], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001370], questStates=[3]):
            return 포털생성01(self.ctx)
        if self.quest_user_detected(boxIds=[9004], questIds=[50001371], questStates=[3]):
            return 포털생성01(self.ctx)


class 포털생성01(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[12900], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22900], visible=False) # Vibrate Sound
        self.set_effect(triggerIds=[12901], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22901], visible=False) # Vibrate Sound
        self.set_effect(triggerIds=[12902], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22902], visible=False) # Vibrate Sound


initial_state = 대기
