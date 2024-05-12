""" trigger/02000378_bf/07_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=22, visible=False, enable=False, minimap_visible=False) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(trigger_ids=[4027], visible=True, start_delay=0, interval=0, fade=0) # RoundBarrier
        self.set_mesh(trigger_ids=[3007], visible=True, start_delay=0, interval=0, fade=0) # CrystalOff
        self.set_mesh(trigger_ids=[3107], visible=False, start_delay=0, interval=0, fade=0) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3007], visible=True, start_delay=0, interval=0) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3107], visible=False, start_delay=0, interval=0) # CrystalOn
        self.set_effect(trigger_ids=[5207], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal(self.ctx)


"""
class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4027], visible=False, start_delay=0, interval=0, fade=0)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_107')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_207')
        self.set_dialogue(type=1, spawn_id=202, script='$02000378_BF__07_FINDWAY__0$', time=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return None # Missing State: ReadyToWalkIn02

"""


"""
class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1307, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2307, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return None # Missing State: ReadyToWalkIn03

"""


"""
class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000378_BF__07_FINDWAY__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Round07_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[102,202])

"""


# 20170223 업데이트 던전 개편 단축
# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4027], visible=False, start_delay=0, interval=0, fade=0) # RoundBarrier
        self.set_user_value(trigger_id=1307, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2307, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.spawn_monster(spawn_ids=[2007], auto_target=False)
        # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=107, script='$02000378_BF__07_FINDWAY__1$', time=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round07_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[107])


class Round07_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1007], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1007, script='$02000378_BF__07_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=907, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='07RoundSuccess', value=1):
            return Round07_Sucess02(self.ctx)


"""
class Round07_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9007, spawn_ids=[2207]):
            return Round07_Sucess02(self.ctx)

"""


# 20170223 업데이트 던전 개편 단축
class Round07_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2007, patrol_name='MS2PatrolData_2007')
        # self.move_npc(spawn_id=2207, patrol_name='MS2PatrolData_2007')
        self.destroy_monster(spawn_ids=[1007])
        self.spawn_monster(spawn_ids=[107], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3007], visible=False, start_delay=100, interval=0, fade=0) # CrystalOff
        # <action name="메쉬를설정한다" arg1="3107" arg2="1" arg3="0" arg4="0" arg5="0" />  CrystalOn
        self.set_mesh_animation(trigger_ids=[3007], visible=False, start_delay=0, interval=0) # CrystalOff
        # <action name="메쉬애니를설정한다" arg1="3107" arg2="1" arg3="0" arg4="0" />  CrystalOn
        self.set_effect(trigger_ids=[5207], visible=True) # Sound_CrystalOn
        self.set_portal(portal_id=22, visible=True, enable=True, minimap_visible=False)
        self.set_dialogue(type=1, spawn_id=107, script='$02000378_BF__07_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round07_RouteSelect(self.ctx)


class Round07_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawn_ids=[2207])
        self.destroy_monster(spawn_ids=[2007])
        self.spawn_monster(spawn_ids=[207], auto_target=False) # 연출용 준타
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_107New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(weight=50):
            return None # Missing State: Round07_PickRoute_Left
        """
        """
        if self.random_condition(weight=50):
            return None # Missing State: Round07_PickRoute_Right
        """
        if self.wait_tick(wait_tick=500):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[107])
        self.move_npc(spawn_id=207, patrol_name='MS2PatrolData_207New')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[207])


initial_state = Wait
