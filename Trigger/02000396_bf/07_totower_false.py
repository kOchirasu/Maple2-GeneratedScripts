""" trigger/02000396_bf/07_totower_false.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001136], state=0) # ToTower_False
        self.set_user_value(key='ToTowerFalse', value=0)
        self.set_user_value(key='AnotherGuide', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ToTowerFalse', value=1):
            return ToTowerFalse(self.ctx)


class ToTowerFalse(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001136], state=1) # ToTower_False

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001136], stateValue=0):
            return NoticeDelay(self.ctx)


class NoticeDelay(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=5, key='AnotherGuide', value=1)
        self.set_user_value(triggerId=6, key='AnotherGuide', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NoticeOn(self.ctx)


class NoticeOn(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039605, textId=20039605) # 가이드 : 철창은 자물쇠로 단단히 묶여 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CloseGuide02(self.ctx)
        if self.user_value(key='AnotherGuide', value=1):
            return CloseGuide01(self.ctx)


class CloseGuide01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return CloseGuide02(self.ctx)


class CloseGuide02(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20039605)
        self.set_user_value(triggerId=5, key='AnotherGuide', value=0)
        self.set_user_value(triggerId=6, key='AnotherGuide', value=0)


initial_state = Wait
