""" trigger/61000008_me/sensor_9340.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='Box34Check', value=10)
        set_mesh(triggerIds=[534], visible=True, arg3=0, arg4=0, arg5=0) # 34 / Ground outter
        set_mesh(triggerIds=[5340], visible=True, arg3=0, arg4=0, arg5=0) # 34 / Ground inner

    def on_tick(self) -> state.State:
        if user_value(key='Box34Check', value=0):
            return Sensor0()
        if user_value(key='Box34Check', value=1):
            return Sensor1()
        if user_value(key='Box34Check', value=2):
            return Sensor2()
        if user_value(key='Box34Check', value=3):
            return Sensor3()
        if user_value(key='Box34Check', value=4):
            return Sensor4()
        if user_value(key='Box34Check', value=5):
            return Sensor5()


class Sensor0(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Fail()


class Sensor1(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=1, operator='Equal'):
            return Pass()
        if not count_users(boxId=9340, boxId=1, operator='Equal'):
            return Fail()


class Sensor2(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=2, operator='Equal'):
            return Pass()
        if not count_users(boxId=9340, boxId=2, operator='Equal'):
            return Fail()


class Sensor3(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=3, operator='Equal'):
            return Pass()
        if not count_users(boxId=9340, boxId=3, operator='Equal'):
            return Fail()


class Sensor4(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=4, operator='Equal'):
            return Pass()
        if not count_users(boxId=9340, boxId=4, operator='Equal'):
            return Fail()


class Sensor5(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9340, boxId=5, operator='Equal'):
            return Pass()
        if not count_users(boxId=9340, boxId=5, operator='Equal'):
            return Fail()


class Pass(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Pass_01')
        set_user_value(triggerId=7340, key='Color34', value=0) # color reset
        set_mesh(triggerIds=[534], visible=False, arg3=0, arg4=0, arg5=2) # 34 / Ground outter

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Reset()


class Fail(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9340], sound='DDStop_Stage_Fail_01')
        set_mesh(triggerIds=[534], visible=False, arg3=0, arg4=0, arg5=2) # 34 / Ground outter
        set_mesh(triggerIds=[5340], visible=False, arg3=0, arg4=0, arg5=0) # 34 / Ground inner
        set_user_value(triggerId=7340, key='Color34', value=4) # color clear

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_user_value(key='Box34Check', value=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()

