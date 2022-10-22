""" trigger/51000003_dg/fail.xml """
from common import *
import state


class gameset(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Fail', value=1):
            return Fail_condition()


class Fail_condition(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=799, boxId=1):
            return Fail()
        if count_users(boxId=705, boxId=1):
            return Fail()
        if not user_detected(boxIds=[701]):
            return Fail()


class Fail(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Ending_Popup_01')
        set_timer(timerId='10', seconds=10, display=True)
        select_camera_path(pathIds=[8800], returnView=False) # 카메라 뒤로 당김
        arcade_boom_boom_ocean(type='EndGame')
        set_user_value(triggerId=991104, key='Reset', value=1) # wave_projectile.xml
        set_user_value(triggerId=991105, key='Reset', value=1) # wave_projectile_02.xml
        set_user_value(triggerId=991106, key='Reset', value=1) # cannon_projectile.xml
        set_user_value(triggerId=991107, key='Reset', value=1) # normal_projectile.xml
        set_user_value(triggerId=991108, key='Reset', value=1) # fog.xml
        set_user_value(triggerId=991111, key='Round_01', value=0) # item_01.xml
        set_user_value(triggerId=991120, key='Reset', value=1) # wave_projectile_03.xml
        set_user_value(triggerId=991121, key='Reset', value=1) # wave_projectile_04.xml
        set_user_value(triggerId=991122, key='Reset', value=1) # wave_projectile_05.xml
        set_user_value(triggerId=991123, key='Reset', value=1) # normal_projectile_02.xml

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return End()


class End(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0, boxId=705)


