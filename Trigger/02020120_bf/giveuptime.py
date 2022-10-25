""" trigger/02020120_bf/giveuptime.xml """
import common


# 이 트리거 사용 안함
class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 타이머(self.ctx)


class 타이머(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
