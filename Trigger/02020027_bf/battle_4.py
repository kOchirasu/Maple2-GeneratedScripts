""" trigger/02020027_bf/battle_4.xml """
from common import *
import state


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 전투시작_2()


class 전투시작_2(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='summon_2_2', value=1):
            return 몬스터소환()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401,402,403,404,405,406])
        set_conversation(type=1, spawnId=401, script='$02020027_BF__battle_1__1$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=403, script='$02020027_BF__battle_1__2$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=405, script='$02020027_BF__battle_1__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[401,402,403,404,405,406]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[201], skillId=62000002, level=1, arg4=True)
        add_buff(boxIds=[201], skillId=51200002, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if true():
            return None


