""" trigger/02020025_bf/background.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903]):
            return 지하배경()


class 지하배경(state.State):
    def on_enter(self):
        change_background(dds='BG_Cave_D.dds')

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[903]):
            return 지상배경()


class 지상배경(state.State):
    def on_enter(self):
        change_background(dds='BG_Tria.dds')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903]):
            return 지하배경()


