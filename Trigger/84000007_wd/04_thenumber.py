""" trigger/84000007_wd/04_thenumber.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn(self.ctx)


class BannerCheckIn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9001, minUsers='70', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=70)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='69', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=69)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='68', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=68)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='67', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=67)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='66', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=66)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='65', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=65)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='64', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=64)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='63', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=63)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='62', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=62)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='61', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=61)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='60', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=60)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='59', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=59)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='58', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=58)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='57', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=57)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='56', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=56)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='55', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=55)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='54', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=54)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='53', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=53)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='52', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=52)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='51', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=51)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='50', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=50)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='49', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=49)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='48', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=48)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='47', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=47)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='46', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=46)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='45', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=45)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='44', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=44)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='43', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=43)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='42', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=42)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='41', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=41)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='40', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=40)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='39', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=39)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='38', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=38)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='37', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=37)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='36', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=36)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='35', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=35)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='34', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=34)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='33', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=33)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='32', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=32)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='31', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=31)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='30', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=30)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='29', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=29)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='28', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=28)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='27', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=27)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='26', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=26)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='25', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=25)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='24', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=24)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='23', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=23)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='22', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=22)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='21', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=21)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='20', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=20)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='19', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=19)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='18', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=18)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='17', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=17)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='16', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=16)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='15', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=15)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='14', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=14)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='13', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=13)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='12', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=12)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='11', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=11)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='10', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=10)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='9', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=9)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='8', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=8)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='7', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=7)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='6', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=6)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='5', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=5)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='4', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=4)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='3', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=3)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='2', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=2)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(boxId=9001, minUsers='1', operator='Equal'):
            self.set_user_value(triggerId=5, key='BannerNumber', value=1)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if not self.user_detected(boxIds=[9001]):
            self.set_user_value(triggerId=5, key='BannerNumber', value=0)
            self.set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='BannerCheckIn', value=0)
        self.set_user_value(key='BannerNumber', value=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
