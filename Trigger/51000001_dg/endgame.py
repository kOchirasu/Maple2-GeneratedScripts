""" trigger/51000001_dg/endgame.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[144]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        select_camera(triggerId=344, enable=True) # action name="이벤트UI를설정한다" arg1="5" arg2="게임 오버" arg3="2000" arg4="0" /

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            play_system_sound_in_box(sound='System_Ending_Popup_01')
            arcade_spring_farm(type='EndGame')
            return 진짜끝()


class 진짜끝(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10, clearAtZero=False, display=True, arg5=-30, arg6='TR')

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 퇴장()


class 퇴장(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)


