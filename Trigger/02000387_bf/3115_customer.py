""" trigger/02000387_bf/3115_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001101], state=0) # Greeting
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
        self.create_monster(spawnIds=[3115], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9130, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9131, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3115, patrolName='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9132, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3115, patrolName='MS2PatrolData_302')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9133, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3115, patrolName='MS2PatrolData_303')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9133, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9133, spawnIds=[3115]):
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001101], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001101], stateValue=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001101], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return PickItem_30000617(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000618(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000668(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000671(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000672(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000673(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000674(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000676(self.ctx)


# 30000617
class PickItem_30000617(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000617)
        self.add_effect_nif(spawnId=3115, nifPath='Map/Common/Field/co_fi_prop_game_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000617(self.ctx)


class DetectItem_30000617(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000617):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000617):
            return WrongItem(self.ctx)


# 30000618
class PickItem_30000618(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000618)
        self.add_effect_nif(spawnId=3115, nifPath='Map/Common/Field/co_fi_prop_game_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000618(self.ctx)


class DetectItem_30000618(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000618):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000618):
            return WrongItem(self.ctx)


# 30000668
class PickItem_30000668(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000668)
        self.add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_cranegame_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000668(self.ctx)


class DetectItem_30000668(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000668):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000668):
            return WrongItem(self.ctx)


# 30000671
class PickItem_30000671(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000671)
        self.add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_photosticker_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000671(self.ctx)


class DetectItem_30000671(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000671):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000671):
            return WrongItem(self.ctx)


# 30000672
class PickItem_30000672(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000672)
        self.add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_pingpong_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000672(self.ctx)


class DetectItem_30000672(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000672):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000672):
            return WrongItem(self.ctx)


# 30000673
class PickItem_30000673(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000673)
        self.add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_pooltable_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000673(self.ctx)


class DetectItem_30000673(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000673):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000673):
            return WrongItem(self.ctx)


# 30000674
class PickItem_30000674(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000674)
        self.add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_pump_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000674(self.ctx)


class DetectItem_30000674(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000674):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000674):
            return WrongItem(self.ctx)


# 30000676
class PickItem_30000676(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000676)
        self.add_effect_nif(spawnId=3115, nifPath='Map/Royalcity/Indoor/ry_in_prop_soccertable_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000676(self.ctx)


class DetectItem_30000676(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000676):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000676):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=3115)
        self.set_conversation(type=1, spawnId=3115, script='$02000387_BF__3115_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3115, patrolName='MS2PatrolData_333')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9303, spawnIds=[3115]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[3115])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=3115)
        self.set_conversation(type=1, spawnId=3115, script='$02000387_BF__3115_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber', value=30000617):
            return PickItem_30000617(self.ctx)
        if self.user_value(key='ItemNumber', value=30000618):
            return PickItem_30000618(self.ctx)
        if self.user_value(key='ItemNumber', value=30000668):
            return PickItem_30000668(self.ctx)
        if self.user_value(key='ItemNumber', value=30000671):
            return PickItem_30000671(self.ctx)
        if self.user_value(key='ItemNumber', value=30000672):
            return PickItem_30000672(self.ctx)
        if self.user_value(key='ItemNumber', value=30000673):
            return PickItem_30000673(self.ctx)
        if self.user_value(key='ItemNumber', value=30000674):
            return PickItem_30000674(self.ctx)
        if self.user_value(key='ItemNumber', value=30000676):
            return PickItem_30000676(self.ctx)


initial_state = Wait
