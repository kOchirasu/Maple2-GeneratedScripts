""" trigger/82000002_survival/07_hidepartyui.xml """
from common import *
import state


class Setting(state.State):
    def on_enter(self):
        set_user_value(key='HidePartyUI', value=0)


class HidePartyUI(state.State):
    def on_enter(self):
        set_visible_ui(uiNames=['PartyDialog'], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return HidePartyUI()
        if user_value(key='HidePartyUI', value=1):
            return Quit()


class Quit(state.State):
    pass


