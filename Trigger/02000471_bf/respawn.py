""" trigger/02000471_bf/respawn.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=1):
            return respawn_timer1()


class respawn_timer1(state.State):
    def on_enter(self):
        set_timer(timerId='respawntimer1', seconds=120, clearAtZero=True, display=False, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if time_expired(timerId='respawntimer1'):
            return respawn1()


class respawn1(state.State):
    def on_enter(self):
        reset_timer(timerId='respawntimer1')
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if not monster_dead(boxIds=[1999]):
            return respawn_timer2()


class respawn_timer2(state.State):
    def on_enter(self):
        set_timer(timerId='respawntimer2', seconds=120, clearAtZero=True, display=False, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if time_expired(timerId='respawntimer2'):
            return respawn2()


class respawn2(state.State):
    def on_enter(self):
        reset_timer(timerId='respawntimer2')
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if not monster_dead(boxIds=[1999]):
            return respawn_timer3()


class respawn_timer3(state.State):
    def on_enter(self):
        set_timer(timerId='respawntimer3', seconds=120, clearAtZero=True, display=False, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if time_expired(timerId='respawntimer3'):
            return respawn3()


class respawn3(state.State):
    def on_enter(self):
        reset_timer(timerId='respawntimer3')
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if not monster_dead(boxIds=[1999]):
            return respawn_timer4()


class respawn_timer4(state.State):
    def on_enter(self):
        set_timer(timerId='respawntimer4', seconds=120, clearAtZero=True, display=False, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if time_expired(timerId='respawntimer4'):
            return respawn4()


class respawn4(state.State):
    def on_enter(self):
        reset_timer(timerId='respawntimer4')
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if not monster_dead(boxIds=[1999]):
            return respawn_timer5()


class respawn_timer5(state.State):
    def on_enter(self):
        set_timer(timerId='respawntimer5', seconds=120, clearAtZero=True, display=False, arg5=0)

    def on_tick(self) -> state.State:
        if user_value(key='respawn', value=2):
            return end()
        if time_expired(timerId='respawntimer5'):
            return respawn5()


class respawn5(state.State):
    def on_enter(self):
        reset_timer(timerId='respawntimer5')
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return end()


class end(state.State):
    pass


