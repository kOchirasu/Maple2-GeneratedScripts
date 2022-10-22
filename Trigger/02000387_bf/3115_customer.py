""" trigger/02000387_bf/3115_customer.xml """
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
        create_monster(spawnIds=[3115], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9130, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9131, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=3115, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9132, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=3115, patrolName='MS2PatrolData_302')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9133, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=3115, patrolName='MS2PatrolData_303')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9133, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9133, spawnIds=[3115]):
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
            return PickItem_30000617()
        if random_condition(rate=1):
            return PickItem_30000618()
        if random_condition(rate=1):
            return PickItem_30000668()
        if random_condition(rate=1):
            return PickItem_30000671()
        if random_condition(rate=1):
            return PickItem_30000672()
        if random_condition(rate=1):
            return PickItem_30000673()
        if random_condition(rate=1):
            return PickItem_30000674()
        if random_condition(rate=1):
            return PickItem_30000676()


#  	30000617 
class PickItem_30000617(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000617)
        add_effect_nif(spawnId=3115, nifPath='Map/Common/Field/co_fi_prop_game_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000617()


class DetectItem_30000617(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000617):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000617):
            return WrongItem()


#  	30000618 
class PickItem_30000618(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000618)
        add_effect_nif(spawnId=3115, nifPath='Map/Common/Field/co_fi_prop_game_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000618()


class DetectItem_30000618(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000618):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000618):
            return WrongItem()


#  	30000668 
class PickItem_30000668(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000668)
        add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_cranegame_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000668()


class DetectItem_30000668(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000668):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000668):
            return WrongItem()


#  	30000671 
class PickItem_30000671(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000671)
        add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_photosticker_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000671()


class DetectItem_30000671(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000671):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000671):
            return WrongItem()


#  	30000672 
class PickItem_30000672(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000672)
        add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_pingpong_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000672()


class DetectItem_30000672(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000672):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000672):
            return WrongItem()


#  	30000673 
class PickItem_30000673(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000673)
        add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_pooltable_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000673()


class DetectItem_30000673(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000673):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000673):
            return WrongItem()


#  	30000674 
class PickItem_30000674(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000674)
        add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_pump_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000674()


class DetectItem_30000674(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000674):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000674):
            return WrongItem()


#  	30000676 
class PickItem_30000676(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000676)
        add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_soccertable_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000676()


class DetectItem_30000676(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000676):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000676):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=3115)
        set_conversation(type=1, spawnId=3115, script='$02000387_BF__3115_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=3115, patrolName='MS2PatrolData_333')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9303, spawnIds=[3115]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[3115])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=3115)
        set_conversation(type=1, spawnId=3115, script='$02000387_BF__3115_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000617):
            return PickItem_30000617()
        if user_value(key='ItemNumber', value=30000618):
            return PickItem_30000618()
        if user_value(key='ItemNumber', value=30000668):
            return PickItem_30000668()
        if user_value(key='ItemNumber', value=30000671):
            return PickItem_30000671()
        if user_value(key='ItemNumber', value=30000672):
            return PickItem_30000672()
        if user_value(key='ItemNumber', value=30000673):
            return PickItem_30000673()
        if user_value(key='ItemNumber', value=30000674):
            return PickItem_30000674()
        if user_value(key='ItemNumber', value=30000676):
            return PickItem_30000676()


