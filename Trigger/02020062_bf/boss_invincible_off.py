""" trigger/02020062_bf/boss_invincible_off.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BombPhase', value=2):
            return 무적해제안내()


class 무적해제안내(state.State):
    def on_enter(self):
        add_buff(boxIds=[9002], skillId=70002371, level=1, arg5=False) # <유저 웨폰 오브젝트 떨구기>
        set_event_ui(type=1, arg2='$02020062_BF__BOSS_INVINCIBLE_OFF__0$', arg3='5000')

    def on_tick(self) -> state.State:
        if user_value(key='BossClear', value=1):
            return 종료()


class 종료(state.State):
    pass


