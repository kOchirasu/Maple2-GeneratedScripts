""" trigger/52000052_qd/910_mobwave_10round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5110], visible=False) # 10Round_ShadowApp

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
        set_effect(triggerIds=[5110], visible=True) # 10Round_ShadowApp

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
        create_monster(spawnIds=[91000,91002,91004,91006,91008], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection11()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91001,91003,91005,91007,91010], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91010,91012,91014,91016,91018], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection21()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91011,91013,91015,91017,91019], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91020,91022,91024,91026,91028], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection31()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91021,91023,91025,91027,91029], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91030,91032,91034,91036,91038], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection41()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91031,91033,91035,91037,91039], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91040,91042,91044,91046,91048], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection51()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91041,91043,91045,91047,91049], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


#  딜레이 랜덤 
class FirstWaveDelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return FirstWaveDelay7000()
        if random_condition(rate=30):
            return FirstWaveDelay8000()
        if random_condition(rate=30):
            return FirstWaveDelay9000()


class FirstWaveDelay7000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDelay8000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FirstWaveDelay9000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom()
        if monster_dead(boxIds=[1010]):
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
        create_monster(spawnIds=[91000,91002,91004,91006,91008], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection11()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91001,91003,91005,91007,91010], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91010,91012,91014,91016,91018], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection21()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91011,91013,91015,91017,91019], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91020,91022,91024,91026,91028], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection31()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91021,91023,91025,91027,91029], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91030,91032,91034,91036,91038], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection41()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91031,91033,91035,91037,91039], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91040,91042,91044,91046,91048], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection51()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91041,91043,91045,91047,91049], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


#  딜레이 랜덤 
class SecondWaveDelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return SecondWaveDelay5000()
        if random_condition(rate=30):
            return SecondWaveDelay6000()
        if random_condition(rate=30):
            return SecondWaveDelay7000()


class SecondWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDelay6000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class SecondWaveDelay7000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1010]):
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
        create_monster(spawnIds=[91000,91002,91004,91006,91008], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection11()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91001,91003,91005,91007,91010], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91010,91012,91014,91016,91018], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection21()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91011,91013,91015,91017,91019], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91020,91022,91024,91026,91028], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection31()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91021,91023,91025,91027,91029], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91030,91032,91034,91036,91038], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection41()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91031,91033,91035,91037,91039], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91040,91042,91044,91046,91048], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection51()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91041,91043,91045,91047,91049], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


#  딜레이 랜덤 
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
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=4) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if true():
            return FourthWaveDirectionRandom()


#  방향 랜덤 
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
        create_monster(spawnIds=[91000,91002,91004,91006,91008], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection11()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91001,91003,91005,91007,91010], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91010,91012,91014,91016,91018], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection21()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91011,91013,91015,91017,91019], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91020,91022,91024,91026,91028], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection31()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91021,91023,91025,91027,91029], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91030,91032,91034,91036,91038], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection41()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91031,91033,91035,91037,91039], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91040,91042,91044,91046,91048], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FourthWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91041,91043,91045,91047,91049], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


#  추가 웨이브 경험치 없음 
class FifthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[91090,91092,91094,91096,91098], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FifthWaveDelay()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class FifthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[91091,91093,91095,91097,91099], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


#  웨이브 종료 
class DefenceSucess01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[91000,91001,91002,91003,91004,91005,91006,91007,91008,91010,91010,91011,91012,91013,91014,91015,91016,91017,91018,91019,91020,91021,91022,91023,91024,91025,91026,91027,91028,91029,91030,91031,91032,91033,91034,91035,91036,91037,91038,91039,91040,91041,91042,91043,91044,91045,91046,91047,91048,91049,91080,91081,91082,91083,91084,91085,91086,91087,91088,91089,91090,91091,91092,91093,91094,91095,91096,91097,91098,91099]):
            return DefenceSucess02()
        if monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart()


class DefenceSucess02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5110], visible=False) # 10Round_ShadowApp
        set_user_value(triggerId=10, key='10RoundSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  패널티 10초 
class NpcDownPenaltyStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=810, key='PenaltyMob', value=1)
        destroy_monster(spawnIds=[1010]) # 수호대상 틴차이
        create_monster(spawnIds=[1110], arg2=False) # 쓰러진 틴차이
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        set_conversation(type=1, spawnId=1110, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        destroy_monster(spawnIds=[1110]) # 쓰러진 틴차이
        create_monster(spawnIds=[1010], arg2=False) # 수호대상 틴차이
        remove_balloon_talk(spawnId=1110)

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


