""" trigger/02000349_bf/wall_15.xml """
import common


class 벽재생(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520], visible=True, arg3=0, delay=10, scale=3)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[115]):
            return 벽삭제(self.ctx)


class 벽삭제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520], visible=False, arg3=0, delay=10, scale=3)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[115]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벽재생(self.ctx)


initial_state = 벽재생
