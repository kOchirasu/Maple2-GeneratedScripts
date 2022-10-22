""" trigger/02000387_bf/4116_customer.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001102], state=0) # Greeting
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
        create_monster(spawnIds=[4116], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9140, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9141, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=4116, patrolName='MS2PatrolData_401')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9142, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=4116, patrolName='MS2PatrolData_402')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9143, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=4116, patrolName='MS2PatrolData_403')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9143, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9143, spawnIds=[4116]):
            return WaitGreeting()


class WaitGreeting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001102], state=1) # Greeting

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001102], arg2=0):
            return OrderRandomPick()

    def on_exit(self):
        set_interact_object(triggerIds=[10001102], state=2) # Greeting


#  고객 주문 랜덤
class OrderRandomPick(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return PickItem_30000639()
        if random_condition(rate=1):
            return PickItem_30000640()
        if random_condition(rate=1):
            return PickItem_30000703()
        if random_condition(rate=1):
            return PickItem_30000704()
        if random_condition(rate=1):
            return PickItem_30000705()
        if random_condition(rate=1):
            return PickItem_30000715()


#  	30000639 
class PickItem_30000639(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000639)
        add_effect_nif(spawnId=4116, nifPath='Map/Tria/Indoor/tr_in_prop_machine_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000639()


class DetectItem_30000639(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000639):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000639):
            return WrongItem()


#  	30000640 
class PickItem_30000640(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000640)
        add_effect_nif(spawnId=4116, nifPath='Map/Tria/Indoor/tr_in_prop_cutter_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000640()


class DetectItem_30000640(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000640):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000640):
            return WrongItem()


#  	30000703 
class PickItem_30000703(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000703)
        add_effect_nif(spawnId=4116, nifPath='Map/Steampunk/Field/sp_fi_prop_anvil_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000703()


class DetectItem_30000703(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000703):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000703):
            return WrongItem()


#  	30000704 
class PickItem_30000704(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000704)
        add_effect_nif(spawnId=4116, nifPath='Map/Steampunk/Field/sp_fi_prop_bellows_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000704()


class DetectItem_30000704(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000704):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000704):
            return WrongItem()


#  	30000705 
class PickItem_30000705(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000705)
        add_effect_nif(spawnId=4116, nifPath='Map/Steampunk/Field/sp_fi_prop_brazier_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000705()


class DetectItem_30000705(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000705):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000705):
            return WrongItem()


#  	30000715 
class PickItem_30000715(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000715)
        add_effect_nif(spawnId=4116, nifPath='Map/Steampunk/Field/sp_fi_prop_brazier_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000715()


class DetectItem_30000715(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000715):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000715):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=4116)
        set_conversation(type=1, spawnId=4116, script='$02000387_BF__4116_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=4116, patrolName='MS2PatrolData_444')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9304, spawnIds=[4116]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[4116])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=4116)
        set_conversation(type=1, spawnId=4116, script='$02000387_BF__4116_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000639):
            return PickItem_30000639()
        if user_value(key='ItemNumber', value=30000640):
            return PickItem_30000640()
        if user_value(key='ItemNumber', value=30000703):
            return PickItem_30000703()
        if user_value(key='ItemNumber', value=30000704):
            return PickItem_30000704()
        if user_value(key='ItemNumber', value=30000705):
            return PickItem_30000705()
        if user_value(key='ItemNumber', value=30000715):
            return PickItem_30000715()


