""" trigger/02010070_bf/wind.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='wind01', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[999994]):
            return Start(self.ctx)


class Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], visible=True, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='wind01', value=1):
            return Change(self.ctx)


class Change(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[30], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[31], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[50], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[49], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[56], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[39], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[41], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[40], visible=False, start_delay=0, interval=0, fade=0)


initial_state = Wait
