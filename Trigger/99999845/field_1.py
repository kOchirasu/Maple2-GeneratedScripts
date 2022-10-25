""" trigger/99999845/field_1.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000304], state=2)
        self.set_interact_object(triggerIds=[12000305], state=2)
        self.set_interact_object(triggerIds=[12000306], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Block', value=1):
            self.set_user_value(triggerId=900002, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block', value=2):
            self.set_user_value(triggerId=900002, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block', value=3):
            self.set_user_value(triggerId=900002, key='Block', value=0)
            return Block_3(self.ctx)


class Block_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1104]):
            self.set_visible_breakable_object(triggerIds=[1004], visible=True)
            self.set_interact_object(triggerIds=[12000304], state=1)
            self.create_monster(spawnIds=[1107], animationEffect=False)
            self.create_monster(spawnIds=[1108], animationEffect=False)
            self.create_monster(spawnIds=[1109], animationEffect=False)
            return CableOn_04(self.ctx)


class Block_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1105]):
            self.set_visible_breakable_object(triggerIds=[1005], visible=True)
            self.set_interact_object(triggerIds=[12000305], state=1)
            self.create_monster(spawnIds=[1107], animationEffect=False)
            self.create_monster(spawnIds=[1108], animationEffect=False)
            self.create_monster(spawnIds=[1109], animationEffect=False)
            return CableOn_05(self.ctx)


class Block_3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1106]):
            self.set_visible_breakable_object(triggerIds=[1006], visible=True)
            self.set_interact_object(triggerIds=[12000306], state=1)
            self.create_monster(spawnIds=[1107], animationEffect=False)
            self.create_monster(spawnIds=[1108], animationEffect=False)
            self.create_monster(spawnIds=[1109], animationEffect=False)
            return CableOn_06(self.ctx)


class CableOn_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000304], stateValue=0):
            self.set_interact_object(triggerIds=[12000304], state=2)
            self.move_user_to_pos(pos=[-12687.7676,-1071.39685,2530], rot=[0,0,0])
            return CableDelay_04(self.ctx)


class CableOn_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000305], stateValue=0):
            self.set_interact_object(triggerIds=[12000305], state=2)
            self.move_user_to_pos(pos=[-11673.0137,-6377.65674,1639], rot=[0,0,0])
            return CableDelay_05(self.ctx)


class CableOn_06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000306], stateValue=0):
            self.set_interact_object(triggerIds=[12000306], state=2)
            self.move_user_to_pos(pos=[-11221.6494,6215.7334,433], rot=[0,0,0])
            return CableDelay_06(self.ctx)


class CableDelay_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1004], enable=True)
            return CableOff_04(self.ctx)


class CableDelay_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1005], enable=True)
            return CableOff_05(self.ctx)


class CableDelay_06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1006], enable=True)
            return CableOff_06(self.ctx)


class CableOff_04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900003, key='Block', value=1)
            return End_01(self.ctx)


class CableOff_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900003, key='Block', value=2)
            return End_01(self.ctx)


class CableOff_06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900003, key='Block', value=3)
            return End_01(self.ctx)


class End_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


initial_state = 대기
