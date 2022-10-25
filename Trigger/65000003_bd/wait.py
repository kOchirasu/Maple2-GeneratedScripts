""" trigger/65000003_bd/wait.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='60', seconds=60, startDelay=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return 어나운스01(self.ctx)


class 어나운스01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26500301, textId=26500301, duration=4500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어나운스01(self.ctx)
        if self.count_users(boxId=104, boxId=2):
            return 종료(self.ctx)
        if self.time_expired(timerId='60'):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=26500301)


class 종료(common.Trigger):
    pass


initial_state = 시작
