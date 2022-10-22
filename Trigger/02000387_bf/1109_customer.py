""" trigger/02000387_bf/1109_customer.xml """
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
        create_monster(spawnIds=[1109], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9110, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9111, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=1109, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9112, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=1109, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9113, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=1109, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9113, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9113, spawnIds=[1109]):
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
            return PickItem_30000641()
        if random_condition(rate=1):
            return PickItem_30000647()
        if random_condition(rate=1):
            return PickItem_30000648()
        if random_condition(rate=1):
            return PickItem_30000711()


#  	30000641 
class PickItem_30000641(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000641)
        add_effect_nif(spawnId=1109, nifPath='Map/Henesys/Indoor/he_in_prop_kettle_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000641()


class DetectItem_30000641(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000641):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000641):
            return WrongItem()


#  	30000647 
class PickItem_30000647(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000647)
        add_effect_nif(spawnId=1109, nifPath='Map/UGC/Indoor/ugc_in_funct_alchemy_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000647()


class DetectItem_30000647(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000647):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000647):
            return WrongItem()


#  	30000648 
class PickItem_30000648(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000648)
        add_effect_nif(spawnId=1109, nifPath='Map/UGC/Indoor/ugc_in_funct_alchemy_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000648()


class DetectItem_30000648(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000648):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000648):
            return WrongItem()


#  	30000711 
class PickItem_30000711(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000711)
        add_effect_nif(spawnId=1109, nifPath='Map/UGC/Indoor/ugc_in_funct_workstone_G01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000711()


class DetectItem_30000711(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000711):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000711):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=1109)
        set_conversation(type=1, spawnId=1109, script='$02000387_BF__1109_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=1109, patrolName='MS2PatrolData_111')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9301, spawnIds=[1109]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1109])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=1109)
        set_conversation(type=1, spawnId=1109, script='$02000387_BF__1109_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000641):
            return PickItem_30000641()
        if user_value(key='ItemNumber', value=30000647):
            return PickItem_30000647()
        if user_value(key='ItemNumber', value=30000648):
            return PickItem_30000648()
        if user_value(key='ItemNumber', value=30000711):
            return PickItem_30000711()


