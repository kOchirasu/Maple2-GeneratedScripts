""" trigger/02000378_bf/09_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4029], visible=True, start_delay=0, interval=0, fade=0) # RoundBarrier
        self.set_mesh(trigger_ids=[3009], visible=True, start_delay=0, interval=0, fade=0) # CrystalOff
        self.set_mesh(trigger_ids=[3109], visible=False, start_delay=0, interval=0, fade=0) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3009], visible=True, start_delay=0, interval=0) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3109], visible=False, start_delay=0, interval=0) # CrystalOn
        self.set_effect(trigger_ids=[5209], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal(self.ctx)


# 20170223 업데이트 던전 개편 단축
# 왼쪽에서 진입 	
#     <state name="ReadyToWalkIn01" >	
#         <onEnter>		
# 			<action name="메쉬를설정한다" arg1="4029" arg2="0" arg3="0" arg4="0" arg5="0" /> 				
# 			<action name="NPC를이동시킨다" arg1="107" arg2="MS2PatrolData_109" />			
# 			<action name="NPC를이동시킨다" arg1="207" arg2="MS2PatrolData_209" />	
# 			<action name="대화를설정한다" arg1="1" arg2="207" arg3="$02000378_BF__09_FINDWAY__0$" arg4="2" arg5="0" />	    			
# 				</onEnter>	
# 				<condition name="WaitTick" waitTick="2000">  
# 					<transition state="ReadyToWalkIn02"/>  
# 				</condition>					
#     <onExit> 
#     </onExit>
#     </state>	
# 	
#     <state name="ReadyToWalkIn02" > 
#         <onEnter>			
# 			<action name="SetUserValue" triggerID="1309" key="RouteSelected" value="1" /> 		
# 			<action name="SetUserValue" triggerID="2309" key="RouteSelected" value="1" /> 						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="2000">  
# 					<transition state="ReadyToWalkIn03"/>
# 				</condition>		
#     <onExit> 
#     </onExit>
#     </state>		
# 
#     <state name="ReadyToWalkIn03" > 	
#         <onEnter>			
# 			<action name="대화를설정한다" arg1="1" arg2="107" arg3="$02000378_BF__09_FINDWAY__1$" arg4="2" arg5="2" />	    						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="5000">  
# 					<transition state="Round09_Start"/>
# 				</condition>		
#     <onExit> 
# 			<action name="몬스터소멸시킨다" arg1="107,207" />		
#     </onExit>
#     </state>
# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4029], visible=False, start_delay=0, interval=0, fade=0) # RoundBarrier
        self.set_user_value(trigger_id=1309, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2309, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[109], auto_target=False)
        self.spawn_monster(spawn_ids=[2009], auto_target=False)
        # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=109, script='$02000378_BF__09_FINDWAY__1$', time=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round09_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[109])


class Round09_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1009], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1009, script='$02000378_BF__09_FINDWAY__2$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=909, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='09RoundSuccess', value=1):
            return Round09_Sucess(self.ctx)


class Round09_Sucess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=2009, patrol_name='MS2PatrolData_2009')
        self.destroy_monster(spawn_ids=[1009])
        self.spawn_monster(spawn_ids=[109], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3009], visible=False, start_delay=100, interval=0, fade=0) # CrystalOff
        self.set_mesh(trigger_ids=[3109], visible=True, start_delay=0, interval=0, fade=0) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3009], visible=False, start_delay=0, interval=0) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3109], visible=True, start_delay=0, interval=0) # CrystalOn
        self.set_effect(trigger_ids=[5209], visible=True) # Sound_CrystalOn
        self.set_dialogue(type=1, spawn_id=109, script='$02000378_BF__09_FINDWAY__3$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round09_RouteSelect(self.ctx)


class Round09_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2009])
        self.spawn_monster(spawn_ids=[209], auto_target=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50):
            return Round09_PickRoute_Left(self.ctx)
        if self.random_condition(weight=50):
            return Round09_PickRoute_Right(self.ctx)


class Round09_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1309, key='MakeTrue', value=1)
        self.set_user_value(trigger_id=2309, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal15(self.ctx)


class GoToPortal15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=109, patrol_name='MS2PatrolData_15')
        self.move_npc(spawn_id=209, patrol_name='MS2PatrolData_25')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Round09_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=1309, key='MakeFalse', value=1)
        self.set_user_value(trigger_id=2309, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return GoToPortal16(self.ctx)


class GoToPortal16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=12, key='FindWay', value=1)
        self.move_npc(spawn_id=109, patrol_name='MS2PatrolData_16')
        self.move_npc(spawn_id=209, patrol_name='MS2PatrolData_26')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[109,209])


initial_state = Wait
