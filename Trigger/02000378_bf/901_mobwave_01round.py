""" trigger/02000378_bf/901_mobwave_01round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5101], visible=False) # 01Round_ShadowApp

    def on_tick(self) -> state.State:
        if user_value(key='MobWaveStart', value=1):
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveStart()


class FirstWaveStart(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__901_MOBWAVE_01ROUND__0$', arg3='6000', arg4='0')
        set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5101], visible=True) # 01Round_ShadowApp
        create_monster(spawnIds=[90100,90102,90104], arg2=False) # ,90106,90108

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class FirstWaveDelayRandom(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90101,90103,90105], arg2=False) # 90107,90109

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return FirstWaveDelay3000()
        if random_condition(rate=30):
            return FirstWaveDelay4000()
        if random_condition(rate=30):
            return FirstWaveDelay5000()


class FirstWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class FirstWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class FirstWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class SecondWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90110,90112,90114], arg2=False) # ,90116,90118

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class SecondWaveDelayRandom(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90111,90113,90115], arg2=False) # ,90117,90119

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return SecondWaveDelay2000()
        if random_condition(rate=30):
            return SecondWaveDelay3000()
        if random_condition(rate=30):
            return SecondWaveDelay4000()


class SecondWaveDelay2000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class SecondWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class SecondWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class ThirdWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90120,90122,90124], arg2=False) # ,90126,90128

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelay()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90131,90133,90135], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class FifthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=5) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90190,90192,90194], arg2=False) # ,90196,90198

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FifthWaveDelay()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class FifthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90191,90193,90195], arg2=False) # ,90197,90199

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class DefenceSucess01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90100,90101,90102,90103,90104,90105,90106,90107,90108,90109,90110,90111,90112,90113,90114,90115,90116,90117,90118,90119,90120,90121,90122,90123,90124,90125,90126,90127,90128,90129,90130,90131,90132,90133,90134,90135,90136,90137,90138,90139,90180,90181,90182,90183,90184,90185,90186,90187,90188,90189,90190,90191,90192,90193,90194,90195,90196,90197,90198,90199]):
            return DefenceSucess02()
        if monster_dead(boxIds=[1001]):
            return NpcDownPenaltyStart()


class DefenceSucess02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # 01Round_ShadowApp
        set_user_value(triggerId=1, key='01RoundSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  패널티 10초 
class NpcDownPenaltyStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=801, key='PenaltyMob', value=1)
        destroy_monster(spawnIds=[1001]) # 수호대상 틴차이
        create_monster(spawnIds=[1101], arg2=False) # 쓰러진 틴차이
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__901_MOBWAVE_01ROUND__1$', arg3='4000', arg4='0')
        set_conversation(type=1, spawnId=1101, script='$02000378_BF__901_MOBWAVE_01ROUND__2$', arg4=4, arg5=4) # 틴차이

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return NpcDownPenaltyEnd()


class NpcDownPenaltyEnd(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='PenaltyFinish', value=1):
            return ReturnToWave()


class ReturnToWave(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__901_MOBWAVE_01ROUND__3$', arg3='4000', arg4='0')
        destroy_monster(spawnIds=[1101]) # 쓰러진 틴차이
        create_monster(spawnIds=[1001], arg2=False) # 수호대상 틴차이
        remove_balloon_talk(spawnId=1101)

    def on_tick(self) -> state.State:
        if user_value(key='WaveTime', value=1):
            return SecondWaveStart()
        if user_value(key='WaveTime', value=2):
            return ThirdWaveStart()
        if user_value(key='WaveTime', value=3):
            return FifthWaveStart()
        """
        <condition name="UserValue" key="WaveTime" value="4" >         
            <transition state="5thWaveStart"/>    
        </condition>
        """
        if user_value(key='WaveTime', value=5):
            return FifthWaveStart()


class Quit(state.State):
    pass


