""" trigger/80000007_bonus/trigger_09.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[158]):
            return 벽삭제(self.ctx)


class 벽삭제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 벽재생(self.ctx)


class 벽재생(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[158]):
            return 대기(self.ctx)


initial_state = 대기
