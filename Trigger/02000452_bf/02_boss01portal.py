""" trigger/02000452_bf/02_boss01portal.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=30, visible=False, enabled=False, minimapVisible=False) # Boss01Spawn

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9900, spawnIds=[901]):
            return ActionPortal01()


class ActionPortal01(state.State):
    def on_enter(self):
        set_portal(portalId=30, visible=False, enabled=True, minimapVisible=False) # Boss01Spawn


