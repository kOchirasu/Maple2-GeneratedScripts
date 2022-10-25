""" trigger/61000022_me/sensor_9330.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='Box33Check', value=10)
        self.set_mesh(triggerIds=[533], visible=True, arg3=0, delay=0, scale=0) # 33 / Ground outter
        self.set_mesh(triggerIds=[5330], visible=True, arg3=0, delay=0, scale=0) # 33 / Ground inner

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Box33Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box33Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box33Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box33Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box33Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box33Check', value=5):
            return Sensor5(self.ctx)
        if self.user_value(key='Box33Check', value=7):
            return Sensor7(self.ctx)
        if self.user_value(key='Box33Check', value=8):
            return Sensor8(self.ctx)
        if self.user_value(key='Box33Check', value=9):
            return Sensor9(self.ctx)
        if self.user_value(key='Box33Check', value=6):
            return Sensor10(self.ctx)
        if self.user_value(key='Box33Check', value=15):
            return Sensor15(self.ctx)
        if self.user_value(key='Box33Check', value=20):
            return Sensor20(self.ctx)
        if self.user_value(key='Box33Check', value=25):
            return Sensor25(self.ctx)
        if self.user_value(key='Box33Check', value=30):
            return Sensor30(self.ctx)


class Sensor0(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return Fail(self.ctx)


class Sensor1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=1, operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=1, operator='Equal'):
            return Fail(self.ctx)


class Sensor2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=2, operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=2, operator='Equal'):
            return Fail(self.ctx)


class Sensor3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=3, operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=3, operator='Equal'):
            return Fail(self.ctx)


class Sensor4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=4, operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=4, operator='Equal'):
            return Fail(self.ctx)


class Sensor5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=5, operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=5, operator='Equal'):
            return Fail(self.ctx)


class Sensor7(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=7, operator='Equal'):
            return GamblePass(self.ctx)
        if not self.count_users(boxId=9330, boxId=7, operator='Equal'):
            return Fail(self.ctx)


class Sensor8(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=8, operator='Equal'):
            return GamblePass(self.ctx)
        if not self.count_users(boxId=9330, boxId=8, operator='Equal'):
            return Fail(self.ctx)


class Sensor9(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=9, operator='Equal'):
            return GamblePass(self.ctx)
        if not self.count_users(boxId=9330, boxId=9, operator='Equal'):
            return Fail(self.ctx)


class Sensor10(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=10, operator='Equal'):
            return GamblePass(self.ctx)
        if not self.count_users(boxId=9330, boxId=10, operator='Equal'):
            return Fail(self.ctx)


class Sensor15(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=15, operator='Equal'):
            return JackpotPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=15, operator='Equal'):
            return Fail(self.ctx)


class Sensor20(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=20, operator='Equal'):
            return JackpotPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=20, operator='Equal'):
            return Fail(self.ctx)


class Sensor25(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=25, operator='Equal'):
            return JackpotPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=25, operator='Equal'):
            return Fail(self.ctx)


class Sensor30(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9330, boxId=30, operator='Equal'):
            return JackpotPass(self.ctx)
        if not self.count_users(boxId=9330, boxId=30, operator='Equal'):
            return Fail(self.ctx)


class NormalPass(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Pass_01')
        self.set_user_value(triggerId=7330, key='Color33', value=0) # color reset
        self.set_mesh(triggerIds=[533], visible=False, arg3=0, delay=0, scale=2) # 33 / Ground outter

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class GamblePass(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Pass_01')
        self.set_user_value(triggerId=7330, key='Color33', value=0) # color reset
        self.set_user_value(triggerId=3, key='GamblePass', value=33) # Gamble Pass Bonus For Everyone
        self.set_mesh(triggerIds=[533], visible=False, arg3=0, delay=0, scale=2) # 33 / Ground outter
        self.write_log(logName='dancedancestop', triggerId=9330, event='char_event', arg4=4, subEvent='gamble')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return GambleReset(self.ctx)


class JackpotPass(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Pass_01')
        self.set_user_value(triggerId=7330, key='Color33', value=0) # color reset
        self.set_user_value(triggerId=3, key='JackpotPass', value=33) # Jackpot Pass Bonus For Everyone
        self.set_mesh(triggerIds=[533], visible=False, arg3=0, delay=0, scale=2) # 33 / Ground outter
        self.write_log(logName='dancedancestop', triggerId=9330, event='char_event', arg4=4, subEvent='jackpot')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return JackpotReset(self.ctx)


class Fail(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9330], sound='DDStop_Stage_Fail_01')
        self.set_mesh(triggerIds=[533], visible=False, arg3=0, delay=0, scale=2) # 33 / Ground outter
        self.set_mesh(triggerIds=[5330], visible=False, arg3=0, delay=0, scale=0) # 33 / Ground inner
        self.set_user_value(triggerId=7330, key='Color33', value=4) # color clear

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Reset(self.ctx)


class GambleReset(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9330, type='trigger', achieve='ddstop_gamble')
        self.mini_game_give_exp(boxId=9330, expRate=0.1, isOutside=False) # Gamble Pass Bonus For challenger
        self.set_user_value(key='Box33Check', value=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


class JackpotReset(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9330, type='trigger', achieve='ddstop_gamble')
        self.mini_game_give_exp(boxId=9330, expRate=0.3, isOutside=False) # Jackpot Pass Bonus For challenger
        self.set_user_value(key='Box33Check', value=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='Box33Check', value=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
