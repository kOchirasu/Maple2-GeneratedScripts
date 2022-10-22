""" trigger/02020063_bf/object5.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[715], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='TurretSpawn_5', value=1):
            return 터렛_활성화()


class 터렛_활성화(state.State):
    def on_enter(self):
        create_monster(spawnIds=[715], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='TurretSpawn_5', value=0):
            return 대기()
        if monster_dead(boxIds=[715]):
            return 터렛_비활성화()
        if monster_dead(boxIds=[801]):
            return 종료()


class 터렛_비활성화(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='TurretSpawn_5', value=0):
            return 대기()
        if monster_dead(boxIds=[801]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[715], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='TurretSpawn_5', value=1):
            return 대기()


