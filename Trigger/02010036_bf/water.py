""" trigger/02010036_bf/water.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001], visible=True, start_delay=0, interval=30, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 부서짐(self.ctx)


class 부서짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001], visible=False, start_delay=0, interval=30, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[101]):
            return 대기(self.ctx)


initial_state = 대기
