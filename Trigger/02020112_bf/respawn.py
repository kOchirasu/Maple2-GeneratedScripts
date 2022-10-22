""" trigger/02020112_bf/respawn.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        limit_spawn_npc_count(limitCount=200)
        set_user_value(key='respawn', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=1):
            return 스폰시작()
        if user_value(key='respawn', value=2):
            return 종료()


class 스폰시작(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020112_BF__RESPAWN__0$', arg3='5000')
        create_monster(spawnIds=[141,142,143,144], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return 종료()
        if true():
            return 대기()


class 종료(state.State):
    pass


