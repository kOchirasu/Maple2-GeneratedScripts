""" trigger/52100052_qd/04_randomportal.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002088], state=0) # ToWall_True
        set_interact_object(triggerIds=[10002089], state=0) # ToRoom_True
        set_interact_object(triggerIds=[10002090], state=0) # ToTower_True
        set_mesh(triggerIds=[3200], visible=True, arg3=0, arg4=0, arg5=0) # CurtainBarrier
        set_mesh(triggerIds=[3201,3202], visible=True, arg3=0, arg4=0, arg5=0) # CurtainOpen
        set_mesh(triggerIds=[3300], visible=True, arg3=0, arg4=0, arg5=0) # ToTowerDoorBarrier
        set_effect(triggerIds=[5000], visible=False) # DoorOpen
        set_actor(triggerId=4000, visible=True, initialSequence='Closed') # NextMap
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False) # ToWall
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False) # ToRoom
        set_portal(portalId=30, visible=False, enabled=False, minimapVisible=False) # ToTower
        set_user_value(key='SearchStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='SearchStart', value=1):
            return PickRandomPortal()


#  3개의 문 중에서 하나 뽑기 
class PickRandomPortal(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return ToWall01()
        if random_condition(rate=30):
            return ToRoom01()
        if random_condition(rate=30):
            return ToTower01()


#  테라스로 나가서 성 외벽으로 
class ToWall01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002088], state=1) # ToWall_True
        set_user_value(triggerId=6, key='ToRoomFalse', value=1) # ToRoom_False
        set_user_value(triggerId=7, key='ToTowerFalse', value=1) # ToTowerFalse

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002088], arg2=0):
            return ToWall02()


class ToWall02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3200], visible=False, arg3=0, arg4=0, arg5=0) # CurtainBarrier
        set_mesh(triggerIds=[3201,3202], visible=False, arg3=0, arg4=0, arg5=3) # CurtainOpen
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=False) # ToWall
        set_event_ui(type=1, arg2='$02000396_BF__04_RANDOMPORTAL__0$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ToWallGuide01()


class ToWallGuide01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001563, script='$52100052_QD__04_RANDOMPORTAL__0$', arg4=5) # 이슈라
        set_skip(state=ToWallGuide01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ToWallGuide01Skip()


class ToWallGuide01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  문을 통해 다른 방으로 
class ToRoom01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002089], state=1) # ToRoom_True
        set_user_value(triggerId=5, key='ToWallFalse', value=1) # ToWall_False
        set_user_value(triggerId=7, key='ToTowerFalse', value=1) # ToTowerFalse

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002089], arg2=0):
            return ToRoom02()


class ToRoom02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52100052_QD__04_RANDOMPORTAL__1$', arg3='2000', arg4='0')
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=False) # ToRoom

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ToRoomGuide01()


class ToRoomGuide01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001563, script='$52100052_QD__04_RANDOMPORTAL__2$', arg4=5) # 이슈라
        set_skip(state=ToRoomGuide01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ToRoomGuide01Skip()


class ToRoomGuide01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  계단을 통해 탑으로 
class ToTower01(state.State):
    def on_enter(self):
        set_user_value(triggerId=5, key='ToWallFalse', value=1) # ToWall_False
        set_user_value(triggerId=6, key='ToRoomFalse', value=1) # ToRoom_False
        set_interact_object(triggerIds=[10002090], state=1) # ToTower_True

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002090], arg2=0):
            return ToTower02()


class ToTower02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52100052_QD__04_RANDOMPORTAL__3$', arg3='2000', arg4='0')
        set_mesh(triggerIds=[3300], visible=False, arg3=0, arg4=0, arg5=0) # ToTowerDoorBarrier
        set_effect(triggerIds=[5000], visible=True) # DoorOpen
        set_actor(triggerId=4000, visible=True, initialSequence='Opened') # NextMap
        set_portal(portalId=30, visible=True, enabled=True, minimapVisible=False) # ToTower

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ToTowerGuide01()


class ToTowerGuide01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001563, script='$52100052_QD__04_RANDOMPORTAL__4$', arg4=5) # 이슈라
        set_skip(state=ToTowerGuide01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ToTowerGuide01Skip()


class ToTowerGuide01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_user_value(triggerId=1, key='FindWay', value=1)


