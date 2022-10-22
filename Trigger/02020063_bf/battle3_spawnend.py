""" trigger/02020063_bf/battle3_spawnend.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[811,812,813,814]):
            set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=0)
            return None


