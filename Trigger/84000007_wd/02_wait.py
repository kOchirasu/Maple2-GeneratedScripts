""" trigger/84000007_wd/02_wait.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=40, startDelay=1, interval=0) # 테스트 수정 가능 지점

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100001, textId=26100001, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9000, boxId=70):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기2(self.ctx)
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 대기2(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26100002, textId=26100002, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9000, boxId=70):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
