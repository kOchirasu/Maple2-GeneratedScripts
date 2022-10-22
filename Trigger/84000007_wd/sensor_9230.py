""" trigger/84000007_wd/sensor_9230.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='Box23Check', value=10)
        set_mesh(triggerIds=[523], visible=True, arg3=0, arg4=0, arg5=0) # 23 / Ground outter
        set_mesh(triggerIds=[5230], visible=True, arg3=0, arg4=0, arg5=0) # 23 / Ground inner

    def on_tick(self) -> state.State:
        if user_value(key='Box23Check', value=0):
            return Sensor0()
        if user_value(key='Box23Check', value=1):
            return Sensor1()
        if user_value(key='Box23Check', value=2):
            return Sensor2()
        if user_value(key='Box23Check', value=3):
            return Sensor3()
        if user_value(key='Box23Check', value=4):
            return Sensor4()
        if user_value(key='Box23Check', value=5):
            return Sensor5()
        if user_value(key='Box23Check', value=7):
            return Sensor7()
        if user_value(key='Box23Check', value=8):
            return Sensor8()
        if user_value(key='Box23Check', value=9):
            return Sensor9()
        if user_value(key='Box23Check', value=6):
            return Sensor10()
        if user_value(key='Box23Check', value=15):
            return Sensor15()
        if user_value(key='Box23Check', value=20):
            return Sensor20()
        if user_value(key='Box23Check', value=25):
            return Sensor25()
        if user_value(key='Box23Check', value=30):
            return Sensor30()


class Sensor0(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Fail()


class Sensor1(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=1, operator='Equal'):
            return NormalPass()
        if not count_users(boxId=9230, boxId=1, operator='Equal'):
            return Fail()


class Sensor2(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=2, operator='Equal'):
            return NormalPass()
        if not count_users(boxId=9230, boxId=2, operator='Equal'):
            return Fail()


class Sensor3(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=3, operator='Equal'):
            return NormalPass()
        if not count_users(boxId=9230, boxId=3, operator='Equal'):
            return Fail()


class Sensor4(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=4, operator='Equal'):
            return NormalPass()
        if not count_users(boxId=9230, boxId=4, operator='Equal'):
            return Fail()


class Sensor5(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=5, operator='Equal'):
            return NormalPass()
        if not count_users(boxId=9230, boxId=5, operator='Equal'):
            return Fail()


class Sensor7(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=7, operator='Equal'):
            return GamblePass()
        if not count_users(boxId=9230, boxId=7, operator='Equal'):
            return Fail()


class Sensor8(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=8, operator='Equal'):
            return GamblePass()
        if not count_users(boxId=9230, boxId=8, operator='Equal'):
            return Fail()


class Sensor9(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=9, operator='Equal'):
            return GamblePass()
        if not count_users(boxId=9230, boxId=9, operator='Equal'):
            return Fail()


class Sensor10(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=10, operator='Equal'):
            return GamblePass()
        if not count_users(boxId=9230, boxId=10, operator='Equal'):
            return Fail()


class Sensor15(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=15, operator='Equal'):
            return JackpotPass()
        if not count_users(boxId=9230, boxId=15, operator='Equal'):
            return Fail()


class Sensor20(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=20, operator='Equal'):
            return JackpotPass()
        if not count_users(boxId=9230, boxId=20, operator='Equal'):
            return Fail()


class Sensor25(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=25, operator='Equal'):
            return JackpotPass()
        if not count_users(boxId=9230, boxId=25, operator='Equal'):
            return Fail()


class Sensor30(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9230, boxId=30, operator='Equal'):
            return JackpotPass()
        if not count_users(boxId=9230, boxId=30, operator='Equal'):
            return Fail()


class NormalPass(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Pass_01')
        set_user_value(triggerId=7230, key='Color23', value=0) # color reset
        set_mesh(triggerIds=[523], visible=False, arg3=0, arg4=0, arg5=2) # 23 / Ground outter

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Reset()


class GamblePass(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Pass_01')
        set_user_value(triggerId=7230, key='Color23', value=0) # color reset
        set_user_value(triggerId=3, key='GamblePass', value=23) # Gamble Pass Bonus For Everyone
        set_mesh(triggerIds=[523], visible=False, arg3=0, arg4=0, arg5=2) # 23 / Ground outter
        write_log(logName='dancedancestop', event='9230', arg3='char_event', arg4='4', arg5='gamble')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return GambleReset()


class JackpotPass(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Pass_01')
        set_user_value(triggerId=7230, key='Color23', value=0) # color reset
        set_user_value(triggerId=3, key='JackpotPass', value=23) # Jackpot Pass Bonus For Everyone
        set_mesh(triggerIds=[523], visible=False, arg3=0, arg4=0, arg5=2) # 23 / Ground outter
        write_log(logName='dancedancestop', event='9230', arg3='char_event', arg4='4', arg5='jackpot')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return JackpotReset()


class Fail(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9230], sound='DDStop_Stage_Fail_01')
        set_mesh(triggerIds=[523], visible=False, arg3=0, arg4=0, arg5=2) # 23 / Ground outter
        set_mesh(triggerIds=[5230], visible=False, arg3=0, arg4=0, arg5=0) # 23 / Ground inner
        set_user_value(triggerId=7230, key='Color23', value=4) # color clear

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Reset()


class GambleReset(state.State):
    def on_enter(self):
        set_achievement(triggerId=9230, type='trigger', achieve='ddstop_gamble')
        mini_game_give_exp(boxId=9230, expRate=0.1, isOutside=False) # Gamble Pass Bonus For challenger
        set_user_value(key='Box23Check', value=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


class JackpotReset(state.State):
    def on_enter(self):
        set_achievement(triggerId=9230, type='trigger', achieve='ddstop_gamble')
        mini_game_give_exp(boxId=9230, expRate=0.3, isOutside=False) # Jackpot Pass Bonus For challenger
        set_user_value(key='Box23Check', value=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


class Reset(state.State):
    def on_enter(self):
        set_user_value(key='Box23Check', value=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()

