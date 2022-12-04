""" trigger/02020101_bf/seed1.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1003], skillId=70002110, level=1, isSkillSet=False)
        # <action name="SetUserValue" triggerID="900005" key="TimerStart" value="0" />
        self.set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        self.set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10002124], state=0)
        self.set_interact_object(triggerIds=[10002125], state=0)
        self.set_interact_object(triggerIds=[10002126], state=0)
        self.set_interact_object(triggerIds=[10002127], state=0)
        self.set_interact_object(triggerIds=[10002128], state=0)
        self.set_interact_object(triggerIds=[10002129], state=0)
        self.set_skill(triggerIds=[901], enable=False)
        self.set_skill(triggerIds=[902], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed', value=1):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 활성화(self.ctx)


class 활성화(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002124], state=1)
        self.set_interact_object(triggerIds=[10002125], state=1)
        self.set_interact_object(triggerIds=[10002126], state=1)
        self.set_interact_object(triggerIds=[10002127], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=20000):
            self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)
            self.set_interact_object(triggerIds=[10002124], state=0)
            self.set_interact_object(triggerIds=[10002125], state=0)
            self.set_interact_object(triggerIds=[10002126], state=0)
            self.set_interact_object(triggerIds=[10002127], state=0)
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002124], stateValue=0):
            self.set_interact_object(triggerIds=[10002125], state=0)
            self.set_interact_object(triggerIds=[10002126], state=0)
            self.set_interact_object(triggerIds=[10002127], state=0)
            self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗심기1(self.ctx)
        if self.object_interacted(interactIds=[10002125], stateValue=0):
            self.set_interact_object(triggerIds=[10002124], state=0)
            self.set_interact_object(triggerIds=[10002126], state=0)
            self.set_interact_object(triggerIds=[10002127], state=0)
            self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗심기2(self.ctx)
        if self.object_interacted(interactIds=[10002126], stateValue=0):
            self.set_interact_object(triggerIds=[10002124], state=0)
            self.set_interact_object(triggerIds=[10002125], state=0)
            self.set_interact_object(triggerIds=[10002127], state=0)
            self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗심기3(self.ctx)
        if self.object_interacted(interactIds=[10002127], stateValue=0):
            self.set_interact_object(triggerIds=[10002124], state=0)
            self.set_interact_object(triggerIds=[10002125], state=0)
            self.set_interact_object(triggerIds=[10002126], state=0)
            self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗심기4(self.ctx)


class 씨앗심기1(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.any_one():
            return 나무생성1(self.ctx)
        if not self.check_any_user_additional_effect(boxId=1004, additionalEffectId=70002109, level=1):
            return 종료(self.ctx)


class 씨앗심기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.any_one():
            return 나무생성1(self.ctx)
        if not self.check_any_user_additional_effect(boxId=1004, additionalEffectId=70002109, level=1):
            return 종료(self.ctx)


class 씨앗심기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.any_one():
            return 나무생성1(self.ctx)
        if not self.check_any_user_additional_effect(boxId=1004, additionalEffectId=70002109, level=1):
            return 종료(self.ctx)


class 씨앗심기4(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.any_one():
            return 나무생성1(self.ctx)
        if not self.check_any_user_additional_effect(boxId=1004, additionalEffectId=70002109, level=1):
            return 종료(self.ctx)


class 나무생성1(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[901], enable=True)
        self.set_skill(triggerIds=[902], enable=True)
        self.set_interact_object(triggerIds=[10002128], state=2)
        self.set_interact_object(triggerIds=[10002129], state=2)
        self.set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        self.set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=20000):
            self.set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
            self.set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
            self.set_interact_object(triggerIds=[10002128], state=0)
            self.set_interact_object(triggerIds=[10002129], state=0)
            self.set_skill(triggerIds=[901], enable=False)
            self.set_skill(triggerIds=[902], enable=False)
            self.set_user_value(triggerId=900009, key='Seed', value=0)
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900009, key='Seed', value=0)
        self.add_buff(boxIds=[1003], skillId=70002110, level=1, isSkillSet=False)
        self.set_skill(triggerIds=[901], enable=False)
        self.set_skill(triggerIds=[902], enable=False)
        self.set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        self.set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        self.set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10002124], state=0)
        self.set_interact_object(triggerIds=[10002125], state=0)
        self.set_interact_object(triggerIds=[10002126], state=0)
        self.set_interact_object(triggerIds=[10002127], state=0)
        self.set_interact_object(triggerIds=[10002128], state=0)
        self.set_interact_object(triggerIds=[10002129], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작(self.ctx)


initial_state = 시작
