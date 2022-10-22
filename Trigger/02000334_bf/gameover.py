""" trigger/02000334_bf/gameover.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200,999], arg2=True) # 성벽

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[200]):
            return 게임오버()


class 게임오버(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[999]) # 게임오버용몬스터 소멸


