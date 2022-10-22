""" trigger/66200001_gd/11_banner_thenumberofsurvivor.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn()


class BannerCheckIn(state.State):
    def on_enter(self):
        set_user_value_from_user_count(triggerBoxId=9001, key='BannerNumberOfBlue', userTagId=1)
        user_value_to_number_mesh(key='BannerNumberOfBlue', startMeshId=700, digitCount=2)
        set_user_value_from_user_count(triggerBoxId=9001, key='BannerNumberOfRed', userTagId=2)
        user_value_to_number_mesh(key='BannerNumberOfRed', startMeshId=1700, digitCount=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NextWait()

    def on_exit(self):
        set_user_value(key='BannerCheckIn', value=0)


class NextWait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn()


