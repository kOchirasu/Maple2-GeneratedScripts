""" trigger/02020201_bf/altar1.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[901]):
            return 전투시작체크(self.ctx)


class 전투시작체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[101]):
            return 생성대기(self.ctx)


class 생성대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='gogo', value=1):
            return 생성대기2(self.ctx)


class 생성대기2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투체크(self.ctx)


class 전투체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[101]):
            return 제단생성(self.ctx)


class 제단생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 제단파괴체크(self.ctx)


class 제단파괴체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[201]):
            return 제단재생성시간(self.ctx)


class 제단재생성시간(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='Sidephase', value=1, isModify=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=40000):
            self.set_ai_extra_data(key='Sidephase', value=-1, isModify=True)
            return 전투체크(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
