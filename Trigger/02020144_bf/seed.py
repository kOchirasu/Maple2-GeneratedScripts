""" trigger/02020144_bf/seed.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1003], skillId=70002110, level=1, isSkillSet=False)
        self.set_user_value(triggerId=900005, key='TimerStart', value=0)
        self.set_user_value(triggerId=900005, key='TimerReset', value=0)
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
        if self.user_detected(boxIds=[1001]):
            return 보스전유저감지(self.ctx)


class 보스전유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1002]):
            return 보스체력체크1(self.ctx)


class 보스체력체크1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=70, spawnId=101, isRelative=True):
            return 씨앗패턴1_확률체크(self.ctx)


class 씨앗패턴1_확률체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900005, key='TimerStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴1_1(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴1_2(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴1_3(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴1_4(self.ctx)


class 씨앗패턴1_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9001], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002124], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.object_interacted(interactIds=[10002124], stateValue=0):
            self.set_mesh(triggerIds=[9001], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴1_1_심기(self.ctx)


class 씨앗패턴1_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9002], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002125], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.object_interacted(interactIds=[10002125], stateValue=0):
            self.set_mesh(triggerIds=[9002], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴1_2_심기(self.ctx)


class 씨앗패턴1_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9003], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002126], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.object_interacted(interactIds=[10002126], stateValue=0):
            self.set_mesh(triggerIds=[9003], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴1_3_심기(self.ctx)


class 씨앗패턴1_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9004], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002127], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.object_interacted(interactIds=[10002127], stateValue=0):
            self.set_mesh(triggerIds=[9004], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴1_4_심기(self.ctx)


class 씨앗패턴1_1_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.any_one():
            return 씨앗패턴1_종료(self.ctx)


class 씨앗패턴1_2_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.any_one():
            return 씨앗패턴1_종료(self.ctx)


class 씨앗패턴1_3_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.any_one():
            return 씨앗패턴1_종료(self.ctx)


class 씨앗패턴1_4_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.any_one():
            return 씨앗패턴1_종료(self.ctx)


class 씨앗패턴1_종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900005, key='TimerStart', value=0)
        self.set_skill(triggerIds=[901], enable=True)
        self.set_skill(triggerIds=[902], enable=True)
        self.set_interact_object(triggerIds=[10002128], state=2)
        self.set_interact_object(triggerIds=[10002129], state=2)
        self.set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        self.set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=1):
            return 보스체력체크2(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 보스체력체크2(self.ctx)


class 보스체력체크2(trigger_api.Trigger):
    def on_enter(self):
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
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=40, spawnId=101, isRelative=True):
            return 씨앗패턴2_확률체크(self.ctx)


class 씨앗패턴2_확률체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900005, key='TimerStart', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴2_1(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴2_2(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴2_3(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴2_4(self.ctx)


class 씨앗패턴2_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9001], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002124], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.object_interacted(interactIds=[10002124], stateValue=0):
            self.set_mesh(triggerIds=[9001], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴2_1_심기(self.ctx)


class 씨앗패턴2_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9002], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002125], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.object_interacted(interactIds=[10002125], stateValue=0):
            self.set_mesh(triggerIds=[9002], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴2_2_심기(self.ctx)


class 씨앗패턴2_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9003], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002126], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.object_interacted(interactIds=[10002126], stateValue=0):
            self.set_mesh(triggerIds=[9003], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴2_3_심기(self.ctx)


class 씨앗패턴2_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9004], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002127], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.object_interacted(interactIds=[10002127], stateValue=0):
            self.set_mesh(triggerIds=[9004], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴2_4_심기(self.ctx)


class 씨앗패턴2_1_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.any_one():
            return 씨앗패턴2_종료(self.ctx)


class 씨앗패턴2_2_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.any_one():
            return 씨앗패턴2_종료(self.ctx)


class 씨앗패턴2_3_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.any_one():
            return 씨앗패턴2_종료(self.ctx)


class 씨앗패턴2_4_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.any_one():
            return 씨앗패턴2_종료(self.ctx)


class 씨앗패턴2_종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900005, key='TimerStart', value=0)
        self.set_skill(triggerIds=[901], enable=True)
        self.set_skill(triggerIds=[902], enable=True)
        self.set_interact_object(triggerIds=[10002128], state=2)
        self.set_interact_object(triggerIds=[10002129], state=2)
        self.set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        self.set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=2):
            return 보스체력체크3(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 보스체력체크3(self.ctx)


class 보스체력체크3(trigger_api.Trigger):
    def on_enter(self):
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
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=15, spawnId=101, isRelative=True):
            return 씨앗패턴3_확률체크(self.ctx)


class 씨앗패턴3_확률체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900005, key='TimerStart', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴3_1(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴3_2(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴3_3(self.ctx)
        if self.random_condition(rate=25):
            return 씨앗패턴3_4(self.ctx)


class 씨앗패턴3_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9001], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002124], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002124], stateValue=0):
            self.set_mesh(triggerIds=[9001], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴3_1_심기(self.ctx)


class 씨앗패턴3_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9002], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002125], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002125], stateValue=0):
            self.set_mesh(triggerIds=[9002], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴3_2_심기(self.ctx)


class 씨앗패턴3_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9003], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002126], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002126], stateValue=0):
            self.set_mesh(triggerIds=[9003], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴3_3_심기(self.ctx)


class 씨앗패턴3_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9004], visible=True, arg3=0, delay=0, scale=2)
        self.set_interact_object(triggerIds=[10002127], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002127], stateValue=0):
            self.set_mesh(triggerIds=[9004], visible=False, arg3=0, delay=0, scale=0)
            return 씨앗패턴3_4_심기(self.ctx)


class 씨앗패턴3_1_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.any_one():
            return 씨앗패턴3_종료(self.ctx)


class 씨앗패턴3_2_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.any_one():
            return 씨앗패턴3_종료(self.ctx)


class 씨앗패턴3_3_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.any_one():
            return 씨앗패턴3_종료(self.ctx)


class 씨앗패턴3_4_심기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002128], state=1)
        self.set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.any_one():
            return 씨앗패턴3_종료(self.ctx)


class 씨앗패턴3_종료(trigger_api.Trigger):
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
        if self.user_value(key='TimerReset', value=3):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1003], skillId=70002110, level=1, isSkillSet=False)
        self.set_user_value(triggerId=900005, key='TimerStart', value=9)
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


initial_state = 시작
