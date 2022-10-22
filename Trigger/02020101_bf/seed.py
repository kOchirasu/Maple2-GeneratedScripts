""" trigger/02020101_bf/seed.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        add_buff(boxIds=[1003], skillId=70002110, level=1, arg5=False)
        set_user_value(triggerId=900005, key='TimerStart', value=0)
        set_user_value(triggerId=900005, key='TimerReset', value=0)
        set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10002124], state=0)
        set_interact_object(triggerIds=[10002125], state=0)
        set_interact_object(triggerIds=[10002126], state=0)
        set_interact_object(triggerIds=[10002127], state=0)
        set_interact_object(triggerIds=[10002128], state=0)
        set_interact_object(triggerIds=[10002129], state=0)
        set_skill(triggerIds=[901], isEnable=False)
        set_skill(triggerIds=[902], isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 보스전유저감지()


class 보스전유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1002]):
            return 보스체력체크1()


class 보스체력체크1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if check_npc_hp(compare='lowerEqual', value=70, spawnId=101, isRelative=True):
            return 씨앗패턴1_확률체크()


class 씨앗패턴1_확률체크(state.State):
    def on_enter(self):
        set_user_value(triggerId=900005, key='TimerStart', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if random_condition(rate=25):
            return 씨앗패턴1_1()
        if random_condition(rate=25):
            return 씨앗패턴1_2()
        if random_condition(rate=25):
            return 씨앗패턴1_3()
        if random_condition(rate=25):
            return 씨앗패턴1_4()


class 씨앗패턴1_1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9001], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002124], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if object_interacted(interactIds=[10002124], arg2=0):
            set_mesh(triggerIds=[9001], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴1_1_심기()


class 씨앗패턴1_2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9002], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002125], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if object_interacted(interactIds=[10002125], arg2=0):
            set_mesh(triggerIds=[9002], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴1_2_심기()


class 씨앗패턴1_3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9003], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002126], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if object_interacted(interactIds=[10002126], arg2=0):
            set_mesh(triggerIds=[9003], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴1_3_심기()


class 씨앗패턴1_4(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9004], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002127], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if object_interacted(interactIds=[10002127], arg2=0):
            set_mesh(triggerIds=[9004], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴1_4_심기()


class 씨앗패턴1_1_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if any_one():
            return 씨앗패턴1_종료()


class 씨앗패턴1_2_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if any_one():
            return 씨앗패턴1_종료()


class 씨앗패턴1_3_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if any_one():
            return 씨앗패턴1_종료()


class 씨앗패턴1_4_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if any_one():
            return 씨앗패턴1_종료()


class 씨앗패턴1_종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=900005, key='TimerStart', value=0)
        set_skill(triggerIds=[901], isEnable=True)
        set_skill(triggerIds=[902], isEnable=True)
        set_interact_object(triggerIds=[10002128], state=2)
        set_interact_object(triggerIds=[10002129], state=2)
        set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=1):
            return 보스체력체크2()
        if wait_tick(waitTick=10000):
            return 보스체력체크2()


class 보스체력체크2(state.State):
    def on_enter(self):
        add_buff(boxIds=[1003], skillId=70002110, level=1, arg5=False)
        set_skill(triggerIds=[901], isEnable=False)
        set_skill(triggerIds=[902], isEnable=False)
        set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10002124], state=0)
        set_interact_object(triggerIds=[10002125], state=0)
        set_interact_object(triggerIds=[10002126], state=0)
        set_interact_object(triggerIds=[10002127], state=0)
        set_interact_object(triggerIds=[10002128], state=0)
        set_interact_object(triggerIds=[10002129], state=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if check_npc_hp(compare='lowerEqual', value=40, spawnId=101, isRelative=True):
            return 씨앗패턴2_확률체크()


class 씨앗패턴2_확률체크(state.State):
    def on_enter(self):
        set_user_value(triggerId=900005, key='TimerStart', value=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if random_condition(rate=25):
            return 씨앗패턴2_1()
        if random_condition(rate=25):
            return 씨앗패턴2_2()
        if random_condition(rate=25):
            return 씨앗패턴2_3()
        if random_condition(rate=25):
            return 씨앗패턴2_4()


class 씨앗패턴2_1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9001], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002124], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if object_interacted(interactIds=[10002124], arg2=0):
            set_mesh(triggerIds=[9001], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴2_1_심기()


class 씨앗패턴2_2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9002], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002125], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if object_interacted(interactIds=[10002125], arg2=0):
            set_mesh(triggerIds=[9002], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴2_2_심기()


class 씨앗패턴2_3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9003], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002126], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if object_interacted(interactIds=[10002126], arg2=0):
            set_mesh(triggerIds=[9003], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴2_3_심기()


class 씨앗패턴2_4(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9004], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002127], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if object_interacted(interactIds=[10002127], arg2=0):
            set_mesh(triggerIds=[9004], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴2_4_심기()


class 씨앗패턴2_1_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if any_one():
            return 씨앗패턴2_종료()


class 씨앗패턴2_2_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if any_one():
            return 씨앗패턴2_종료()


class 씨앗패턴2_3_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if any_one():
            return 씨앗패턴2_종료()


class 씨앗패턴2_4_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if any_one():
            return 씨앗패턴2_종료()


class 씨앗패턴2_종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=900005, key='TimerStart', value=0)
        set_skill(triggerIds=[901], isEnable=True)
        set_skill(triggerIds=[902], isEnable=True)
        set_interact_object(triggerIds=[10002128], state=2)
        set_interact_object(triggerIds=[10002129], state=2)
        set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=2):
            return 보스체력체크3()
        if wait_tick(waitTick=10000):
            return 보스체력체크3()


class 보스체력체크3(state.State):
    def on_enter(self):
        add_buff(boxIds=[1003], skillId=70002110, level=1, arg5=False)
        set_skill(triggerIds=[901], isEnable=False)
        set_skill(triggerIds=[902], isEnable=False)
        set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10002124], state=0)
        set_interact_object(triggerIds=[10002125], state=0)
        set_interact_object(triggerIds=[10002126], state=0)
        set_interact_object(triggerIds=[10002127], state=0)
        set_interact_object(triggerIds=[10002128], state=0)
        set_interact_object(triggerIds=[10002129], state=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if check_npc_hp(compare='lowerEqual', value=15, spawnId=101, isRelative=True):
            return 씨앗패턴3_확률체크()


class 씨앗패턴3_확률체크(state.State):
    def on_enter(self):
        set_user_value(triggerId=900005, key='TimerStart', value=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if random_condition(rate=25):
            return 씨앗패턴3_1()
        if random_condition(rate=25):
            return 씨앗패턴3_2()
        if random_condition(rate=25):
            return 씨앗패턴3_3()
        if random_condition(rate=25):
            return 씨앗패턴3_4()


class 씨앗패턴3_1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9001], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002124], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if object_interacted(interactIds=[10002124], arg2=0):
            set_mesh(triggerIds=[9001], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴3_1_심기()


class 씨앗패턴3_2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9002], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002125], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if object_interacted(interactIds=[10002125], arg2=0):
            set_mesh(triggerIds=[9002], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴3_2_심기()


class 씨앗패턴3_3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9003], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002126], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if object_interacted(interactIds=[10002126], arg2=0):
            set_mesh(triggerIds=[9003], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴3_3_심기()


class 씨앗패턴3_4(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9004], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002127], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if object_interacted(interactIds=[10002127], arg2=0):
            set_mesh(triggerIds=[9004], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗패턴3_4_심기()


class 씨앗패턴3_1_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if any_one():
            return 씨앗패턴3_종료()


class 씨앗패턴3_2_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if any_one():
            return 씨앗패턴3_종료()


class 씨앗패턴3_3_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if any_one():
            return 씨앗패턴3_종료()


class 씨앗패턴3_4_심기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if any_one():
            return 씨앗패턴3_종료()


class 씨앗패턴3_종료(state.State):
    def on_enter(self):
        set_skill(triggerIds=[901], isEnable=True)
        set_skill(triggerIds=[902], isEnable=True)
        set_interact_object(triggerIds=[10002128], state=2)
        set_interact_object(triggerIds=[10002129], state=2)
        set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_On')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if user_value(key='TimerReset', value=3):
            return 종료()
        if wait_tick(waitTick=10000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        add_buff(boxIds=[1003], skillId=70002110, level=1, arg5=False)
        set_user_value(triggerId=900005, key='TimerStart', value=9)
        set_skill(triggerIds=[901], isEnable=False)
        set_skill(triggerIds=[902], isEnable=False)
        set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
        set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10002124], state=0)
        set_interact_object(triggerIds=[10002125], state=0)
        set_interact_object(triggerIds=[10002126], state=0)
        set_interact_object(triggerIds=[10002127], state=0)
        set_interact_object(triggerIds=[10002128], state=0)
        set_interact_object(triggerIds=[10002129], state=0)


