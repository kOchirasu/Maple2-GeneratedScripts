""" trigger/52000052_qd/910_mobwave_10round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5110], visible=False) # 10Round_ShadowApp

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobWaveStart', value=1):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart(self.ctx)


class FirstWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__0$', arg3='6000', arg4='0')
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5110], visible=True) # 10Round_ShadowApp

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirectionRandom(self.ctx)


# 방향 랜덤
class FirstWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class FirstWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91000,91002,91004,91006,91008], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91001,91003,91005,91007,91010], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91010,91012,91014,91016,91018], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91011,91013,91015,91017,91019], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91020,91022,91024,91026,91028], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91021,91023,91025,91027,91029], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91030,91032,91034,91036,91038], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91031,91033,91035,91037,91039], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91040,91042,91044,91046,91048], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91041,91043,91045,91047,91049], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class FirstWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=30):
            return FirstWaveDelay7000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay8000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay9000(self.ctx)


class FirstWaveDelay7000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay8000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay9000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class SecondWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class SecondWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91000,91002,91004,91006,91008], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91001,91003,91005,91007,91010], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91010,91012,91014,91016,91018], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91011,91013,91015,91017,91019], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91020,91022,91024,91026,91028], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91021,91023,91025,91027,91029], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91030,91032,91034,91036,91038], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91031,91033,91035,91037,91039], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91040,91042,91044,91046,91048], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91041,91043,91045,91047,91049], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class SecondWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=30):
            return SecondWaveDelay5000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay6000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay7000(self.ctx)


class SecondWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay6000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay7000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class ThirdWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ThirdWaveDirectionRandom(self.ctx)


class ThirdWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class ThirdWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91000,91002,91004,91006,91008], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91001,91003,91005,91007,91010], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91010,91012,91014,91016,91018], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91011,91013,91015,91017,91019], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91020,91022,91024,91026,91028], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91021,91023,91025,91027,91029], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91030,91032,91034,91036,91038], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91031,91033,91035,91037,91039], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91040,91042,91044,91046,91048], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91041,91043,91045,91047,91049], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class ThirdWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=30):
            return ThirdWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return ThirdWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return ThirdWaveDelay5000(self.ctx)


class ThirdWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=4) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return FourthWaveDirectionRandom(self.ctx)


# 방향 랜덤
class FourthWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class FourthWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91000,91002,91004,91006,91008], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91001,91003,91005,91007,91010], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91010,91012,91014,91016,91018], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91011,91013,91015,91017,91019], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91020,91022,91024,91026,91028], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91021,91023,91025,91027,91029], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91030,91032,91034,91036,91038], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91031,91033,91035,91037,91039], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91040,91042,91044,91046,91048], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91041,91043,91045,91047,91049], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 추가 웨이브 경험치 없음
class FifthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[91090,91092,91094,91096,91098], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[91091,91093,91095,91097,91099], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 웨이브 종료
class DefenceSucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[91000,91001,91002,91003,91004,91005,91006,91007,91008,91010,91010,91011,91012,91013,91014,91015,91016,91017,91018,91019,91020,91021,91022,91023,91024,91025,91026,91027,91028,91029,91030,91031,91032,91033,91034,91035,91036,91037,91038,91039,91040,91041,91042,91043,91044,91045,91046,91047,91048,91049,91080,91081,91082,91083,91084,91085,91086,91087,91088,91089,91090,91091,91092,91093,91094,91095,91096,91097,91098,91099]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1010]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5110], visible=False) # 10Round_ShadowApp
        self.set_user_value(triggerId=10, key='10RoundSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=810, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1010]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1110], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1110, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return NpcDownPenaltyEnd(self.ctx)


class NpcDownPenaltyEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PenaltyFinish', value=1):
            return ReturnToWave(self.ctx)


class ReturnToWave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__3$', arg3='4000', arg4='0')
        self.destroy_monster(spawnIds=[1110]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1010], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1110)

    def on_tick(self) -> trigger_api.Trigger:
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


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
