""" trigger/52000052_qd/912_mobwave_12round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5112], visible=False) # 12Round_ShadowApp

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
        set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__0$', arg3='6000', arg4='0')
        set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5112], visible=True) # 12Round_ShadowApp
        create_monster(spawnIds=[91200,91202,91204,91206,91208], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FirstWaveDelayRandom(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91201,91203,91205], arg2=False)

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
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FirstWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FirstWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class SecondWaveStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=712, key='TotemApp', value=1)
        set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[91210,91212,91214], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class SecondWaveDelayRandom(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91211,91213,91215], arg2=False)

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return SecondWaveDelay3000()
        if random_condition(rate=30):
            return SecondWaveDelay4000()
        if random_condition(rate=30):
            return SecondWaveDelay5000()


class SecondWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class SecondWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class SecondWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1012]):
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
        create_monster(spawnIds=[91220,91222,91224], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection11()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91221,91223,91225], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  오른쪽 위 
class ThirdWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91230,91232,91234], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection21()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91231,91233,91235], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  왼쪽 중앙 
class ThirdWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91240,91242,91244], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection31()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91241,91243,91245], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  오른쪽 중앙 
class ThirdWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91250,91252,91254], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection41()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91251,91253,91255], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  왼쪽 아래 
class ThirdWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91260,91262,91264], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection51()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91261,91263,91265], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  오른쪽 아래 
class ThirdWaveDirection60(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91270,91272,91274], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection61()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection61(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91271,91273,91275], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return ThirdWaveDelay3000()
        if random_condition(rate=30):
            return ThirdWaveDelay4000()
        if random_condition(rate=30):
            return ThirdWaveDelay5000()


class ThirdWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1012]):
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
        create_monster(spawnIds=[91220,91222,91224], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection11()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FourthWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91221,91223,91225], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  오른쪽 위 
class FourthWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91230,91232,91234], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection21()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FourthWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91231,91233,91235], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  왼쪽 중앙 
class FourthWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91240,91242,91244], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection31()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FourthWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91241,91243,91245], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  오른쪽 중앙 
class FourthWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91250,91252,91254], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection41()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FourthWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91251,91253,91255], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  왼쪽 아래 
class FourthWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91260,91262,91264], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection51()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FourthWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91261,91263,91265], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  오른쪽 아래 
class FourthWaveDirection60(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91270,91272,91274], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection61()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FourthWaveDirection61(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91271,91273,91275], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class FourthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91271,91273,91275], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


#  추가 웨이브 경험치 없음 
class SeventhWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=7) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[91290,91292,91294], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SeventhWaveDelay()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class SeventhWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91291,91293,91295], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class DefenceSucess01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[91200,91201,91202,91203,91204,91205,91206,91207,91208,91209,91210,91211,91212,91213,91214,91215,91216,91217,91218,91219,91220,91221,91222,91223,91224,91225,91226,91227,91228,91229,91230,91231,91232,91233,91234,91235,91236,91237,91238,91239,91240,91241,91242,91243,91244,91245,91246,91247,91248,91249,91250,91251,91252,91253,91254,91255,91256,91257,91258,91259,91260,91261,91262,91263,91264,91265,91266,91267,91268,91269,91270,91271,91272,91273,91274,91275,91276,91277,91278,91279,91280,91281,91282,91283,91284,91285,91286,91287,91288,91289,91290,91291,91292,91293,91294,91295,91296,91297,91298,91299]):
            return DefenceSucess02()
        if monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart()


class DefenceSucess02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5112], visible=False) # 12Round_ShadowApp
        set_user_value(triggerId=12, key='12RoundSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  패널티 10초 
class NpcDownPenaltyStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=812, key='PenaltyMob', value=1)
        destroy_monster(spawnIds=[1012]) # 수호대상 틴차이
        create_monster(spawnIds=[1112], arg2=False) # 쓰러진 틴차이
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        set_conversation(type=1, spawnId=1112, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__3$', arg3='4000', arg4='0')
        destroy_monster(spawnIds=[1112]) # 쓰러진 틴차이
        create_monster(spawnIds=[1012], arg2=False) # 수호대상 틴차이
        remove_balloon_talk(spawnId=1112)

    def on_tick(self) -> state.State:
        if user_value(key='WaveTime', value=1):
            return SecondWaveStart()
        if user_value(key='WaveTime', value=2):
            return ThirdWaveStart()
        if user_value(key='WaveTime', value=3):
            return FourthWaveStart()
        if user_value(key='WaveTime', value=4):
            return SeventhWaveStart()
        """
        <condition name="UserValue" key="WaveTime" value="5" >         
            <transition state="6thWaveStart"/>    
        </condition>         
            <condition name="UserValue" key="WaveTime" value="6" >         
            <transition state="7thWaveStart"/>    
        </condition>
        """
        if user_value(key='WaveTime', value=7):
            return SeventhWaveStart()


class Quit(state.State):
    pass


