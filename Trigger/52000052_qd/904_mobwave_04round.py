""" trigger/52000052_qd/904_mobwave_04round.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5104], visible=False) # 04Round_ShadowApp

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
        self.set_effect(triggerIds=[5104], visible=True) # 04Round_ShadowApp

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
        self.create_monster(spawnIds=[90400,90402,90404,90406,90408], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90401,90403,90405,90407,90409], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90410,90412,90414,90416,90418], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90411,90413,90415,90417,90419], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90420,90422,90424,90426,90428], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90421,90423,90425,90427,90429], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90430,90432,90434,90436,90438], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90431,90433,90435,90437,90439], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90440,90442,90444,90446,90448], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90441,90443,90445,90447,90449], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class FirstWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return FirstWaveDelay5000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay6000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay7000(self.ctx)


class FirstWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay6000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay7000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
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
        self.create_monster(spawnIds=[90400,90402,90404,90406,90408], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90401,90403,90405,90407,90409], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90410,90412,90414,90416,90418], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90411,90413,90415,90417,90419], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90420,90422,90424,90426,90428], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90421,90423,90425,90427,90429], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90430,90432,90434,90436,90438], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90431,90433,90435,90437,90439], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90440,90442,90444,90446,90448], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90441,90443,90445,90447,90449], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1004]):
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
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay6000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1004]):
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
        self.create_monster(spawnIds=[90400,90402,90404,90406,90408], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90401,90403,90405,90407,90409], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90410,90412,90414,90416,90418], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90411,90413,90415,90417,90419], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90420,90422,90424,90426,90428], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90421,90423,90425,90427,90429], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90430,90432,90434,90436,90438], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90431,90433,90435,90437,90439], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90440,90442,90444,90446,90448], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90441,90443,90445,90447,90449], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90447,90437,90427], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 추가 웨이브 경험치 없음
class FifthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90490,90492,90494,90496,90498], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90491,90493,90495,90497,90499], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


# 웨이브 종료
class DefenceSucess01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[90400,90401,90402,90403,90404,90405,90406,90407,90408,90410,90410,90411,90412,90413,90414,90415,90416,90417,90418,90419,90420,90421,90422,90423,90424,90425,90426,90427,90428,90429,90430,90431,90432,90433,90434,90435,90436,90437,90438,90439,90440,90441,90442,90443,90444,90445,90446,90447,90448,90449,90480,90481,90482,90483,90484,90485,90486,90487,90488,90489,90490,90491,90492,90493,90494,90495,90496,90497,90498,90499]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1004]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=False) # 04Round_ShadowApp
        self.set_user_value(triggerId=4, key='04RoundSuccess', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=804, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1004]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1104], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1104, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        self.destroy_monster(spawnIds=[1104]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1004], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1104)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='WaveTime', value=1):
            return SecondWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=2):
            return ThirdWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=3):
            return FifthWaveStart(self.ctx)
        """
        <condition name="UserValue" key="WaveTime" value="4" >         
            <transition state="5thWaveStart"/>    
        </condition>
        """
        if self.user_value(key='WaveTime', value=5):
            return FifthWaveStart(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
