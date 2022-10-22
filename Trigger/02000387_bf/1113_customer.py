""" trigger/02000387_bf/1113_customer.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001099], state=0) # Greeting
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
        create_monster(spawnIds=[1113], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9110, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9111, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=1113, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9112, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=1113, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9113, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=1113, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9113, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9113, spawnIds=[1113]):
            return WaitGreeting()


class WaitGreeting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001099], state=1) # Greeting

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001099], arg2=0):
            return OrderRandomPick()

    def on_exit(self):
        set_interact_object(triggerIds=[10001099], state=2) # Greeting


#  고객 주문 랜덤
class OrderRandomPick(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return PickItem_30000617()
        if random_condition(rate=1):
            return PickItem_30000618()
        if random_condition(rate=1):
            return PickItem_30000622()
        if random_condition(rate=1):
            return None # Missing State: PickItem_30000661
        if random_condition(rate=1):
            return PickItem_30000662()
        if random_condition(rate=1):
            return PickItem_30000664()
        if random_condition(rate=1):
            return PickItem_30000665()
        if random_condition(rate=1):
            return PickItem_30000666()
        if random_condition(rate=1):
            return PickItem_30000667()
        if random_condition(rate=1):
            return PickItem_30000670()
        if random_condition(rate=1):
            return PickItem_30000681()
        if random_condition(rate=1):
            return PickItem_30000684()


#  	30000617 
class PickItem_30000617(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000617)
        add_effect_nif(spawnId=1113, nifPath='Map/Common/Field/co_fi_prop_game_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000617()


class DetectItem_30000617(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000617):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000617):
            return WrongItem()


#  	30000618 
class PickItem_30000618(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000618)
        add_effect_nif(spawnId=1113, nifPath='Map/Common/Field/co_fi_prop_game_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000618()


class DetectItem_30000618(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000618):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000618):
            return WrongItem()


#  	30000622 
class PickItem_30000622(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000622)
        add_effect_nif(spawnId=1113, nifPath='Map/Iceland/Indoor/ic_in_prop_snowball_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000622()


class DetectItem_30000622(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000622):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000622):
            return WrongItem()


#  	30000662 
class PickItem_30000662(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000662)
        add_effect_nif(spawnId=1113, nifPath='Map/Royalcity/Indoor/ry_in_prop_basketball_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000662()


class DetectItem_30000662(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000662):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000662):
            return WrongItem()


#  	30000664 
class PickItem_30000664(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000664)
        add_effect_nif(spawnId=1113, nifPath='Map/Royalcity/Indoor/ry_in_prop_trampoline_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000664()


class DetectItem_30000664(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000664):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000664):
            return WrongItem()


#  	30000665 
class PickItem_30000665(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000665)
        add_effect_nif(spawnId=1113, nifPath='Map/Royalcity/Indoor/ry_in_prop_baseballcart_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000665()


class DetectItem_30000665(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000665):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000665):
            return WrongItem()


#  	30000666 
class PickItem_30000666(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000666)
        add_effect_nif(spawnId=1113, nifPath='Map/Royalcity/Indoor/ry_in_prop_basketball_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000666()


class DetectItem_30000666(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000666):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000666):
            return WrongItem()


#  	30000667 
class PickItem_30000667(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000667)
        add_effect_nif(spawnId=1113, nifPath='Map/Royalcity/Indoor/ry_in_prop_handball_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000667()


class DetectItem_30000667(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000667):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000667):
            return WrongItem()


#  	30000670 
class PickItem_30000670(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000670)
        add_effect_nif(spawnId=1113, nifPath='Map/Royalcity/Indoor/ry_in_prop_goalpost_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000670()


class DetectItem_30000670(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000670):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000670):
            return WrongItem()


#  	30000681 
class PickItem_30000681(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000681)
        add_effect_nif(spawnId=1113, nifPath='Map/Orient/Field/or_fi_prop_seesaw_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000681()


class DetectItem_30000681(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000681):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000681):
            return WrongItem()


#  	30000684 
class PickItem_30000684(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000684)
        add_effect_nif(spawnId=1113, nifPath='Map/Ludibrium/Field/lu_fi_prop_rocket_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000684()


class DetectItem_30000684(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000684):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000684):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=1113)
        set_conversation(type=1, spawnId=1113, script='$02000387_BF__1113_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=1113, patrolName='MS2PatrolData_111')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9301, spawnIds=[1113]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1113])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=1113)
        set_conversation(type=1, spawnId=1113, script='$02000387_BF__1113_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000617):
            return PickItem_30000617()
        if user_value(key='ItemNumber', value=30000618):
            return PickItem_30000618()
        if user_value(key='ItemNumber', value=30000622):
            return PickItem_30000622()
        if user_value(key='ItemNumber', value=30000661):
            return None # Missing State: PickItem_30000661
        if user_value(key='ItemNumber', value=30000662):
            return PickItem_30000662()
        if user_value(key='ItemNumber', value=30000664):
            return PickItem_30000664()
        if user_value(key='ItemNumber', value=30000665):
            return PickItem_30000665()
        if user_value(key='ItemNumber', value=30000666):
            return PickItem_30000666()
        if user_value(key='ItemNumber', value=30000667):
            return PickItem_30000667()
        if user_value(key='ItemNumber', value=30000670):
            return PickItem_30000670()
        if user_value(key='ItemNumber', value=30000681):
            return PickItem_30000681()
        if user_value(key='ItemNumber', value=30000684):
            return PickItem_30000684()


