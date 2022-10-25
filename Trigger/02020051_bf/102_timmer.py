""" trigger/02020051_bf/102_timmer.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='990')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Timmer', value=1):
            return 타이머(self.ctx)


class 타이머(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='990', seconds=600, startDelay=1, interval=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=600000):
            return 종료(self.ctx)
        if self.user_value(key='Timmer', value=3):
            return 시작(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_shy', script='$02020051_BF__102_TIMMER__0$', duration=5684, voice='ko/Npc/00002201')
        self.set_user_value(triggerId=104, key='End', value=3)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Timmer', value=2):
            return 시작(self.ctx)


initial_state = 시작
