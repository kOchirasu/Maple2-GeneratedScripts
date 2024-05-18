""" trigger/02010054_bf/brick_20.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[34020], visible=True)
        self.set_skill(trigger_ids=[7020])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1120]):
            return 발판(self.ctx)


class 발판(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[7020], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            self.set_mesh(trigger_ids=[34020])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
