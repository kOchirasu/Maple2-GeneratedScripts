""" trigger/81000003_item/trigger_04.xml """
from common import *
import state


class 레버(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[510,511,512,513,514,515,516], visible=True)
        set_effect(triggerIds=[701], visible=False)
        set_effect(triggerIds=[702], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[401]):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[510,511,512,513,514,515,516], visible=False)
        set_effect(triggerIds=[701], visible=True)
        set_effect(triggerIds=[702], visible=True)
        set_timer(timerId='11', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 폭죽끄기()


class 폭죽끄기(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=120)
        set_effect(triggerIds=[701], visible=False)
        set_effect(triggerIds=[702], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 레버()


