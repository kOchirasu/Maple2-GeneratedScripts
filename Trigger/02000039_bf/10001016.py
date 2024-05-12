""" trigger/02000039_bf/10001016.xml """
import trigger_api


class 오브젝트반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], visible=True, start_delay=0, interval=0, fade=0)
        self.set_interact_object(trigger_ids=[10001016], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001016], state=0):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], visible=False, start_delay=0, interval=0, fade=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 오브젝트반응대기(self.ctx)


initial_state = 오브젝트반응대기
