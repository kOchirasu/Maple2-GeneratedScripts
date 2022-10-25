""" trigger/51000001_dg/endgame.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[144]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='0,0')
        self.select_camera(triggerId=344, enable=True)
        # action name="이벤트UI를설정한다" arg1="5" arg2="게임 오버" arg3="2000" arg4="0" /

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.play_system_sound_in_box(sound='System_Ending_Popup_01')
            self.arcade_spring_farm(type='EndGame')
            return 진짜끝(self.ctx)


class 진짜끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10, startDelay=0, interval=1, vOffset=-30, type='TR')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 퇴장(self.ctx)


class 퇴장(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0)


initial_state = 대기
