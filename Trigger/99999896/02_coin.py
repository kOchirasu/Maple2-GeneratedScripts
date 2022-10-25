""" trigger/99999896/02_coin.xml """
import common


class 동전생성01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            self.set_timer(timerId='1', seconds=2)
            self.create_item(spawnIds=[4,5,6,7,8,9,10,11,12])
            self.set_event_ui(type=1, arg2='$99999896__02_COIN__0$', arg3='2000')
            return 동전생성02(self.ctx)


class 동전생성02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            self.create_item(spawnIds=[13,14,15,16,17,18,19,20,21])
            self.set_event_ui(type=1, arg2='$99999896__02_COIN__1$', arg3='2000')
            return 동전생성03(self.ctx)


class 동전생성03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            self.set_event_ui(type=1, arg2='$99999896__02_COIN__2$', arg3='2000')
            self.create_item(spawnIds=[22,23,24,25,26,27,28,29,30])
            self.set_event_ui(type=3, arg2='$99999896__02_COIN__3$', arg3='2000')
            self.create_item(spawnIds=[31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48])
            return 완료(self.ctx)


class 완료(common.Trigger):
    pass


initial_state = 동전생성01
