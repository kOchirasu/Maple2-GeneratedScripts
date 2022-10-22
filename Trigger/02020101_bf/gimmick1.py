""" trigger/02020101_bf/gimmick1.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='summon', value=1):
            return 몬스터소환()
        if monster_dead(boxIds=[101]):
            return 종료()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,202,203,204], arg2=False)
        set_user_value(triggerId=900003, key='summon', value=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if wait_tick(waitTick=3000):
            return 대기()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,202,203,204], arg2=False)
        set_user_value(triggerId=900003, key='summon', value=2)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


