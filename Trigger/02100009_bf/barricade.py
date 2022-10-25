""" trigger/02100009_bf/barricade.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[80000], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return CheckUser10_GuildRaid(self.ctx)


class CheckUser10_GuildRaid(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=1, interval=0, vOffset=0) # 최대 30초 대기

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=102, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start(self.ctx)
        if self.count_users(boxId=102, boxId=10, operator='Less'):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Wait(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=102, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start(self.ctx)
        if self.time_expired(timerId='1'):
            return MaxCount10_Start(self.ctx)
        if self.wait_tick(waitTick=6000):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Start(common.Trigger):
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
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100009_BF__BARRICADE__0$')
        self.set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return ShowCaption01Skip(self.ctx)


class ShowCaption01Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return ShowCaption02(self.ctx)


class ShowCaption02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100009_BF__BARRICADE__1$')
        self.set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CloseCaptionSetting(self.ctx)


class CloseCaptionSetting(common.Trigger):
    def on_enter(self):
        self.close_cinematic()
        self.select_camera(triggerId=904, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_effect(triggerIds=[7002], visible=False)
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7004], visible=False)
        self.set_mesh(triggerIds=[8000], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.any_one():
            return 유저감지(self.ctx)


class 유저감지(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 카운트(self.ctx)


class 카운트(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02100009_BF__BARRICADE__2$', arg3='3000')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 차단(self.ctx)


class 차단(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8000], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[7001], visible=True)
        self.set_effect(triggerIds=[7002], visible=True)
        self.set_effect(triggerIds=[7003], visible=True)
        self.set_effect(triggerIds=[7004], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[100000001,100000002]):
            return 차단해제(self.ctx)


class 차단해제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8000], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_effect(triggerIds=[7002], visible=False)
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7004], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = Wait
