""" trigger/65000003_bd/pvp.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='60', seconds=60, clearAtZero=False, display=True)

    def on_tick(self) -> state.State:
        if count_users(boxId=104, boxId=20):
            return PvP()
        if time_expired(timerId='60'):
            return 대기()

    def on_exit(self):
        reset_timer(timerId='60')


class 대기(state.State):
    def on_enter(self):
        reset_timer(timerId='1')

    def on_tick(self) -> state.State:
        if count_users(boxId=104, boxId=2):
            return PvP()
        if not count_users(boxId=104, boxId=2):
            return 비김()


class PvP(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1, clearAtZero=False)
        set_achievement(triggerId=104, type='trigger', achieve='dailyquest_start') # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        give_guild_exp(boxId=0, type=2)
        set_pvp_zone(boxId=104, arg2=3, duration=600, additionalEffectId=90001002, arg5=3, boxIds=[1,2,101,102,103])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 문열림()


class 문열림(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return PvP종료()


class PvP종료(state.State):
    def on_tick(self) -> state.State:
        if pvp_zone_ended(boxId=104):
            return 게임종료()


class 게임종료(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 종료()


class 비김(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_event_ui(type=5, arg2='$65000002_BD__PVP__5$', arg3='3000', arg4='0')
            return 완료()


class 완료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            move_user(mapId=0, portalId=0)
            return 종료()


class 종료(state.State):
    pass


