""" trigger/02000315_bf/guide_03.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # UI
        self.set_user_value(key='CameraWalkEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CameraWalkEnd', value=1):
            return LoadingDelay02(self.ctx)


class LoadingDelay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstBattleGuide(self.ctx)


class FirstBattleGuide(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031501, textId=20031501, duration=8000) # 부상병을 치료하고 함께 몬스터를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[502]):
            return FirstBridgeGuide(self.ctx)


class FirstBridgeGuide(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031502, textId=20031502, duration=5000) # 레버를 당기면 다음 지역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[503]):
            return SecondBattleGuide(self.ctx)


class SecondBattleGuide(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031501, textId=20031501, duration=8000) # 부상병을 치료하고 함께 몬스터를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[505]):
            return SecondBridgeGuide(self.ctx)


class SecondBridgeGuide(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031502, textId=20031502, duration=5000) # 레버를 당기면 다음 지역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[506]):
            return ThirdBattleGuide(self.ctx)


class ThirdBattleGuide(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031501, textId=20031501, duration=8000) # 부상병을 치료하고 함께 몬스터를 처치하세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[508]):
            return ThirdBridgeGuide(self.ctx)


class ThirdBridgeGuide(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # UI
        self.show_guide_summary(entityId=20031502, textId=20031502, duration=5000) # 레버를 당기면 다음 지역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[402]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031502)


initial_state = Wait
