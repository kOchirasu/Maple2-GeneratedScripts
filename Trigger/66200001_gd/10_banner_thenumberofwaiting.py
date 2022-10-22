""" trigger/66200001_gd/10_banner_thenumberofwaiting.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn()


class BannerCheckIn(state.State):
    def on_enter(self):
        set_user_value_from_user_count(triggerBoxId=9021, key='BannerNumberOfBlue', userTagId=1)
        user_value_to_number_mesh(key='BannerNumberOfBlue', startMeshId=1500, digitCount=2)
        set_user_value_from_user_count(triggerBoxId=9022, key='BannerNumberOfRed', userTagId=2)
        user_value_to_number_mesh(key='BannerNumberOfRed', startMeshId=2500, digitCount=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NextWait()


class NextWait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn()
        if user_value(key='BannerCheckIn', value=0):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_user_value_from_user_count(triggerBoxId=9021, key='BannerNumberOfBlue', userTagId=1)
        user_value_to_number_mesh(key='BannerNumberOfBlue', startMeshId=1500, digitCount=2)
        set_user_value_from_user_count(triggerBoxId=9022, key='BannerNumberOfRed', userTagId=2)
        user_value_to_number_mesh(key='BannerNumberOfRed', startMeshId=2500, digitCount=2)


