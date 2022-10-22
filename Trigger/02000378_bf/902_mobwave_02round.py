""" trigger/02000378_bf/902_mobwave_02round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5102], visible=False) # 02Round_ShadowApp

    def on_tick(self) -> state.State:
        if user_value(key='MobWaveStart', value=1):
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveStart()


class FirstWaveStart(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__902_MOBWAVE_02ROUND__0$', arg3='6000', arg4='0')
        set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5102], visible=True) # 02Round_ShadowApp
        create_monster(spawnIds=[90200,90202,90204], arg2=False) # ,90206,90208

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FirstWaveDelayRandom(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90201,90203,90205], arg2=False) # ,90207,90209

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return FirstWaveDelay3000()
        if random_condition(rate=30):
            return FirstWaveDelay4000()
        if random_condition(rate=30):
            return FirstWaveDelay5000()


class FirstWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FirstWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FirstWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class SecondWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90210,90212,90214], arg2=False) # ,90216,90218

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class SecondWaveDelayRandom(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90211,90213,90215], arg2=False) # ,90217,90219

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return SecondWaveDelay3000()
        if random_condition(rate=30):
            return SecondWaveDelay4000()
        if random_condition(rate=30):
            return SecondWaveDelay2000()


class SecondWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class SecondWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class SecondWaveDelay2000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  방향 랜덤 
class ThirdWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if true():
            return ThirdWaveDirectionRandom()


class ThirdWaveDirectionRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return ThirdWaveDirection10()
        if random_condition(rate=20):
            return ThirdWaveDirection20()
        if random_condition(rate=20):
            return ThirdWaveDirection30()
        if random_condition(rate=20):
            return ThirdWaveDirection40()
        if random_condition(rate=20):
            return ThirdWaveDirection50()
        if random_condition(rate=20):
            return ThirdWaveDirection60()


#  왼쪽 위 
class ThirdWaveDirection10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90220,90222,90224], arg2=False) # ,90226,90228

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection11()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90221,90223,90225], arg2=False) # ,90227,90229

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  오른쪽 위 
class ThirdWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90230,90232,90234], arg2=False) # ,90236,90238

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection21()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90231,90233,90235], arg2=False) # ,90237,90239

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  왼쪽 중앙 
class ThirdWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90240,90242,90244], arg2=False) # ,90246,90248

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection31()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90241,90243,90245], arg2=False) # ,90247,90249

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  오른쪽 중앙 
class ThirdWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90250,90252,90254], arg2=False) # ,90256,90258

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection41()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90251,90253,90255], arg2=False) # ,90257,90259

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  왼쪽 아래 
class ThirdWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90260,90262,90264], arg2=False) # ,90266,90268

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection51()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90261,90263,90265], arg2=False) # ,90267,90269

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  오른쪽 아래 
class ThirdWaveDirection60(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90270,90272,90274], arg2=False) # ,90276,90278

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection61()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection61(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90271,90273,90275], arg2=False) # ,90277,90279

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return ThirdWaveDelay3000()
        if random_condition(rate=30):
            return ThirdWaveDelay4000()
        if random_condition(rate=30):
            return ThirdWaveDelay2000()


class ThirdWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay2000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FourthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=4) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if true():
            return FourthWaveDirectionRandom()


class FourthWaveDirectionRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return FourthWaveDirection10()
        if random_condition(rate=20):
            return FourthWaveDirection20()
        if random_condition(rate=20):
            return FourthWaveDirection30()
        if random_condition(rate=20):
            return FourthWaveDirection40()
        if random_condition(rate=20):
            return FourthWaveDirection50()
        if random_condition(rate=20):
            return FourthWaveDirection60()


#  왼쪽 위 
class FourthWaveDirection10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90220,90222,90224], arg2=False) # ,90226,90228

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection11()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FourthWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90221,90223,90225], arg2=False) # ,90227,90229

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  오른쪽 위 
class FourthWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90230,90232,90234], arg2=False) # ,90236,90238

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection21()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FourthWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90231,90233,90235], arg2=False) # ,90237,90239

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  왼쪽 중앙 
class FourthWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90240,90242,90244], arg2=False) # ,90246,90248

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection31()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FourthWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90241,90243,90245], arg2=False) # ,90247,90249

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  오른쪽 중앙 
class FourthWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90250,90252,90254], arg2=False) # ,90256,90258

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection41()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FourthWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90251,90253,90255], arg2=False) # ,90257,90259

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  왼쪽 아래 
class FourthWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90260,90262,90264], arg2=False) # ,90266,90268

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection51()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FourthWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90261,90263,90265], arg2=False) # ,90267,90269

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


#  오른쪽 아래 
class FourthWaveDirection60(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90270,90272,90274], arg2=False) # ,90276,90278

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection61()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FourthWaveDirection61(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90271,90273,90275], arg2=False) # ,90277,90279

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class FourthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90220,90222,90224], arg2=False) # ,90226,90228

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class SixthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=6) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90290,90292,90294], arg2=False) # ,90296,90298

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SixthWaveDelay()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class SixthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90291,90293,90295], arg2=False) # ,90297,90299

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class DefenceSucess01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90200,90201,90202,90203,90204,90205,90206,90207,90208,90209,90210,90211,90212,90213,90214,90215,90216,90217,90218,90219,90220,90221,90222,90223,90224,90225,90226,90227,90228,90229,90230,90231,90232,90233,90234,90235,90236,90237,90238,90239,90240,90241,90242,90243,90244,90245,90246,90247,90248,90249,90250,90251,90252,90253,90254,90255,90256,90257,90258,90259,90260,90261,90262,90263,90264,90265,90266,90267,90268,90269,90270,90271,90272,90273,90274,90275,90276,90277,90278,90279,90280,90281,90282,90283,90284,90285,90286,90287,90288,90289,90290,90291,90292,90293,90294,90295,90296,90297,90298,90299]):
            return DefenceSucess02()
        if monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart()


class DefenceSucess02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # 02Round_ShadowApp
        set_user_value(triggerId=2, key='02RoundSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  패널티 10초 
class NpcDownPenaltyStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=802, key='PenaltyMob', value=1)
        destroy_monster(spawnIds=[1002]) # 수호대상 틴차이
        create_monster(spawnIds=[1102], arg2=False) # 쓰러진 틴차이
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__902_MOBWAVE_02ROUND__1$', arg3='4000', arg4='0')
        set_conversation(type=1, spawnId=1102, script='$02000378_BF__902_MOBWAVE_02ROUND__2$', arg4=4, arg5=4) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return NpcDownPenaltyEnd()


class NpcDownPenaltyEnd(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='PenaltyFinish', value=1):
            return ReturnToWave()


class ReturnToWave(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__902_MOBWAVE_02ROUND__3$', arg3='4000', arg4='0')
        destroy_monster(spawnIds=[1102]) # 쓰러진 틴차이
        create_monster(spawnIds=[1002], arg2=False) # 수호대상 틴차이
        remove_balloon_talk(spawnId=1102)

    def on_tick(self) -> state.State:
        if user_value(key='WaveTime', value=1):
            return SecondWaveStart()
        if user_value(key='WaveTime', value=2):
            return ThirdWaveStart()
        if user_value(key='WaveTime', value=3):
            return FourthWaveStart()
        if user_value(key='WaveTime', value=4):
            return SixthWaveStart()
        """
        <condition name="UserValue" key="WaveTime" value="5" >         
            <transition state="6thWaveStart"/>    
        </condition>
        """
        if user_value(key='WaveTime', value=6):
            return SixthWaveStart()


class Quit(state.State):
    pass


