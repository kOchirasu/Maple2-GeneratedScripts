""" trigger/52000052_qd/902_mobwave_02round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(trigger_ids=[5102], visible=False) # 02Round_ShadowApp

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobWaveStart', value=1):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveStart(self.ctx)


class FirstWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__0$', arg3='6000', arg4='0')
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(trigger_ids=[5102], visible=True) # 02Round_ShadowApp
        self.spawn_monster(spawn_ids=[90200,90202], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90205,90207,90209], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30):
            return FirstWaveDelay3000(self.ctx)
        if self.random_condition(weight=30):
            return FirstWaveDelay4000(self.ctx)
        if self.random_condition(weight=30):
            return FirstWaveDelay5000(self.ctx)


class FirstWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        self.spawn_monster(spawn_ids=[90212,90214], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90213,90215,90217], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30):
            return SecondWaveDelay3000(self.ctx)
        if self.random_condition(weight=30):
            return SecondWaveDelay4000(self.ctx)
        if self.random_condition(weight=30):
            return SecondWaveDelay5000(self.ctx)


class SecondWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 방향 랜덤
class ThirdWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=702, key='TotemApp', value=1)
        self.set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        return ThirdWaveDirectionRandom(self.ctx)


class ThirdWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20):
            return ThirdWaveDirection10(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection20(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection30(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection40(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection50(self.ctx)
        if self.random_condition(weight=20):
            return ThirdWaveDirection60(self.ctx)


# 왼쪽 위
class ThirdWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90222,90224], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90221,90223,90227], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class ThirdWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90232,90238], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90231,90233,90237], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class ThirdWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90246,90248], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90241,90243,90245], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class ThirdWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90250,90258], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90253,90255,90259], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class ThirdWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90262,90266], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90263,90265,90269], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class ThirdWaveDirection60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90270,90272], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDirection61(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDirection61(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90271,90277,90279], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ThirdWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30):
            return ThirdWaveDelay3000(self.ctx)
        if self.random_condition(weight=30):
            return ThirdWaveDelay4000(self.ctx)
        if self.random_condition(weight=30):
            return ThirdWaveDelay5000(self.ctx)


class ThirdWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return FourthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=4) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        return FourthWaveDirectionRandom(self.ctx)


class FourthWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20):
            return FourthWaveDirection10(self.ctx)
        if self.random_condition(weight=20):
            return FourthWaveDirection20(self.ctx)
        if self.random_condition(weight=20):
            return FourthWaveDirection30(self.ctx)
        if self.random_condition(weight=20):
            return FourthWaveDirection40(self.ctx)
        if self.random_condition(weight=20):
            return FourthWaveDirection50(self.ctx)
        if self.random_condition(weight=20):
            return FourthWaveDirection60(self.ctx)


# 왼쪽 위
class FourthWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90222,90224], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90221,90225,90227], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class FourthWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90232,90238], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90231,90233,90237], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class FourthWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90246,90248], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90241,90243,90245], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class FourthWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90250,90258], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90253,90255,90257], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class FourthWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90262,90266], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90263,90267,90269], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class FourthWaveDirection60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90270,90272], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDirection61(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDirection61(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90271,90277,90279], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FourthWaveDelayRandom(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDelayRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=30):
            return FourthWaveDelay3000(self.ctx)
        if self.random_condition(weight=30):
            return FourthWaveDelay4000(self.ctx)
        if self.random_condition(weight=30):
            return FourthWaveDelay2000(self.ctx)


class FourthWaveDelay3000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FourthWaveDelay2000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return FifthWaveStart(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억

    def on_tick(self) -> trigger_api.Trigger:
        return FifthWaveDirectionRandom(self.ctx)


class FifthWaveDirectionRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=20):
            return FifthWaveDirection10(self.ctx)
        if self.random_condition(weight=20):
            return FifthWaveDirection20(self.ctx)
        if self.random_condition(weight=20):
            return FifthWaveDirection30(self.ctx)
        if self.random_condition(weight=20):
            return FifthWaveDirection40(self.ctx)
        if self.random_condition(weight=20):
            return FifthWaveDirection50(self.ctx)
        if self.random_condition(weight=20):
            return FifthWaveDirection60(self.ctx)


# 왼쪽 위
class FifthWaveDirection10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90222,90224], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection11(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90221,90223,90227], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 위
class FifthWaveDirection20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90232,90238], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection21(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90233,90237,90239], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 중앙
class FifthWaveDirection30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90246,90248], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection31(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90241,90243,90247], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 중앙
class FifthWaveDirection40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90250,90258], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection41(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection41(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90253,90255,90259], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 왼쪽 아래
class FifthWaveDirection50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90262,90266], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection51(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection51(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90263,90267,90269], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


# 오른쪽 아래
class FifthWaveDirection60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90270,90272], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return FifthWaveDirection61(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDirection61(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90275,90277,90279], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SixthWaveStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='WaveTime', value=6) # 웨이브 진행 순서 기억
        self.spawn_monster(spawn_ids=[90290,90292], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return SixthWaveDelay(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class SixthWaveDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[90295,90297,90299], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[90200,90201,90202,90203,90204,90205,90206,90207,90208,90209,90210,90211,90212,90213,90214,90215,90216,90217,90218,90219,90220,90221,90222,90223,90224,90225,90226,90227,90228,90229,90230,90231,90232,90233,90234,90235,90236,90237,90238,90239,90240,90241,90242,90243,90244,90245,90246,90247,90248,90249,90250,90251,90252,90253,90254,90255,90256,90257,90258,90259,90260,90261,90262,90263,90264,90265,90266,90267,90268,90269,90270,90271,90272,90273,90274,90275,90276,90277,90278,90279,90280,90281,90282,90283,90284,90285,90286,90287,90288,90289,90290,90291,90292,90293,90294,90295,90296,90297,90298,90299]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(spawn_ids=[1002]):
            # 수호대상 틴차이
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=False) # 02Round_ShadowApp
        self.set_user_value(trigger_id=2, key='02RoundSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=802, key='PenaltyMob', value=1)
        self.destroy_monster(spawn_ids=[1002]) # 수호대상 틴차이
        self.spawn_monster(spawn_ids=[1102], auto_target=False) # 쓰러진 틴차이
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        self.set_dialogue(type=1, spawn_id=1102, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', time=4, arg5=4) # 틴차이

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return NpcDownPenaltyEnd(self.ctx)


class NpcDownPenaltyEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PenaltyFinish', value=1):
            return ReturnToWave(self.ctx)


class ReturnToWave(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_effect(trigger_ids=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__3$', arg3='4000', arg4='0')
        self.destroy_monster(spawn_ids=[1102]) # 쓰러진 틴차이
        self.spawn_monster(spawn_ids=[1002], auto_target=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawn_id=1102)

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
            return SixthWaveStart(self.ctx)
        if self.user_value(key='WaveTime', value=6):
            return SixthWaveStart(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
