""" trigger/02020101_bf/seed1.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        add_buff(boxIds=[1003], skillId=70002110, level=1, arg5=False)
        # <action name="SetUserValue" triggerID="900005" key="TimerStart" value="0" />
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
        if user_value(key='Seed', value=1):
            return 대기시간()


class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 활성화()


class 활성화(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[9001,9002,9003,9004], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002124], state=1)
        set_interact_object(triggerIds=[10002125], state=1)
        set_interact_object(triggerIds=[10002126], state=1)
        set_interact_object(triggerIds=[10002127], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if wait_tick(waitTick=20000):
            set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
            set_interact_object(triggerIds=[10002124], state=0)
            set_interact_object(triggerIds=[10002125], state=0)
            set_interact_object(triggerIds=[10002126], state=0)
            set_interact_object(triggerIds=[10002127], state=0)
            return 종료()
        if object_interacted(interactIds=[10002124], arg2=0):
            set_interact_object(triggerIds=[10002125], state=0)
            set_interact_object(triggerIds=[10002126], state=0)
            set_interact_object(triggerIds=[10002127], state=0)
            set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗심기1()
        if object_interacted(interactIds=[10002125], arg2=0):
            set_interact_object(triggerIds=[10002124], state=0)
            set_interact_object(triggerIds=[10002126], state=0)
            set_interact_object(triggerIds=[10002127], state=0)
            set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗심기2()
        if object_interacted(interactIds=[10002126], arg2=0):
            set_interact_object(triggerIds=[10002124], state=0)
            set_interact_object(triggerIds=[10002125], state=0)
            set_interact_object(triggerIds=[10002127], state=0)
            set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗심기3()
        if object_interacted(interactIds=[10002127], arg2=0):
            set_interact_object(triggerIds=[10002124], state=0)
            set_interact_object(triggerIds=[10002125], state=0)
            set_interact_object(triggerIds=[10002126], state=0)
            set_mesh(triggerIds=[9001,9002,9003,9004], visible=False, arg3=0, arg4=0, arg5=0)
            return 씨앗심기4()


class 씨앗심기1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if any_one():
            return 나무생성1()
        if not check_any_user_additional_effect(boxId=1004, additionalEffectId=70002109, level=1):
            return 종료()


class 씨앗심기2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if any_one():
            return 나무생성1()
        if not check_any_user_additional_effect(boxId=1004, additionalEffectId=70002109, level=1):
            return 종료()


class 씨앗심기3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if any_one():
            return 나무생성1()
        if not check_any_user_additional_effect(boxId=1004, additionalEffectId=70002109, level=1):
            return 종료()


class 씨앗심기4(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002128], state=1)
        set_interact_object(triggerIds=[10002129], state=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 종료()
        if any_one():
            return 나무생성1()
        if not check_any_user_additional_effect(boxId=1004, additionalEffectId=70002109, level=1):
            return 종료()


class 나무생성1(state.State):
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
        if wait_tick(waitTick=20000):
            set_actor(triggerId=1401, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
            set_actor(triggerId=1402, visible=True, initialSequence='Interaction_lapentatree_A01_Off')
            set_interact_object(triggerIds=[10002128], state=0)
            set_interact_object(triggerIds=[10002129], state=0)
            set_skill(triggerIds=[901], isEnable=False)
            set_skill(triggerIds=[902], isEnable=False)
            set_user_value(triggerId=900009, key='Seed', value=0)
            return 시작()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=900009, key='Seed', value=0)
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
        if true():
            return 시작()


