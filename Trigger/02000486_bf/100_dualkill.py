""" trigger/02000486_bf/100_dualkill.xml """
from common import *
import state


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return Wait()


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='CheckDualKill', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='CheckDualKill', value=1):
            return CheckDualKill()


class CheckDualKill(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            return LionBlueDead()
        if monster_dead(boxIds=[901]):
            return LionRedDead()


class LionBlueDead(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[901]):
            set_achievement(triggerId=9900, type='trigger', achieve='ChangeLionDualKill')
            return Quit()
        if wait_tick(waitTick=2000):
            return Quit()


class LionRedDead(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900]):
            set_achievement(triggerId=9900, type='trigger', achieve='ChangeLionDualKill')
            return Quit()
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    pass


