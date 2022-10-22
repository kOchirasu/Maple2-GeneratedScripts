""" trigger/02000378_bf/908_mobwave_08round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5108], visible=False) # 08Round_ShadowApp

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
        set_event_ui(type=1, arg2='$02000378_BF__908_MOBWAVE_08ROUND__0$', arg3='6000', arg4='0')
        set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5108], visible=True) # 08Round_ShadowApp

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirectionRandom()


#  방향 랜덤 
class FirstWaveDirectionRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return FirstWaveDirection10()
        if random_condition(rate=20):
            return FirstWaveDirection20()
        if random_condition(rate=20):
            return FirstWaveDirection30()
        if random_condition(rate=20):
            return FirstWaveDirection40()
        if random_condition(rate=20):
            return FirstWaveDirection50()


class FirstWaveDirection10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90800,90802,90804], arg2=False) # ,90806,90808

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection11()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90801,90803,90805], arg2=False) # ,90807,90809

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90810,90812,90814], arg2=False) # ,90816,90818

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection21()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90811,90813,90815], arg2=False) # ,90817,90819

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90820,90822,90824], arg2=False) # ,90826,90828

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection31()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90821,90823,90825], arg2=False) # ,90827,90829

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90830,90832,90834], arg2=False) # ,90836,90838

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection41()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90831,90833,90835], arg2=False) # ,90837,90839

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90840,90842,90844], arg2=False) # ,90846,90848

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection51()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90841,90843,90845], arg2=False) # ,90847,90849

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


#  딜레이 랜덤 
class FirstWaveDelayRandom(state.State):
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
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FirstWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


#  방향 랜덤 
class SecondWaveDirectionRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return SecondWaveDirection10()
        if random_condition(rate=20):
            return SecondWaveDirection20()
        if random_condition(rate=20):
            return SecondWaveDirection30()
        if random_condition(rate=20):
            return SecondWaveDirection40()
        if random_condition(rate=20):
            return SecondWaveDirection50()


class SecondWaveDirection10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90800,90802,90804], arg2=False) # ,90806,90808

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection11()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90801,90803,90805], arg2=False) # ,90807,90809

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90810,90812,90814], arg2=False) # ,90816,90818

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection21()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90811,90813,90815], arg2=False) # ,90817,90819

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90820,90822,90824], arg2=False) # ,90826,90828

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection31()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90821,90823,90825], arg2=False) # ,90827,90829

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90830,90832,90834], arg2=False) # ,90836,90838

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection41()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90831,90833,90835], arg2=False) # ,90837,90839

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90840,90842,90844], arg2=False) # ,90846,90848

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection51()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90841,90843,90845], arg2=False) # ,90847,90849

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


#  딜레이 랜덤 
class SecondWaveDelayRandom(state.State):
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
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class SecondWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1008]):
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


class ThirdWaveDirection10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90800,90802,90804], arg2=False) # ,90806,90808

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection11()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90801,90803,90805], arg2=False) # ,90807,90809

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90810,90812,90814], arg2=False) # ,90816,90818

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection21()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90811,90813,90815], arg2=False) # ,90817,90819

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90820,90822,90824], arg2=False) # ,90826,90828

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection31()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90821,90823,90825], arg2=False) # ,90827,90829

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90830,90832,90834], arg2=False) # ,90836,90838

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection41()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90831,90833,90835], arg2=False) # ,90837,90839

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90840,90842,90844], arg2=False) # ,90846,90848

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection51()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90841,90843,90845], arg2=False) # ,90847,90849

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


#  딜레이 랜덤 	
class ThirdWaveDelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return ThirdWaveDelay2000()
        if random_condition(rate=30):
            return ThirdWaveDelay3000()
        if random_condition(rate=30):
            return ThirdWaveDelay4000()


class ThirdWaveDelay2000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=4)

    def on_tick(self) -> state.State:
        if true():
            return FourthWaveDirectionRandom()


# 방향 랜덤 	
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


class FourthWaveDirection10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90800,90802,90804], arg2=False) # ,90806,90808

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection11()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90801,90803,90805], arg2=False) # ,90807,90809

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90810,90812,90814], arg2=False) # ,90816,90818

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection21()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90811,90813,90815], arg2=False) # ,90817,90819

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90820,90822,90824], arg2=False) # ,90826,90828

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection31()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90821,90823,90825], arg2=False) # ,90827,90829

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90830,90832,90834], arg2=False) # ,90836,90838

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection41()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90831,90833,90835], arg2=False) # ,90837,90839

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90840,90842,90844], arg2=False) # ,90846,90848

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FourthWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90841,90843,90845], arg2=False) # ,90847,90849

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


#  추가 웨이브 경험치 없음 
class FifthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90890,90892,90894], arg2=False) # ,90896,90898

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FifthWaveDelay()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class FifthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90891,90893,90895], arg2=False) # ,90897,90899

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


#  웨이브 종료 
class DefenceSucess01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90800,90801,90802,90803,90804,90805,90806,90807,90808,90810,90810,90811,90812,90813,90814,90815,90816,90817,90818,90819,90820,90821,90822,90823,90824,90825,90826,90827,90828,90829,90830,90831,90832,90833,90834,90835,90836,90837,90838,90839,90840,90841,90842,90843,90844,90845,90846,90847,90848,90849,90880,90881,90882,90883,90884,90885,90886,90887,90888,90889,90890,90891,90892,90893,90894,90895,90896,90897,90898,90899]):
            return DefenceSucess02()
        if monster_dead(boxIds=[1008]):
            return NpcDownPenaltyStart()


class DefenceSucess02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5108], visible=False) # 08Round_ShadowApp
        set_user_value(triggerId=8, key='08RoundSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  패널티 10초 
class NpcDownPenaltyStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=808, key='PenaltyMob', value=1)
        destroy_monster(spawnIds=[1008]) # 수호대상 틴차이
        create_monster(spawnIds=[1108], arg2=False) # 쓰러진 틴차이
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__908_MOBWAVE_08ROUND__1$', arg3='4000', arg4='0')
        set_conversation(type=1, spawnId=1108, script='$02000378_BF__908_MOBWAVE_08ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        set_event_ui(type=1, arg2='$02000378_BF__908_MOBWAVE_08ROUND__3$', arg3='4000', arg4='0')
        destroy_monster(spawnIds=[1108]) # 쓰러진 틴차이
        create_monster(spawnIds=[1008], arg2=False) # 수호대상 틴차이
        remove_balloon_talk(spawnId=1108)

    def on_tick(self) -> state.State:
        if user_value(key='WaveTime', value=1):
            return SecondWaveStart()
        if user_value(key='WaveTime', value=2):
            return ThirdWaveStart()
        if user_value(key='WaveTime', value=3):
            return FourthWaveStart()
        if user_value(key='WaveTime', value=4):
            return FifthWaveStart()
        if user_value(key='WaveTime', value=5):
            return FifthWaveStart()


class Quit(state.State):
    pass


