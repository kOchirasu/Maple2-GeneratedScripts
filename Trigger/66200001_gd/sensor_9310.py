""" trigger/66200001_gd/sensor_9310.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='Box31Check', value=10)
        set_mesh(triggerIds=[531], visible=True, arg3=0, arg4=0, arg5=0) # 31 / Ground outter
        set_mesh(triggerIds=[5310], visible=True, arg3=0, arg4=0, arg5=0) # 31 / Ground inner

    def on_tick(self) -> state.State:
        if user_value(key='Box31Check', value=0):
            return Sensor0()
        if user_value(key='Box31Check', value=1):
            return Sensor1()
        if user_value(key='Box31Check', value=2):
            return Sensor2()
        if user_value(key='Box31Check', value=3):
            return Sensor3()
        if user_value(key='Box31Check', value=4):
            return Sensor4()
        if user_value(key='Box31Check', value=5):
            return Sensor5()


class Sensor0(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Fail()


class Sensor1(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=1, operator='Equal'):
            return Pass()
        if not count_users(boxId=9310, boxId=1, operator='Equal'):
            return Fail()


class Sensor2(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=2, operator='Equal'):
            return Pass()
        if not count_users(boxId=9310, boxId=2, operator='Equal'):
            return Fail()


class Sensor3(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=3, operator='Equal'):
            return Pass()
        if not count_users(boxId=9310, boxId=3, operator='Equal'):
            return Fail()


class Sensor4(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=4, operator='Equal'):
            return Pass()
        if not count_users(boxId=9310, boxId=4, operator='Equal'):
            return Fail()


class Sensor5(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9310, boxId=5, operator='Equal'):
            return Pass()
        if not count_users(boxId=9310, boxId=5, operator='Equal'):
            return Fail()


class Pass(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9310], sound='DDStop_Stage_Pass_01')
        set_mesh(triggerIds=[531], visible=False, arg3=0, arg4=0, arg5=2) # 31 / Ground outter
        set_user_value(triggerId=7310, key='ColorReset', value=1) # color reset

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Reset()


class Fail(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9310], sound='DDStop_Stage_Fail_01')
        set_mesh(triggerIds=[531], visible=False, arg3=0, arg4=0, arg5=2) # 31 / Ground outter
        set_mesh(triggerIds=[5310], visible=False, arg3=0, arg4=0, arg5=0) # 31 / Ground inner
        set_user_value(triggerId=7310, key='ColorClear', value=1) # color clear

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_user_value(key='Box31Check', value=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()

