""" trigger/61000005_me/wait.xml """
import common


class 입장(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='90', seconds=90, startDelay=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[196]):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$61000005_ME__WAIT__0$', arg3='5000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=196, boxId=20):
            return 시작(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 대기(self.ctx)
        if self.time_expired(timerId='90'):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$61000005_ME__WAIT__1$', arg3='3000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 입장
