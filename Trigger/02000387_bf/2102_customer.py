""" trigger/02000387_bf/2102_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001100], state=0) # Greeting
        self.set_user_value(key='CustomerEnter', value=0)
        self.set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CustomerEnter', value=1):
            return CustomerEnterDelay(self.ctx)


class CustomerEnterDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CustomerEnter(self.ctx)


class CustomerEnter(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9120, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9121, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2102, patrolName='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9122, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2102, patrolName='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9123, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2102, patrolName='MS2PatrolData_203')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9123, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9123, spawnIds=[2102]):
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001100], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001100], stateValue=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001100], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return PickItem_30000623(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000624(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000625(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000626(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000627(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000629(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000631(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000632(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000633(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000634(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000635(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000636(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000637(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000638(self.ctx)


# 30000623
class PickItem_30000623(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000623)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_bath_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000623(self.ctx)


class DetectItem_30000623(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000623):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000623):
            return WrongItem(self.ctx)


# 30000624
class PickItem_30000624(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000624)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_bath_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000624(self.ctx)


class DetectItem_30000624(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000624):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000624):
            return WrongItem(self.ctx)


# 30000625
class PickItem_30000625(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000625)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_shower_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000625(self.ctx)


class DetectItem_30000625(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000625):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000625):
            return WrongItem(self.ctx)


# 30000626
class PickItem_30000626(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000626)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_C02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000626(self.ctx)


class DetectItem_30000626(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000626):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000626):
            return WrongItem(self.ctx)


# 30000627
class PickItem_30000627(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000627)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_D03.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000627(self.ctx)


class DetectItem_30000627(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000627):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000627):
            return WrongItem(self.ctx)


# 30000629
class PickItem_30000629(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000629)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000629(self.ctx)


class DetectItem_30000629(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000629):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000629):
            return WrongItem(self.ctx)


# 30000631
class PickItem_30000631(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000631)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_washstand_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000631(self.ctx)


class DetectItem_30000631(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000631):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000631):
            return WrongItem(self.ctx)


# 30000632
class PickItem_30000632(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000632)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_sink_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000632(self.ctx)


class DetectItem_30000632(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000632):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000632):
            return WrongItem(self.ctx)


# 30000633
class PickItem_30000633(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000633)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_sink_A03.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000633(self.ctx)


class DetectItem_30000633(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000633):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000633):
            return WrongItem(self.ctx)


# 30000634
class PickItem_30000634(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000634)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_tv_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000634(self.ctx)


class DetectItem_30000634(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000634):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000634):
            return WrongItem(self.ctx)


# 30000635
class PickItem_30000635(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000635)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_tv_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000635(self.ctx)


class DetectItem_30000635(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000635):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000635):
            return WrongItem(self.ctx)


# 30000636
class PickItem_30000636(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000636)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_toilet_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000636(self.ctx)


class DetectItem_30000636(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000636):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000636):
            return WrongItem(self.ctx)


# 30000637
class PickItem_30000637(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000637)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_washer_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000637(self.ctx)


class DetectItem_30000637(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000637):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000637):
            return WrongItem(self.ctx)


# 30000638
class PickItem_30000638(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000638)
        self.add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fan_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000638(self.ctx)


class DetectItem_30000638(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000638):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000638):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=2102)
        self.set_conversation(type=1, spawnId=2102, script='$02000387_BF__2102_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2102, patrolName='MS2PatrolData_222')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9302, spawnIds=[2102]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=2102)
        self.set_conversation(type=1, spawnId=2102, script='$02000387_BF__2102_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber', value=30000623):
            return PickItem_30000623(self.ctx)
        if self.user_value(key='ItemNumber', value=30000624):
            return PickItem_30000624(self.ctx)
        if self.user_value(key='ItemNumber', value=30000625):
            return PickItem_30000625(self.ctx)
        if self.user_value(key='ItemNumber', value=30000626):
            return PickItem_30000626(self.ctx)
        if self.user_value(key='ItemNumber', value=30000627):
            return PickItem_30000627(self.ctx)
        if self.user_value(key='ItemNumber', value=30000629):
            return PickItem_30000629(self.ctx)
        if self.user_value(key='ItemNumber', value=30000631):
            return PickItem_30000631(self.ctx)
        if self.user_value(key='ItemNumber', value=30000632):
            return PickItem_30000632(self.ctx)
        if self.user_value(key='ItemNumber', value=30000633):
            return PickItem_30000633(self.ctx)
        if self.user_value(key='ItemNumber', value=30000634):
            return PickItem_30000634(self.ctx)
        if self.user_value(key='ItemNumber', value=30000635):
            return PickItem_30000635(self.ctx)
        if self.user_value(key='ItemNumber', value=30000636):
            return PickItem_30000636(self.ctx)
        if self.user_value(key='ItemNumber', value=30000637):
            return PickItem_30000637(self.ctx)
        if self.user_value(key='ItemNumber', value=30000638):
            return PickItem_30000638(self.ctx)


initial_state = Wait
