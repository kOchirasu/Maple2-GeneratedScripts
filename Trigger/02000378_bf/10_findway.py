""" trigger/02000378_bf/10_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4030], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3010], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3110], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3010], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3110], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5210], visible=False) # Sound_CrystalOn
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
# 			<action name="메쉬를설정한다" arg1="4030" arg2="0" arg3="0" arg4="0" arg5="0" />		
# 			<action name="NPC를이동시킨다" arg1="107" arg2="MS2PatrolData_110L" />			
# 			<action name="NPC를이동시킨다" arg1="207" arg2="MS2PatrolData_210L" />	
# 			<action name="대화를설정한다" arg1="1" arg2="207" arg3="$02000378_BF__10_FINDWAY__0$" arg4="2" arg5="0" />	    			
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
# 			<action name="SetUserValue" triggerID="1310" key="RouteSelected" value="1" /> 		
# 			<action name="SetUserValue" triggerID="2310" key="RouteSelected" value="1" /> 						
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
# 			<action name="대화를설정한다" arg1="1" arg2="107" arg3="$02000378_BF__10_FINDWAY__1$" arg4="2" arg5="2" />	    						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="5000">  
# 					<transition state="Round10_Start"/>
# 				</condition>		
#     <onExit> 
# 			<action name="몬스터소멸시킨다" arg1="107,207" />		
#     </onExit>
#     </state>
# 오른쪽에서 진입 
#     <state name="ReadyToWalkIn_FromRight01" >	
#         <onEnter>		
# 			<action name="메쉬를설정한다" arg1="4030" arg2="0" arg3="0" arg4="0" arg5="0" /> 			
# 			<action name="NPC를이동시킨다" arg1="108" arg2="MS2PatrolData_110R" />			
# 			<action name="NPC를이동시킨다" arg1="208" arg2="MS2PatrolData_210R" />	
# 			<action name="대화를설정한다" arg1="1" arg2="208" arg3="$02000378_BF__10_FINDWAY__2$" arg4="2" arg5="0" />	    			
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
# 			<action name="SetUserValue" triggerID="1310" key="RouteSelected" value="1" /> 		
# 			<action name="SetUserValue" triggerID="2310" key="RouteSelected" value="1" /> 						
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
# 			<action name="대화를설정한다" arg1="1" arg2="108" arg3="$02000378_BF__10_FINDWAY__3$" arg4="2" arg5="2" />	    						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="5000">  
# 					<transition state="Round10_Start"/>
# 				</condition>		
#     <onExit> 
# 			<action name="몬스터소멸시킨다" arg1="108,208" />		
#     </onExit>
#     </state>
# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4030], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_user_value(triggerId=1310, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2310, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[2010], animationEffect=False)
        # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=110, script='$02000378_BF__10_FINDWAY__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round10_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[110])


class Round10_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1010], animationEffect=False) # 수호대상 틴차이
        self.set_conversation(type=1, spawnId=1010, script='$02000378_BF__10_FINDWAY__4$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=910, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='10RoundSuccess', value=1):
            return Round10_Sucess01(self.ctx)


class Round10_Sucess01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=2010, patrolName='MS2PatrolData_2010')
        self.destroy_monster(spawnIds=[1010])
        self.create_monster(spawnIds=[110], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3010], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3110], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3010], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3110], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5210], visible=True) # Sound_CrystalOn
        self.set_conversation(type=1, spawnId=110, script='$02000378_BF__10_FINDWAY__5$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round10_RouteSelect(self.ctx)


class Round10_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2010])
        self.create_monster(spawnIds=[210], animationEffect=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round10_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round10_PickRoute_Right(self.ctx)


class Round10_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1310, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2310, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal17(self.ctx)


class GoToPortal17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_17')
        self.move_npc(spawnId=210, patrolName='MS2PatrolData_27')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Round10_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1310, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2310, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal18(self.ctx)


class GoToPortal18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_18')
        self.move_npc(spawnId=210, patrolName='MS2PatrolData_28')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[110,210])


initial_state = Wait
