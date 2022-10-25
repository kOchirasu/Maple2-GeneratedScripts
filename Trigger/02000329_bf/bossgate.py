""" trigger/02000329_bf/bossgate.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[710]):
            return 사다리가이드(self.ctx)


class 사다리가이드(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=106, textId=20000060) # 다음 지역으로 이동하세요
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 대기(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=106)


initial_state = 대기
