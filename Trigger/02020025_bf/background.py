""" trigger/02020025_bf/background.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[903]):
            return 지하배경(self.ctx)


class 지하배경(common.Trigger):
    def on_enter(self):
        self.change_background(dds='BG_Cave_D.dds')

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[903]):
            return 지상배경(self.ctx)


class 지상배경(common.Trigger):
    def on_enter(self):
        self.change_background(dds='BG_Tria.dds')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[903]):
            return 지하배경(self.ctx)


initial_state = 대기
