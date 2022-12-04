""" trigger/02000253_bf/wall_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_mesh(triggerIds=[501,502], visible=True)
        self.set_mesh(triggerIds=[601,602,603], visible=True)
        self.set_interact_object(triggerIds=[10000437], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000437], stateValue=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_mesh(triggerIds=[501,502], visible=False)
        self.set_mesh(triggerIds=[601,602,603], visible=False)


initial_state = 대기
