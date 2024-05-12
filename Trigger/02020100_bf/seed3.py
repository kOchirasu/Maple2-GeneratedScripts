""" trigger/02020100_bf/seed3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990001, key='EliteClear', value=0)
        self.set_user_value(triggerId=99990001, key='Seed3interact', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed3start', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[229])
        self.set_mesh(triggerIds=[1304], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002111], state=1, arg3=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed3start', value=2):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002111], stateValue=0):
            return 씨앗3_심기(self.ctx)


class 씨앗3_심기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990001, key='Seed3interact', value=1)
        self.set_mesh(triggerIds=[1304], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10002122], state=1, arg3=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed3start', value=2):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002122], stateValue=0):
            return 씨앗3_중보(self.ctx)
        if not self.check_any_user_additional_effect(boxId=0, additionalEffectId=70002109, level=1):
            return 시작(self.ctx)


class 씨앗3_중보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=1404, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        self.destroy_monster(spawnIds=[121,122,123,124])
        self.create_monster(spawnIds=[229], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[229]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990001, key='EliteClear', value=1)
        self.set_interact_object(triggerIds=[10002111], state=0)


initial_state = 대기
