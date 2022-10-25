""" trigger/02000349_bf/wall_16.xml """
import common


class 벽재생(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623,31624,31625], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[116]):
            return 벽삭제(self.ctx)


class 벽삭제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623,31624,31625], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[116]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
