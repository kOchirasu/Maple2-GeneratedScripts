""" trigger/80000014_bonus/lever.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001314], state=1)
        self.set_mesh(triggerIds=[3501,3502,3503,3504,3505,3506], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 안내(self.ctx)
        if self.object_interacted(interactIds=[10001314], stateValue=0):
            return 문열림(self.ctx)


class 안내(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$80000014_bonus__lever__0$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001314], stateValue=0):
            return 문열림(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 반응대기(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3501,3502,3503,3504,3505,3506], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
