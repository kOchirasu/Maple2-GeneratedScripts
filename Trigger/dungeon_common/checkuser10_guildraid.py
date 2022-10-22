""" trigger/dungeon_common/checkuser10_guildraid.xml """
from common import *
import state


class CheckUser10_GuildRaid(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True, display=False, arg5=0) # 최대 30초 대기

    def on_tick(self) -> state.State:
        if count_users(boxId=9900, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start()
        if count_users(boxId=9900, boxId=10, operator='Less'):
            return MaxCount10_Wait()


class MaxCount10_Wait(state.State):
    def on_enter(self):
        show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> state.State:
        if count_users(boxId=9900, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start()
        if time_expired(timerId='1'):
            return MaxCount10_Start()
        if wait_tick(waitTick=6000):
            return MaxCount10_Wait()


class MaxCount10_Start(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if true():
            return state.DungeonStart()


