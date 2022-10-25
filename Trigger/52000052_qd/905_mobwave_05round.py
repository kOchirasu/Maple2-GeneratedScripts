""" trigger/52000052_qd/905_mobwave_05round.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5105], visible=False) # 05Round_ShadowApp

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MobWaveStart', value=1):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart(self.ctx)


class FirstWaveStart(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__0$', arg3='6000', arg4='0')
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5105], visible=True) # 05Round_ShadowApp

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirectionRandom(self.ctx)


# 방향 랜덤
class FirstWaveDirectionRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=20):
            return FirstWaveDirection10(self.ctx)
        if self.random_condition(rate=20):
            return FirstWaveDirection20(self.ctx)
        if self.random_condition(rate=20):
            return FirstWaveDirection30(self.ctx)
        if self.random_condition(rate=20):
            return FirstWaveDirection40(self.ctx)
        if self.random_condition(rate=20):
            return FirstWaveDirection50(self.ctx)


class FirstWaveDirection10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90500,90502,90504,90506,90508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90501,90503,90505,90507,90509], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90510,90512,90514,90516,90518], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90511,90513,90515,90517,90519], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90520,90522,90524,90526,90528], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90521,90523,90525,90527,90529], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90530,90532,90534,90536,90538], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90531,90533,90535,90537,90539], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90540,90542,90544,90546,90548], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90541,90543,90545,90547,90549], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class FirstWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return FirstWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay5000(self.ctx)


class FirstWaveDelay3000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class SecondWaveDirectionRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=20):
            return SecondWaveDirection10(self.ctx)
        if self.random_condition(rate=20):
            return SecondWaveDirection20(self.ctx)
        if self.random_condition(rate=20):
            return SecondWaveDirection30(self.ctx)
        if self.random_condition(rate=20):
            return SecondWaveDirection40(self.ctx)
        if self.random_condition(rate=20):
            return SecondWaveDirection50(self.ctx)


class SecondWaveDirection10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90500,90502,90504,90506,90508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90501,90503,90505,90507,90509], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90510,90512,90514,90516,90518], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90511,90513,90515,90517,90519], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90520,90522,90524,90526,90528], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90521,90523,90525,90527,90529], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90530,90532,90534,90536,90538], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90531,90533,90535,90537,90539], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90540,90542,90544,90546,90548], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90541,90543,90545,90547,90549], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class SecondWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return SecondWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay5000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay6000(self.ctx)


class SecondWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay6000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class ThirdWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억

    def on_tick(self) -> common.Trigger:
        if self.true():
            return ThirdWaveDirectionRandom(self.ctx)


class ThirdWaveDirectionRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=20):
            return ThirdWaveDirection10(self.ctx)
        if self.random_condition(rate=20):
            return ThirdWaveDirection20(self.ctx)
        if self.random_condition(rate=20):
            return ThirdWaveDirection30(self.ctx)
        if self.random_condition(rate=20):
            return ThirdWaveDirection40(self.ctx)
        if self.random_condition(rate=20):
            return ThirdWaveDirection50(self.ctx)


class ThirdWaveDirection10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90500,90502,90504,90506,90508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90501,90503,90505,90507,90509], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90510,90512,90514,90516,90518], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90511,90513,90515,90517,90519], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90520,90522,90524,90526,90528], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90521,90523,90525,90527,90529], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90530,90532,90534,90536,90538], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90531,90533,90535,90537,90539], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90540,90542,90544,90546,90548], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90541,90543,90545,90547,90549], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class ThirdWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return ThirdWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return ThirdWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return ThirdWaveDelay5000(self.ctx)


class ThirdWaveDelay3000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=4) # 웨이브 진행 순서 기억

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FourthWaveDirectionRandom(self.ctx)


# 방향 랜덤
class FourthWaveDirectionRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=20):
            return FourthWaveDirection10(self.ctx)
        if self.random_condition(rate=20):
            return FourthWaveDirection20(self.ctx)
        if self.random_condition(rate=20):
            return FourthWaveDirection30(self.ctx)
        if self.random_condition(rate=20):
            return FourthWaveDirection40(self.ctx)
        if self.random_condition(rate=20):
            return FourthWaveDirection50(self.ctx)


class FourthWaveDirection10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90500,90502,90504,90506,90508], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90501,90503,90505,90507,90509], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90510,90512,90514,90516,90518], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90511,90513,90515,90517,90519], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90520,90522,90524,90526,90528], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90521,90523,90525,90527,90529], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90530,90532,90534,90536,90538], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90531,90533,90535,90537,90539], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90540,90542,90544,90546,90548], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90541,90543,90545,90547,90549], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


# 추가 웨이브 경험치 없음
class FifthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90590,90592,90594,90596,90598], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90591,90593,90595,90597,90599], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


# 웨이브 종료
class DefenceSucess01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[90500,90501,90502,90503,90504,90505,90506,90507,90508,90510,90510,90511,90512,90513,90514,90515,90516,90517,90518,90519,90520,90521,90522,90523,90524,90525,90526,90527,90528,90529,90530,90531,90532,90533,90534,90535,90536,90537,90538,90539,90540,90541,90542,90543,90544,90545,90546,90547,90548,90549,90580,90581,90582,90583,90584,90585,90586,90587,90588,90589,90590,90591,90592,90593,90594,90595,90596,90597,90598,90599]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1005]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5105], visible=False) # 05Round_ShadowApp
        self.set_user_value(triggerId=5, key='05RoundSuccess', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=805, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1005]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1105], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1105, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return NpcDownPenaltyEnd(self.ctx)


class NpcDownPenaltyEnd(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PenaltyFinish', value=1):
            return ReturnToWave(self.ctx)


class ReturnToWave(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__3$', arg3='4000', arg4='0')
        self.destroy_monster(spawnIds=[1105]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1005], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1105)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='WaveTime', value=1):
            return SecondWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=2):
            return ThirdWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=3):
            return FourthWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=4):
            return FifthWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=5):
            return FifthWaveStart(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
