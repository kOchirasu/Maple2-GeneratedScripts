""" trigger/02020311_bf/blackbuff.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000406], state=0)
        self.set_interact_object(triggerIds=[12000406], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[801]):
            return 오브젝트체크(self.ctx)
        """
        <condition  name="WaitTick" waitTick="3000"  >
            <action name="오브젝트반응설정한다" arg1="12000406" arg2="1" />
            <transition state="대기이"/>
        </condition>
        """


class 대기이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)
        if self.user_detected(boxIds=[801]):
            return 오브젝트체크(self.ctx)


class 오브젝트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000406], stateValue=0):
            return 오브젝트재생성(self.ctx)


class 오브젝트재생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_interact_object(triggerIds=[12000406], state=1)
            return 오브젝트체크(self.ctx)


initial_state = 대기
