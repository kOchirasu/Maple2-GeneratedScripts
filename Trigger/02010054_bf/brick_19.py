""" trigger/02010054_bf/brick_19.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[34019], visible=True, start_delay=0, interval=0, fade=0)
        self.set_skill(trigger_ids=[7019], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1119]):
            return 발판(self.ctx)


class 발판(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7019], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            self.set_mesh(trigger_ids=[34019], visible=False, start_delay=0, interval=0, fade=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
