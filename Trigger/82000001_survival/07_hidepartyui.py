""" trigger/82000001_survival/07_hidepartyui.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='HidePartyUI', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return HidePartyUI(self.ctx)


class HidePartyUI(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_ui(uiNames=['PartyDialog'], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return HidePartyUI(self.ctx)
        if self.user_value(key='HidePartyUI', value=1):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Setting
