""" trigger/52000052_qd/901_mobwave_01round.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PenaltyFinish', value=0)
        self.set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5101], visible=False) # 01Round_ShadowApp

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
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__0$', arg3='6000', arg4='0')
        self.set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        self.set_effect(triggerIds=[5101], visible=True) # 01Round_ShadowApp
        self.create_monster(spawnIds=[90100,90102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90105,90107,90109], animationEffect=False)

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
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class FirstWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return SecondWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90116,90118], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondWaveDelayRandom(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelayRandom(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90113,90115,90117], animationEffect=False)

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
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay4000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class SecondWaveDelay5000(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ThirdWaveStart(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90124,90126], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ThirdWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class ThirdWaveDelay(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90121,90125,90129], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        self.create_monster(spawnIds=[90192,90196], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FifthWaveDelay(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class FifthWaveDelay(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[90195,90197,90199], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return DefenceSucess01(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[90100,90101,90102,90103,90104,90105,90106,90107,90108,90109,90110,90111,90112,90113,90114,90115,90116,90117,90118,90119,90120,90121,90122,90123,90124,90125,90126,90127,90128,90129,90130,90131,90132,90133,90134,90135,90136,90137,90138,90139,90180,90181,90182,90183,90184,90185,90186,90187,90188,90189,90190,90191,90192,90193,90194,90195,90196,90197,90198,90199]):
            return DefenceSucess02(self.ctx)
        if self.monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart(self.ctx)


class DefenceSucess02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False) # 01Round_ShadowApp
        self.set_user_value(triggerId=1, key='01RoundSuccess', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 패널티 10초
class NpcDownPenaltyStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=801, key='PenaltyMob', value=1)
        self.destroy_monster(spawnIds=[1001]) # 수호대상 틴차이
        self.create_monster(spawnIds=[1101], animationEffect=False) # 쓰러진 틴차이
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        self.set_conversation(type=1, spawnId=1101, script='$52000052_QD__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        self.set_event_ui(type=1, arg2='$52000052_QD__901_MOBWAVE_01ROUND__3$', arg3='4000', arg4='0')
        self.destroy_monster(spawnIds=[1101]) # 쓰러진 틴차이
        self.create_monster(spawnIds=[1001], animationEffect=False) # 수호대상 틴차이
        self.remove_balloon_talk(spawnId=1101)

    def on_tick(self) -> trigger_api.Trigger:
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


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
