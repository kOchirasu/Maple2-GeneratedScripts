""" trigger/63000030_cs/push02.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6107], visible=False) # Voice_Junta_00001768
        set_effect(triggerIds=[6006], visible=False) # Voice_Tinchai_00001700
        set_agent(triggerIds=[8100], visible=False)
        set_agent(triggerIds=[8101], visible=False)
        set_agent(triggerIds=[8102], visible=False)
        set_agent(triggerIds=[8103], visible=False)
        set_agent(triggerIds=[8104], visible=False)
        set_agent(triggerIds=[8105], visible=False)
        set_agent(triggerIds=[8106], visible=False)
        set_agent(triggerIds=[8107], visible=False)
        set_agent(triggerIds=[8108], visible=False)
        set_agent(triggerIds=[8109], visible=False)
        set_agent(triggerIds=[8110], visible=False)
        set_agent(triggerIds=[8111], visible=False)
        set_agent(triggerIds=[8112], visible=False)
        set_skill(triggerIds=[7000], isEnable=False) # Push
        set_mesh(triggerIds=[3100], visible=False, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        set_user_value(key='PushStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PushStart', value=1):
            return Enter01()


class Enter01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        set_agent(triggerIds=[8100], visible=True)
        set_agent(triggerIds=[8101], visible=True)
        set_agent(triggerIds=[8102], visible=True)
        set_agent(triggerIds=[8103], visible=True)
        set_agent(triggerIds=[8104], visible=True)
        set_agent(triggerIds=[8105], visible=True)
        set_agent(triggerIds=[8106], visible=True)
        set_agent(triggerIds=[8107], visible=True)
        set_agent(triggerIds=[8108], visible=True)
        set_agent(triggerIds=[8109], visible=True)
        set_agent(triggerIds=[8110], visible=True)
        set_agent(triggerIds=[8111], visible=True)
        set_agent(triggerIds=[8112], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return Push01()


class Push01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7000], isEnable=True) # Push

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NpcTalkRandom()


class NpcTalkRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return JuntaTalk01()
        if random_condition(rate=50):
            return TinChaiTalk01()


class JuntaTalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[6107], visible=True) # Voice_Junta_00001768
        set_conversation(type=2, spawnId=11001557, script='$63000030_CS__PUSH02__0$', arg4=5) # 준타 00001768

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Delay01()


class TinChaiTalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[6006], visible=True) # Voice_Tinchai_00001700
        set_conversation(type=2, spawnId=11001708, script='$63000030_CS__PUSH02__1$', arg4=4) # 틴차이 00001700

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Delay01()


class Delay01(state.State):
    def on_enter(self):
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Reset01()


class Reset01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return Push01()


