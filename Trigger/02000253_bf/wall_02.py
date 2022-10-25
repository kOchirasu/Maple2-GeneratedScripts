""" trigger/02000253_bf/wall_02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_mesh(triggerIds=[503,504], visible=True)
        self.set_mesh(triggerIds=[604,605,606], visible=True)
        self.set_interact_object(triggerIds=[10000438], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000438], stateValue=0):
            return 열기(self.ctx)


class 열기(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_mesh(triggerIds=[503,504], visible=False)
        self.set_mesh(triggerIds=[604,605,606], visible=False)


initial_state = 대기
