""" trigger/52000052_qd/906_mobwave_06round.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5106], visible=False) # 06Round_ShadowApp

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
        self.set_effect(triggerIds=[5106], visible=True) # 06Round_ShadowApp

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
        self.create_monster(spawnIds=[90600,90602,90604,90606,90608], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90601,90603,90605,90607,90609], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90610,90612,90614,90616,90618], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90611,90613,90615,90617,90619], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90620,90622,90624,90626,90628], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90621,90623,90625,90627,90629], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90630,90632,90634,90636,90638], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90631,90633,90635,90637,90639], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90640,90642,90644,90646,90648], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90641,90643,90645,90647,90649], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class FirstWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return FirstWaveDelay7000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay8000(self.ctx)
        if self.random_condition(rate=30):
            return FirstWaveDelay9000(self.ctx)


class FirstWaveDelay7000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay8000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay9000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirectionRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
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
        self.create_monster(spawnIds=[90600,90602,90604,90606,90608], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90601,90603,90605,90607,90609], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90610,90612,90614,90616,90618], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90611,90613,90615,90617,90619], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90620,90622,90624,90626,90628], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90621,90623,90625,90627,90629], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90630,90632,90634,90636,90638], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90631,90633,90635,90637,90639], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90640,90642,90644,90646,90648], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90641,90643,90645,90647,90649], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


# 딜레이 랜덤
class SecondWaveDelayRandom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=30):
            return SecondWaveDelay5000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay6000(self.ctx)
        if self.random_condition(rate=30):
            return SecondWaveDelay7000(self.ctx)


class SecondWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay6000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay7000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1006]):
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
        self.create_monster(spawnIds=[90600,90602,90604,90606,90608], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90601,90603,90605,90607,90609], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90610,90612,90614,90616,90618], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90611,90613,90615,90617,90619], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90620,90622,90624,90626,90628], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90621,90623,90625,90627,90629], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90630,90632,90634,90636,90638], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90631,90633,90635,90637,90639], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90640,90642,90644,90646,90648], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90641,90643,90645,90647,90649], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1006]):
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
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay5000(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1006]):
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
        self.create_monster(spawnIds=[90600,90602,90604,90606,90608], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90601,90603,90605,90607,90609], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection20(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90610,90612,90614,90616,90618], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90611,90613,90615,90617,90619], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection30(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90620,90622,90624,90626,90628], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90621,90623,90625,90627,90629], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection40(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90630,90632,90634,90636,90638], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90631,90633,90635,90637,90639], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection50(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90640,90642,90644,90646,90648], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90641,90643,90645,90647,90649], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


# 추가 웨이브 경험치 없음
class FifthWaveStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90690,90692,90694,90696,90698], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90691,90693,90695,90697,90699], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


# 웨이브 종료
class DefenceSucess01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[90600,90601,90602,90603,90604,90605,90606,90607,90608,90610,90610,90611,90612,90613,90614,90615,90616,90617,90618,90619,90620,90621,90622,90623,90624,90625,90626,90627,90628,90629,90630,90631,90632,90633,90634,90635,90636,90637,90638,90639,90640,90641,90642,90643,90644,90645,90646,90647,90648,90649,90680,90681,90682,90683,90684,90685,90686,90687,90688,90689,90690,90691,90692,90693,90694,90695,90696,90697,90698,90699]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1006]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5106], visible=False) # 06Round_ShadowApp
        self.set_user_value(triggerId=6, key='06RoundSuccess', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=806, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1006]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1106], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1106, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        self.destroy_monster(spawnIds=[1106]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1006], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1106)

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
