""" trigger/02000378_bf/904_mobwave_04round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5104], visible=False) # 04Round_ShadowApp

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobWaveStart', value=1):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveStart(self.ctx)


class FirstWaveStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$02000378_BF__904_MOBWAVE_04ROUND__0$', arg3='6000', arg4='0')
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5104], visible=True) # 04Round_ShadowApp

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
    def on_enter(self):
        self.create_monster(spawnIds=[90400,90402,90404], animationEffect=False) # ,90406,90408

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection11(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90401,90403,90405], animationEffect=False) # ,90407,90409

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection20(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90410,90412,90414], animationEffect=False) # ,90416,90418

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection21(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90411,90413,90415], animationEffect=False) # ,90417,90419

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection30(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90420,90422,90424], animationEffect=False) # ,90426,90428

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection31(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90421,90423,90425], animationEffect=False) # ,90427,90429

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection40(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90430,90432,90434], animationEffect=False) # ,90436,90438

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection41(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90431,90433,90435], animationEffect=False) # ,90437,90439

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection50(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90440,90442,90444], animationEffect=False) # ,90446,90448

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection51(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90441,90443,90445], animationEffect=False) # ,90447,90449

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class FirstWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=30):
            return FirstWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay5000(self.ctx)


class FirstWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
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
    def on_enter(self):
        self.create_monster(spawnIds=[90400,90402,90404], animationEffect=False) # ,90406,90408

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection11(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90401,90403,90405], animationEffect=False) # ,90407,90409

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection20(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90410,90412,90414], animationEffect=False) # ,90416,90418

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection21(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90411,90413,90415], animationEffect=False) # ,90417,90419

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection30(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90420,90422,90424], animationEffect=False) # ,90426,90428

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection31(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90421,90423,90425], animationEffect=False) # ,90427,90429

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection40(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90430,90432,90434], animationEffect=False) # ,90436,90438

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection41(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90431,90433,90435], animationEffect=False) # ,90437,90439

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection50(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90440,90442,90444], animationEffect=False) # ,90446,90448

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection51(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90441,90443,90445], animationEffect=False) # ,90447,90449

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class SecondWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=30):
            return SecondWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay4000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay5000(self.ctx)


class SecondWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class ThirdWaveStart(trigger_api.Trigger):
    def on_enter(self):
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
    def on_enter(self):
        self.create_monster(spawnIds=[90400,90402,90404], animationEffect=False) # ,90406,90408

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90401,90403,90405], animationEffect=False) # ,90407,90409

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection20(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90410,90412,90414], animationEffect=False) # ,90416,90418

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90411,90413,90415], animationEffect=False) # ,90417,90419

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection30(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90420,90422,90424], animationEffect=False) # ,90426,90428

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90421,90423,90425], animationEffect=False) # ,90427,90429

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection40(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90430,90432,90434], animationEffect=False) # ,90436,90438

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90431,90433,90435], animationEffect=False) # ,90437,90439

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection50(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90440,90442,90444], animationEffect=False) # ,90446,90448

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90441,90443,90445], animationEffect=False) # ,90447,90449

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class ThirdWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=30):
            return ThirdWaveDelay2000(self.ctx)
        if self.random_condition(rate=30):
            return ThirdWaveDelay3000(self.ctx)
        if self.random_condition(rate=30):
            return ThirdWaveDelay4000(self.ctx)


class ThirdWaveDelay2000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=4)

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
    def on_enter(self):
        self.create_monster(spawnIds=[90400,90402,90404], animationEffect=False) # ,90406,90408

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90401,90403,90405], animationEffect=False) # ,90407,90409

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection20(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90410,90412,90414], animationEffect=False) # ,90416,90418

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90411,90413,90415], animationEffect=False) # ,90417,90419

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection30(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90420,90422,90424], animationEffect=False) # ,90426,90428

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90421,90423,90425], animationEffect=False) # ,90427,90429

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection40(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90430,90432,90434], animationEffect=False) # ,90436,90438

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90431,90433,90435], animationEffect=False) # ,90437,90439

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection50(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90440,90442,90444], animationEffect=False) # ,90446,90448

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90441,90443,90445], animationEffect=False) # ,90447,90449

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 추가 웨이브 경험치 없음
class FifthWaveStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90490,90492,90494], animationEffect=False) # ,90496,90498

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90491,90493,90495], animationEffect=False) # ,90497,90499

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 웨이브 종료
class DefenceSucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[90400,90401,90402,90403,90404,90405,90406,90407,90408,90410,90410,90411,90412,90413,90414,90415,90416,90417,90418,90419,90420,90421,90422,90423,90424,90425,90426,90427,90428,90429,90430,90431,90432,90433,90434,90435,90436,90437,90438,90439,90440,90441,90442,90443,90444,90445,90446,90447,90448,90449,90480,90481,90482,90483,90484,90485,90486,90487,90488,90489,90490,90491,90492,90493,90494,90495,90496,90497,90498,90499]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=False) # 04Round_ShadowApp
        self.set_user_value(triggerId=4, key='04RoundSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=804, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1004]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1104], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$02000378_BF__904_MOBWAVE_04ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1104, script='$02000378_BF__904_MOBWAVE_04ROUND__2$', arg4=4, arg5=4) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return NpcDownPenaltyEnd(self.ctx)


class NpcDownPenaltyEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PenaltyFinish', value=1):
            return ReturnToWave(self.ctx)


class ReturnToWave(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$02000378_BF__904_MOBWAVE_04ROUND__3$', arg3='4000', arg4='0')
        self.destroy_monster(spawnIds=[1104]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1004], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1104)

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
