""" trigger/65000001_bd/enter.xml """
from common import *
import state


class 시간표확인(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_timer(timerId='60', seconds=60, clearAtZero=False, display=True)
        set_effect(triggerIds=[601], visible=False) # 공지 효과음

    def on_tick(self) -> state.State:
        if count_users(boxId=101, boxId=10):
            return 어나운스0()
        if time_expired(timerId='60'):
            return 대기()

    def on_exit(self):
        reset_timer(timerId='60')


class 대기(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=101, boxId=2):
            return 어나운스0()
        if not count_users(boxId=101, boxId=2):
            return 비김()


class 어나운스0(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6, clearAtZero=False)
        play_system_sound_in_box(sound='BD_Enter_00')
        set_event_ui(type=1, arg2='$65000001_BD__ENTER__0$', arg3='6000', arg4='101')

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 어나운스1()


class 어나운스1(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False)
        play_system_sound_in_box(sound='BD_Enter_01')
        set_event_ui(type=1, arg2='$65000001_BD__ENTER__1$', arg3='3000', arg4='101')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return PvP()


class PvP(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_achievement(triggerId=105, type='trigger', achieve='dailyquest_start')
            give_guild_exp(boxId=0, type=2)
            set_pvp_zone(boxId=102, arg2=1, duration=120, additionalEffectId=90001002, arg5=1)
            return PvP종료()


class PvP종료(state.State):
    def on_tick(self) -> state.State:
        if pvp_zone_ended(boxId=102):
            return 게임종료()


class 비김(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_event_ui(type=5, arg2='$65000001_BD__ENTER__2$', arg3='3000', arg4='0')
            return 완료()


class 게임종료(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=6)
        set_event_ui(type=0, arg2='0,0')
        set_event_ui(type=3, arg2='$65000001_BD__ENTER__3$', arg3='5000', arg4='102')
        add_buff(boxIds=[102], skillId=70000063, level=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 보상()


class 보상(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=15)
        play_system_sound_in_box(boxIds=[102], sound='BD_Enter_04')
        play_system_sound_in_box(boxIds=[103], sound='BD_Enter_05')
        set_event_ui(type=3, arg2='$65000001_BD__ENTER__4$', arg3='5000', arg4='102')
        set_event_ui(type=6, arg2='$65000001_BD__ENTER__5$', arg3='5000', arg4='!102')
        create_item(spawnIds=[9001,9002,9003])
        create_item(spawnIds=[9004], triggerId=104)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 완료()


class 완료(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            move_user(mapId=0, portalId=0)
            return 종료()


class 종료(state.State):
    pass


