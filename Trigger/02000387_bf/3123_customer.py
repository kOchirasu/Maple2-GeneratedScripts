""" trigger/02000387_bf/3123_customer.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001101], state=0) # Greeting
        self.set_user_value(key='CustomerEnter', value=0)
        self.set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CustomerEnter', value=1):
            return CustomerEnterDelay(self.ctx)


class CustomerEnterDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CustomerEnter(self.ctx)


class CustomerEnter(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[3123], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9130, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9131, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3123, patrolName='MS2PatrolData_301')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9132, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3123, patrolName='MS2PatrolData_302')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9133, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3123, patrolName='MS2PatrolData_303')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9133, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9133, spawnIds=[3123]):
            return WaitGreeting(self.ctx)


class WaitGreeting(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001101], state=1) # Greeting

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001101], stateValue=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001101], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return PickItem_30000623(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000625(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000692(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000696(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000698(self.ctx)


# 30000623
class PickItem_30000623(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000623)
        self.add_effect_nif(spawnId=3123, nifPath='Map/Kerningcity/Indoor/ke_in_prop_bath_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000623(self.ctx)


class DetectItem_30000623(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000623):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000623):
            return WrongItem(self.ctx)


# 30000625
class PickItem_30000625(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000625)
        self.add_effect_nif(spawnId=3123, nifPath='Map/Kerningcity/Indoor/ke_in_prop_shower_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000625(self.ctx)


class DetectItem_30000625(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000625):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000625):
            return WrongItem(self.ctx)


# 30000692
class PickItem_30000692(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000692)
        self.add_effect_nif(spawnId=3123, nifPath='Map/Kerningcity/Indoor/ke_in_prop_dresser_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000692(self.ctx)


class DetectItem_30000692(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000692):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000692):
            return WrongItem(self.ctx)


# 30000696
class PickItem_30000696(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000696)
        self.add_effect_nif(spawnId=3123, nifPath='Npc/Etc/UGC_F1RacingCar/UGC_F1RacingCar_01.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000696(self.ctx)


class DetectItem_30000696(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000696):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000696):
            return WrongItem(self.ctx)


# 30000698
class PickItem_30000698(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000698)
        self.add_effect_nif(spawnId=3123, nifPath='Npc/Etc/UGC_FlameBike_Npc/UGC_FlameBike_03.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=0):
            return DetectItem_30000698(self.ctx)


class DetectItem_30000698(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9203], itemId=30000698):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9203], itemId=30000698):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=3123)
        self.set_conversation(type=1, spawnId=3123, script='$02000387_BF__3123_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3123, patrolName='MS2PatrolData_333')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9303, spawnIds=[3123]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[3123])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5103], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=3123)
        self.set_conversation(type=1, spawnId=3123, script='$02000387_BF__3123_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ItemNumber', value=30000623):
            return PickItem_30000623(self.ctx)
        if self.user_value(key='ItemNumber', value=30000625):
            return PickItem_30000625(self.ctx)
        if self.user_value(key='ItemNumber', value=30000692):
            return PickItem_30000692(self.ctx)
        if self.user_value(key='ItemNumber', value=30000696):
            return PickItem_30000696(self.ctx)
        if self.user_value(key='ItemNumber', value=30000698):
            return PickItem_30000698(self.ctx)


initial_state = Wait
