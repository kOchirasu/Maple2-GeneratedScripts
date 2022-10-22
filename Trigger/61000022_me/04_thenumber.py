""" trigger/61000022_me/04_thenumber.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BannerCheckIn', value=1):
            return BannerCheckIn()


class BannerCheckIn(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=50)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=49, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=49)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=48, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=48)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=47, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=47)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=46, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=46)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=45, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=45)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=44, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=44)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=43, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=43)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=42, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=42)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=41, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=41)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=40, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=40)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=39, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=39)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=38, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=38)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=37, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=37)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=36, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=36)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=35, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=35)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=34, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=34)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=33, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=33)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=32, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=32)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=31, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=31)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=30, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=30)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=29, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=29)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=28, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=28)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=27, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=27)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=26, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=26)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=25, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=25)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=24, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=24)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=23, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=23)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=22, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=22)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=21, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=21)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=20, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=20)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=19, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=19)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=18, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=18)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=17, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=17)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=16, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=16)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=15, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=15)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=14, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=14)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=13, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=13)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=12, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=12)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=11, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=11)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=10, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=10)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=9, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=9)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=8, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=8)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=7, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=7)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=6, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=6)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=5, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=5)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=4, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=4)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=3, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=3)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=2, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=2)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if count_users(boxId=9001, boxId=1, operator='Equal'):
            set_user_value(triggerId=5, key='BannerNumber', value=1)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()
        if not user_detected(boxIds=[9001]):
            set_user_value(triggerId=5, key='BannerNumber', value=0)
            set_user_value(triggerId=5, key='SetBanner', value=1)
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_user_value(key='BannerCheckIn', value=0)
        set_user_value(key='BannerNumber', value=100)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


