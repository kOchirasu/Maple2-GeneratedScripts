""" trigger/51000004_dg/fail.xml """
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
        write_log(logName='PinkBeanThreeTwoOne_log', event='9001', arg3='char_event', arg5='gameover')
        set_timer(timerId='10', seconds=10, display=True)
        select_camera_path(pathIds=[8011,8010], returnView=False) # 카메라 뒤로 당김
        arcade_three_two_one(type='EndGame')

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return End()


class End(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)


