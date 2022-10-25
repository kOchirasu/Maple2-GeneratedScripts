""" trigger/99999845/field_5.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000322], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Block', value=1):
            self.set_user_value(triggerId=900006, key='Block', value=0)
            return Block_1(self.ctx)


class Block_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[1117]):
            self.set_visible_breakable_object(triggerIds=[1022], visible=True)
            self.set_interact_object(triggerIds=[12000322], state=1)
            return None # Missing State: CableOn_04


class CableOn_22(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000322], stateValue=0):
            self.set_interact_object(triggerIds=[12000322], state=2)
            self.move_user_to_pos(pos=[-12687.7676,-1071.39685,2530], rot=[0,0,0])
            return CableDelay_04(self.ctx)


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
            self.move_user_to_pos(pos=[-9825,-1425,1350], rot=[0,0,0])
            self.set_user_value(triggerId=900003, key='Block', value=1)
            return End_01(self.ctx)


class CableOff_05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.move_user_to_pos(pos=[-9375,-9225,150], rot=[0,0,0])
            self.set_user_value(triggerId=900003, key='Block', value=2)
            return End_01(self.ctx)


class CableOff_06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.move_user_to_pos(pos=[-8475,7275,2700], rot=[0,0,0])
            self.set_user_value(triggerId=900003, key='Block', value=3)
            return End_01(self.ctx)


class End_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_visible_breakable_object(triggerIds=[1004], visible=False)
            self.set_visible_breakable_object(triggerIds=[1005], visible=False)
            self.set_visible_breakable_object(triggerIds=[1006], visible=False)
            return None


initial_state = 대기
