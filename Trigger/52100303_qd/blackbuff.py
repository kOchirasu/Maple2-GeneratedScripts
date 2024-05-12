""" trigger/52100303_qd/blackbuff.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000607], state=0)
        self.set_interact_object(triggerIds=[12000607], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.wait_tick(waitTick=3000):
            self.set_interact_object(triggerIds=[12000407], state=1)
            return 대기이(self.ctx)
        """
        if self.user_detected(boxIds=[801]):
            return 오브젝트체크(self.ctx)


class 대기이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)
        if self.user_detected(boxIds=[801]):
            return 오브젝트체크(self.ctx)


class 오브젝트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000606], stateValue=0):
            return 오브젝트재생성(self.ctx)


class 오브젝트재생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_interact_object(triggerIds=[12000606], state=1)
            return 오브젝트체크(self.ctx)


initial_state = 대기
