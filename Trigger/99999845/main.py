""" trigger/99999845/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000301], state=2)
        self.set_interact_object(triggerIds=[12000302], state=2)
        self.set_interact_object(triggerIds=[12000303], state=2)
        self.set_interact_object(triggerIds=[12000304], state=2)
        self.set_interact_object(triggerIds=[12000305], state=2)
        self.set_interact_object(triggerIds=[12000306], state=2)
        self.set_interact_object(triggerIds=[12000307], state=2)
        self.set_interact_object(triggerIds=[12000308], state=2)
        self.set_interact_object(triggerIds=[12000309], state=2)
        self.set_interact_object(triggerIds=[12000310], state=2)
        self.set_interact_object(triggerIds=[12000311], state=2)
        self.set_interact_object(triggerIds=[12000312], state=2)
        self.set_interact_object(triggerIds=[12000313], state=2)
        self.set_interact_object(triggerIds=[12000314], state=2)
        self.set_interact_object(triggerIds=[12000315], state=2)
        self.set_interact_object(triggerIds=[12000316], state=2)
        self.set_interact_object(triggerIds=[12000317], state=2)
        self.set_interact_object(triggerIds=[12000318], state=2)
        self.set_interact_object(triggerIds=[12000319], state=2)
        self.set_interact_object(triggerIds=[12000320], state=2)
        self.set_interact_object(triggerIds=[12000321], state=2)
        self.set_interact_object(triggerIds=[12000322], state=2)
        self.set_mesh(triggerIds=[1001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1003], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1004], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1005], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[1006], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2003], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2004], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2005], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2006], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2007], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2008], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3004], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3005], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3006], visible=True, arg3=0, delay=0, scale=0)
        self.set_visible_breakable_object(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], visible=False)
        self.set_visible_breakable_object(triggerIds=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], visible=False)
        self.set_visible_breakable_object(triggerIds=[1021,1022], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[900]):
            # self.create_monster(spawnIds=[1001], animationEffect=False)
            # self.create_monster(spawnIds=[1002], animationEffect=False)
            return LineStart(self.ctx)


class LineStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.create_monster(spawnIds=[1102], animationEffect=False)
        self.create_monster(spawnIds=[1103], animationEffect=False)
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], animationEffect=False)
        self.create_monster(spawnIds=[1011,1012,1013,1014,1015,1016,1017,1018,1019,1020], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1101,1103]):
            self.set_mesh(triggerIds=[1001], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1002], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1003], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1004], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1005], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1006], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[2001], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[2002], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[2003], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[2004], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[2005], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[2006], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[2007], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[2008], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3004], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3005], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3006], visible=False, arg3=0, delay=0, scale=0)
            self.set_visible_breakable_object(triggerIds=[1001,1002,1003], visible=True)
            self.set_interact_object(triggerIds=[12000301], state=1)
            self.set_interact_object(triggerIds=[12000302], state=1)
            self.set_interact_object(triggerIds=[12000303], state=1)
            self.create_monster(spawnIds=[1104], animationEffect=False)
            self.create_monster(spawnIds=[1105], animationEffect=False)
            self.create_monster(spawnIds=[1106], animationEffect=False)
            return CableOn_01(self.ctx)


class CableOn_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000302], stateValue=0):
            self.set_interact_object(triggerIds=[12000301], state=2)
            self.set_interact_object(triggerIds=[12000302], state=2)
            self.set_interact_object(triggerIds=[12000303], state=2)
            self.move_user_to_pos(pos=[-15571.11,75.2856445,3600], rot=[0,0,0])
            # self.set_mesh(triggerIds=[2000], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2001], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2002], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2003], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2004], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2005], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2006], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2007], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2008], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[2009], visible=True, arg3=0, delay=0, scale=0)
            return CableDelay_01_1(self.ctx)
        if self.object_interacted(interactIds=[12000303], stateValue=0):
            self.set_interact_object(triggerIds=[12000301], state=2)
            self.set_interact_object(triggerIds=[12000302], state=2)
            self.set_interact_object(triggerIds=[12000303], state=2)
            self.move_user_to_pos(pos=[-15571.11,-1561.813,3600], rot=[0,0,0])
            # self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[3004], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[3005], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[3006], visible=True, arg3=0, delay=0, scale=0)
            return CableDelay_01_2(self.ctx)
        if self.object_interacted(interactIds=[12000301], stateValue=0):
            self.set_interact_object(triggerIds=[12000301], state=2)
            self.set_interact_object(triggerIds=[12000302], state=2)
            self.set_interact_object(triggerIds=[12000303], state=2)
            self.move_user_to_pos(pos=[-15571.11,1730.293,3600], rot=[0,0,0])
            # self.set_mesh(triggerIds=[1001], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[1002], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[1003], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[1004], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[1005], visible=True, arg3=0, delay=0, scale=0)
            # self.set_mesh(triggerIds=[1006], visible=True, arg3=0, delay=0, scale=0)
            return CableDelay_01_3(self.ctx)


class CableDelay_01_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1002], enable=True)
            return CableOff_01(self.ctx)


class CableDelay_01_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1003], enable=True)
            return CableOff_02(self.ctx)


class CableDelay_01_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_breakable(triggerIds=[1001], enable=True)
            return CableOff_03(self.ctx)


class CableOff_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[-13125,75,2550], rot=[0,0,0])
            self.set_user_value(triggerId=900002, key='Block', value=1)
            return End_01(self.ctx)


class CableOff_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[-13275,-5025,1650], rot=[0,0,0])
            self.set_user_value(triggerId=900002, key='Block', value=2)
            return End_01(self.ctx)


class CableOff_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # self.move_user_to_pos(pos=[-12925,5025,550], rot=[0,0,0])
            self.set_user_value(triggerId=900002, key='Block', value=3)
            return End_01(self.ctx)


class End_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            # self.set_visible_breakable_object(triggerIds=[1001], visible=False)
            # self.set_visible_breakable_object(triggerIds=[1002], visible=False)
            # self.set_visible_breakable_object(triggerIds=[1003], visible=False)
            # <transition state="대기"/>
            pass


initial_state = 대기
