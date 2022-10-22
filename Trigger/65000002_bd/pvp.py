""" trigger/65000002_bd/pvp.xml """
from common import *
import state


class 시간표확인(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_timer(timerId='60', seconds=60, clearAtZero=False, display=True)
        set_effect(triggerIds=[601], visible=False) # 공지 효과음
        set_effect(triggerIds=[602], visible=False) # 종료 효과음

    def on_tick(self) -> state.State:
        if count_users(boxId=102, boxId=10):
            return 어나운스0()
        if time_expired(timerId='60'):
            return 대기()

    def on_exit(self):
        reset_timer(timerId='60')


class 대기(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=102, boxId=2):
            return 어나운스0()
        if not count_users(boxId=102, boxId=2):
            return 비김()


class 어나운스0(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6, clearAtZero=False)
        play_system_sound_in_box(sound='BD_PVP_00')
        set_event_ui(type=1, arg2='$65000002_BD__PVP__0$', arg3='6000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 어나운스1()


class 어나운스1(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6, clearAtZero=False)
        play_system_sound_in_box(sound='BD_PVP_01')
        set_event_ui(type=1, arg2='$65000002_BD__PVP__1$', arg3='6000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 어나운스2()


class 어나운스2(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6, clearAtZero=False)
        play_system_sound_in_box(sound='BD_PVP_02')
        set_event_ui(type=1, arg2='$65000002_BD__PVP__2$', arg3='6000', arg4='101')

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 어나운스3()


class 어나운스3(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False)
        play_system_sound_in_box(sound='BD_PVP_03')
        set_event_ui(type=1, arg2='$65000002_BD__PVP__3$', arg3='3000')
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return PvP()


class PvP(state.State):
    def on_enter(self):
        set_achievement(triggerId=101, type='trigger', achieve='dailyquest_start') # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        give_guild_exp(boxId=0, type=2)
        add_buff(boxIds=[101], skillId=70000088, level=1, arg4=False, arg5=False)
        add_buff(boxIds=[101], skillId=70000089, level=1, arg4=False, arg5=False)
        set_timer(timerId='1', seconds=1, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            set_pvp_zone(boxId=101, arg2=5, duration=300, additionalEffectId=90001002, arg5=2)
            return PvP종료()


class PvP종료(state.State):
    def on_tick(self) -> state.State:
        if pvp_zone_ended(boxId=101):
            return 경기종료()


class 경기종료(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4, clearAtZero=False)
        play_system_sound_in_box(sound='BD_PVP_04')
        set_event_ui(type=1, arg2='$65000002_BD__PVP__4$', arg3='3000', arg4='101')
        set_effect(triggerIds=[602], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 완료()


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


