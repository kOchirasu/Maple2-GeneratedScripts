""" trigger/02020051_bf/107_text.xml """
import common


class 가이드시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Text', value=1):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 가이드_1(self.ctx)


class 가이드_1(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', script='$02020051_BF__107_TEXT__0$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Text', value=2):
            return 가이드시작(self.ctx)


initial_state = 가이드시작
