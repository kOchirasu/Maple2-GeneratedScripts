""" trigger/02000378_bf/04_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=21, visible=False, enable=False, minimap_visible=False) # 20170223 업데이트 던전 개편 단축
        self.set_mesh(trigger_ids=[4024], visible=True, start_delay=0, interval=0, fade=0) # RoundBarrier
        self.set_mesh(trigger_ids=[3004], visible=True, start_delay=0, interval=0, fade=0) # CrystalOff
        self.set_mesh(trigger_ids=[3104], visible=False, start_delay=0, interval=0, fade=0) # CrystalOn
        self.set_mesh_animation(trigger_ids=[3004], visible=True, start_delay=0, interval=0) # CrystalOff
        self.set_mesh_animation(trigger_ids=[3104], visible=False, start_delay=0, interval=0) # CrystalOn
        self.set_effect(trigger_ids=[5204], visible=False) # Sound_CrystalOn
        # self.set_user_value(key='FindWayLeft', value=0)
        # self.set_user_value(key='FindWayRight', value=0)
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal(self.ctx)


# 20170223 업데이트 던전 개편 단축
# 왼쪽에서 진입 	
#     <state name="ReadyToWalkIn_FromLeft01" >	
#         <onEnter>		
# 			<action name="메쉬를설정한다" arg1="4024" arg2="0" arg3="0" arg4="0" arg5="0" /> 				
# 			<action name="NPC를이동시킨다" arg1="102" arg2="MS2PatrolData_104L" />			
# 			<action name="NPC를이동시킨다" arg1="202" arg2="MS2PatrolData_204L" />	
# 			<action name="대화를설정한다" arg1="1" arg2="202" arg3="$02000378_BF__04_FINDWAY__0$" arg4="2" arg5="0" />	    					
# 				</onEnter>	
# 				<condition name="WaitTick" waitTick="2000">  
# 					<transition state="ReadyToWalkIn_FromLeft02"/>  
# 				</condition>					
#     <onExit> 
#     </onExit>
#     </state>	
# 	
#     <state name="ReadyToWalkIn_FromLeft02" > 
#         <onEnter>			
# 			<action name="SetUserValue" triggerID="1304" key="RouteSelected" value="1" /> 		
# 			<action name="SetUserValue" triggerID="2304" key="RouteSelected" value="1" /> 						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="2000">  
# 					<transition state="ReadyToWalkIn_FromLeft03"/>
# 				</condition>		
#     <onExit> 
#     </onExit>
#     </state>		
# 
#     <state name="ReadyToWalkIn_FromLeft03" > 	
#         <onEnter>			
# 			<action name="대화를설정한다" arg1="1" arg2="102" arg3="$02000378_BF__04_FINDWAY__1$" arg4="2" arg5="2" />	    					
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="5000">  
# 					<transition state="Round04_Start"/>
# 				</condition>		
#     <onExit> 
# 			<action name="몬스터소멸시킨다" arg1="102,202" />		
#     </onExit>
#     </state>
# 오른쪽에서 진입 
#     <state name="ReadyToWalkIn_FromRight01" >	
#         <onEnter>		
# 			<action name="메쉬를설정한다" arg1="4024" arg2="0" arg3="0" arg4="0" arg5="0" /> 				
# 			<action name="NPC를이동시킨다" arg1="103" arg2="MS2PatrolData_104R" />			
# 			<action name="NPC를이동시킨다" arg1="203" arg2="MS2PatrolData_204R" />	
# 			<action name="대화를설정한다" arg1="1" arg2="203" arg3="$02000378_BF__04_FINDWAY__2$" arg4="2" arg5="0" />	    				
# 				</onEnter>	
# 				<condition name="WaitTick" waitTick="2000">  
# 					<transition state="ReadyToWalkIn_FromRight02"/>  
# 				</condition>					
#     <onExit> 
#     </onExit>
#     </state>	
# 	
#     <state name="ReadyToWalkIn_FromRight02" > 
#         <onEnter>			
# 			<action name="SetUserValue" triggerID="1304" key="RouteSelected" value="1" /> 		
# 			<action name="SetUserValue" triggerID="2304" key="RouteSelected" value="1" /> 						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="2000">  
# 					<transition state="ReadyToWalkIn_FromRight03"/>
# 				</condition>		
#     <onExit> 
#     </onExit>
#     </state>		
# 
#     <state name="ReadyToWalkIn_FromRight03" > 	
#         <onEnter>			
# 			<action name="대화를설정한다" arg1="1" arg2="103" arg3="$02000378_BF__04_FINDWAY__3$" arg4="2" arg5="2" />	   				
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="5000">  
# 					<transition state="Round04_Start"/>
# 				</condition>		
#     <onExit> 
# 			<action name="몬스터소멸시킨다" arg1="103,203" />		
#     </onExit>
#     </state>
# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4024], visible=False, start_delay=0, interval=0, fade=0) # RoundBarrier
        self.set_user_value(trigger_id=1304, key='RouteSelected', value=1)
        self.set_user_value(trigger_id=2304, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[2004], auto_target=False)
        # 전투용 준타
        self.spawn_monster(spawn_ids=[104], auto_target=False)


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=104, script='$02000378_BF__04_FINDWAY__1$', time=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round04_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[104])


class Round04_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1004], auto_target=False) # 수호대상 틴차이
        self.set_dialogue(type=1, spawn_id=1004, script='$02000378_BF__04_FINDWAY__4$', time=3, arg5=2) # 틴차이
        self.set_user_value(trigger_id=904, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='04RoundSuccess', value=1):
            return Round04_Sucess02(self.ctx)


"""
class Round04_Sucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9004, spawn_ids=[2204]):
            return Round04_Sucess02(self.ctx)

"""


# 20170223 업데이트 던전 개편 단축
class Round04_Sucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.move_npc(spawn_id=2204, patrol_name='MS2PatrolData_2004')
        self.move_npc(spawn_id=2004, patrol_name='MS2PatrolData_2004')
        self.destroy_monster(spawn_ids=[1004])
        self.spawn_monster(spawn_ids=[104], auto_target=False) # 연출용 틴차이
        self.set_mesh(trigger_ids=[3004], visible=False, start_delay=100, interval=0, fade=0) # CrystalOff
        # <action name="메쉬를설정한다" arg1="3104" arg2="1" arg3="0" arg4="0" arg5="0" /> CrystalOn
        self.set_mesh_animation(trigger_ids=[3004], visible=False, start_delay=0, interval=0) # CrystalOff
        # <action name="메쉬애니를설정한다" arg1="3104" arg2="1" arg3="0" arg4="0" />  CrystalOn
        self.set_effect(trigger_ids=[5204], visible=True) # Sound_CrystalOn
        self.set_portal(portal_id=21, visible=True, enable=True, minimap_visible=False)
        self.set_dialogue(type=1, spawn_id=104, script='$02000378_BF__04_FINDWAY__5$', time=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Round04_RouteSelect(self.ctx)


class Round04_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.destroy_monster(spawn_ids=[2204])
        self.destroy_monster(spawn_ids=[2004])
        self.spawn_monster(spawn_ids=[204], auto_target=False) # 연출용 준타
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_104New')

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.random_condition(weight=50):
            return None # Missing State: Round04_PickRoute_Left
        """
        """
        if self.random_condition(weight=50):
            return None # Missing State: Round04_PickRoute_Right
        """
        if self.wait_tick(wait_tick=500):
            return GoToRound12(self.ctx)


class GoToRound12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104])
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_204New')
        self.set_user_value(trigger_id=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[204])


initial_state = Wait
