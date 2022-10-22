""" trigger/52000052_qd/905_mobwave_05round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5105], visible=False) # 05Round_ShadowApp

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
        set_effect(triggerIds=[5105], visible=True) # 05Round_ShadowApp

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
        create_monster(spawnIds=[90500,90502,90504,90506,90508], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection11()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90501,90503,90505,90507,90509], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90510,90512,90514,90516,90518], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection21()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90511,90513,90515,90517,90519], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90520,90522,90524,90526,90528], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection31()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90521,90523,90525,90527,90529], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90530,90532,90534,90536,90538], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection41()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90531,90533,90535,90537,90539], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90540,90542,90544,90546,90548], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDirection51()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90541,90543,90545,90547,90549], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
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
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FirstWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom()
        if monster_dead(boxIds=[1005]):
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
        create_monster(spawnIds=[90500,90502,90504,90506,90508], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection11()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90501,90503,90505,90507,90509], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90510,90512,90514,90516,90518], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection21()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90511,90513,90515,90517,90519], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90520,90522,90524,90526,90528], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection31()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90521,90523,90525,90527,90529], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90530,90532,90534,90536,90538], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection41()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90531,90533,90535,90537,90539], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90540,90542,90544,90546,90548], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDirection51()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90541,90543,90545,90547,90549], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


#  딜레이 랜덤 
class SecondWaveDelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return SecondWaveDelay4000()
        if random_condition(rate=30):
            return SecondWaveDelay5000()
        if random_condition(rate=30):
            return SecondWaveDelay6000()


class SecondWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class SecondWaveDelay6000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1005]):
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
        create_monster(spawnIds=[90500,90502,90504,90506,90508], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection11()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90501,90503,90505,90507,90509], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90510,90512,90514,90516,90518], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection21()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90511,90513,90515,90517,90519], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90520,90522,90524,90526,90528], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection31()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90521,90523,90525,90527,90529], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90530,90532,90534,90536,90538], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection41()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90531,90533,90535,90537,90539], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90540,90542,90544,90546,90548], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection51()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90541,90543,90545,90547,90549], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1005]):
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
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1005]):
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
        create_monster(spawnIds=[90500,90502,90504,90506,90508], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection11()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90501,90503,90505,90507,90509], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90510,90512,90514,90516,90518], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection21()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90511,90513,90515,90517,90519], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90520,90522,90524,90526,90528], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection31()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90521,90523,90525,90527,90529], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90530,90532,90534,90536,90538], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection41()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90531,90533,90535,90537,90539], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90540,90542,90544,90546,90548], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FourthWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90541,90543,90545,90547,90549], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


#  추가 웨이브 경험치 없음 
class FifthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90590,90592,90594,90596,90598], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FifthWaveDelay()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class FifthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90591,90593,90595,90597,90599], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


#  웨이브 종료 
class DefenceSucess01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90500,90501,90502,90503,90504,90505,90506,90507,90508,90510,90510,90511,90512,90513,90514,90515,90516,90517,90518,90519,90520,90521,90522,90523,90524,90525,90526,90527,90528,90529,90530,90531,90532,90533,90534,90535,90536,90537,90538,90539,90540,90541,90542,90543,90544,90545,90546,90547,90548,90549,90580,90581,90582,90583,90584,90585,90586,90587,90588,90589,90590,90591,90592,90593,90594,90595,90596,90597,90598,90599]):
            return DefenceSucess02()
        if monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart()


class DefenceSucess02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5105], visible=False) # 05Round_ShadowApp
        set_user_value(triggerId=5, key='05RoundSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  패널티 10초 
class NpcDownPenaltyStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=805, key='PenaltyMob', value=1)
        destroy_monster(spawnIds=[1005]) # 수호대상 틴차이
        create_monster(spawnIds=[1105], arg2=False) # 쓰러진 틴차이
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        set_conversation(type=1, spawnId=1105, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        destroy_monster(spawnIds=[1105]) # 쓰러진 틴차이
        create_monster(spawnIds=[1005], arg2=False) # 수호대상 틴차이
        remove_balloon_talk(spawnId=1105)

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


