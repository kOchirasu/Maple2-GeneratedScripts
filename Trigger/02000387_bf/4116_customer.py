""" trigger/02000387_bf/4116_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001102], state=0) # Greeting
        self.set_user_value(key='CustomerEnter', value=0)
        self.set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CustomerEnter') >= 1:
            return CustomerEnterDelay(self.ctx)


class CustomerEnterDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CustomerEnter(self.ctx)


class CustomerEnter(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[4116], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9140, spawn_ids=[0]):
            # 대기열에 아무도 없으면
            return Patrol03(self.ctx)
        if not self.npc_detected(box_id=9141, spawn_ids=[0]):
            # 세 번째 대기 손님이 없으면
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4116, patrol_name='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9142, spawn_ids=[0]):
            # 두 번째 대기 손님이 없으면
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4116, patrol_name='MS2PatrolData_402')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9143, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4116, patrol_name='MS2PatrolData_403')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=9143, spawn_ids=[0]):
            # 첫 번째 대기 손님이 없으면
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9143, spawn_ids=[4116]):
            # 카운터 앞에 도착했으면
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001102], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001102], state=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[10001102], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1):
            return PickItem_30000639(self.ctx)
        if self.random_condition(weight=1):
            return PickItem_30000640(self.ctx)
        if self.random_condition(weight=1):
            return PickItem_30000703(self.ctx)
        if self.random_condition(weight=1):
            return PickItem_30000704(self.ctx)
        if self.random_condition(weight=1):
            return PickItem_30000705(self.ctx)
        if self.random_condition(weight=1):
            return PickItem_30000715(self.ctx)


# 30000639
class PickItem_30000639(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000639)
        self.add_effect_nif(spawn_id=4116, nif_path='Map/Tria/Indoor/tr_in_prop_machine_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000639(self.ctx)


class DetectItem_30000639(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000639):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000639):
            # 오답
            return WrongItem(self.ctx)


# 30000640
class PickItem_30000640(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000640)
        self.add_effect_nif(spawn_id=4116, nif_path='Map/Tria/Indoor/tr_in_prop_cutter_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000640(self.ctx)


class DetectItem_30000640(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000640):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000640):
            # 오답
            return WrongItem(self.ctx)


# 30000703
class PickItem_30000703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000703)
        self.add_effect_nif(spawn_id=4116, nif_path='Map/Steampunk/Field/sp_fi_prop_anvil_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000703(self.ctx)


class DetectItem_30000703(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000703):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000703):
            # 오답
            return WrongItem(self.ctx)


# 30000704
class PickItem_30000704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000704)
        self.add_effect_nif(spawn_id=4116, nif_path='Map/Steampunk/Field/sp_fi_prop_bellows_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000704(self.ctx)


class DetectItem_30000704(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000704):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000704):
            # 오답
            return WrongItem(self.ctx)


# 30000705
class PickItem_30000705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000705)
        self.add_effect_nif(spawn_id=4116, nif_path='Map/Steampunk/Field/sp_fi_prop_brazier_C01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000705(self.ctx)


class DetectItem_30000705(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000705):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000705):
            # 오답
            return WrongItem(self.ctx)


# 30000715
class PickItem_30000715(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000715)
        self.add_effect_nif(spawn_id=4116, nif_path='Map/Steampunk/Field/sp_fi_prop_brazier_A01.nif', is_outline=True, scale=1.2, rotate_z=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=0):
            return DetectItem_30000715(self.ctx)


class DetectItem_30000715(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9204], item_id=30000715):
            # 정답
            return RightItem(self.ctx)
        if not self.detect_liftable_object(box_ids=[9204], item_id=30000715):
            # 오답
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=False) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawn_id=4116)
        self.set_dialogue(type=1, spawn_id=4116, script='$02000387_BF__4116_CUSTOMER__0$', time=3, arg5=0)
        self.add_buff(box_ids=[9900], skill_id=70000112, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=4116, patrol_name='MS2PatrolData_444')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9304, spawn_ids=[4116]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[4116])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=False) # DownArrow
        self.play_system_sound_in_box(box_ids=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawn_id=4116)
        self.set_dialogue(type=1, spawn_id=4116, script='$02000387_BF__4116_CUSTOMER__1$', time=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber') >= 30000639:
            return PickItem_30000639(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000640:
            return PickItem_30000640(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000703:
            return PickItem_30000703(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000704:
            return PickItem_30000704(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000705:
            return PickItem_30000705(self.ctx)
        if self.user_value(key='ItemNumber') >= 30000715:
            return PickItem_30000715(self.ctx)


initial_state = Wait
