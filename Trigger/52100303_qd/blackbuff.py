""" trigger/52100303_qd/blackbuff.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000607], state=0)
        self.set_interact_object(triggerIds=[12000607], state=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[801]):
            return 오브젝트체크(self.ctx)
        """
        <condition  name="WaitTick" waitTick="3000"  >
            <action name="오브젝트반응설정한다" arg1="12000407" arg2="1" />
            <transition state="대기이"/>
        </condition>
        """


class 대기이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)
        if self.user_detected(boxIds=[801]):
            return 오브젝트체크(self.ctx)


class 오브젝트체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000606], stateValue=0):
            return 오브젝트재생성(self.ctx)


class 오브젝트재생성(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_interact_object(triggerIds=[12000606], state=1)
            return 오브젝트체크(self.ctx)


initial_state = 대기
