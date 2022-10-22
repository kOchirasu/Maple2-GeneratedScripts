""" trigger/02020101_bf/gimmick2.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Plant', value=1):
            return 몬스터소환()
        if monster_dead(boxIds=[101]):
            return 종료()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301,302,303,304], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if wait_tick(waitTick=1000):
            return 힌트()


class 힌트(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020101_BF__GIMMICK2__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if wait_tick(waitTick=4000):
            return 알림()


class 알림(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if wait_tick(waitTick=25000):
            return 종료()
        if monster_dead(boxIds=[301,302,303,304]):
            set_user_value(triggerId=900009, key='Seed', value=1)
            set_user_value(triggerId=900004, key='Plant', value=0)
            return 대기()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[301,302,303,304], arg2=False)
        set_user_value(triggerId=900004, key='Plant', value=0)
        set_user_value(triggerId=900009, key='Seed', value=0)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


