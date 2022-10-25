""" trigger/02000298_bf/mob_07.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[606], visible=False)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3211,3212,3213,3214,3215], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[106]):
            self.create_monster(spawnIds=[1007], animationEffect=False)
            return 방호벽대기(self.ctx)
        if self.user_detected(boxIds=[107]):
            self.create_monster(spawnIds=[1007], animationEffect=False)
            return 방호벽대기(self.ctx)


class 방호벽대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1007]):
            return 방호벽해제(self.ctx)


class 방호벽해제(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=True)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205], visible=False, arg3=0, delay=0, scale=5)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 번생성11(self.ctx)


class 번생성11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1011], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1011]):
            return 방호벽해제2(self.ctx)


class 방호벽해제2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[606], visible=True)
        self.set_mesh(triggerIds=[3211,3212,3213,3214,3215], visible=False, arg3=0, delay=0, scale=5)
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
