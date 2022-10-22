""" trigger/02000387_bf/3103_customer.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001101], state=0) # Greeting
        set_user_value(key='CustomerEnter', value=0)
        set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='CustomerEnter', value=1):
            return CustomerEnterDelay()


class CustomerEnterDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CustomerEnter()


class CustomerEnter(state.State):
    def on_enter(self):
        create_monster(spawnIds=[3103], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9130, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9131, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=3103, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9132, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=3103, patrolName='MS2PatrolData_302')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9133, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=3103, patrolName='MS2PatrolData_303')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9133, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9133, spawnIds=[3103]):
            return WaitGreeting()


class WaitGreeting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001101], state=1) # Greeting

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001101], arg2=0):
            return OrderRandomPick()

    def on_exit(self):
        set_interact_object(triggerIds=[10001101], state=2) # Greeting


#  고객 주문 랜덤
class OrderRandomPick(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return PickItem_30000677()
        if random_condition(rate=1):
            return PickItem_30000679()
        if random_condition(rate=1):
            return PickItem_30000684()
        if random_condition(rate=1):
            return None # Missing State: PickItem_30000687


#  	30000677 
class PickItem_30000677(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000677)
        add_effect_nif(spawnId=3103, nifPath='Map/Royalcity/Field/ry_fi_prop_plane_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000677()


class DetectItem_30000677(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000677):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000677):
            return WrongItem()


#  	30000679 
class PickItem_30000679(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000679)
        add_effect_nif(spawnId=3103, nifPath='Map/Royalcity/Field/ry_fi_prop_yacht_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000679()


class DetectItem_30000679(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000679):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000679):
            return WrongItem()


#  	30000684 
class PickItem_30000684(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000684)
        add_effect_nif(spawnId=3103, nifPath='Map/Ludibrium/Field/lu_fi_prop_rocket_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000684()


class DetectItem_30000684(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000684):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000684):
            return WrongItem()


#  	30000697 
class PickItem_30000697(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000697)
        add_effect_nif(spawnId=3103, nifPath='Npc/Etc/UGC_Poclain/UGC_Poclain_01.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000697()


class DetectItem_30000697(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000697):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000697):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=3103)
        set_conversation(type=1, spawnId=3103, script='$02000387_BF__3103_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=3103, patrolName='MS2PatrolData_333')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9303, spawnIds=[3103]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[3103])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=3103)
        set_conversation(type=1, spawnId=3103, script='$02000387_BF__3103_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000677):
            return PickItem_30000677()
        if user_value(key='ItemNumber', value=30000679):
            return PickItem_30000679()
        if user_value(key='ItemNumber', value=30000684):
            return PickItem_30000684()
        if user_value(key='ItemNumber', value=30000697):
            return PickItem_30000697()

