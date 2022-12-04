""" trigger/02000471_bf/interactcheck.xml """
import trigger_api


class check(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2040314, key='InteractClear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return clear(self.ctx)


class clear(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2040314, key='InteractClear', value=1)
        self.set_user_value(triggerId=2040322, key='InteractClear', value=1)


initial_state = check
