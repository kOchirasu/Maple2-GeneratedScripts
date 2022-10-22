""" trigger/02000387_bf/2118_customer.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001100], state=0) # Greeting
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
        create_monster(spawnIds=[2118], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9120, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9121, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=2118, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9122, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=2118, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=2118, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9123, spawnIds=[2118]):
            return WaitGreeting()


class WaitGreeting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001100], state=1) # Greeting

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001100], arg2=0):
            return OrderRandomPick()

    def on_exit(self):
        set_interact_object(triggerIds=[10001100], state=2) # Greeting


#  고객 주문 랜덤
class OrderRandomPick(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return PickItem_30000647()
        if random_condition(rate=1):
            return PickItem_30000648()
        if random_condition(rate=1):
            return PickItem_30000657()
        if random_condition(rate=1):
            return PickItem_30000661()
        if random_condition(rate=1):
            return PickItem_30000690()
        if random_condition(rate=1):
            return PickItem_30000713()
        if random_condition(rate=1):
            return PickItem_30000714()


#  	30000647 
class PickItem_30000647(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000647)
        add_effect_nif(spawnId=2118, nifPath='Map/UGC/Indoor/ugc_in_funct_alchemy_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000647()


class DetectItem_30000647(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000647):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000647):
            return WrongItem()


#  	30000648 
class PickItem_30000648(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000648)
        add_effect_nif(spawnId=2118, nifPath='Map/UGC/Indoor/ugc_in_funct_alchemy_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000648()


class DetectItem_30000648(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000648):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000648):
            return WrongItem()


#  	30000657 
class PickItem_30000657(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000657)
        add_effect_nif(spawnId=2118, nifPath='Map/Iceland/Indoor/ic_in_prop_bed_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000657()


class DetectItem_30000657(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000657):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000657):
            return WrongItem()


#  	30000661 
class PickItem_30000661(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000661)
        add_effect_nif(spawnId=2118, nifPath='Map/Royalcity/Indoor/ry_in_cubric_fishtank_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000661()


class DetectItem_30000661(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000661):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000661):
            return WrongItem()


#  	30000690 
class PickItem_30000690(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000690)
        add_effect_nif(spawnId=2118, nifPath='Map/Tria/Indoor/tr_in_prop_sofa_D01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000690()


class DetectItem_30000690(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000690):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000690):
            return WrongItem()


#  	30000713 
class PickItem_30000713(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000713)
        add_effect_nif(spawnId=2118, nifPath='Map/Steampunk/Indoor/sp_in_prop_desk_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000713()


class DetectItem_30000713(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000713):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000713):
            return WrongItem()


#  	30000714 
class PickItem_30000714(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000714)
        add_effect_nif(spawnId=2118, nifPath='Map/SF/Field/sf_fi_prop_incubator_D01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000714()


class DetectItem_30000714(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000714):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000714):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=2118)
        set_conversation(type=1, spawnId=2118, script='$02000387_BF__2118_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=2118, patrolName='MS2PatrolData_222')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9302, spawnIds=[2118]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2118])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=2118)
        set_conversation(type=1, spawnId=2118, script='$02000387_BF__2118_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000647):
            return PickItem_30000647()
        if user_value(key='ItemNumber', value=30000648):
            return PickItem_30000648()
        if user_value(key='ItemNumber', value=30000657):
            return PickItem_30000657()
        if user_value(key='ItemNumber', value=30000661):
            return PickItem_30000661()
        if user_value(key='ItemNumber', value=30000690):
            return PickItem_30000690()
        if user_value(key='ItemNumber', value=30000713):
            return PickItem_30000713()
        if user_value(key='ItemNumber', value=30000714):
            return PickItem_30000714()


