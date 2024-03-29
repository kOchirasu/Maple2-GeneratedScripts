""" trigger/99999925/ladder01.xml """
import trigger_api


class ladderIdle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001077], stateValue=0):
            return ladderWolk(self.ctx)


class ladderWolk(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[701], visible=False, arg3=1)
        self.set_ai_extra_data(key='LadderCnt', value=1, isModify=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ladderEnd(self.ctx)


class ladderEnd(trigger_api.Trigger):
    pass


initial_state = ladderIdle
