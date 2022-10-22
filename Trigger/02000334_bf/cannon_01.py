""" trigger/02000334_bf/cannon_01.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98010], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='cannon_01', value=1):
            return 마킹비표시()


class 마킹비표시(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98010], visible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90011, spawnIds=[190]):
            return 마킹표시()


class 마킹표시(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98010], visible=True)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=90011, spawnIds=[190]):
            return 마킹비표시()


