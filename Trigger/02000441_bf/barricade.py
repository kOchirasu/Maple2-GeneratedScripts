""" trigger/02000441_bf/barricade.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[80000], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return CheckUser04_GuildRaid(self.ctx)


class CheckUser04_GuildRaid(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=1, interval=0, vOffset=0) # 최대 30초 대기

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=701, boxId=4, operator='GreaterEqual'):
            return MaxCount04_Start(self.ctx)
        if self.count_users(boxId=701, boxId=4, operator='Less'):
            return MaxCount04_Wait(self.ctx)


class MaxCount04_Wait(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=701, boxId=4, operator='GreaterEqual'):
            return MaxCount04_Start(self.ctx)
        if self.time_expired(timerId='1'):
            return MaxCount04_Start(self.ctx)
        if self.wait_tick(waitTick=6000):
            return MaxCount04_Wait(self.ctx)


class MaxCount04_Start(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return DungeonStart(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=904, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2038801, key='start', value=1)
        self.set_effect(triggerIds=[70001], visible=False)
        self.set_effect(triggerIds=[70002], visible=False)
        self.set_effect(triggerIds=[70003], visible=False)
        self.set_mesh(triggerIds=[80000], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 유저감지(self.ctx)


class 유저감지(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[706]):
            return 카운트(self.ctx)


class 카운트(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000441_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 차단(self.ctx)


class 차단(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[80000], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[70001], visible=True)
        self.set_effect(triggerIds=[70002], visible=True)
        self.set_effect(triggerIds=[70003], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = Wait
