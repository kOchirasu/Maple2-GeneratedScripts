""" trigger/02000387_bf/4112_customer.xml """
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
        create_monster(spawnIds=[4112], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9140, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9141, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=4112, patrolName='MS2PatrolData_401')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9142, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=4112, patrolName='MS2PatrolData_402')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9143, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=4112, patrolName='MS2PatrolData_403')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9143, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9143, spawnIds=[4112]):
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
            return PickItem_30000649()
        if random_condition(rate=1):
            return PickItem_30000657()
        if random_condition(rate=1):
            return PickItem_30000697()
        if random_condition(rate=1):
            return PickItem_30000698()
        if random_condition(rate=1):
            return PickItem_30000701()
        if random_condition(rate=1):
            return PickItem_30000716()


#  	30000649 
class PickItem_30000649(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000649)
        add_effect_nif(spawnId=4112, nifPath='Map/Tria/Indoor/tr_in_prop_mirror_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000649()


class DetectItem_30000649(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000649):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000649):
            return WrongItem()


#  	30000657 
class PickItem_30000657(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000657)
        add_effect_nif(spawnId=4112, nifPath='Map/Iceland/Indoor/ic_in_prop_bed_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000657()


class DetectItem_30000657(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000657):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000657):
            return WrongItem()


#  	30000697 
class PickItem_30000697(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000697)
        add_effect_nif(spawnId=4112, nifPath='Npc/Etc/UGC_Poclain/UGC_Poclain_01.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000697()


class DetectItem_30000697(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000697):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000697):
            return WrongItem()


#  	30000698 
class PickItem_30000698(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000698)
        add_effect_nif(spawnId=4112, nifPath='Npc/Etc/UGC_FlameBike_Npc/UGC_FlameBike_03.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000698()


class DetectItem_30000698(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000698):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000698):
            return WrongItem()


#  	30000701 
class PickItem_30000701(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000701)
        add_effect_nif(spawnId=4112, nifPath='Map/Common/Indoor/co_in_prop_security_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000701()


class DetectItem_30000701(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000701):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000701):
            return WrongItem()


#  	30000716 
class PickItem_30000716(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000716)
        add_effect_nif(spawnId=4112, nifPath='Map/Kerningcity/Field/ke_fi_prop_tire_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000716()


class DetectItem_30000716(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9204], itemId=30000716):
            return RightItem()
        if not detect_liftable_object(boxIds=[9204], itemId=30000716):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=4112)
        set_conversation(type=1, spawnId=4112, script='$02000387_BF__4112_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=4112, patrolName='MS2PatrolData_444')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9304, spawnIds=[4112]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[4112])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=4112)
        set_conversation(type=1, spawnId=4112, script='$02000387_BF__4112_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000649):
            return PickItem_30000649()
        if user_value(key='ItemNumber', value=30000657):
            return PickItem_30000657()
        if user_value(key='ItemNumber', value=30000697):
            return PickItem_30000697()
        if user_value(key='ItemNumber', value=30000698):
            return PickItem_30000698()
        if user_value(key='ItemNumber', value=30000701):
            return PickItem_30000701()
        if user_value(key='ItemNumber', value=30000716):
            return PickItem_30000716()


