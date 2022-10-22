""" trigger/02000387_bf/1117_customer.xml """
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
        create_monster(spawnIds=[1117], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9110, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9111, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=1117, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9112, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=1117, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9113, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=1117, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9113, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9113, spawnIds=[1117]):
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
            return PickItem_30000639()
        if random_condition(rate=1):
            return PickItem_30000640()
        if random_condition(rate=1):
            return PickItem_30000702()
        if random_condition(rate=1):
            return PickItem_30000713()


#  	30000639 
class PickItem_30000639(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000639)
        add_effect_nif(spawnId=1117, nifPath='Map/Tria/Indoor/tr_in_prop_machine_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000639()


class DetectItem_30000639(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000639):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000639):
            return WrongItem()


#  	30000640 
class PickItem_30000640(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000640)
        add_effect_nif(spawnId=1117, nifPath='Map/Tria/Indoor/tr_in_prop_cutter_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000640()


class DetectItem_30000640(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000640):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000640):
            return WrongItem()


#  	30000702 
class PickItem_30000702(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000702)
        add_effect_nif(spawnId=1117, nifPath='Map/Tria/Indoor/tr_in_prop_workit_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000702()


class DetectItem_30000702(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000702):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000702):
            return WrongItem()


#  	30000713 
class PickItem_30000713(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000713)
        add_effect_nif(spawnId=1117, nifPath='Map/Steampunk/Indoor/sp_in_prop_desk_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000713()


class DetectItem_30000713(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9201], itemId=30000713):
            return RightItem()
        if not detect_liftable_object(boxIds=[9201], itemId=30000713):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=1117)
        set_conversation(type=1, spawnId=1117, script='$02000387_BF__1117_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=1117, patrolName='MS2PatrolData_111')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9301, spawnIds=[1117]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1117])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=1117)
        set_conversation(type=1, spawnId=1117, script='$02000387_BF__1117_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000617):
            return None # Missing State: PickItem_30000617
        if user_value(key='ItemNumber', value=30000618):
            return None # Missing State: PickItem_30000618
        if user_value(key='ItemNumber', value=30000619):
            return None # Missing State: PickItem_30000619
        if user_value(key='ItemNumber', value=30000620):
            return None # Missing State: PickItem_30000620
        if user_value(key='ItemNumber', value=30000621):
            return None # Missing State: PickItem_30000621
        if user_value(key='ItemNumber', value=30000622):
            return None # Missing State: PickItem_30000622
        if user_value(key='ItemNumber', value=30000623):
            return None # Missing State: PickItem_30000623
        if user_value(key='ItemNumber', value=30000624):
            return None # Missing State: PickItem_30000624
        if user_value(key='ItemNumber', value=30000625):
            return None # Missing State: PickItem_30000625
        if user_value(key='ItemNumber', value=30000626):
            return None # Missing State: PickItem_30000626
        if user_value(key='ItemNumber', value=30000627):
            return None # Missing State: PickItem_30000627
        if user_value(key='ItemNumber', value=30000628):
            return None # Missing State: PickItem_30000628
        if user_value(key='ItemNumber', value=30000629):
            return None # Missing State: PickItem_30000629
        if user_value(key='ItemNumber', value=30000630):
            return None # Missing State: PickItem_30000630
        if user_value(key='ItemNumber', value=30000631):
            return None # Missing State: PickItem_30000631
        if user_value(key='ItemNumber', value=30000632):
            return None # Missing State: PickItem_30000632
        if user_value(key='ItemNumber', value=30000633):
            return None # Missing State: PickItem_30000633
        if user_value(key='ItemNumber', value=30000634):
            return None # Missing State: PickItem_30000634
        if user_value(key='ItemNumber', value=30000635):
            return None # Missing State: PickItem_30000635
        if user_value(key='ItemNumber', value=30000636):
            return None # Missing State: PickItem_30000636
        if user_value(key='ItemNumber', value=30000637):
            return None # Missing State: PickItem_30000637
        if user_value(key='ItemNumber', value=30000638):
            return None # Missing State: PickItem_30000638
        if user_value(key='ItemNumber', value=30000639):
            return PickItem_30000639()
        if user_value(key='ItemNumber', value=30000640):
            return PickItem_30000640()
        if user_value(key='ItemNumber', value=30000641):
            return None # Missing State: PickItem_30000641
        if user_value(key='ItemNumber', value=30000642):
            return None # Missing State: PickItem_30000642
        if user_value(key='ItemNumber', value=30000643):
            return None # Missing State: PickItem_30000643
        if user_value(key='ItemNumber', value=30000644):
            return None # Missing State: PickItem_30000644
        if user_value(key='ItemNumber', value=30000645):
            return None # Missing State: PickItem_30000645
        if user_value(key='ItemNumber', value=30000646):
            return None # Missing State: PickItem_30000646
        if user_value(key='ItemNumber', value=30000647):
            return None # Missing State: PickItem_30000647
        if user_value(key='ItemNumber', value=30000648):
            return None # Missing State: PickItem_30000648
        if user_value(key='ItemNumber', value=30000649):
            return None # Missing State: PickItem_30000649
        if user_value(key='ItemNumber', value=30000650):
            return None # Missing State: PickItem_30000650
        if user_value(key='ItemNumber', value=30000651):
            return None # Missing State: PickItem_30000651
        if user_value(key='ItemNumber', value=30000652):
            return None # Missing State: PickItem_30000652
        if user_value(key='ItemNumber', value=30000653):
            return None # Missing State: PickItem_30000653
        if user_value(key='ItemNumber', value=30000654):
            return None # Missing State: PickItem_30000654
        if user_value(key='ItemNumber', value=30000655):
            return None # Missing State: PickItem_30000655
        if user_value(key='ItemNumber', value=30000656):
            return None # Missing State: PickItem_30000656
        if user_value(key='ItemNumber', value=30000657):
            return None # Missing State: PickItem_30000657
        if user_value(key='ItemNumber', value=30000658):
            return None # Missing State: PickItem_30000658
        if user_value(key='ItemNumber', value=30000659):
            return None # Missing State: PickItem_30000659
        if user_value(key='ItemNumber', value=30000660):
            return None # Missing State: PickItem_30000660
        if user_value(key='ItemNumber', value=30000661):
            return None # Missing State: PickItem_30000661
        if user_value(key='ItemNumber', value=30000662):
            return None # Missing State: PickItem_30000662
        if user_value(key='ItemNumber', value=30000663):
            return None # Missing State: PickItem_30000663
        if user_value(key='ItemNumber', value=30000664):
            return None # Missing State: PickItem_30000664
        if user_value(key='ItemNumber', value=30000665):
            return None # Missing State: PickItem_30000665
        if user_value(key='ItemNumber', value=30000666):
            return None # Missing State: PickItem_30000666
        if user_value(key='ItemNumber', value=30000667):
            return None # Missing State: PickItem_30000667
        if user_value(key='ItemNumber', value=30000668):
            return None # Missing State: PickItem_30000668
        if user_value(key='ItemNumber', value=30000669):
            return None # Missing State: PickItem_30000669
        if user_value(key='ItemNumber', value=30000670):
            return None # Missing State: PickItem_30000670
        if user_value(key='ItemNumber', value=30000671):
            return None # Missing State: PickItem_30000671
        if user_value(key='ItemNumber', value=30000672):
            return None # Missing State: PickItem_30000672
        if user_value(key='ItemNumber', value=30000673):
            return None # Missing State: PickItem_30000673
        if user_value(key='ItemNumber', value=30000674):
            return None # Missing State: PickItem_30000674
        if user_value(key='ItemNumber', value=30000675):
            return None # Missing State: PickItem_30000675
        if user_value(key='ItemNumber', value=30000676):
            return None # Missing State: PickItem_30000676
        if user_value(key='ItemNumber', value=30000677):
            return None # Missing State: PickItem_30000677
        if user_value(key='ItemNumber', value=30000678):
            return None # Missing State: PickItem_30000678
        if user_value(key='ItemNumber', value=30000679):
            return None # Missing State: PickItem_30000679
        if user_value(key='ItemNumber', value=30000680):
            return None # Missing State: PickItem_30000680
        if user_value(key='ItemNumber', value=30000681):
            return None # Missing State: PickItem_30000681
        if user_value(key='ItemNumber', value=30000682):
            return None # Missing State: PickItem_30000682
        if user_value(key='ItemNumber', value=30000683):
            return None # Missing State: PickItem_30000683
        if user_value(key='ItemNumber', value=30000684):
            return None # Missing State: PickItem_30000684
        if user_value(key='ItemNumber', value=30000685):
            return None # Missing State: PickItem_30000685
        if user_value(key='ItemNumber', value=30000686):
            return None # Missing State: PickItem_30000686
        if user_value(key='ItemNumber', value=30000687):
            return None # Missing State: PickItem_30000687
        if user_value(key='ItemNumber', value=30000688):
            return None # Missing State: PickItem_30000688
        if user_value(key='ItemNumber', value=30000689):
            return None # Missing State: PickItem_30000689
        if user_value(key='ItemNumber', value=30000690):
            return None # Missing State: PickItem_30000690
        if user_value(key='ItemNumber', value=30000691):
            return None # Missing State: PickItem_30000691
        if user_value(key='ItemNumber', value=30000692):
            return None # Missing State: PickItem_30000692
        if user_value(key='ItemNumber', value=30000693):
            return None # Missing State: PickItem_30000693
        if user_value(key='ItemNumber', value=30000694):
            return None # Missing State: PickItem_30000694
        if user_value(key='ItemNumber', value=30000695):
            return None # Missing State: PickItem_30000695
        if user_value(key='ItemNumber', value=30000696):
            return None # Missing State: PickItem_30000696
        if user_value(key='ItemNumber', value=30000697):
            return None # Missing State: PickItem_30000697
        if user_value(key='ItemNumber', value=30000698):
            return None # Missing State: PickItem_30000698
        if user_value(key='ItemNumber', value=30000699):
            return None # Missing State: PickItem_30000699
        if user_value(key='ItemNumber', value=30000700):
            return None # Missing State: PickItem_30000700
        if user_value(key='ItemNumber', value=30000701):
            return None # Missing State: PickItem_30000701
        if user_value(key='ItemNumber', value=30000702):
            return PickItem_30000702()
        if user_value(key='ItemNumber', value=30000703):
            return None # Missing State: PickItem_30000703
        if user_value(key='ItemNumber', value=30000704):
            return None # Missing State: PickItem_30000704
        if user_value(key='ItemNumber', value=30000705):
            return None # Missing State: PickItem_30000705
        if user_value(key='ItemNumber', value=30000706):
            return None # Missing State: PickItem_30000706
        if user_value(key='ItemNumber', value=30000707):
            return None # Missing State: PickItem_30000707
        if user_value(key='ItemNumber', value=30000708):
            return None # Missing State: PickItem_30000708
        if user_value(key='ItemNumber', value=30000709):
            return None # Missing State: PickItem_30000709
        if user_value(key='ItemNumber', value=30000710):
            return None # Missing State: PickItem_30000710
        if user_value(key='ItemNumber', value=30000711):
            return None # Missing State: PickItem_30000711
        if user_value(key='ItemNumber', value=30000712):
            return None # Missing State: PickItem_30000712
        if user_value(key='ItemNumber', value=30000713):
            return PickItem_30000713()
        if user_value(key='ItemNumber', value=30000714):
            return None # Missing State: PickItem_30000714
        if user_value(key='ItemNumber', value=30000715):
            return None # Missing State: PickItem_30000715
        if user_value(key='ItemNumber', value=30000716):
            return None # Missing State: PickItem_30000716


