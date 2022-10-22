""" trigger/02000315_bf/guide_03.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # UI
        set_user_value(key='CameraWalkEnd', value=0)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay01()


class LoadingDelay01(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='CameraWalkEnd', value=1):
            return LoadingDelay02()


class LoadingDelay02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstBattleGuide()


class FirstBattleGuide(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031501, textId=20031501, duration=8000) # 부상병을 치료하고 함께 몬스터를 처치하세요.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[502]):
            return FirstBridgeGuide()


class FirstBridgeGuide(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031502, textId=20031502, duration=5000) # 레버를 당기면 다음 지역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[503]):
            return SecondBattleGuide()


class SecondBattleGuide(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031501, textId=20031501, duration=8000) # 부상병을 치료하고 함께 몬스터를 처치하세요.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[505]):
            return SecondBridgeGuide()


class SecondBridgeGuide(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031502, textId=20031502, duration=5000) # 레버를 당기면 다음 지역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[506]):
            return ThirdBattleGuide()


class ThirdBattleGuide(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031501, textId=20031501, duration=8000) # 부상병을 치료하고 함께 몬스터를 처치하세요.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[508]):
            return ThirdBridgeGuide()


class ThirdBridgeGuide(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # UI
        show_guide_summary(entityId=20031502, textId=20031502, duration=5000) # 레버를 당기면 다음 지역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[402]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031502)


