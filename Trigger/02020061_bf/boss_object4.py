""" trigger/02020061_bf/boss_object4.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5301], visible=False)
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawnIds=[714,724])
        self.set_interact_object(triggerIds=[12000097], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=1):
            return 레버4_체크(self.ctx)


class 레버4_체크(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[724], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[714]):
            return 레버4_발동(self.ctx)
        if self.all_of():
            return 종료(self.ctx)


class 레버4_발동(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5301], visible=True)
        self.set_interact_object(triggerIds=[12000097], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 대기(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000097], stateValue=0):
            return 레버4_안내(self.ctx)


class 레버4_안내(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 레버4_재활성(self.ctx)


class 레버4_재활성(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000097], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000097], stateValue=0):
            return 레버4_재활성_대기(self.ctx)


class 레버4_재활성_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart', value=2):
            return 종료(self.ctx)
        if self.all_of():
            return 종료(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 레버4_재활성(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5301], visible=False)
        self.set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawnIds=[714,724])
        self.set_interact_object(triggerIds=[12000097], state=2)


initial_state = 대기
