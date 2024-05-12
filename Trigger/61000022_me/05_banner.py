""" trigger/61000022_me/05_banner.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2) # Banner10
        self.set_mesh(trigger_ids=[700], visible=True, start_delay=0, interval=0, fade=2) # Banner1
        self.set_mesh(trigger_ids=[711,712,713,714,715], visible=False, start_delay=0, interval=0, fade=0) # Banner10
        self.set_mesh(trigger_ids=[701,702,703,704,705,706,707,708,709], visible=False, start_delay=0, interval=0, fade=0) # Banner1

    def on_tick(self) -> trigger_api.Trigger:
        return NextWait(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(key='SetBanner', value=0)


class SetBanner(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715], visible=False, start_delay=0, interval=0, fade=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BannerNumber', value=50):
            self.set_mesh(trigger_ids=[715], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[700], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=49):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[709], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=48):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[708], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=47):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[707], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=46):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[706], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=45):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[705], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=44):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[704], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=43):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[703], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=42):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[702], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=41):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[701], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=40):
            self.set_mesh(trigger_ids=[714], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[700], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=39):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[709], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=38):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[708], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=37):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[707], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=36):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[706], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=35):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[705], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=34):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[704], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=33):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[703], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=32):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[702], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=31):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[701], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=30):
            self.set_mesh(trigger_ids=[713], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[700], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=29):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[709], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=28):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[708], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=27):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[707], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=26):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[706], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=25):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[705], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=24):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[704], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=23):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[703], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=22):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[702], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=21):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[701], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=20):
            self.set_mesh(trigger_ids=[712], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[700], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=19):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[709], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=18):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[708], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=17):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[707], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=16):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[706], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=15):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[705], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=14):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[704], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=13):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[703], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=12):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[702], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=11):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[701], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=10):
            self.set_mesh(trigger_ids=[711], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[700], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=9):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[709], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=8):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[708], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=7):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[707], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=6):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[706], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=5):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[705], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=4):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[704], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=3):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[703], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=2):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[702], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=1):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[701], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)
        if self.user_value(key='BannerNumber', value=0):
            self.set_mesh(trigger_ids=[710], visible=True, start_delay=0, interval=0, fade=2)
            self.set_mesh(trigger_ids=[700], visible=True, start_delay=0, interval=0, fade=2)
            return NextWait(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(key='SetBanner', value=0)


class NextWait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SetBanner', value=1):
            return SetBanner(self.ctx)


initial_state = Wait
