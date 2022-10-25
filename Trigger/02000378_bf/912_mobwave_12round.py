""" trigger/02000378_bf/912_mobwave_12round.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5112], visible=False) # 12Round_ShadowApp

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
        self.set_event_ui(type=1, arg2='$02000378_BF__912_MOBWAVE_12ROUND__0$', arg3='6000', arg4='0')
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5112], visible=True) # 12Round_ShadowApp
        self.create_monster(spawnIds=[91200,91202,91204], animationEffect=False) # ,91206,91208

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelayRandom(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91201,91203,91205], animationEffect=False) # ,91207,91209

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
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=712, key='TotemApp', value=1)
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[91210,91212,91214], animationEffect=False) # ,91216,91218

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelayRandom(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91211,91213,91215], animationEffect=False) # ,91217,91219

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
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1012]):
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
        if self.random_condition(rate=20):
            return ThirdWaveDirection60(self.ctx)


# 왼쪽 위
class ThirdWaveDirection10(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91220,91222,91224], animationEffect=False) # ,91226,91228

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91221,91223,91225], animationEffect=False) # ,91227,91229

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class ThirdWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91230,91232,91234], animationEffect=False) # ,91236,91238

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91231,91233,91235], animationEffect=False) # ,91237,91239

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class ThirdWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91240,91242,91244], animationEffect=False) # ,91246,91248

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91241,91243,91245], animationEffect=False) # ,91247,91249

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class ThirdWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91250,91252,91254], animationEffect=False) # ,91256,91258

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91251,91253,91255], animationEffect=False) # ,91257,91259

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class ThirdWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91260,91262,91264], animationEffect=False) # ,91266,91268

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91261,91263,91265], animationEffect=False) # ,91267,91269

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class ThirdWaveDirection60(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91270,91272,91274], animationEffect=False) # ,91276,91278

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection61(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection61(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91271,91273,91275], animationEffect=False) # ,91277,91279

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1012]):
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
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1012]):
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
        self.create_monster(spawnIds=[91220,91222,91224], animationEffect=False) # ,91226,91228

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91221,91223,91225], animationEffect=False) # ,91227,91229

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class FourthWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91230,91232,91234], animationEffect=False) # ,91236,91238

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91231,91233,91235], animationEffect=False) # ,91237,91239

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class FourthWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91240,91242,91244], animationEffect=False) # ,91246,91248

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91241,91243,91245], animationEffect=False) # ,91247,91249

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class FourthWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91250,91252,91254], animationEffect=False) # ,91256,91258

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91251,91253,91255], animationEffect=False) # ,91257,91259

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class FourthWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91260,91262,91264], animationEffect=False) # ,91266,91268

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91261,91263,91265], animationEffect=False) # ,91267,91269

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class FourthWaveDirection60(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91270,91272,91274], animationEffect=False) # ,91276,91278

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection61(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection61(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91271,91273,91275], animationEffect=False) # ,91277,91279

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91271,91273,91275], animationEffect=False) # ,91277,91279

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


# 추가 웨이브 경험치 없음
class SeventhWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=7) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[91290,91292,91294], animationEffect=False) # ,91296,91298

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SeventhWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class SeventhWaveDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[91291,91293,91295], animationEffect=False) # ,91297,91299

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[91200,91201,91202,91203,91204,91205,91206,91207,91208,91209,91210,91211,91212,91213,91214,91215,91216,91217,91218,91219,91220,91221,91222,91223,91224,91225,91226,91227,91228,91229,91230,91231,91232,91233,91234,91235,91236,91237,91238,91239,91240,91241,91242,91243,91244,91245,91246,91247,91248,91249,91250,91251,91252,91253,91254,91255,91256,91257,91258,91259,91260,91261,91262,91263,91264,91265,91266,91267,91268,91269,91270,91271,91272,91273,91274,91275,91276,91277,91278,91279,91280,91281,91282,91283,91284,91285,91286,91287,91288,91289,91290,91291,91292,91293,91294,91295,91296,91297,91298,91299]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5112], visible=False) # 12Round_ShadowApp
        self.set_user_value(triggerId=12, key='12RoundSuccess', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=812, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1012]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1112], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$02000378_BF__912_MOBWAVE_12ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1112, script='$02000378_BF__912_MOBWAVE_12ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        self.set_event_ui(type=1, arg2='$02000378_BF__912_MOBWAVE_12ROUND__3$', arg3='4000', arg4='0')
        self.destroy_monster(spawnIds=[1112]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1012], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1112)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='WaveTime', value=1):
            return SecondWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=2):
            return ThirdWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=3):
            return FourthWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=4):
            return SeventhWaveStart(self.ctx)
        """
        <condition name="UserValue" key="WaveTime" value="5" >         
            <transition state="6thWaveStart"/>    
        </condition>         
            <condition name="UserValue" key="WaveTime" value="6" >         
            <transition state="7thWaveStart"/>    
        </condition>
        """
        if self.user_value(key='WaveTime', value=7):
            return SeventhWaveStart(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
