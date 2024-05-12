""" trigger/02020112_bf/safezone2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990017, key='Safe', value=0)
        self.set_interact_object(triggerIds=[10002118], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[903], jobCode=0):
            return 안전장치_활성화(self.ctx)


class 안전장치_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=8, visible=True, enable=True, minimapVisible=False)
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False)
        self.set_interact_object(triggerIds=[10002118], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002118], stateValue=0):
            return 안전장치_작동(self.ctx)


class 안전장치_작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020112_BF__SAFEZONE2__0$', arg3='5000')
        self.set_user_value(triggerId=99990017, key='Safe', value=1)


initial_state = 대기
