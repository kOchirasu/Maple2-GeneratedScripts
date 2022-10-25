""" trigger/66200001_gd/11_banner_thenumberofsurvivor.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn(self.ctx)


class BannerCheckIn(common.Trigger):
    def on_enter(self):
        self.set_user_value_from_user_count(triggerBoxId=9001, key='BannerNumberOfBlue', userTagId=1)
        self.user_value_to_number_mesh(key='BannerNumberOfBlue', startMeshId=700, digitCount=2)
        self.set_user_value_from_user_count(triggerBoxId=9001, key='BannerNumberOfRed', userTagId=2)
        self.user_value_to_number_mesh(key='BannerNumberOfRed', startMeshId=1700, digitCount=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NextWait(self.ctx)

    def on_exit(self):
        self.set_user_value(key='BannerCheckIn', value=0)


class NextWait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn(self.ctx)


initial_state = Wait
