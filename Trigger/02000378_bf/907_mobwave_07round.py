""" trigger/02000378_bf/907_mobwave_07round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5107], visible=False) # 07Round_ShadowApp

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
        set_event_ui(type=1, arg2='$02000378_BF__907_MOBWAVE_07ROUND__0$', arg3='6000', arg4='0')
        set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5107], visible=True) # 07Round_ShadowApp

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
        create_monster(spawnIds=[90700,90702,90704], arg2=False) # ,90706,90708

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection11()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90701,90703,90705], arg2=False) # ,90707,90709

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90710,90712,90714], arg2=False) # ,90716,90718

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection21()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90711,90713,90715], arg2=False) # ,90717,90719

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90720,90722,90724], arg2=False) # ,90726,90728

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection31()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90721,90723,90725], arg2=False) # ,90727,90729

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90730,90732,90734], arg2=False) # ,90736,90738

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection41()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90731,90733,90735], arg2=False) # ,90737,90739

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90740,90742,90744], arg2=False) # ,90746,90748

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection51()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90741,90743,90745], arg2=False) # ,90747,90749

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
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
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FirstWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom()
        if monster_dead(boxIds=[1007]):
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
        create_monster(spawnIds=[90700,90702,90704], arg2=False) # ,90706,90708

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection11()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90701,90703,90705], arg2=False) # ,90707,90709

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90710,90712,90714], arg2=False) # ,90716,90718

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection21()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90711,90713,90715], arg2=False) # ,90717,90719

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90720,90722,90724], arg2=False) # ,90726,90728

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection31()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90721,90723,90725], arg2=False) # ,90727,90729

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90730,90732,90734], arg2=False) # ,90736,90738

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection41()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90731,90733,90735], arg2=False) # ,90737,90739

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90740,90742,90744], arg2=False) # ,90746,90748

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection51()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90741,90743,90745], arg2=False) # ,90747,90749

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
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
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class SecondWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1007]):
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
        create_monster(spawnIds=[90700,90702,90704], arg2=False) # ,90706,90708

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection11()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90701,90703,90705], arg2=False) # ,90707,90709

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90710,90712,90714], arg2=False) # ,90716,90718

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection21()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90711,90713,90715], arg2=False) # ,90717,90719

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90720,90722,90724], arg2=False) # ,90726,90728

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection31()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90721,90723,90725], arg2=False) # ,90727,90729

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90730,90732,90734], arg2=False) # ,90736,90738

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection41()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90731,90733,90735], arg2=False) # ,90737,90739

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90740,90742,90744], arg2=False) # ,90746,90748

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection51()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90741,90743,90745], arg2=False) # ,90747,90749

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1007]):
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
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=4)

    def on_tick(self) -> state.State:
        if true():
            return FourthWaveDirectionRandom()


#   방향 랜덤 	
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
        create_monster(spawnIds=[90700,90702,90704], arg2=False) # ,90706,90708

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection11()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90701,90703,90705], arg2=False) # ,90707,90709

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90710,90712,90714], arg2=False) # ,90716,90718

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection21()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90711,90713,90715], arg2=False) # ,90717,90719

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90720,90722,90724], arg2=False) # ,90726,90728

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection31()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90721,90723,90725], arg2=False) # ,90727,90729

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90730,90732,90734], arg2=False) # ,90736,90738

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection41()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90731,90733,90735], arg2=False) # ,90737,90739

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90740,90742,90744], arg2=False) # ,90746,90748

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FourthWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90741,90743,90745], arg2=False) # ,90747,90749

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


#  추가 웨이브 경험치 없음 
class FifthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90790,90792,90794], arg2=False) # ,90796,90798

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FifthWaveDelay()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class FifthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90791,90793,90795], arg2=False) # ,90797,90799

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


#  웨이브 종료 
class DefenceSucess01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90700,90701,90702,90703,90704,90705,90706,90707,90708,90710,90710,90711,90712,90713,90714,90715,90716,90717,90718,90719,90720,90721,90722,90723,90724,90725,90726,90727,90728,90729,90730,90731,90732,90733,90734,90735,90736,90737,90738,90739,90740,90741,90742,90743,90744,90745,90746,90747,90748,90749,90780,90781,90782,90783,90784,90785,90786,90787,90788,90789,90790,90791,90792,90793,90794,90795,90796,90797,90798,90799]):
            return DefenceSucess02()
        if monster_dead(boxIds=[1007]):
            return NpcDownPenaltyStart()


class DefenceSucess02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5107], visible=False) # 07Round_ShadowApp
        set_user_value(triggerId=7, key='07RoundSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  패널티 10초 
class NpcDownPenaltyStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=807, key='PenaltyMob', value=1)
        destroy_monster(spawnIds=[1007]) # 수호대상 틴차이
        create_monster(spawnIds=[1107], arg2=False) # 쓰러진 틴차이
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__907_MOBWAVE_07ROUND__1$', arg3='4000', arg4='0')
        set_conversation(type=1, spawnId=1107, script='$02000378_BF__907_MOBWAVE_07ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        set_event_ui(type=1, arg2='$02000378_BF__907_MOBWAVE_07ROUND__3$', arg3='4000', arg4='0')
        destroy_monster(spawnIds=[1107]) # 쓰러진 틴차이
        create_monster(spawnIds=[1007], arg2=False) # 수호대상 틴차이
        remove_balloon_talk(spawnId=1107)

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


