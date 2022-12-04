""" trigger/02000387_bf/10_randomportal.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2011,2012,2013,2014], visible=True, arg3=0, delay=0, scale=0) # DoorMesh_AlwaysOn
        self.set_effect(triggerIds=[5001], visible=False) # FrontDoorStep
        self.set_effect(triggerIds=[5002], visible=False) # FrontDoorStep
        self.set_effect(triggerIds=[5003], visible=False) # FrontDoorStep
        self.set_effect(triggerIds=[5004], visible=False) # FrontDoorStep
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=14, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=22, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=23, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=24, visible=False, enable=False, minimapVisible=False)
        self.set_actor(triggerId=4101, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(triggerId=4102, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(triggerId=4103, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(triggerId=4104, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_user_value(key='RandomPortalOn', value=0)
        self.set_user_value(key='CounterDoorPick', value=0)
        self.set_user_value(key='DungeonClear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RandomPortalOn', value=1):
            return Guide01(self.ctx)


class Guide01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000387_BF__10_RANDOMPORTAL__0$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[5001], visible=True) # FrontDoorStep
        self.set_effect(triggerIds=[5002], visible=True) # FrontDoorStep
        self.set_effect(triggerIds=[5003], visible=True) # FrontDoorStep
        self.set_effect(triggerIds=[5004], visible=True) # FrontDoorStep

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckMember01(self.ctx)


class CheckMember01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9001, boxId=1, operator='Equal'):
            return CheckMember02(self.ctx)


class CheckMember02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9001, boxId=1, operator='Equal'):
            return CheckMember01(self.ctx)
        if self.count_users(boxId=9002, boxId=1, operator='Equal'):
            return CheckMember03(self.ctx)


class CheckMember03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9001, boxId=1, operator='Equal'):
            return CheckMember01(self.ctx)
        if not self.count_users(boxId=9002, boxId=1, operator='Equal'):
            return CheckMember01(self.ctx)
        if self.count_users(boxId=9003, boxId=1, operator='Equal'):
            return CheckMember04(self.ctx)


class CheckMember04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.count_users(boxId=9001, boxId=1, operator='Equal'):
            return CheckMember01(self.ctx)
        if not self.count_users(boxId=9002, boxId=1, operator='Equal'):
            return CheckMember01(self.ctx)
        if not self.count_users(boxId=9003, boxId=1, operator='Equal'):
            return CheckMember01(self.ctx)
        if self.count_users(boxId=9004, boxId=1, operator='Equal'):
            return DoorActivate01(self.ctx)


class DoorActivate01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return DoorActivate02(self.ctx)


class DoorActivate02(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4101, visible=True, initialSequence='ry_functobj_door_B01_on') # OfficeDoor
        self.set_actor(triggerId=4102, visible=True, initialSequence='ry_functobj_door_B01_on') # OfficeDoor
        self.set_actor(triggerId=4103, visible=True, initialSequence='ry_functobj_door_B01_on') # OfficeDoor
        self.set_actor(triggerId=4104, visible=True, initialSequence='ry_functobj_door_B01_on') # OfficeDoor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PickPortalPattern(self.ctx)


# 4개의 문 중에서 하나만 카운터로
class PickPortalPattern(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return FirstDoorPick(self.ctx)
        if self.random_condition(rate=25):
            return SecondDoorPick(self.ctx)
        if self.random_condition(rate=25):
            return ThirdDoorPick(self.ctx)
        if self.random_condition(rate=25):
            return rdDoorPick4(self.ctx)


class FirstDoorPick(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=22, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=23, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=24, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return GameStart00(self.ctx)


class SecondDoorPick(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=12, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=23, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=24, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return GameStart00(self.ctx)


class ThirdDoorPick(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=13, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=22, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=24, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return GameStart00(self.ctx)


class rdDoorPick4(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=14, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=22, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=23, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return GameStart00(self.ctx)


class GameStart00(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9800, boxId=4, operator='Equal'):
            return GameStart01(self.ctx)
        if self.count_users(boxId=9800, boxId=4, operator='Less'):
            return GameStartDelay01(self.ctx)


class GameStartDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return GameStart01(self.ctx)


class GameStart01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=14, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=21, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=22, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=23, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=24, visible=False, enable=False, minimapVisible=False)
        self.set_actor(triggerId=4101, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(triggerId=4102, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(triggerId=4103, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_actor(triggerId=4104, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        self.set_effect(triggerIds=[5001], visible=False) # FrontDoorStep
        self.set_effect(triggerIds=[5002], visible=False) # FrontDoorStep
        self.set_effect(triggerIds=[5003], visible=False) # FrontDoorStep
        self.set_effect(triggerIds=[5004], visible=False) # FrontDoorStep

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9005, boxId=1, operator='Equal'):
            return GameStart02(self.ctx)
        if self.count_users(boxId=9900, boxId=4, operator='Less'):
            return EndGame01(self.ctx)


class GameStart02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9006, boxId=3, operator='Equal'):
            return secondsWait10(self.ctx)
        if self.count_users(boxId=9900, boxId=4, operator='Less'):
            return EndGame01(self.ctx)


class secondsWait10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear', value=1):
            return Quit(self.ctx)
        if self.wait_tick(waitTick=10000):
            return CheckMemeberAgain(self.ctx)


class CheckMemeberAgain(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9900, boxId=4, operator='Equal'):
            return secondsWait10(self.ctx)
        if self.count_users(boxId=9900, boxId=4, operator='Less'):
            return EndGame01(self.ctx)
        if self.user_value(key='DungeonClear', value=1):
            return Quit(self.ctx)


class EndGame01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000387_BF__10_RANDOMPORTAL__1$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return PCMoveOut01(self.ctx)
        if self.user_value(key='DungeonClear', value=1):
            return Quit(self.ctx)


class PCMoveOut01(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000387, portalId=1, boxId=9900) # 사무실로 강제 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FieredNotice01(self.ctx)


class FieredNotice01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000491, script='$02000387_BF__10_RANDOMPORTAL__2$', arg4=4)
        self.set_skip(state=FieredNotice01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return FieredNotice01Skip(self.ctx)


class FieredNotice01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return FieredNotice02(self.ctx)


class FieredNotice02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000491, script='$02000387_BF__10_RANDOMPORTAL__3$', arg4=4)
        self.set_skip(state=FieredNotice02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return FieredNotice02Skip(self.ctx)


class FieredNotice02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCForceToLeave(self.ctx)


class PCForceToLeave(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0)

    def on_exit(self):
        self.destroy_monster(spawnIds=[100])


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
