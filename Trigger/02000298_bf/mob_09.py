""" trigger/02000298_bf/mob_09.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[607], visible=False)
        self.set_mesh(triggerIds=[3016,3017,3018,3019,3020], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3216,3217,3218,3219,3220], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[110]):
            self.create_monster(spawnIds=[1009], animationEffect=False)
            return 방호벽대기(self.ctx)
        if self.user_detected(boxIds=[111]):
            self.create_monster(spawnIds=[1009], animationEffect=False)
            return 방호벽대기(self.ctx)


class 방호벽대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1009]):
            return 방호벽해제(self.ctx)


class 방호벽해제(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[604], visible=True)
        self.set_mesh(triggerIds=[3016,3017,3018,3019,3020], visible=False, arg3=0, delay=0, scale=5)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 번생성12(self.ctx)


class 번생성12(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1012], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1012]):
            return 방호벽해제2(self.ctx)


class 방호벽해제2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[607], visible=True)
        self.set_mesh(triggerIds=[3216,3217,3218,3219,3220], visible=False, arg3=0, delay=0, scale=5)
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
