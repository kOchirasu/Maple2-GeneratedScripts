""" trigger/02000368_bf/mob_03.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[7301], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 전투01(self.ctx)
        if self.user_detected(boxIds=[1002]):
            return 전투01(self.ctx)


class 전투01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,311], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[301,311]):
            return 전투02(self.ctx)


class 전투02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[7301], enable=True)
        self.create_monster(spawnIds=[302], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[302]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
