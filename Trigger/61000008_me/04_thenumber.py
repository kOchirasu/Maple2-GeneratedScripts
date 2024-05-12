""" trigger/61000008_me/04_thenumber.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn(self.ctx)


class BannerCheckIn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=9001, min_users='50', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=50)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='49', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=49)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='48', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=48)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='47', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=47)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='46', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=46)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='45', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=45)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='44', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=44)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='43', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=43)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='42', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=42)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='41', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=41)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='40', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=40)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='39', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=39)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='38', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=38)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='37', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=37)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='36', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=36)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='35', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=35)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='34', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=34)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='33', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=33)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='32', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=32)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='31', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=31)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='30', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=30)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='29', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=29)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='28', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=28)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='27', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=27)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='26', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=26)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='25', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=25)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='24', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=24)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='23', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=23)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='22', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=22)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='21', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=21)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='20', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=20)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='19', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=19)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='18', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=18)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='17', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=17)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='16', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=16)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='15', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=15)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='14', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=14)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='13', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=13)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='12', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=12)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='11', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=11)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='10', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=10)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='9', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=9)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='8', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=8)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='7', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=7)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='6', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=6)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='5', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=5)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='4', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=4)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='3', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=3)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='2', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=2)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if self.count_users(box_id=9001, min_users='1', operator='Equal'):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=1)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)
        if not self.user_detected(box_ids=[9001]):
            self.set_user_value(trigger_id=5, key='BannerNumber', value=0)
            self.set_user_value(trigger_id=5, key='SetBanner', value=1)
            return Reset(self.ctx)


class Reset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='BannerCheckIn', value=0)
        self.set_user_value(key='BannerNumber', value=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
