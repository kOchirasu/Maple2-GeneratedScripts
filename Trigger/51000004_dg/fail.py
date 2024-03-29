""" trigger/51000004_dg/fail.xml """
import trigger_api


class gameset(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8011, enable=False) # 카메라 옆으로 보냄, 줌인

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Fail', value=1):
            return Fail_condition(self.ctx)


class Fail_condition(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return Fail(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Result_01')
        self.write_log(logName='PinkBeanThreeTwoOne_log', triggerId=9001, event='char_event', subEvent='gameover')
        self.set_timer(timerId='10', seconds=10, interval=1)
        self.select_camera_path(pathIds=[8011,8010], returnView=False) # 카메라 뒤로 당김
        self.arcade_three_two_one(type='EndGame')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0)


initial_state = gameset
