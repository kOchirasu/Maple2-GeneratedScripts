""" trigger/52000052_qd/902_mobwave_02round.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5102], visible=False) # 02Round_ShadowApp

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
        self.set_effect(triggerIds=[5102], visible=True) # 02Round_ShadowApp
        self.create_monster(spawnIds=[90200,90202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelayRandom(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90205,90207,90209], animationEffect=False)

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
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90212,90214], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelayRandom(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90213,90215,90217], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return SecondWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay5000(self.ctx)


class SecondWaveDelay3000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class ThirdWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=702, key='TotemApp', value=1)
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
        if self.random_condition(rate=20):
            return ThirdWaveDirection60(self.ctx)


# 왼쪽 위
class ThirdWaveDirection10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90222,90224], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90221,90223,90227], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class ThirdWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90232,90238], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90231,90233,90237], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class ThirdWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90246,90248], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90241,90243,90245], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class ThirdWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90250,90258], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90253,90255,90259], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class ThirdWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90262,90266], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90263,90265,90269], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class ThirdWaveDirection60(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90270,90272], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection61(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection61(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90271,90277,90279], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


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
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=4) # 웨이브 진행 순서 기억

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FourthWaveDirectionRandom(self.ctx)


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
        if self.random_condition(rate=20):
            return FourthWaveDirection60(self.ctx)


# 왼쪽 위
class FourthWaveDirection10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90222,90224], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90221,90225,90227], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class FourthWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90232,90238], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90231,90233,90237], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class FourthWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90246,90248], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90241,90243,90245], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class FourthWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90250,90258], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90253,90255,90257], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class FourthWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90262,90266], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90263,90267,90269], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class FourthWaveDirection60(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90270,90272], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection61(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection61(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90271,90277,90279], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return FourthWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return FourthWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return FourthWaveDelay2000(self.ctx)


class FourthWaveDelay3000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDelay2000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억

    def on_tick(self) -> common.Trigger:
        if self.true():
            return FifthWaveDirectionRandom(self.ctx)


class FifthWaveDirectionRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=20):
            return FifthWaveDirection10(self.ctx)
        if self.random_condition(rate=20):
            return FifthWaveDirection20(self.ctx)
        if self.random_condition(rate=20):
            return FifthWaveDirection30(self.ctx)
        if self.random_condition(rate=20):
            return FifthWaveDirection40(self.ctx)
        if self.random_condition(rate=20):
            return FifthWaveDirection50(self.ctx)
        if self.random_condition(rate=20):
            return FifthWaveDirection60(self.ctx)


# 왼쪽 위
class FifthWaveDirection10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90222,90224], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90221,90223,90227], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class FifthWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90232,90238], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90233,90237,90239], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class FifthWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90246,90248], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90241,90243,90247], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class FifthWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90250,90258], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90253,90255,90259], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class FifthWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90262,90266], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90263,90267,90269], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class FifthWaveDirection60(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90270,90272], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDirection61(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection61(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90275,90277,90279], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class SixthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=6) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90290,90292], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SixthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class SixthWaveDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90295,90297,90299], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[90200,90201,90202,90203,90204,90205,90206,90207,90208,90209,90210,90211,90212,90213,90214,90215,90216,90217,90218,90219,90220,90221,90222,90223,90224,90225,90226,90227,90228,90229,90230,90231,90232,90233,90234,90235,90236,90237,90238,90239,90240,90241,90242,90243,90244,90245,90246,90247,90248,90249,90250,90251,90252,90253,90254,90255,90256,90257,90258,90259,90260,90261,90262,90263,90264,90265,90266,90267,90268,90269,90270,90271,90272,90273,90274,90275,90276,90277,90278,90279,90280,90281,90282,90283,90284,90285,90286,90287,90288,90289,90290,90291,90292,90293,90294,90295,90296,90297,90298,90299]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1002]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=False) # 02Round_ShadowApp
        self.set_user_value(triggerId=2, key='02RoundSuccess', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=802, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1002]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1102], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1102, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        self.destroy_monster(spawnIds=[1102]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1002], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1102)

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
            return SixthWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=6):
            return SixthWaveStart(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
