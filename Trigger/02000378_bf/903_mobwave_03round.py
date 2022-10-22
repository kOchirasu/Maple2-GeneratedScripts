""" trigger/02000378_bf/903_mobwave_03round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PenaltyFinish', value=0)
        set_user_value(key='WaveTime', value=0) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5103], visible=False) # 03Round_ShadowApp

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
        set_event_ui(type=1, arg2='$02000378_BF__903_MOBWAVE_03ROUND__0$', arg3='6000', arg4='0')
        set_user_value(key='WaveTime', value=1) # 웨이브 진행 순서 기억
        set_effect(triggerIds=[5103], visible=True) # 03Round_ShadowApp
        create_monster(spawnIds=[90300,90302,90304], arg2=False) # ,90306,90308

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstWaveDelayRandom()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FirstWaveDelayRandom(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90301,90303,90305], arg2=False) # ,90307,90309

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
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FirstWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FirstWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondWaveStart()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class SecondWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=2) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90310,90312,90314], arg2=False) # ,90316,90318

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondWaveDelayRandom()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class SecondWaveDelayRandom(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90311,90313,90315], arg2=False) # ,90317,90319

    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return SecondWaveDelay3000()
        if random_condition(rate=30):
            return SecondWaveDelay4000()
        if random_condition(rate=30):
            return SecondWaveDelay5000()


class SecondWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class SecondWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class SecondWaveDelay5000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ThirdWaveStart()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  방향 랜덤 
class ThirdWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=3) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if true():
            return ThirdWaveDirectionRandom()


class ThirdWaveDirectionRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return ThirdWaveDirection10()
        if random_condition(rate=20):
            return ThirdWaveDirection20()
        if random_condition(rate=20):
            return ThirdWaveDirection30()
        if random_condition(rate=20):
            return ThirdWaveDirection40()
        if random_condition(rate=20):
            return ThirdWaveDirection50()
        if random_condition(rate=20):
            return ThirdWaveDirection60()


#  왼쪽 위 
class ThirdWaveDirection10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90320,90322,90324], arg2=False) # ,90326,90328

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection11()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90321,90323,90325], arg2=False) # ,90327,90329

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  오른쪽 위 
class ThirdWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90330,90332,90334], arg2=False) # ,90336,90338

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection21()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90331,90333,90335], arg2=False) # ,90337,90339

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  왼쪽 중앙 
class ThirdWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90340,90342,90344], arg2=False) # ,90346,90348

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection31()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90341,90343,90345], arg2=False) # ,90347,90349

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  오른쪽 중앙 
class ThirdWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90350,90352,90354], arg2=False) # ,90356,90358

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection41()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90351,90353,90355], arg2=False) # ,90357,90359

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  왼쪽 아래 
class ThirdWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90360,90362,90364], arg2=False) # ,90366,90368

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection51()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90361,90363,90365], arg2=False) # ,90367,90369

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  오른쪽 아래 
class ThirdWaveDirection60(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90370,90372,90374], arg2=False) # ,90376,90378

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDirection61()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDirection61(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90371,90373,90375], arg2=False) # ,90377,90379

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ThirdWaveDelayRandom()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDelayRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=30):
            return ThirdWaveDelay3000()
        if random_condition(rate=30):
            return ThirdWaveDelay4000()
        if random_condition(rate=30):
            return ThirdWaveDelay2000()


class ThirdWaveDelay3000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay4000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class ThirdWaveDelay2000(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return FourthWaveStart()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FourthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=4) # 웨이브 진행 순서 기억

    def on_tick(self) -> state.State:
        if true():
            return FourthWaveDirectionRandom()


class FourthWaveDirectionRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return FourthWaveDirection10()
        if random_condition(rate=20):
            return FourthWaveDirection20()
        if random_condition(rate=20):
            return FourthWaveDirection30()
        if random_condition(rate=20):
            return FourthWaveDirection40()
        if random_condition(rate=20):
            return FourthWaveDirection50()
        if random_condition(rate=20):
            return FourthWaveDirection60()


#  왼쪽 위 
class FourthWaveDirection10(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90320,90322,90324], arg2=False) # ,90326,90328

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection11()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FourthWaveDirection11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90321,90323,90325], arg2=False) # ,90327,90329

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  오른쪽 위 
class FourthWaveDirection20(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90330,90332,90334], arg2=False) # ,90336,90338

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection21()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FourthWaveDirection21(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90331,90333,90335], arg2=False) # ,90337,90339

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  왼쪽 중앙 
class FourthWaveDirection30(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90340,90342,90344], arg2=False) # ,90346,90348

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection31()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FourthWaveDirection31(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90341,90343,90345], arg2=False) # ,90347,90349

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  오른쪽 중앙 
class FourthWaveDirection40(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90350,90352,90354], arg2=False) # ,90356,90358

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection41()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FourthWaveDirection41(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90351,90353,90355], arg2=False) # ,90357,90359

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  왼쪽 아래 
class FourthWaveDirection50(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90360,90362,90364], arg2=False) # ,90366,90368

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection51()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FourthWaveDirection51(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90361,90363,90365], arg2=False) # ,90367,90369

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


#  오른쪽 아래 
class FourthWaveDirection60(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90370,90372,90374], arg2=False) # ,90376,90378

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDirection61()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FourthWaveDirection61(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90371,90373,90375], arg2=False) # ,90377,90379

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthWaveDelay()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class FourthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90320,90322,90324], arg2=False) # ,90326,90328

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class SixthWaveStart(state.State):
    def on_enter(self):
        set_user_value(key='WaveTime', value=6) # 웨이브 진행 순서 기억
        create_monster(spawnIds=[90390,90392,90394,90396,90398], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SixthWaveDelay()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class SixthWaveDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[90391,90393,90395], arg2=False) # ,90397,90399

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return DefenceSucess01()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class DefenceSucess01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[90300,90301,90302,90303,90304,90305,90306,90307,90308,90309,90310,90311,90312,90313,90314,90315,90316,90317,90318,90319,90320,90321,90322,90323,90324,90325,90326,90327,90328,90329,90330,90331,90332,90333,90334,90335,90336,90337,90338,90339,90340,90341,90342,90343,90344,90345,90346,90347,90348,90349,90350,90351,90352,90353,90354,90355,90356,90357,90358,90359,90360,90361,90362,90363,90364,90365,90366,90367,90368,90369,90370,90371,90372,90373,90374,90375,90376,90377,90378,90379,90380,90381,90382,90383,90384,90385,90386,90387,90388,90389,90390,90391,90392,90393,90394,90395,90396,90397,90398,90399]):
            return DefenceSucess02()
        if monster_dead(boxIds=[1003]):
            return NpcDownPenaltyStart()


class DefenceSucess02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5103], visible=False) # 03Round_ShadowApp
        set_user_value(triggerId=3, key='03RoundSuccess', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


#  패널티 10초 
class NpcDownPenaltyStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=803, key='PenaltyMob', value=1)
        destroy_monster(spawnIds=[1003]) # 수호대상 틴차이
        create_monster(spawnIds=[1103], arg2=False) # 쓰러진 틴차이
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$02000378_BF__903_MOBWAVE_03ROUND__1$', arg3='4000', arg4='0')
        set_conversation(type=1, spawnId=1103, script='$02000378_BF__903_MOBWAVE_03ROUND__2$', arg4=4, arg5=4) # 틴차이

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
        set_event_ui(type=1, arg2='$02000378_BF__903_MOBWAVE_03ROUND__3$', arg3='4000', arg4='0')
        destroy_monster(spawnIds=[1103]) # 쓰러진 틴차이
        create_monster(spawnIds=[1003], arg2=False) # 수호대상 틴차이
        remove_balloon_talk(spawnId=1103)

    def on_tick(self) -> state.State:
        if user_value(key='WaveTime', value=1):
            return SecondWaveStart()
        if user_value(key='WaveTime', value=2):
            return ThirdWaveStart()
        if user_value(key='WaveTime', value=3):
            return FourthWaveStart()
        if user_value(key='WaveTime', value=4):
            return SixthWaveStart()
        """
        <condition name="UserValue" key="WaveTime" value="5" >         
            <transition state="6thWaveStart"/>    
        </condition>
        """
        if user_value(key='WaveTime', value=6):
            return SixthWaveStart()


class Quit(state.State):
    pass


