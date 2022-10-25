""" trigger/61000022_me/04_thenumber.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn(self.ctx)


class BannerCheckIn(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9001, boxId=50, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=50)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=49, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=49)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=48, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=48)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=47, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=47)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=46, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=46)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=45, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=45)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=44, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=44)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=43, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=43)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=42, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=42)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=41, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=41)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=40, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=40)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=39, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=39)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=38, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=38)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=37, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=37)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=36, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=36)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=35, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=35)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=34, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=34)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=33, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=33)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=32, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=32)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=31, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=31)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=30, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=30)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=29, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=29)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=28, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=28)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=27, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=27)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=26, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=26)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=25, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=25)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=24, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=24)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=23, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=23)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=22, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=22)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=21, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=21)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=20, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=20)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=19, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=19)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=18, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=18)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=17, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=17)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=16, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=16)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=15, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=15)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=14, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=14)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=13, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=13)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=12, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=12)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=11, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=11)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=10, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=10)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=9, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=9)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=8, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=8)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=7, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=7)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=6, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=6)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=5, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=5)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=4, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=4)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=3, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=3)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=2, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=2)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, boxId=1, operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=1)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if not self.user_detected(boxIds=[9001]):
            self.set_user_value(triggerId=5, key='BannerNumber', value=0)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='BannerCheckIn', value=0)
        self.set_user_value(key='BannerNumber', value=100)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
