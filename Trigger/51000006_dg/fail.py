""" trigger/51000006_dg/fail.xml """
from common import *
import state


class gameset(state.State):
    def on_enter(self):
        select_camera(triggerId=8011, enable=False) # 카메라 옆으로 보냄, 줌인

    def on_tick(self) -> state.State:
        if user_value(key='Fail', value=1):
            return Fail_condition()


class Fail_condition(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return Fail()


class Fail(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_PinkBeans_Arcade_Result_01')
        write_log(logName='ThreeTwoOne_log', event='9001', arg3='char_event', arg5='BlackbeanThreeTwoOnegameover') # 로그를 남기기 위한 행 : arg5가 트리거 전체에서 유니크한 값이 들어가야 하며, arg1은 코드에 남고 있지 않음(서바이벌일 때만 서바이벌 로그 불러옴)
        set_timer(timerId='10', seconds=10, display=True)
        select_camera_path(pathIds=[8011,8010], returnView=False) # 카메라 뒤로 당김
        arcade_three_two_one(type='EndGame')

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return End()


class End(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0) # 게임에 들어오기 전에 있던 맵으로 강제이동


