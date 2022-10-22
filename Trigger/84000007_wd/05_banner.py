""" trigger/84000007_wd/05_banner.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2) # Banner10
        set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2) # Banner1
        set_mesh(triggerIds=[711,712,713,714,715,716,717], visible=False, arg3=0, arg4=0, arg5=0) # Banner10
        set_mesh(triggerIds=[701,702,703,704,705,706,707,708,709], visible=False, arg3=0, arg4=0, arg5=0) # Banner1

    def on_tick(self) -> state.State:
        if true():
            return NextWait()

    def on_exit(self):
        set_user_value(key='SetBanner', value=0)


class SetBanner(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if user_value(key='BannerNumber', value=70):
            set_mesh(triggerIds=[717], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=69):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[709], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=68):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[708], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=67):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[707], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=66):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[706], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=65):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[705], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=64):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[704], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=63):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[703], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=62):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[702], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=61):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[701], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=60):
            set_mesh(triggerIds=[716], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=59):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[709], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=58):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[708], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=57):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[707], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=56):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[706], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=55):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[705], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=54):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[704], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=53):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[703], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=52):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[702], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=51):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[701], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=50):
            set_mesh(triggerIds=[715], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=49):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[709], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=48):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[708], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=47):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[707], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=46):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[706], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=45):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[705], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=44):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[704], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=43):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[703], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=42):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[702], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=41):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[701], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=40):
            set_mesh(triggerIds=[714], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=39):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[709], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=38):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[708], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=37):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[707], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=36):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[706], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=35):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[705], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=34):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[704], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=33):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[703], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=32):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[702], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=31):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[701], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=30):
            set_mesh(triggerIds=[713], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=29):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[709], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=28):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[708], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=27):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[707], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=26):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[706], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=25):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[705], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=24):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[704], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=23):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[703], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=22):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[702], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=21):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[701], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=20):
            set_mesh(triggerIds=[712], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=19):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[709], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=18):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[708], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=17):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[707], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=16):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[706], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=15):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[705], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=14):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[704], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=13):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[703], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=12):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[702], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=11):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[701], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=10):
            set_mesh(triggerIds=[711], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=9):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[709], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=8):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[708], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=7):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[707], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=6):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[706], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=5):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[705], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=4):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[704], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=3):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[703], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=2):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[702], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=1):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[701], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()
        if user_value(key='BannerNumber', value=0):
            set_mesh(triggerIds=[710], visible=True, arg3=0, arg4=0, arg5=2)
            set_mesh(triggerIds=[700], visible=True, arg3=0, arg4=0, arg5=2)
            return NextWait()

    def on_exit(self):
        set_user_value(key='SetBanner', value=0)


class NextWait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SetBanner', value=1):
            return SetBanner()


