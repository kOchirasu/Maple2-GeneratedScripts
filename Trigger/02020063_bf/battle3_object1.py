""" trigger/02020063_bf/battle3_object1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[811], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='Battle3_TurretSpawn_1', value=1):
            return 터렛_활성화()


class 터렛_활성화(state.State):
    def on_enter(self):
        create_monster(spawnIds=[811], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='Battle3_TurretSpawn_1', value=0):
            return 대기()
        if monster_dead(boxIds=[811]):
            return 터렛_비활성화()
        if monster_dead(boxIds=[801]):
            return 종료()


class 터렛_비활성화(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Battle3_TurretSpawn_1', value=0):
            return 대기()
        if monster_dead(boxIds=[801]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[811], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='Battle3_TurretSpawn_1', value=0):
            return 대기()


