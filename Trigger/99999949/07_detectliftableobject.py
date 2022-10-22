""" trigger/99999949/07_detectliftableobject.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5007], visible=False) # 내려놓을 위치 가이드

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9061]):
            return Guide()


class Guide(state.State):
    def on_enter(self):
        debug_string(string='7번 영역에 들어가면 DetectLiftableObject 트리거가 발동됩니다.')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9060]):
            return Ready01()


class Ready01(state.State):
    def on_enter(self):
        debug_string(string='DetectLiftableObject 2초 후에 시작됩니다.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ready02()


class Ready02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__0$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return QuizRandom01()


class QuizRandom01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5007], visible=True) # 내려놓을 위치 가이드

    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return AnswerIsWood01()
        if random_condition(rate=50):
            return AnswerIsRock01()


class AnswerIsWood01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__1$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9062], itemId=0):
            return CheckAnswerWood01()


class CheckAnswerWood01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5007], visible=False) # 내려놓을 위치 가이드

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9062], itemId=30000377):
            return RightAnswerWood01()
        if not detect_liftable_object(boxIds=[9062], itemId=30000377):
            return WrongAnswerWood01()


class RightAnswerWood01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__2$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return ClearDetectBox01()


class WrongAnswerWood01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__3$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return ClearDetectBox01()


class AnswerIsRock01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__4$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9062], itemId=0):
            return CheckAnswerRock01()


class CheckAnswerRock01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5007], visible=False) # 내려놓을 위치 가이드

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9062], itemId=30000440):
            return RightAnswerRock01()
        if not detect_liftable_object(boxIds=[9062], itemId=30000440):
            return WrongAnswerRock01()


class RightAnswerRock01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__5$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return ClearDetectBox01()


class WrongAnswerRock01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__6$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return ClearDetectBox01()


class ClearDetectBox01(state.State):
    def on_tick(self) -> state.State:
        if not detect_liftable_object(boxIds=[9062], itemId=0):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        debug_string(string='3초 후에 트리거가 리셋됩니다. 7번 영역 밖으로 나가세요.')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


