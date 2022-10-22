""" trigger/02020051_bf/107_text.xml """
from common import *
import state


class 가이드시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Text', value=1):
            return 대기()


class 대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 가이드_1()


class 가이드_1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', script='$02020051_BF__107_TEXT__0$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 종료(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Text', value=2):
            return 가이드시작()


