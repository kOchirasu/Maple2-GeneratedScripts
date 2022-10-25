""" trigger/61000002_me_002/wait.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='60', seconds=60, startDelay=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[301]):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='ME_001_Wait_00')
        self.show_guide_summary(entityId=26100001, textId=26100001)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=301, boxId=50):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기2(self.ctx)
        if self.time_expired(timerId='60'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=26100001)


class 대기2(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='ME_001_Wait_00')
        self.show_guide_summary(entityId=26100002, textId=26100002)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=301, boxId=50):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)
        if self.time_expired(timerId='60'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=26100002)


class 종료(common.Trigger):
    pass


initial_state = 시작
