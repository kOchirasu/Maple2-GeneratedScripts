""" trigger/51000003_dg/fail.xml """
import common


class gameset(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Fail', value=1):
            return Fail_condition(self.ctx)


class Fail_condition(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=799, boxId=1):
            return Fail(self.ctx)
        if self.count_users(boxId=705, boxId=1):
            return Fail(self.ctx)
        if not self.user_detected(boxIds=[701]):
            return Fail(self.ctx)


class Fail(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Ending_Popup_01')
        self.set_timer(timerId='10', seconds=10, interval=1)
        self.select_camera_path(pathIds=[8800], returnView=False) # 카메라 뒤로 당김
        self.arcade_boom_boom_ocean(type='EndGame')
        self.set_user_value(triggerId=991104, key='Reset', value=1) # wave_projectile.xml
        self.set_user_value(triggerId=991105, key='Reset', value=1) # wave_projectile_02.xml
        self.set_user_value(triggerId=991106, key='Reset', value=1) # cannon_projectile.xml
        self.set_user_value(triggerId=991107, key='Reset', value=1) # normal_projectile.xml
        self.set_user_value(triggerId=991108, key='Reset', value=1) # fog.xml
        self.set_user_value(triggerId=991111, key='Round_01', value=0) # item_01.xml
        self.set_user_value(triggerId=991120, key='Reset', value=1) # wave_projectile_03.xml
        self.set_user_value(triggerId=991121, key='Reset', value=1) # wave_projectile_04.xml
        self.set_user_value(triggerId=991122, key='Reset', value=1) # wave_projectile_05.xml
        self.set_user_value(triggerId=991123, key='Reset', value=1) # normal_projectile_02.xml

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return End(self.ctx)


class End(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0, boxId=705)


initial_state = gameset
