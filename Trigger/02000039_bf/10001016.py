""" trigger/02000039_bf/10001016.xml """
import trigger_api


class 오브젝트반응대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10001016], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001016], stateValue=0):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 오브젝트반응대기(self.ctx)


initial_state = 오브젝트반응대기
