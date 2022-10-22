""" trigger/02000489_bf/main.xml """
from common import *
import state


class ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6001], visible=False)
        set_mesh(triggerIds=[6002], visible=False)
        set_mesh(triggerIds=[6003], visible=False)
        set_mesh(triggerIds=[6004], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return chaos_raid()


class chaos_raid(state.State):
    def on_enter(self):
        create_monster(spawnIds=[402], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ExitPortal', value=1):
            return end()


class end(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)


