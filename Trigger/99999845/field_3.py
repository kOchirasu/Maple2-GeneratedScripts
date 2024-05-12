""" trigger/99999845/field_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000313], state=2)
        self.set_interact_object(triggerIds=[12000314], state=2)
        self.set_interact_object(triggerIds=[12000315], state=2)
        self.set_interact_object(triggerIds=[12000316], state=2)
        self.set_interact_object(triggerIds=[12000317], state=2)
        self.set_interact_object(triggerIds=[12000318], state=2)
        # self.set_visible_breakable_object(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], visible=False)
        # self.set_visible_breakable_object(triggerIds=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], visible=False)
        # self.set_visible_breakable_object(triggerIds=[1021,1022], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Block', value=1):
            self.set_user_value(triggerId=900004, key='Block', value=0)
            return Block_1(self.ctx)
        if self.user_value(key='Block', value=2):
            self.set_user_value(triggerId=900004, key='Block', value=0)
            return Block_2(self.ctx)
        if self.user_value(key='Block', value=3):
            self.set_user_value(triggerId=900004, key='Block', value=0)
            return Block_3(self.ctx)
        if self.user_value(key='Block', value=4):
            self.set_user_value(triggerId=900004, key='Block', value=0)
            return Block_4(self.ctx)


class Block_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1110]):
            self.set_visible_breakable_object(triggerIds=[1013], visible=True)
            self.set_interact_object(triggerIds=[12000313], state=1)
            self.create_monster(spawnIds=[1114], animationEffect=False)
            self.create_monster(spawnIds=[1115], animationEffect=False)
            self.create_monster(spawnIds=[1116], animationEffect=False)
            return CableOn_13(self.ctx)


class Block_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1111]):
            self.set_visible_breakable_object(triggerIds=[1014], visible=True)
            self.set_visible_breakable_object(triggerIds=[1015], visible=True)
            self.set_interact_object(triggerIds=[12000314], state=1)
            self.set_interact_object(triggerIds=[12000315], state=1)
            self.create_monster(spawnIds=[1114], animationEffect=False)
            self.create_monster(spawnIds=[1115], animationEffect=False)
            self.create_monster(spawnIds=[1116], animationEffect=False)
            return CableOn_14_15(self.ctx)


class Block_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1112]):
            self.set_visible_breakable_object(triggerIds=[1016], visible=True)
            self.set_visible_breakable_object(triggerIds=[1017], visible=True)
            self.set_interact_object(triggerIds=[12000316], state=1)
            self.set_interact_object(triggerIds=[12000317], state=1)
            self.create_monster(spawnIds=[1114], animationEffect=False)
            self.create_monster(spawnIds=[1115], animationEffect=False)
            self.create_monster(spawnIds=[1116], animationEffect=False)
            return CableOn_16_17(self.ctx)


class Block_4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1113]):
            self.set_visible_breakable_object(triggerIds=[1018], visible=True)
            self.set_interact_object(triggerIds=[12000318], state=1)
            self.create_monster(spawnIds=[1114], animationEffect=False)
            self.create_monster(spawnIds=[1115], animationEffect=False)
            self.create_monster(spawnIds=[1116], animationEffect=False)
            return CableOn_18(self.ctx)


class CableOn_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000313], stateValue=0):
            self.set_interact_object(triggerIds=[12000313], state=2)
            self.move_user_to_pos(pos=[-2514.072,3816.40259,1500], rot=[0,0,0])
            return CableDelay_13(self.ctx)


class CableOn_14_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000314], stateValue=0):
            self.set_interact_object(triggerIds=[12000314], state=2)
            self.set_interact_object(triggerIds=[12000315], state=2)
            self.move_user_to_pos(pos=[-3524.431,-1479.53162,137], rot=[0,0,0])
            return CableDelay_14(self.ctx)
        if self.object_interacted(interactIds=[12000315], stateValue=0):
            self.set_interact_object(triggerIds=[12000314], state=2)
            self.set_interact_object(triggerIds=[12000315], state=2)
            self.move_user_to_pos(pos=[-1478.22412,-4127.897,137], rot=[0,0,0])
            return CableDelay_15(self.ctx)


class CableOn_16_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000316], stateValue=0):
            self.set_interact_object(triggerIds=[12000316], state=2)
            self.set_interact_object(triggerIds=[12000317], state=2)
            self.move_user_to_pos(pos=[-848.5522,-7473.63,2690], rot=[0,0,0])
            return CableDelay_16(self.ctx)
        if self.object_interacted(interactIds=[12000317], stateValue=0):
            self.set_interact_object(triggerIds=[12000316], state=2)
            self.set_interact_object(triggerIds=[12000317], state=2)
            self.move_user_to_pos(pos=[1372.17615,-8612.513,2690], rot=[0,0,0])
            return CableDelay_17(self.ctx)


class CableOn_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000318], stateValue=0):
            self.set_interact_object(triggerIds=[12000318], state=2)
            self.move_user_to_pos(pos=[-840.132935,6427.83936,1640], rot=[0,0,0])
            return CableDelay_18(self.ctx)


class CableDelay_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1013], enable=True)
            return CableOff_13(self.ctx)


class CableDelay_14(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1014], enable=True)
            return CableOff_14(self.ctx)


class CableDelay_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1015], enable=True)
            return CableOff_15(self.ctx)


class CableDelay_16(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1016], enable=True)
            return CableOff_16(self.ctx)


class CableDelay_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1017], enable=True)
            return CableOff_17(self.ctx)


class CableDelay_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1018], enable=True)
            return CableOff_18(self.ctx)


class CableOff_13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[525,1425,300], rot=[0,0,0])
            self.set_user_value(triggerId=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_14(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[-375,-75,300], rot=[0,0,0])
            self.set_user_value(triggerId=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_15(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[3375,-5475,1500], rot=[0,0,0])
            self.set_user_value(triggerId=900005, key='Block', value=2)
            return End_03(self.ctx)


class CableOff_16(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[525,-1575,300], rot=[0,0,0])
            self.set_user_value(triggerId=900005, key='Block', value=1)
            return End_03(self.ctx)


class CableOff_17(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[3975,-5925,1500], rot=[0,0,0])
            self.set_user_value(triggerId=900005, key='Block', value=2)
            return End_03(self.ctx)


class CableOff_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[2475,4575,2550], rot=[0,0,0])
            self.set_user_value(triggerId=900005, key='Block', value=3)
            return End_03(self.ctx)


class End_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            # self.set_visible_breakable_object(triggerIds=[1013], visible=False)
            # self.set_visible_breakable_object(triggerIds=[1014], visible=False)
            # self.set_visible_breakable_object(triggerIds=[1015], visible=False)
            # self.set_visible_breakable_object(triggerIds=[1016], visible=False)
            # self.set_visible_breakable_object(triggerIds=[1017], visible=False)
            # self.set_visible_breakable_object(triggerIds=[1018], visible=False)
            return 대기(self.ctx)


initial_state = 대기
