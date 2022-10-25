""" trigger/63000076_cs/63000076_chat_706.xml """
import common


class 준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[706]):
            return 잡담_01_706(self.ctx)


class 잡담_01_706(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=118, msg='$63000076_CS__63000076_CHAT_706__0$', duration=2500, delayTick=0) # 신발… 아…이 신발, 신어보고 싶어요

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 준비
