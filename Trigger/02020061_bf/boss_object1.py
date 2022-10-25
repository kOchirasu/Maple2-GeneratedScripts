""" trigger/02020061_bf/boss_object1.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawnIds=[711,721])
        self.set_interact_object(triggerIds=[12000094], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BossObjectStart', value=1):
            return 레버1_체크(self.ctx)


class 레버1_체크(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[721], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[711]):
            return 레버1_발동(self.ctx)
        if self.all_of():
            return 종료(self.ctx)


class 레버1_발동(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_interact_object(triggerIds=[12000094], state=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000094], stateValue=0):
            return 레버1_안내(self.ctx)


class 레버1_안내(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 레버1_재활성(self.ctx)


class 레버1_재활성(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000094], state=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000094], stateValue=0):
            return 레버1_재활성_대기(self.ctx)


class 레버1_재활성_대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 레버1_재활성(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawnIds=[711,721])
        self.set_interact_object(triggerIds=[12000094], state=2)


initial_state = 대기
