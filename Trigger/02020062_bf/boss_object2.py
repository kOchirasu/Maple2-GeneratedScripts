""" trigger/02020062_bf/boss_object2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False)
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawnIds=[712,722])
        self.set_interact_object(triggerIds=[12000112], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=1):
            return 레버2_체크(self.ctx)


class 레버2_체크(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[722], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[712]):
            return 레버2_발동(self.ctx)
        if self.all_of():
            return 종료(self.ctx)


class 레버2_발동(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True)
        self.set_interact_object(triggerIds=[12000112], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 대기(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000112], stateValue=0):
            return 레버2_안내(self.ctx)


class 레버2_안내(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.wait_tick(waitTick=20000):
            return 레버2_재활성(self.ctx)


class 레버2_재활성(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000112], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000112], stateValue=0):
            return 레버2_재활성_대기(self.ctx)


class 레버2_재활성_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.wait_tick(waitTick=20000):
            return 레버2_재활성(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False)
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawnIds=[712,722])
        self.set_interact_object(triggerIds=[12000112], state=2)


initial_state = 대기
