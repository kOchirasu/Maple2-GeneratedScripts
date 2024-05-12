""" trigger/02000378_bf/06_findway.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4026], visible=True, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_mesh(triggerIds=[3006], visible=True, arg3=0, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3106], visible=False, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3006], visible=True, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3106], visible=False, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5206], visible=False) # Sound_CrystalOn
        self.set_user_value(key='FindWay', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FindWay', value=1):
            return ReadyToWalkIn_FromPortal(self.ctx)


# 20170223 업데이트 던전 개편 단축
# 왼쪽에서 진입 	
#     <state name="ReadyToWalkIn01" >	
#         <onEnter>		
# 			<action name="메쉬를설정한다" arg1="4026" arg2="0" arg3="0" arg4="0" arg5="0" /> 		
# 			<action name="NPC를이동시킨다" arg1="104" arg2="MS2PatrolData_106" />			
# 			<action name="NPC를이동시킨다" arg1="204" arg2="MS2PatrolData_206" />	
# 			<action name="대화를설정한다" arg1="1" arg2="204" arg3="$02000378_BF__06_FINDWAY__0$" arg4="2" arg5="0" />	  				
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
# 			<action name="SetUserValue" triggerID="1306" key="RouteSelected" value="1" /> 		
# 			<action name="SetUserValue" triggerID="2306" key="RouteSelected" value="1" /> 						
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
# 			<action name="대화를설정한다" arg1="1" arg2="104" arg3="$02000378_BF__06_FINDWAY__1$" arg4="2" arg5="2" />	    						
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="5000">  
# 					<transition state="Round06_Start"/>
# 				</condition>		
#     <onExit> 
# 			<action name="몬스터소멸시킨다" arg1="104,204" />		
#     </onExit>
#     </state>
# 포탈로 진입
class ReadyToWalkIn_FromPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[4026], visible=False, arg3=0, delay=0, scale=0) # RoundBarrier
        self.set_user_value(triggerId=1306, key='RouteSelected', value=1)
        self.set_user_value(triggerId=2306, key='RouteSelected', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToWalkIn_FromPortal02(self.ctx)

    def on_exit(self) -> None:
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[2006], animationEffect=False)
        # 전투용 준타


class ReadyToWalkIn_FromPortal02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=106, script='$02000378_BF__06_FINDWAY__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Round06_Start(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[106])


class Round06_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1006], animationEffect=False) # 수호대상 틴차이
        self.set_conversation(type=1, spawnId=1006, script='$02000378_BF__06_FINDWAY__2$', arg4=3, arg5=2) # 틴차이
        self.set_user_value(triggerId=906, key='MobWaveStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='06RoundSuccess', value=1):
            return Round06_Sucess(self.ctx)


class Round06_Sucess(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=2006, patrolName='MS2PatrolData_2006')
        self.destroy_monster(spawnIds=[1006])
        self.create_monster(spawnIds=[106], animationEffect=False) # 연출용 틴차이
        self.set_mesh(triggerIds=[3006], visible=False, arg3=100, delay=0, scale=0) # CrystalOff
        self.set_mesh(triggerIds=[3106], visible=True, arg3=0, delay=0, scale=0) # CrystalOn
        self.set_mesh_animation(triggerIds=[3006], visible=False, arg3=0, arg4=0) # CrystalOff
        self.set_mesh_animation(triggerIds=[3106], visible=True, arg3=0, arg4=0) # CrystalOn
        self.set_effect(triggerIds=[5206], visible=True) # Sound_CrystalOn
        self.set_conversation(type=1, spawnId=106, script='$02000378_BF__06_FINDWAY__3$', arg4=2, arg5=1) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Round06_RouteSelect(self.ctx)


class Round06_RouteSelect(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[2006])
        self.create_monster(spawnIds=[206], animationEffect=False) # 연출용 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return Round06_PickRoute_Left(self.ctx)
        if self.random_condition(rate=50):
            return Round06_PickRoute_Right(self.ctx)


class Round06_PickRoute_Left(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1306, key='MakeTrue', value=1)
        self.set_user_value(triggerId=2306, key='MakeFalse', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal13(self.ctx)


class GoToPortal13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_13')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_23')
        self.set_user_value(triggerId=12, key='FindWay', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Round06_PickRoute_Right(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=1306, key='MakeFalse', value=1)
        self.set_user_value(triggerId=2306, key='MakeTrue', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return GoToPortal14(self.ctx)


class GoToPortal14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=12, key='FindWay', value=1)
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_14')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_24')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[106,206])


initial_state = Wait
