""" trigger/52000014_qd/collapse_2000.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2000,2001,2002,2003,2004], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[12000], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22000], visible=False) # Vibrate Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 무너짐01(self.ctx)


class 무너짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=2)
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2000__0$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 무너짐02(self.ctx)


class 무너짐02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='4', seconds=8)
        self.set_effect(triggerIds=[12000], visible=True) # Vibrate Short
        self.set_effect(triggerIds=[22000], visible=True) # Vibrate Sound
        self.set_random_mesh(triggerIds=[2000,2001,2002,2003,2004], visible=False, meshCount=5, arg4=0, delay=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return None # Missing State: 무너짐03


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[12000], visible=False) # Vibrate Short
        self.set_effect(triggerIds=[22000], visible=False) # Vibrate Sound


initial_state = 대기
