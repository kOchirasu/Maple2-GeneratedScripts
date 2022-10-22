""" trigger/02100000_bf/spawnpoint.xml """
from common import *
import state


class 리스폰변경_1(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return None


