""" trigger/02000312_bf/filter_10.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='1stTreeRemove', value=0)
        self.set_user_value(key='2ndTreeRemove', value=0)
        self.set_user_value(key='3rdTreeRemove', value=0)
        self.set_user_value(key='4thTreeRemove', value=0)
        self.set_user_value(key='5thTreeRemove', value=0)
        self.set_user_value(key='6thTreeRemove', value=0)
        self.set_user_value(key='7thTreeRemove', value=0)
        self.set_user_value(key='8thTreeRemove', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return CheckStart(self.ctx)


# 제거된 씨앗 체크
class CheckStart(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Check01(self.ctx)


class Check01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='1stTreeRemove', value=1):
            return Check02(self.ctx)
        if self.wait_tick(waitTick=2000):
            return CheckStart(self.ctx)


class Check02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='2ndTreeRemove', value=1):
            return Check03(self.ctx)
        if self.wait_tick(waitTick=2000):
            return CheckStart(self.ctx)


class Check03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='3rdTreeRemove', value=1):
            return Check04(self.ctx)
        if self.wait_tick(waitTick=2000):
            return CheckStart(self.ctx)


class Check04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='4thTreeRemove', value=1):
            return Check05(self.ctx)
        if self.wait_tick(waitTick=2000):
            return CheckStart(self.ctx)


class Check05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='5thTreeRemove', value=1):
            return Check06(self.ctx)
        if self.wait_tick(waitTick=2000):
            return CheckStart(self.ctx)


class Check06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='6thTreeRemove', value=1):
            return Check07(self.ctx)
        if self.wait_tick(waitTick=2000):
            return CheckStart(self.ctx)


class Check07(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='7thTreeRemove', value=1):
            return Check08(self.ctx)
        if self.wait_tick(waitTick=2000):
            return CheckStart(self.ctx)


class Check08(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='8thTreeRemove', value=1):
            return BoardApp(self.ctx)
        if self.wait_tick(waitTick=2000):
            return CheckStart(self.ctx)


class BoardApp(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='BoardApp', value=1)
        self.set_user_value(triggerId=11, key='MobWaveStop', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
