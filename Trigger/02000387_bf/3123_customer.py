""" trigger/02000387_bf/3123_customer.xml """
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
        create_monster(spawnIds=[3123], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9130, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9131, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=3123, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9132, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=3123, patrolName='MS2PatrolData_302')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9133, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=3123, patrolName='MS2PatrolData_303')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9133, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9133, spawnIds=[3123]):
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
            return PickItem_30000623()
        if random_condition(rate=1):
            return PickItem_30000625()
        if random_condition(rate=1):
            return PickItem_30000692()
        if random_condition(rate=1):
            return PickItem_30000696()
        if random_condition(rate=1):
            return PickItem_30000698()


#  	30000623 
class PickItem_30000623(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000623)
        add_effect_nif(spawnId=3123, nifPath='Map/Kerningcity/Indoor/ke_in_prop_bath_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000623()


class DetectItem_30000623(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000623):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000623):
            return WrongItem()


#  	30000625 
class PickItem_30000625(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000625)
        add_effect_nif(spawnId=3123, nifPath='Map/Kerningcity/Indoor/ke_in_prop_shower_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000625()


class DetectItem_30000625(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000625):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000625):
            return WrongItem()


#  	30000692 
class PickItem_30000692(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000692)
        add_effect_nif(spawnId=3123, nifPath='Map/Kerningcity/Indoor/ke_in_prop_dresser_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000692()


class DetectItem_30000692(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000692):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000692):
            return WrongItem()


#  	30000696 
class PickItem_30000696(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000696)
        add_effect_nif(spawnId=3123, nifPath='Npc/Etc/UGC_F1RacingCar/UGC_F1RacingCar_01.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000696()


class DetectItem_30000696(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000696):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000696):
            return WrongItem()


#  	30000698 
class PickItem_30000698(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000698)
        add_effect_nif(spawnId=3123, nifPath='Npc/Etc/UGC_FlameBike_Npc/UGC_FlameBike_03.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000698()


class DetectItem_30000698(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9203], itemId=30000698):
            return RightItem()
        if not detect_liftable_object(boxIds=[9203], itemId=30000698):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=3123)
        set_conversation(type=1, spawnId=3123, script='$02000387_BF__3123_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=3123, patrolName='MS2PatrolData_333')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9303, spawnIds=[3123]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[3123])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=3123)
        set_conversation(type=1, spawnId=3123, script='$02000387_BF__3123_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000623):
            return PickItem_30000623()
        if user_value(key='ItemNumber', value=30000625):
            return PickItem_30000625()
        if user_value(key='ItemNumber', value=30000692):
            return PickItem_30000692()
        if user_value(key='ItemNumber', value=30000696):
            return PickItem_30000696()
        if user_value(key='ItemNumber', value=30000698):
            return PickItem_30000698()


