""" trigger/02000387_bf/10_randomportal.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2011,2012,2013,2014], visible=True, arg3=0, arg4=0, arg5=0) # DoorMesh_AlwaysOn
        set_effect(triggerIds=[5001], visible=False) # FrontDoorStep
        set_effect(triggerIds=[5002], visible=False) # FrontDoorStep
        set_effect(triggerIds=[5003], visible=False) # FrontDoorStep
        set_effect(triggerIds=[5004], visible=False) # FrontDoorStep
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=14, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=22, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=23, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=24, visible=False, enabled=False, minimapVisible=False)
        set_actor(triggerId=4101, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        set_actor(triggerId=4102, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        set_actor(triggerId=4103, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        set_actor(triggerId=4104, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        set_user_value(key='RandomPortalOn', value=0)
        set_user_value(key='CounterDoorPick', value=0)
        set_user_value(key='DungeonClear', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RandomPortalOn', value=1):
            return Guide01()


class Guide01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000387_BF__10_RANDOMPORTAL__0$', arg3='3000', arg4='0')
        set_effect(triggerIds=[5001], visible=True) # FrontDoorStep
        set_effect(triggerIds=[5002], visible=True) # FrontDoorStep
        set_effect(triggerIds=[5003], visible=True) # FrontDoorStep
        set_effect(triggerIds=[5004], visible=True) # FrontDoorStep

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckMember01()


class CheckMember01(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=1, operator='Equal'):
            return CheckMember02()


class CheckMember02(state.State):
    def on_tick(self) -> state.State:
        if not count_users(boxId=9001, boxId=1, operator='Equal'):
            return CheckMember01()
        if count_users(boxId=9002, boxId=1, operator='Equal'):
            return CheckMember03()


class CheckMember03(state.State):
    def on_tick(self) -> state.State:
        if not count_users(boxId=9001, boxId=1, operator='Equal'):
            return CheckMember01()
        if not count_users(boxId=9002, boxId=1, operator='Equal'):
            return CheckMember01()
        if count_users(boxId=9003, boxId=1, operator='Equal'):
            return CheckMember04()


class CheckMember04(state.State):
    def on_tick(self) -> state.State:
        if not count_users(boxId=9001, boxId=1, operator='Equal'):
            return CheckMember01()
        if not count_users(boxId=9002, boxId=1, operator='Equal'):
            return CheckMember01()
        if not count_users(boxId=9003, boxId=1, operator='Equal'):
            return CheckMember01()
        if count_users(boxId=9004, boxId=1, operator='Equal'):
            return DoorActivate01()


class DoorActivate01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return DoorActivate02()


class DoorActivate02(state.State):
    def on_enter(self):
        set_actor(triggerId=4101, visible=True, initialSequence='ry_functobj_door_B01_on') # OfficeDoor
        set_actor(triggerId=4102, visible=True, initialSequence='ry_functobj_door_B01_on') # OfficeDoor
        set_actor(triggerId=4103, visible=True, initialSequence='ry_functobj_door_B01_on') # OfficeDoor
        set_actor(triggerId=4104, visible=True, initialSequence='ry_functobj_door_B01_on') # OfficeDoor

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PickPortalPattern()


#  4개의 문 중에서 하나만 카운터로 
class PickPortalPattern(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return FirstDoorPick()
        if random_condition(rate=25):
            return SecondDoorPick()
        if random_condition(rate=25):
            return ThirdDoorPick()
        if random_condition(rate=25):
            return rdDoorPick4()


class FirstDoorPick(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=22, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=23, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=24, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GameStart00()


class SecondDoorPick(state.State):
    def on_enter(self):
        set_portal(portalId=12, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=23, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=24, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GameStart00()


class ThirdDoorPick(state.State):
    def on_enter(self):
        set_portal(portalId=13, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=22, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=24, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GameStart00()


class rdDoorPick4(state.State):
    def on_enter(self):
        set_portal(portalId=14, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=22, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=23, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GameStart00()


class GameStart00(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9800, boxId=4, operator='Equal'):
            return GameStart01()
        if count_users(boxId=9800, boxId=4, operator='Less'):
            return GameStartDelay01()


class GameStartDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GameStart01()


class GameStart01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=14, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=21, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=22, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=23, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=24, visible=False, enabled=False, minimapVisible=False)
        set_actor(triggerId=4101, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        set_actor(triggerId=4102, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        set_actor(triggerId=4103, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        set_actor(triggerId=4104, visible=True, initialSequence='ry_functobj_door_B01_off') # OfficeDoor
        set_effect(triggerIds=[5001], visible=False) # FrontDoorStep
        set_effect(triggerIds=[5002], visible=False) # FrontDoorStep
        set_effect(triggerIds=[5003], visible=False) # FrontDoorStep
        set_effect(triggerIds=[5004], visible=False) # FrontDoorStep

    def on_tick(self) -> state.State:
        if count_users(boxId=9005, boxId=1, operator='Equal'):
            return GameStart02()
        if count_users(boxId=9900, boxId=4, operator='Less'):
            return EndGame01()


class GameStart02(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9006, boxId=3, operator='Equal'):
            return secondsWait10()
        if count_users(boxId=9900, boxId=4, operator='Less'):
            return EndGame01()


class secondsWait10(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DungeonClear', value=1):
            return Quit()
        if wait_tick(waitTick=10000):
            return CheckMemeberAgain()


class CheckMemeberAgain(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9900, boxId=4, operator='Equal'):
            return secondsWait10()
        if count_users(boxId=9900, boxId=4, operator='Less'):
            return EndGame01()
        if user_value(key='DungeonClear', value=1):
            return Quit()


class EndGame01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000387_BF__10_RANDOMPORTAL__1$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PCMoveOut01()
        if user_value(key='DungeonClear', value=1):
            return Quit()


class PCMoveOut01(state.State):
    def on_enter(self):
        move_user(mapId=2000387, portalId=1, boxId=9900) # 사무실로 강제 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FieredNotice01()


class FieredNotice01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000491, script='$02000387_BF__10_RANDOMPORTAL__2$', arg4=4)
        set_skip(state=FieredNotice01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FieredNotice01Skip()


class FieredNotice01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return FieredNotice02()


class FieredNotice02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000491, script='$02000387_BF__10_RANDOMPORTAL__3$', arg4=4)
        set_skip(state=FieredNotice02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FieredNotice02Skip()


class FieredNotice02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCForceToLeave()


class PCForceToLeave(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)

    def on_exit(self):
        destroy_monster(spawnIds=[100])


class Quit(state.State):
    pass


