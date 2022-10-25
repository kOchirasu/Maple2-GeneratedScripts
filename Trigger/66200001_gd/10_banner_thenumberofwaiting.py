""" trigger/66200001_gd/10_banner_thenumberofwaiting.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn(self.ctx)


class BannerCheckIn(common.Trigger):
    def on_enter(self):
        self.set_user_value_from_user_count(triggerBoxId=9021, key='BannerNumberOfBlue', userTagId=1)
        self.user_value_to_number_mesh(key='BannerNumberOfBlue', startMeshId=1500, digitCount=2)
        self.set_user_value_from_user_count(triggerBoxId=9022, key='BannerNumberOfRed', userTagId=2)
        self.user_value_to_number_mesh(key='BannerNumberOfRed', startMeshId=2500, digitCount=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NextWait(self.ctx)


class NextWait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn(self.ctx)
        if self.user_value(key='BannerCheckIn', value=0):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_user_value_from_user_count(triggerBoxId=9021, key='BannerNumberOfBlue', userTagId=1)
        self.user_value_to_number_mesh(key='BannerNumberOfBlue', startMeshId=1500, digitCount=2)
        self.set_user_value_from_user_count(triggerBoxId=9022, key='BannerNumberOfRed', userTagId=2)
        self.user_value_to_number_mesh(key='BannerNumberOfRed', startMeshId=2500, digitCount=2)


initial_state = Wait
