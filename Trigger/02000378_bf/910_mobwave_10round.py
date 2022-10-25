""" trigger/02000378_bf/910_mobwave_10round.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5110], visible=False) # 10Round_ShadowApp

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
        self.set_event_ui(type=1, arg2='$02000378_BF__910_MOBWAVE_10ROUND__0$', arg3='6000', arg4='0')
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5110], visible=True) # 10Round_ShadowApp

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
        self.create_monster(spawnIds=[91004,91006,91008], animationEffect=False) # 91000,91002,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91005,91007,91010], animationEffect=False) # 91001,91003,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91014,91016,91018], animationEffect=False) # 91010,91012,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91015,91017,91019], animationEffect=False) # 91011,91013,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91024,91026,91028], animationEffect=False) # 91020,91022,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91025,91027,91029], animationEffect=False) # 91021,91023,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91034,91036,91038], animationEffect=False) # 91030,91032,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91035,91037,91039], animationEffect=False) # 91031,91033,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91044,91046,91048], animationEffect=False) # 91040,91042,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91045,91047,91049], animationEffect=False) # 91041,91043,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class FirstWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return FirstWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay5000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay6000(self.ctx)


class FirstWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay6000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
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
        self.create_monster(spawnIds=[91000,91002,91004], animationEffect=False) # ,91006,91008

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91001,91003,91005], animationEffect=False) # ,91007,91010

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91010,91012,91014], animationEffect=False) # ,91016,91018

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91011,91013,91015], animationEffect=False) # ,91017,91019

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91020,91022,91024], animationEffect=False) # ,91026,91028

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91021,91023,91025], animationEffect=False) # ,91027,91029

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91030,91032,91034], animationEffect=False) # ,91036,91038

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91031,91033,91035], animationEffect=False) # ,91037,91039

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91040,91042,91044], animationEffect=False) # ,91046,91048

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91041,91043,91045], animationEffect=False) # ,91047,91049

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class SecondWaveDelayRandom(common.Trigger):
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
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
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
        self.create_monster(spawnIds=[91000,91002,91008], animationEffect=False) # 91004,91006,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91001,91003,91010], animationEffect=False) # 91005,91007,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91010,91012,91018], animationEffect=False) # 91014,91016,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91011,91013,91019], animationEffect=False) # 91015,91017,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91020,91022,91028], animationEffect=False) # 91024,91026,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91021,91023,91029], animationEffect=False) # 91025,91027,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91030,91032,91038], animationEffect=False) # 91034,91036,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91031,91033,91039], animationEffect=False) # 91035,91037,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91040,91042,91048], animationEffect=False) # 91044,91046,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91041,91043,91049], animationEffect=False) # 91045,91047,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class ThirdWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return ThirdWaveDelay2000(self.ctx)
        if self.random_condition(rate=30):
            return ThirdWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return ThirdWaveDelay4000(self.ctx)


class ThirdWaveDelay2000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay3000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=4)

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
        self.create_monster(spawnIds=[91000,91006,91008], animationEffect=False) # 91002,91004,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91001,91007,91010], animationEffect=False) # 91003,91005,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91010,91016,91018], animationEffect=False) # 91012,91014,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91011,91017,91019], animationEffect=False) # 91013,91015,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91020,91026,91028], animationEffect=False) # 91022,91024,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91021,91027,91029], animationEffect=False) # 91023,91025,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91030,91036,91038], animationEffect=False) # 91032,91034,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91031,91037,91039], animationEffect=False) # 91033,91035,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91040,91046,91048], animationEffect=False) # 91042,91044,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91041,91047,91049], animationEffect=False) # 91043,91045,

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


# 추가 웨이브 경험치 없음
class FifthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[91090,91092,91094], animationEffect=False) # ,91096,91098

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91091,91093,91095], animationEffect=False) # ,91097,91099

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


# 웨이브 종료
class DefenceSucess01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[91000,91001,91002,91003,91004,91005,91006,91007,91008,91010,91010,91011,91012,91013,91014,91015,91016,91017,91018,91019,91020,91021,91022,91023,91024,91025,91026,91027,91028,91029,91030,91031,91032,91033,91034,91035,91036,91037,91038,91039,91040,91041,91042,91043,91044,91045,91046,91047,91048,91049,91080,91081,91082,91083,91084,91085,91086,91087,91088,91089,91090,91091,91092,91093,91094,91095,91096,91097,91098,91099]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5110], visible=False) # 10Round_ShadowApp
        self.set_user_value(triggerId=10, key='10RoundSuccess', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=810, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1010]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1110], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$02000378_BF__910_MOBWAVE_10ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1110, script='$02000378_BF__910_MOBWAVE_10ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        self.set_event_ui(type=1, arg2='$02000378_BF__910_MOBWAVE_10ROUND__3$', arg3='4000', arg4='0')
        self.destroy_monster(spawnIds=[1110]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1010], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1110)

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
