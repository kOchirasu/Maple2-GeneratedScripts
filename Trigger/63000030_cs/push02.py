""" trigger/63000030_cs/push02.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6107], visible=False) # Voice_Junta_00001768
        self.set_effect(triggerIds=[6006], visible=False) # Voice_Tinchai_00001700
        self.set_agent(triggerIds=[8100], visible=False)
        self.set_agent(triggerIds=[8101], visible=False)
        self.set_agent(triggerIds=[8102], visible=False)
        self.set_agent(triggerIds=[8103], visible=False)
        self.set_agent(triggerIds=[8104], visible=False)
        self.set_agent(triggerIds=[8105], visible=False)
        self.set_agent(triggerIds=[8106], visible=False)
        self.set_agent(triggerIds=[8107], visible=False)
        self.set_agent(triggerIds=[8108], visible=False)
        self.set_agent(triggerIds=[8109], visible=False)
        self.set_agent(triggerIds=[8110], visible=False)
        self.set_agent(triggerIds=[8111], visible=False)
        self.set_agent(triggerIds=[8112], visible=False)
        self.set_skill(triggerIds=[7000], enable=False) # Push
        self.set_mesh(triggerIds=[3100], visible=False, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.set_user_value(key='PushStart', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PushStart', value=1):
            return Enter01(self.ctx)


class Enter01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.set_agent(triggerIds=[8100], visible=True)
        self.set_agent(triggerIds=[8101], visible=True)
        self.set_agent(triggerIds=[8102], visible=True)
        self.set_agent(triggerIds=[8103], visible=True)
        self.set_agent(triggerIds=[8104], visible=True)
        self.set_agent(triggerIds=[8105], visible=True)
        self.set_agent(triggerIds=[8106], visible=True)
        self.set_agent(triggerIds=[8107], visible=True)
        self.set_agent(triggerIds=[8108], visible=True)
        self.set_agent(triggerIds=[8109], visible=True)
        self.set_agent(triggerIds=[8110], visible=True)
        self.set_agent(triggerIds=[8111], visible=True)
        self.set_agent(triggerIds=[8112], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return Push01(self.ctx)


class Push01(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7000], enable=True) # Push

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return NpcTalkRandom(self.ctx)


class NpcTalkRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            return JuntaTalk01(self.ctx)
        if self.random_condition(rate=50):
            return TinChaiTalk01(self.ctx)


class JuntaTalk01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[6107], visible=True) # Voice_Junta_00001768
        self.set_conversation(type=2, spawnId=11001557, script='$63000030_CS__PUSH02__0$', arg4=5) # 준타 00001768

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Delay01(self.ctx)


class TinChaiTalk01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[6006], visible=True) # Voice_Tinchai_00001700
        self.set_conversation(type=2, spawnId=11001708, script='$63000030_CS__PUSH02__1$', arg4=4) # 틴차이 00001700

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Delay01(self.ctx)


class Delay01(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Reset01(self.ctx)


class Reset01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return Push01(self.ctx)


initial_state = Wait
