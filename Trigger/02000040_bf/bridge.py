""" trigger/02000040_bf/bridge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[301,302,303], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000319], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000319], stateValue=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[301,302,303], visible=True, arg3=0, delay=500, scale=2)
        self.set_timer(timerId='3', seconds=3, startDelay=0, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_mesh(triggerIds=[303,302,301], visible=False, arg3=0, delay=500, scale=2)
            return 재사용대기(self.ctx)


class 재사용대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='10', seconds=10, startDelay=0, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 대기(self.ctx)


initial_state = 대기
