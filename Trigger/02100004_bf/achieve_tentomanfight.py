""" trigger/02100004_bf/achieve_tentomanfight.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='LastRoundStart', value=0)
        set_user_value(key='LastRoundEnd', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='LastRoundStart', value=1):
            return MobCheck01()


class MobCheck01(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[2000]):
            return MobCheck02()


class MobCheck02(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return CheckSuccess()
        if user_value(key='LastRoundEnd', value=1):
            return Quit()


class CheckSuccess(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000]):
            return MemberCheck()
        if user_value(key='LastRoundEnd', value=1):
            return Quit()


class MemberCheck(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=102, boxId=10, operator='Equal'):
            return Achieve()
        if user_value(key='LastRoundEnd', value=1):
            return Quit()


class Achieve(state.State):
    def on_enter(self):
        set_achievement(triggerId=102, type='trigger', achieve='TenToOneFight')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    pass


