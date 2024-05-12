""" trigger/02020100_bf/seed0.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='Seed0interact', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed0start') >= 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1301], visible=True, start_delay=0, interval=0, fade=2)
        self.set_interact_object(trigger_ids=[10002115], state=1, arg3=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed0start') >= 2:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002115], state=0):
            return 씨앗0_대기(self.ctx)


class 씨앗0_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1301], visible=False, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10002115], state=0, arg3=True)
        self.set_user_value(trigger_id=99990001, key='Seed0interact', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed0start') >= 2:
            return 종료(self.ctx)
        if not self.check_any_user_additional_effect(box_id=0, additional_effect_id=70002109, level=1):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002115], state=0)


initial_state = 대기
