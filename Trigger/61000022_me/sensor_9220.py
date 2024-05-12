""" trigger/61000022_me/sensor_9220.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box22Check', value=10)
        self.set_mesh(trigger_ids=[522], visible=True, start_delay=0, interval=0, fade=0) # 22 / Ground outter
        self.set_mesh(trigger_ids=[5220], visible=True, start_delay=0, interval=0, fade=0) # 22 / Ground inner

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Box22Check', value=0):
            return Sensor0(self.ctx)
        if self.user_value(key='Box22Check', value=1):
            return Sensor1(self.ctx)
        if self.user_value(key='Box22Check', value=2):
            return Sensor2(self.ctx)
        if self.user_value(key='Box22Check', value=3):
            return Sensor3(self.ctx)
        if self.user_value(key='Box22Check', value=4):
            return Sensor4(self.ctx)
        if self.user_value(key='Box22Check', value=5):
            return Sensor5(self.ctx)
        if self.user_value(key='Box22Check', value=7):
            return Sensor7(self.ctx)
        if self.user_value(key='Box22Check', value=8):
            return Sensor8(self.ctx)
        if self.user_value(key='Box22Check', value=9):
            return Sensor9(self.ctx)
        if self.user_value(key='Box22Check', value=6):
            return Sensor10(self.ctx)
        if self.user_value(key='Box22Check', value=15):
            return Sensor15(self.ctx)
        if self.user_value(key='Box22Check', value=20):
            return Sensor20(self.ctx)
        if self.user_value(key='Box22Check', value=25):
            return Sensor25(self.ctx)
        if self.user_value(key='Box22Check', value=30):
            return Sensor30(self.ctx)


class Sensor0(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return Fail(self.ctx)


class Sensor1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='1', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='1', operator='Equal'):
            return Fail(self.ctx)


class Sensor2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='2', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='2', operator='Equal'):
            return Fail(self.ctx)


class Sensor3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='3', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='3', operator='Equal'):
            return Fail(self.ctx)


class Sensor4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='4', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='4', operator='Equal'):
            return Fail(self.ctx)


class Sensor5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='5', operator='Equal'):
            return NormalPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='5', operator='Equal'):
            return Fail(self.ctx)


class Sensor7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='7', operator='Equal'):
            return GamblePass(self.ctx)
        if not self.count_users(box_id=9220, min_users='7', operator='Equal'):
            return Fail(self.ctx)


class Sensor8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='8', operator='Equal'):
            return GamblePass(self.ctx)
        if not self.count_users(box_id=9220, min_users='8', operator='Equal'):
            return Fail(self.ctx)


class Sensor9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='9', operator='Equal'):
            return GamblePass(self.ctx)
        if not self.count_users(box_id=9220, min_users='9', operator='Equal'):
            return Fail(self.ctx)


class Sensor10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='10', operator='Equal'):
            return GamblePass(self.ctx)
        if not self.count_users(box_id=9220, min_users='10', operator='Equal'):
            return Fail(self.ctx)


class Sensor15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='15', operator='Equal'):
            return JackpotPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='15', operator='Equal'):
            return Fail(self.ctx)


class Sensor20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='20', operator='Equal'):
            return JackpotPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='20', operator='Equal'):
            return Fail(self.ctx)


class Sensor25(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='25', operator='Equal'):
            return JackpotPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='25', operator='Equal'):
            return Fail(self.ctx)


class Sensor30(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9220, min_users='30', operator='Equal'):
            return JackpotPass(self.ctx)
        if not self.count_users(box_id=9220, min_users='30', operator='Equal'):
            return Fail(self.ctx)


class NormalPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7220, key='Color22', value=0) # color reset
        self.set_mesh(trigger_ids=[522], visible=False, start_delay=0, interval=0, fade=2) # 22 / Ground outter

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class GamblePass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7220, key='Color22', value=0) # color reset
        # Gamble Pass Bonus For Everyone
        self.set_user_value(trigger_id=3, key='GamblePass', value=22)
        self.set_mesh(trigger_ids=[522], visible=False, start_delay=0, interval=0, fade=2) # 22 / Ground outter
        self.write_log(log_name='dancedancestop', trigger_id=9220, event='char_event', arg4=4, sub_event='gamble')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return GambleReset(self.ctx)


class JackpotPass(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Pass_01')
        self.set_user_value(trigger_id=7220, key='Color22', value=0) # color reset
        # Jackpot Pass Bonus For Everyone
        self.set_user_value(trigger_id=3, key='JackpotPass', value=22)
        self.set_mesh(trigger_ids=[522], visible=False, start_delay=0, interval=0, fade=2) # 22 / Ground outter
        self.write_log(log_name='dancedancestop', trigger_id=9220, event='char_event', arg4=4, sub_event='jackpot')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return JackpotReset(self.ctx)


class Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9220], sound='DDStop_Stage_Fail_01')
        self.set_mesh(trigger_ids=[522], visible=False, start_delay=0, interval=0, fade=2) # 22 / Ground outter
        self.set_mesh(trigger_ids=[5220], visible=False, start_delay=0, interval=0, fade=0) # 22 / Ground inner
        self.set_user_value(trigger_id=7220, key='Color22', value=4) # color clear

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Reset(self.ctx)


class GambleReset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9220, type='trigger', achieve='ddstop_gamble')
        # Gamble Pass Bonus For challenger
        self.mini_game_give_exp(box_id=9220, exp_rate=0.1, is_outside=False)
        # self.create_item(spawn_ids=[7100,7101,7102,7102,7103,7104,7105,7106,7107,7108,7109,7110,7111,7112], trigger_id=9220)
        self.set_user_value(key='Box22Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


class JackpotReset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9220, type='trigger', achieve='ddstop_gamble')
        # Jackpot Pass Bonus For challenger
        self.mini_game_give_exp(box_id=9220, exp_rate=0.3, is_outside=False)
        # self.create_item(spawn_ids=[7500,7501,7502,7502,7503,7504,7505,7506,7507,7508,7509,7510,7511,7512], trigger_id=9220)
        self.set_user_value(key='Box22Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='Box22Check', value=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
