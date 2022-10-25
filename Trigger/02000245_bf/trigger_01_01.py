""" trigger/02000245_bf/trigger_01_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000302], state=1)
        self.set_mesh(triggerIds=[701,702], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000302], stateValue=0):
            return 개봉(self.ctx)


class 개봉(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[701,702], visible=False)
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
