""" trigger/02000252_bf/bigdoor_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[165,166,167,168], visible=True)
        self.set_interact_object(triggerIds=[10000406], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000406], stateValue=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[9001], triggerId=998)
        self.set_mesh(triggerIds=[165,166,167,168], visible=False)


initial_state = 대기
