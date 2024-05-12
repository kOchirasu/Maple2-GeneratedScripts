""" trigger/52000052_qd/904_mobwave_04round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(trigger_ids=[5104], visible=False) # 04Round_ShadowApp

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobWaveStart', value=1):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveStart(self.ctx)


class FirstWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__0$', arg3='6000', arg4='0')
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(trigger_ids=[5104], visible=True) # 04Round_ShadowApp

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDirectionRandom(self.ctx)


# 방향 랜덤
class FirstWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20):
            return FirstWaveDirection10(self.ctx)
        if self.random_condition(weight=20):
            return FirstWaveDirection20(self.ctx)
        if self.random_condition(weight=20):
            return FirstWaveDirection30(self.ctx)
        if self.random_condition(weight=20):
            return FirstWaveDirection40(self.ctx)
        if self.random_condition(weight=20):
            return FirstWaveDirection50(self.ctx)


class FirstWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90400,90402,90404,90406,90408], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90401,90403,90405,90407,90409], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90410,90412,90414,90416,90418], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90411,90413,90415,90417,90419], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90420,90422,90424,90426,90428], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90421,90423,90425,90427,90429], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90430,90432,90434,90436,90438], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90431,90433,90435,90437,90439], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90440,90442,90444,90446,90448], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90441,90443,90445,90447,90449], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class FirstWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30):
            return FirstWaveDelay5000(self.ctx)
        if self.random_condition(weight=30):
            return FirstWaveDelay6000(self.ctx)
        if self.random_condition(weight=30):
            return FirstWaveDelay7000(self.ctx)


class FirstWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay6000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay7000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 20170223 업데이트 던전 개편 단축
        # self.set_user_value(trigger_id=704, key='TotemApp', value=1)
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDirectionRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class SecondWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20):
            return SecondWaveDirection10(self.ctx)
        if self.random_condition(weight=20):
            return SecondWaveDirection20(self.ctx)
        if self.random_condition(weight=20):
            return SecondWaveDirection30(self.ctx)
        if self.random_condition(weight=20):
            return SecondWaveDirection40(self.ctx)
        if self.random_condition(weight=20):
            return SecondWaveDirection50(self.ctx)


class SecondWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90400,90402,90404,90406,90408], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90401,90403,90405,90407,90409], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90410,90412,90414,90416,90418], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90411,90413,90415,90417,90419], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90420,90422,90424,90426,90428], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90421,90423,90425,90427,90429], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90430,90432,90434,90436,90438], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90431,90433,90435,90437,90439], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90440,90442,90444,90446,90448], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90441,90443,90445,90447,90449], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class SecondWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30):
            return SecondWaveDelay4000(self.ctx)
        if self.random_condition(weight=30):
            return SecondWaveDelay5000(self.ctx)
        if self.random_condition(weight=30):
            return SecondWaveDelay6000(self.ctx)


class SecondWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay6000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class ThirdWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        return ThirdWaveDirectionRandom(self.ctx)


class ThirdWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20):
            return ThirdWaveDirection10(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection20(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection30(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection40(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection50(self.ctx)


class ThirdWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90400,90402,90404,90406,90408], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90401,90403,90405,90407,90409], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90410,90412,90414,90416,90418], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90411,90413,90415,90417,90419], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90420,90422,90424,90426,90428], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90421,90423,90425,90427,90429], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90430,90432,90434,90436,90438], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90431,90433,90435,90437,90439], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90440,90442,90444,90446,90448], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90441,90443,90445,90447,90449], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90447,90437,90427], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤 	
# 	<state name="3rdWaveDelayRandom">	
# 		<onEnter>						
# 		</onEnter>
# 				<condition name="랜덤조건" arg1="30">	
# 					<transition state="3rdWaveDelay3000"/>
# 				</condition> 
# 				<condition name="랜덤조건" arg1="30"> 
# 					<transition state="3rdWaveDelay4000" />	
# 				</condition>	
# 				<condition name="랜덤조건" arg1="30"> 
# 					<transition state="3rdWaveDelay5000" />
# 				</condition>				
# 		<onExit> 
# 		</onExit> 
# 	</state>	
#     <state name="3rdWaveDelay3000" >
#         <onEnter>					
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="3000">
# 					<transition state="4thWaveStart"/>
# 				</condition>				
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
#     <onExit> 
#     </onExit>	
#     </state>		
#     <state name="3rdWaveDelay4000" >
#         <onEnter>					
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="4000">
# 					<transition state="4thWaveStart"/>
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
#     <onExit> 
#     </onExit>	
#     </state>		
#     <state name="3rdWaveDelay5000" >
#         <onEnter>					
# 				</onEnter>		
# 				<condition name="WaitTick" waitTick="5000">
# 					<transition state="4thWaveStart"/>
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
#     <onExit> 
#     </onExit>	
#     </state>		
# 
# 	
#     <state name="4thWaveStart" >	
#         <onEnter>		
# 			<action name="SetUserValue" key="WaveTime" value="4" /> 					
# 				</onEnter>	
# 				<condition name="무조건" >
# 			<transition state="4thWaveDirectionRandom"/>	
# 		</condition> 				
#     <onExit> 
#     </onExit>	
#     </state>	
# 
#  방향 랜덤 	
#     <state name="4thWaveDirectionRandom" >	
#         <onEnter>			
# 				</onEnter>	
# 				<condition name="랜덤조건" arg1="20">	
# 					<transition state="4thWaveDirection10"/>
# 				</condition> 
# 				<condition name="랜덤조건" arg1="20"> 
# 					<transition state="4thWaveDirection20" />	
# 				</condition>	
# 				<condition name="랜덤조건" arg1="20"> 
# 					<transition state="4thWaveDirection30" />
# 				</condition>			
# 				<condition name="랜덤조건" arg1="20"> 
# 					<transition state="4thWaveDirection40" />
# 				</condition>		
# 				<condition name="랜덤조건" arg1="20"> 
# 					<transition state="4thWaveDirection50" />
# 				</condition>						
#     <onExit> 
#     </onExit>	
#     </state>	
# 
# 	<state name="4thWaveDirection10">
# 		<onEnter>
# 			<action name="몬스터를생성한다" arg1="90400,90402,90404,90406,90408" arg2="0" /> 							
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="4thWaveDirection11"/>	
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 
# 	</state>		
# 	<state name="4thWaveDirection11">
# 		<onEnter>		
# 			<action name="몬스터를생성한다" arg1="90401,90403,90405,90407,90409" arg2="0" /> 					
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="DefenceSucess01"/>	
# 				</condition>			
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 
# 	</state>		
# 
# 	<state name="4thWaveDirection20">
# 		<onEnter>
# 			<action name="몬스터를생성한다" arg1="90410,90412,90414,90416,90418" arg2="0" /> 							
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="4thWaveDirection21"/>	
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 
# 	</state>		
# 	<state name="4thWaveDirection21">
# 		<onEnter>		
# 			<action name="몬스터를생성한다" arg1="90411,90413,90415,90417,90419" arg2="0" /> 					
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="DefenceSucess01"/>	
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 	
# 	</state>	
# 
# 	<state name="4thWaveDirection30">
# 		<onEnter>
# 			<action name="몬스터를생성한다" arg1="90420,90422,90424,90426,90428" arg2="0" /> 							
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="4thWaveDirection31"/>	
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 
# 	</state>		
# 	<state name="4thWaveDirection31">
# 		<onEnter>		
# 			<action name="몬스터를생성한다" arg1="90421,90423,90425,90427,90429" arg2="0" /> 					
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="DefenceSucess01"/>	
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 	
# 	</state>	
# 
# 	<state name="4thWaveDirection40">
# 		<onEnter>
# 			<action name="몬스터를생성한다" arg1="90430,90432,90434,90436,90438" arg2="0" /> 							
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="4thWaveDirection41"/>	
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 
# 	</state>		
# 	<state name="4thWaveDirection41">
# 		<onEnter>		
# 			<action name="몬스터를생성한다" arg1="90431,90433,90435,90437,90439" arg2="0" /> 					
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="DefenceSucess01"/>	
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 	
# 	</state>	
# 	
# 	<state name="4thWaveDirection50">
# 		<onEnter>
# 			<action name="몬스터를생성한다" arg1="90440,90442,90444,90446,90448" arg2="0" /> 							
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="DefenceSucess01"/>	
# 				</condition>		
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 
# 	</state>		
# 	<state name="4thWaveDirection51">
# 		<onEnter>		
# 			<action name="몬스터를생성한다" arg1="90441,90443,90445,90447,90449" arg2="0" /> 					
# 		</onEnter>
# 				<condition name="WaitTick" waitTick="1000">		
# 					<transition state="DefenceSucess01"/>	
# 				</condition>			
# 				<condition name="몬스터가죽어있으면" arg1="1004" >		
# 					<transition state="NpcDownPenaltyStart"/>	
# 				</condition>						
# 		<onExit> 
# 		</onExit> 	
# 	</state>
# 추가 웨이브 경험치 없음
class FifthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.spawn_monster(spawn_ids=[90490,90492,90494,90496,90498], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90491,90493,90495,90497,90499], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 웨이브 종료
class DefenceSucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[90400,90401,90402,90403,90404,90405,90406,90407,90408,90410,90410,90411,90412,90413,90414,90415,90416,90417,90418,90419,90420,90421,90422,90423,90424,90425,90426,90427,90428,90429,90430,90431,90432,90433,90434,90435,90436,90437,90438,90439,90440,90441,90442,90443,90444,90445,90446,90447,90448,90449,90480,90481,90482,90483,90484,90485,90486,90487,90488,90489,90490,90491,90492,90493,90494,90495,90496,90497,90498,90499]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(spawn_ids=[1004]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5104], visible=False) # 04Round_ShadowApp
        self.set_user_value(trigger_id=4, key='04RoundSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=804, key='PenaltyMob', value=1)
        self.destroy_monster(spawn_ids=[1004]) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[1104], auto_target=False) # 쓰러진 틴차이
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        self.set_dialogue(type=1, spawn_id=1104, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', time=4, arg5=4) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return NpcDownPenaltyEnd(self.ctx)


class NpcDownPenaltyEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PenaltyFinish', value=1):
            return ReturnToWave(self.ctx)


class ReturnToWave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__3$', arg3='4000', arg4='0')
        self.destroy_monster(spawn_ids=[1104]) # 쓰러진 틴차이
        self.spawn_monster(spawn_ids=[1004], auto_target=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawn_id=1104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='WaveTime', value=1):
            return SecondWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=2):
            return ThirdWaveStart(self.ctx)
        """
        if self.user_value(key='WaveTime', value=4):
            return FifthWaveStart(self.ctx)
        """
        if self.user_value(key='WaveTime', value=3):
            return FifthWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=5):
            return FifthWaveStart(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
