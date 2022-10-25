""" trigger/02020112_bf/button7.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[931], jobCode=0):
            return 작동(self.ctx)


class 작동(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=9907, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ButtonSuccess', value=1):
            return 종료(self.ctx)
        if self.user_detected(boxIds=[923], jobCode=0):
            return 감지(self.ctx)


class 감지(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=9907, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ButtonSuccess', value=1):
            return 종료(self.ctx)
        if not self.user_detected(boxIds=[923], jobCode=0):
            return 작동(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=9907, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')


initial_state = 대기
