""" trigger/66000003_gd/enter.xml """
from common import *
import state


class 시간표확인(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_timer(timerId='60', seconds=30, clearAtZero=False, display=True)
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
        set_event_ui(type=1, arg2='$66000003_GD__ENTER__0$', arg3='6000', arg4='101')

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 어나운스1()


class 어나운스1(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False)
        set_event_ui(type=1, arg2='$65000001_BD__ENTER__1$', arg3='3000', arg4='101')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return PvP()


class PvP(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
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
        set_event_ui(type=3, arg2='$65000001_BD__ENTER__3$', arg3='5000', arg4='102') # action name="버프를걸어준다" arg1="102" arg2="70000063" arg3="1"/

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 보상()


class 보상(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=15) # action name="이벤트UI를설정한다" arg1="3" arg2="$65000001_BD__ENTER__4$" arg3="5000" arg4="102"/>
      <action name="이벤트UI를설정한다" arg1="6" arg2="$65000001_BD__ENTER__5$" arg3="5000" arg4="!102"/>
      <action name="아이템을생성한다" arg1="9001,9002,9003" />
      <action name="아이템을생성한다" arg1="9004" arg2="104" /

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


