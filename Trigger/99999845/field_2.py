""" trigger/99999845/field_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000307], state=2)
        self.set_interact_object(triggerIds=[12000308], state=2)
        self.set_interact_object(triggerIds=[12000309], state=2)
        self.set_interact_object(triggerIds=[12000310], state=2)
        self.set_interact_object(triggerIds=[12000311], state=2)
        self.set_interact_object(triggerIds=[12000312], state=2)
        # <action name="SetVisibleBreakableObject" arg1="1001,1002,1003,1004,1005,1006,1007,1008,1009,1010" arg2="0" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block', value=1):
            self.set_user_value(triggerId=900003, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block', value=2):
            self.set_user_value(triggerId=900003, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block', value=3):
            self.set_user_value(triggerId=900003, key='Block', value=0)
            return Block_3(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1107]):
            self.set_visible_breakable_object(triggerIds=[1007], visible=True)
            self.set_visible_breakable_object(triggerIds=[1008], visible=True)
            self.set_interact_object(triggerIds=[12000307], state=1)
            self.set_interact_object(triggerIds=[12000308], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            return CableOn_07_08(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1108]):
            self.set_visible_breakable_object(triggerIds=[1009], visible=True)
            self.set_visible_breakable_object(triggerIds=[1010], visible=True)
            self.set_interact_object(triggerIds=[12000309], state=1)
            self.set_interact_object(triggerIds=[12000310], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            return CableOn_09_10(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1109]):
            self.set_visible_breakable_object(triggerIds=[1011], visible=True)
            self.set_visible_breakable_object(triggerIds=[1012], visible=True)
            self.set_interact_object(triggerIds=[12000311], state=1)
            self.set_interact_object(triggerIds=[12000312], state=1)
            self.create_monster(spawnIds=[1110], animationEffect=False)
            self.create_monster(spawnIds=[1111], animationEffect=False)
            self.create_monster(spawnIds=[1112], animationEffect=False)
            self.create_monster(spawnIds=[1113], animationEffect=False)
            return CableOn_11_12(self.ctx)


class CableOn_07_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000307], stateValue=0):
            self.set_interact_object(triggerIds=[12000307], state=2)
            self.set_interact_object(triggerIds=[12000308], state=2)
            self.move_user_to_pos(pos=[-8476.297,-3480.99072,1343], rot=[0,0,0])
            return CableDelay_07(self.ctx)
        if self.object_interacted(interactIds=[12000308], stateValue=0):
            self.set_interact_object(triggerIds=[12000307], state=2)
            self.set_interact_object(triggerIds=[12000308], state=2)
            self.move_user_to_pos(pos=[-6726.70264,-377.953552,1343], rot=[0,0,0])
            return CableDelay_08(self.ctx)


class CableOn_09_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000309], stateValue=0):
            self.set_interact_object(triggerIds=[12000309], state=2)
            self.set_interact_object(triggerIds=[12000310], state=2)
            self.move_user_to_pos(pos=[-8321.446,-7475.03271,135], rot=[0,0,0])
            return CableDelay_09(self.ctx)
        if self.object_interacted(interactIds=[12000310], stateValue=0):
            self.set_interact_object(triggerIds=[12000309], state=2)
            self.set_interact_object(triggerIds=[12000310], state=2)
            self.move_user_to_pos(pos=[-6576.207,-9063.119,135], rot=[0,0,0])
            return CableDelay_10(self.ctx)


class CableOn_11_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000311], stateValue=0):
            self.set_interact_object(triggerIds=[12000311], state=2)
            self.set_interact_object(triggerIds=[12000312], state=2)
            self.move_user_to_pos(pos=[-7723.194,5673.29346,2690], rot=[0,0,0])
            return CableDelay_11(self.ctx)
        if self.object_interacted(interactIds=[12000312], stateValue=0):
            self.set_interact_object(triggerIds=[12000311], state=2)
            self.set_interact_object(triggerIds=[12000312], state=2)
            self.move_user_to_pos(pos=[-6276.41748,8028.68164,2690], rot=[0,0,0])
            return CableDelay_12(self.ctx)


class CableDelay_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1007], enable=True)
            return CableOff_07(self.ctx)


class CableDelay_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1008], enable=True)
            return CableOff_08(self.ctx)


class CableDelay_09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1009], enable=True)
            return CableOff_09(self.ctx)


class CableDelay_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1010], enable=True)
            return CableOff_10(self.ctx)


class CableDelay_11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1011], enable=True)
            return CableOff_11(self.ctx)


class CableDelay_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1012], enable=True)
            return CableOff_12(self.ctx)


class CableOff_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=2)
            return End_02(self.ctx)


class CableOff_08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=1)
            return End_02(self.ctx)


class CableOff_09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=2)
            return End_02(self.ctx)


class CableOff_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=3)
            return End_02(self.ctx)


class CableOff_11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=1)
            return End_02(self.ctx)


class CableOff_12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_user_value(triggerId=900004, key='Block', value=4)
            return End_02(self.ctx)


class End_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


initial_state = 대기
