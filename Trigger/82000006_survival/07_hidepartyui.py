""" trigger/82000006_survival/07_hidepartyui.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='HidePartyUI', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return HidePartyUI(self.ctx)


class HidePartyUI(common.Trigger):
    def on_enter(self):
        self.set_visible_ui(uiNames=['PartyDialog'], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return HidePartyUI(self.ctx)
        if self.user_value(key='HidePartyUI', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Setting
