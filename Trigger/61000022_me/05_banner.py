""" trigger/61000022_me/05_banner.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2) # Banner10
        self.set_mesh(triggerIds=[700], visible=True, arg3=0, delay=0, scale=2) # Banner1
        self.set_mesh(triggerIds=[711,712,713,714,715], visible=False, arg3=0, delay=0, scale=0) # Banner10
        self.set_mesh(triggerIds=[701,702,703,704,705,706,707,708,709], visible=False, arg3=0, delay=0, scale=0) # Banner1

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NextWait(self.ctx)

    def on_exit(self):
        self.set_user_value(key='SetBanner', value=0)


class SetBanner(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BannerNumber', value=50):
            self.set_mesh(triggerIds=[715], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[700], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=49):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[709], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=48):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[708], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=47):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[707], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=46):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[706], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=45):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[705], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=44):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[704], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=43):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[703], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=42):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[702], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=41):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[701], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=40):
            self.set_mesh(triggerIds=[714], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[700], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=39):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[709], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=38):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[708], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=37):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[707], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=36):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[706], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=35):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[705], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=34):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[704], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=33):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[703], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=32):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[702], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=31):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[701], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=30):
            self.set_mesh(triggerIds=[713], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[700], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=29):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[709], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=28):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[708], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=27):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[707], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=26):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[706], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=25):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[705], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=24):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[704], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=23):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[703], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=22):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[702], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=21):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[701], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=20):
            self.set_mesh(triggerIds=[712], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[700], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=19):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[709], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=18):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[708], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=17):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[707], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=16):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[706], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=15):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[705], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=14):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[704], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=13):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[703], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=12):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[702], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=11):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[701], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=10):
            self.set_mesh(triggerIds=[711], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[700], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=9):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[709], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=8):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[708], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=7):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[707], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=6):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[706], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=5):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[705], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=4):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[704], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=3):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[703], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=2):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[702], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=1):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[701], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=0):
            self.set_mesh(triggerIds=[710], visible=True, arg3=0, delay=0, scale=2)
            self.set_mesh(triggerIds=[700], visible=True, arg3=0, delay=0, scale=2)
            return NextWait(self.ctx)

    def on_exit(self):
        self.set_user_value(key='SetBanner', value=0)


class NextWait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SetBanner', value=1):
            return SetBanner(self.ctx)


initial_state = Wait
