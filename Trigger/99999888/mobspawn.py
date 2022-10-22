""" trigger/99999888/mobspawn.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=911, boxId=1):
            create_monster(spawnIds=[101], arg2=True)
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=101, additionalEffectId=50000900, level=1):
            debug_string(string='버프가감지되었습니다. 20초 후 삭제합니다')
            return 버프삭제()


class 버프삭제(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            debug_string(string='버프가 삭제되었습니다.')
            npc_remove_additional_effect(spawnId=101, additionalEffectId=50000900)
            return 종료()


class 종료(state.State):
    pass


