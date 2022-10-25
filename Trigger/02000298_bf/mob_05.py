""" trigger/02000298_bf/mob_05.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_mesh(triggerIds=[3006,3007,3008,3009,3010], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3206,3207,3208,3209,3210], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            self.create_monster(spawnIds=[1005], animationEffect=False)
            return 방호벽대기(self.ctx)
        if self.user_detected(boxIds=[103]):
            self.create_monster(spawnIds=[1005], animationEffect=False)
            return 방호벽대기(self.ctx)


class 방호벽대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1005]):
            return 방호벽해제(self.ctx)


class 방호벽해제(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=True)
        self.set_mesh(triggerIds=[3006,3007,3008,3009,3010], visible=False, arg3=0, delay=0, scale=5)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 번생성10(self.ctx)


class 번생성10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1010], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1010]):
            return 방호벽해제2(self.ctx)


class 방호벽해제2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=True)
        self.set_mesh(triggerIds=[3206,3207,3208,3209,3210], visible=False, arg3=0, delay=0, scale=5)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1800000'):
            return None # Missing State: 종료2


initial_state = 대기
