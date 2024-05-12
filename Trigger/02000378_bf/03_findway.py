""" trigger/02000378_bf/03_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=25, visible=False, enable=False, minimap_visible=False) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(trigger_ids=[4023], visible=True, start_delay=0, interval=0, fade=0) # RoundBarrier
        self.set_mesh(trigger_ids=[3003], visible=True, start_delay=0, interval=0, fade=0) # CrystalOff
        self.set_mesh(trigger_ids=[3103], visible=False, start_delay=0, interval=0, fade=0) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3003], visible=True, start_delay=0, interval=0) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3103], visible=False, start_delay=0, interval=0) # CrystalOn
        self.set_effect(trigger_ids=[5203], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn01(self.ctx)


class ReadyToWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4023], visible=False, start_delay=0, interval=0, fade=0) # RoundBarrier
        self.spawn_monster(spawn_ids=[904,905,906], auto_target=False)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_103')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_203')
        self.set_dialogue(type=1, spawn_id=201, script='$02000378_BF__03_FINDWAY__0$', time=2, arg5=0) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ReadyToWalkIn02(self.ctx)


class ReadyToWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1303, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2303, key='RouteSelected', value=1)
        self.set_dialogue(type=1, spawn_id=201, script='$02000378_BF__03_FINDWAY__1$', time=2, arg5=1) # 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ReadyToWalkIn03(self.ctx)


class ReadyToWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$02000378_BF__03_FINDWAY__2$', time=2, arg5=2) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Round03_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[101,201])


class Round03_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1003], auto_target=False) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[2003], auto_target=False) # 전투용 준타
        self.set_dialogue(type=1, spawn_id=1003, script='$02000378_BF__03_FINDWAY__3$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=903, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='03RoundSuccess', value=1):
            return Round03_Sucess02(self.ctx)


# 20170223 업데이트 던전 개편 단축 			
#     <state name="Round03_Sucess01" >	
#         <onEnter>				
# 				</onEnter>		
# 			<condition name="NPC를감지했으면" arg1="9003" arg2="2203">	
# 			<transition state="Round03_Sucess02"/>	
# 		</condition> 		
#     <onExit> 
#     </onExit>	
#     </state>
class Round03_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawn_id=2203, patrol_name='MS2PatrolData_2003')
        self.move_npc(spawn_id=2003, patrol_name='MS2PatrolData_2003')
        self.destroy_monster(spawn_ids=[1003])
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3003], visible=False, start_delay=100, interval=0, fade=0) # CrystalOff
        # <action name="메쉬를설정한다" arg1="3103" arg2="1" arg3="0" arg4="0" arg5="0" />  CrystalOn
        self.set_mesh_animation(trigger_ids=[3003], visible=False, start_delay=0, interval=0) # CrystalOff
        # <action name="메쉬애니를설정한다" arg1="3103" arg2="1" arg3="0" arg4="0" />  CrystalOn
        self.set_effect(trigger_ids=[5203], visible=True) # Sound_CrystalOn
        self.set_portal(portal_id=25, visible=True, enable=True, minimap_visible=False)
        self.set_dialogue(type=1, spawn_id=103, script='$02000378_BF__03_FINDWAY__4$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round03_RouteSelect(self.ctx)


class Round03_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawn_ids=[2203])
        self.destroy_monster(spawn_ids=[2003])
        self.spawn_monster(spawn_ids=[203], auto_target=False) # 연출용 준타
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_103New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(weight=50):
            return None # Missing State: Round03_PickRoute_Left
        """
        """
        if self.random_condition(weight=50):
            return None # Missing State: Round03_PickRoute_Right
        """
        if self.wait_tick(wait_tick=500):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_203New')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[203])
        self.destroy_monster(spawn_ids=[904,905,906])


initial_state = Wait
