""" trigger/02000331_bf/seeker01.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[11000], visible=False) # 입구로 되돌아 가는 길 막기
        self.set_agent(triggerIds=[11001], visible=False) # 입구로 되돌아 가는 길 막기
        self.set_agent(triggerIds=[13001], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(triggerIds=[13002], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(triggerIds=[13003], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(triggerIds=[13004], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(triggerIds=[13005], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(triggerIds=[13006], visible=True) # 두번째 전투 전에 몬스터 길  막기
        self.set_agent(triggerIds=[15000], visible=False) # 끊어진 다리 길 막기
        self.set_agent(triggerIds=[15001], visible=False) # 끊어진 다리 길 막기
        self.set_agent(triggerIds=[15002], visible=False) # 끊어진 다리 길 막기
        self.set_agent(triggerIds=[16000], visible=False) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16001], visible=False) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16002], visible=False) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16003], visible=False) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16004], visible=False) # 새로운 다리 길 막기
        self.set_mesh(triggerIds=[90000], visible=False, arg3=0, delay=0, scale=0) # 1st barrier ON
        self.set_mesh(triggerIds=[90001], visible=False, arg3=0, delay=0, scale=0) # 2st barrier OFF
        self.set_mesh(triggerIds=[90002], visible=True, arg3=0, delay=0, scale=0) # 3rd barrier ON
        self.set_mesh(triggerIds=[90003], visible=True, arg3=0, delay=0, scale=0) # 4th barrier ON
        self.set_mesh(triggerIds=[90004], visible=True, arg3=0, delay=0, scale=0) # 5th barrier ON
        self.set_mesh(triggerIds=[90005], visible=True, arg3=0, delay=0, scale=0) # 6th barrier ON
        self.set_mesh(triggerIds=[90006], visible=True, arg3=0, delay=0, scale=0) # 7th barrier ON
        self.set_mesh(triggerIds=[90007], visible=True, arg3=0, delay=0, scale=0) # 8th barrier ON
        self.set_mesh(triggerIds=[90008], visible=True, arg3=0, delay=0, scale=0) # 9th barrier ON
        self.set_mesh(triggerIds=[98880], visible=True, arg3=0, delay=0, scale=0) # 마지막꼬마 CAGE 메시 켜기
        self.set_actor(triggerId=4000, visible=True, initialSequence='Closed') # EnterDoor
        self.set_mesh(triggerIds=[89999], visible=True, arg3=0, delay=0, scale=0) # EnterDoorInvisibleBlock
        self.set_actor(triggerId=92220, visible=True, initialSequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(triggerId=92221, visible=True, initialSequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(triggerId=92222, visible=True, initialSequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(triggerId=92223, visible=True, initialSequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(triggerId=92224, visible=True, initialSequence='Idle_A') # 첫번째장벽 덤불
        self.set_actor(triggerId=93330, visible=True, initialSequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(triggerId=93331, visible=True, initialSequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(triggerId=93332, visible=True, initialSequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(triggerId=93333, visible=True, initialSequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(triggerId=93334, visible=True, initialSequence='Idle_A') # 두번째장벽 덤불
        self.set_actor(triggerId=94440, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94441, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94442, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94443, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94444, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94445, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94446, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94447, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94448, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94449, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94450, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94451, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94452, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94453, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=94454, visible=True, initialSequence='Idle_A') # 세번째장벽 덤불
        self.set_actor(triggerId=96660, visible=True, initialSequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(triggerId=96661, visible=True, initialSequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(triggerId=96662, visible=True, initialSequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(triggerId=96663, visible=True, initialSequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(triggerId=96664, visible=True, initialSequence='Idle_A') # 네번째장벽 덤불
        self.set_actor(triggerId=97770, visible=True, initialSequence='Closed') # 마지막꼬마 CAGE 액터 보여주기
        self.set_mesh(triggerIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016], visible=True, arg3=0, delay=0, scale=0) # 1st bridge ON
        self.set_mesh(triggerIds=[10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,10030,10031,10032,10033], visible=True, arg3=0, delay=0, scale=0) # 2nd bridge ON
        self.set_mesh(triggerIds=[10040,10041,10042,10043,10044], visible=False, arg3=0, delay=0, scale=0) # 3rd bridge OFF
        self.set_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=False, arg3=0, delay=0, scale=0) # 1st 꼬마01 Hint OFF
        self.set_mesh(triggerIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117], visible=False, arg3=0, delay=0, scale=0) # 1st 꼬마02 Hint OFF
        self.set_mesh(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=False, arg3=0, delay=0, scale=0) # 1st 꼬마03 Hint OFF
        self.set_mesh(triggerIds=[2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,2313,2314,2315], visible=False, arg3=0, delay=0, scale=0) # 1st 꼬마04 Hint OFF
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018], visible=False, arg3=0, delay=0, scale=0) # 2nd Hint OFF
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=False, arg3=0, delay=0, scale=0) # 2nd Hint OFF
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=False, arg3=0, delay=0, scale=0) # 2nd Hint OFF
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318], visible=False, arg3=0, delay=0, scale=0) # 2nd Hint OFF
        self.set_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419], visible=False, arg3=0, delay=0, scale=0) # 2nd Hint OFF
        self.set_mesh(triggerIds=[4001,4002,4003,4004,4005,4006,4007,4008], visible=False, arg3=0, delay=0, scale=0) # 3rd Hint OFF
        self.set_mesh(triggerIds=[90090,90091,90092,90093,90094,90095,90096,90097,90098,90099], visible=True, arg3=0, delay=0, scale=0) # 클리어포털감춤
        self.set_interact_object(triggerIds=[10000766], state=2) # 1st 꼬마 랜덤
        self.set_interact_object(triggerIds=[10000767], state=2) # 1st 꼬마 랜덤
        self.set_interact_object(triggerIds=[10000768], state=2) # 1st 꼬마 랜덤
        self.set_interact_object(triggerIds=[10000769], state=2) # 1st 꼬마 랜덤
        self.set_interact_object(triggerIds=[10000771], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(triggerIds=[10000772], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(triggerIds=[10000773], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(triggerIds=[10000774], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(triggerIds=[10000775], state=2) # 2nd 덩굴 랜덤
        self.set_interact_object(triggerIds=[10000784], state=2) # 발판내리기 레버 감춤 랜덤01
        self.set_interact_object(triggerIds=[10000792], state=2) # 발판내리기 레버 감춤 랜덤02
        self.set_interact_object(triggerIds=[10000793], state=2) # 발판내리기 레버 감춤 랜덤03
        self.set_interact_object(triggerIds=[10000794], state=2) # 발판내리기 레버 감춤 랜덤04
        self.set_interact_object(triggerIds=[10000795], state=2) # 발판내리기 레버 감춤 랜덤05
        self.set_interact_object(triggerIds=[10000785], state=2) # 외다리 생성하는 레버 감춤 랜덤01
        self.set_interact_object(triggerIds=[10000796], state=2) # 외다리 생성하는 레버 감춤 랜덤02
        self.set_interact_object(triggerIds=[10000797], state=2) # 외다리 생성하는 레버 감춤 랜덤03
        self.set_interact_object(triggerIds=[10000798], state=2) # 외다리 생성하는 레버 감춤 랜덤04
        self.set_interact_object(triggerIds=[10000799], state=2) # 외다리 생성하는 레버 감춤 랜덤05
        self.set_interact_object(triggerIds=[10000776], state=2) # 열 수 있는 철창 감춤
        self.create_monster(spawnIds=[401], animationEffect=False)
        self.create_monster(spawnIds=[610], animationEffect=False)
        self.set_effect(triggerIds=[99999], visible=False) # 치유 이펙트
        self.set_effect(triggerIds=[7771], visible=False) # UI  메시지 알림 사운드
        self.set_effect(triggerIds=[7772], visible=False) # 치유 스킬 이펙트 사운드
        self.set_effect(triggerIds=[777401], visible=False) # 덤불 제거01 사운드
        self.set_effect(triggerIds=[777402], visible=False) # 덤불 제거02 사운드
        self.set_effect(triggerIds=[777403], visible=False) # 덤불 제거03 사운드
        self.set_effect(triggerIds=[777404], visible=False) # 덤불 제거04 사운드
        self.set_effect(triggerIds=[777405], visible=False) # 덤불 제거05 사운드
        self.set_effect(triggerIds=[777501], visible=False) # 발자국 나타남01 사운드
        self.set_effect(triggerIds=[777502], visible=False) # 발자국 나타남02 사운드
        self.set_effect(triggerIds=[7776], visible=False) # 추격 소음01 사운드
        self.set_effect(triggerIds=[777701], visible=False) # 길 나타남01 사운드 / 첫 번째 다리
        self.set_effect(triggerIds=[777702], visible=False) # 길 나타남02 사운드 / 외다리
        self.set_effect(triggerIds=[777801], visible=False) # 길 없어짐01 사운드  / 첫 번째 다리
        self.set_effect(triggerIds=[777802], visible=False) # 길 없어짐02 사운드 /  외다리
        self.set_effect(triggerIds=[777803], visible=False) # 길 없어짐02 사운드 / 막힌 길
        self.set_effect(triggerIds=[777901], visible=False) # KaseMu Voice01
        self.set_effect(triggerIds=[777902], visible=False) # KaseMu Voice02
        self.set_effect(triggerIds=[777903], visible=False) # KaseMu Voice03
        self.set_effect(triggerIds=[777904], visible=False) # KaseMu Voice04
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[100], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return GateOpen01(self.ctx)


class GateOpen01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=True, initialSequence='Opened') # EnterDoor
        self.set_mesh(triggerIds=[89999], visible=False, arg3=0, delay=0, scale=0) # EnterDoorInvisibleBlock

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 술래말풍선01(self.ctx)


class 술래말풍선01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__0$', arg4=2, arg5=0)
        self.set_mesh(triggerIds=[90000], visible=False, arg3=0, delay=0, scale=0) # 1st barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 술래패트롤01(self.ctx)


class 술래패트롤01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003311, textId=20003311) # 가이드 : 메린이를 따라가 보세요.
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9002, spawnIds=[100]):
            return 몬스터출현01_시작(self.ctx)


class 몬스터출현01_시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=False, initialSequence='Opened') # EnterDoor
        self.hide_guide_summary(entityId=20003311)
        self.create_monster(spawnIds=[900], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현01_연출01(self.ctx)


class 몬스터출현01_연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__1$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[900]):
            return 몬스터출현01_연출02(self.ctx)


class 몬스터출현01_연출02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 몬스터출현01_생성랜덤01(self.ctx)


class 몬스터출현01_생성랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 몬스터출현01_1번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_2번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_3번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_4번생성(self.ctx)


class 몬스터출현01_1번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901,902], animationEffect=False)
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__801$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현01_생성랜덤02(self.ctx)


class 몬스터출현01_2번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[902,904], animationEffect=False)
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__801$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현01_생성랜덤02(self.ctx)


class 몬스터출현01_3번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[903,905], animationEffect=False)
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__801$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현01_생성랜덤02(self.ctx)


class 몬스터출현01_4번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901,905], animationEffect=False)
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__801$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현01_생성랜덤02(self.ctx)


class 몬스터출현01_생성랜덤02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 몬스터출현01_5번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_6번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_7번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_8번생성(self.ctx)


class 몬스터출현01_5번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[905,906,907], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 몬스터출현01_생성랜덤03(self.ctx)


class 몬스터출현01_6번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[906,907,909], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현01_생성랜덤03(self.ctx)


class 몬스터출현01_7번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[907,909,910], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 몬스터출현01_생성랜덤03(self.ctx)


class 몬스터출현01_8번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[907,908,909], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현01_생성랜덤03(self.ctx)


class 몬스터출현01_생성랜덤03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 몬스터출현01_9번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_10번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_11번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현01_12번생성(self.ctx)


class 몬스터출현01_9번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901,902,903], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906,907,908,909,910]):
            return 몬스터출현01_종료(self.ctx)


class 몬스터출현01_10번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[902,903,904], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906,907,908,909,910]):
            return 몬스터출현01_종료(self.ctx)


class 몬스터출현01_11번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901,904,905], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906,907,908,909,910]):
            return 몬스터출현01_종료(self.ctx)


class 몬스터출현01_12번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[903,904,905], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906,907,908,909,910]):
            return 몬스터출현01_종료(self.ctx)


class 몬스터출현01_종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__2$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫번째다리붕괴01(self.ctx)


class 첫번째다리붕괴01(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[11000], visible=True)
        self.set_agent(triggerIds=[11001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[99990]):
            return 첫번째무너짐연출시작01(self.ctx)


class 첫번째무너짐연출시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__900$')
        self.select_camera(triggerId=802, enable=True)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_999')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫번째다리붕괴02(self.ctx)


class 첫번째다리붕괴02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016], visible=False, meshCount=16, arg4=100, delay=100)
        self.set_effect(triggerIds=[777801], visible=True) # 길 없어짐01 사운드  / 첫 번째 다리
        self.set_mesh(triggerIds=[90001], visible=True, arg3=0, delay=0, scale=0) # 2st barrier ON
        self.set_mesh(triggerIds=[90000], visible=True, arg3=0, delay=0, scale=0) # 1st barrier ON
        self.set_skip(state=첫번째무너짐연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫번째무너짐연출종료01(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=18, key='clearafter', value=1)


class 첫번째무너짐연출종료01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[777801], visible=False) # 길 없어짐01 사운드  / 첫 번째 다리
        self.select_camera(triggerId=802, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 술래말풍선02(self.ctx)


class 술래말풍선02(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=16, key='FirstBridgeOff', value=1)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__3$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__4$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 술래패트롤02(self.ctx)


class 술래패트롤02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1001')
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__5$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__24$', arg4=2, arg5=2)
        self.create_monster(spawnIds=[91002], animationEffect=False) # 첫 번째 꽃덤불 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 첫번째덤불등장01(self.ctx)


class 첫번째덤불등장01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003312, textId=20003312) # 가이드 : 스킬을 사용해서 덤불을 없애 주세요.
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[91002]):
            return 첫번째덤불제거01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[777401], visible=True) # 덤불 제거01 사운드
        self.hide_guide_summary(entityId=20003312)


class 첫번째덤불제거01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=92220, visible=True, initialSequence='Dead_A') # 첫번째장벽 덤불
        self.set_mesh(triggerIds=[90002], visible=False, arg3=0, delay=0, scale=0) # 1st barrier OFF
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__6$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫번째꼬마찾기시작(self.ctx)


class 첫번째꼬마찾기시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=92000, visible=False, initialSequence='Dead_A') # 첫번째장벽 덤불
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9003, spawnIds=[100]):
            return 첫번째꼬마랜덤(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=92220, visible=False, initialSequence='Dead_A') # 첫번째장벽 덤불 제거
        self.set_effect(triggerIds=[777401], visible=False) # 덤불 제거01 사운드


class 첫번째꼬마랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 첫번째힌트발견01(self.ctx)
        if self.random_condition(rate=25):
            return 첫번째힌트발견02(self.ctx)
        if self.random_condition(rate=25):
            return 첫번째힌트발견03(self.ctx)
        if self.random_condition(rate=25):
            return 첫번째힌트발견04(self.ctx)


# 첫번째힌트발견01 - 110000766, 201
class 첫번째힌트발견01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(triggerIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016], visible=True, meshCount=16, arg4=100, delay=100) # 1st Hint ON
        self.set_effect(triggerIds=[777501], visible=True) # 발자국 나타남01 사운드
        self.set_interact_object(triggerIds=[10000766], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 첫번째힌트수색01(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 첫번째힌트수색01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__10$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000766], stateValue=0):
            return 첫번째꼬마발견01(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10000766], state=2)
        self.hide_guide_summary(entityId=20003313)


class 첫번째꼬마발견01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.set_conversation(type=1, spawnId=201, script='$02000331_BF__Seeker01__11$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫번째꼬마만남01(self.ctx)


class 첫번째꼬마만남01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__12$', arg4=2, arg5=1)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9004, spawnIds=[201]):
            return 첫번째꼬마교체딜레이01(self.ctx)


class 첫번째꼬마교체딜레이01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 첫번째꼬마교체01(self.ctx)


class 첫번째꼬마교체01(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=201, addSpawnId=200)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_998')
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__13$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__14$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9012, spawnIds=[100]):
            return 몬스터출현02_생성랜덤01(self.ctx)


# 첫번째힌트발견02 - 110000767, 202
class 첫번째힌트발견02(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(triggerIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117], visible=True, meshCount=17, arg4=100, delay=100) # 1st Hint ON
        self.set_effect(triggerIds=[777501], visible=True) # 발자국 나타남01 사운드
        self.set_interact_object(triggerIds=[10000767], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 첫번째힌트수색02(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 첫번째힌트수색02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__10$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000767], stateValue=0):
            return 첫번째꼬마발견02(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10000767], state=2)
        self.hide_guide_summary(entityId=20003313)


class 첫번째꼬마발견02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.set_conversation(type=1, spawnId=202, script='$02000331_BF__Seeker01__15$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫번째꼬마만남02(self.ctx)


class 첫번째꼬마만남02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__12$', arg4=2, arg5=1)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_2202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9004, spawnIds=[202]):
            return 첫번째꼬마교체딜레이02(self.ctx)


class 첫번째꼬마교체딜레이02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 첫번째꼬마교체02(self.ctx)


class 첫번째꼬마교체02(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=202, addSpawnId=200)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_998')
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__18$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__19$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9012, spawnIds=[100]):
            return 몬스터출현02_생성랜덤01(self.ctx)


# 첫번째힌트발견03 - 10000768, 203
class 첫번째힌트발견03(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(triggerIds=[2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220], visible=True, meshCount=20, arg4=100, delay=100) # 1st Hint ON
        self.set_effect(triggerIds=[777501], visible=True) # 발자국 나타남01 사운드
        self.set_interact_object(triggerIds=[10000768], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 첫번째힌트수색03(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 첫번째힌트수색03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__10$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000768], stateValue=0):
            return 첫번째꼬마발견03(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10000768], state=2)
        self.hide_guide_summary(entityId=20003313)


class 첫번째꼬마발견03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[203], animationEffect=False)
        self.set_conversation(type=1, spawnId=203, script='$02000331_BF__Seeker01__16$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫번째꼬마만남03(self.ctx)


class 첫번째꼬마만남03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__12$', arg4=2, arg5=1)
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_2203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9004, spawnIds=[203]):
            return 첫번째꼬마교체딜레이03(self.ctx)


class 첫번째꼬마교체딜레이03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 첫번째꼬마교체03(self.ctx)


class 첫번째꼬마교체03(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=203, addSpawnId=200)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_998')
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__20$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__21$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9012, spawnIds=[100]):
            return 몬스터출현02_생성랜덤01(self.ctx)


# 첫번째힌트발견04 - 10000769, 204
class 첫번째힌트발견04(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(triggerIds=[2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,2313,2314,2315], visible=True, meshCount=15, arg4=100, delay=100) # 1st Hint ON
        self.set_effect(triggerIds=[777501], visible=True) # 발자국 나타남01 사운드
        self.set_interact_object(triggerIds=[10000769], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 첫번째힌트수색04(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 첫번째힌트수색04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__10$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000769], stateValue=0):
            return 첫번째꼬마발견04(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10000769], state=2)
        self.hide_guide_summary(entityId=20003313)


class 첫번째꼬마발견04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204], animationEffect=False)
        self.set_conversation(type=1, spawnId=204, script='$02000331_BF__Seeker01__17$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫번째꼬마만남04(self.ctx)


class 첫번째꼬마만남04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__12$', arg4=2, arg5=1)
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_2204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9004, spawnIds=[204]):
            return 첫번째꼬마교체딜레이04(self.ctx)


class 첫번째꼬마교체딜레이04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 첫번째꼬마교체04(self.ctx)


class 첫번째꼬마교체04(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=204, addSpawnId=200)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_998')
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__22$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__23$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9012, spawnIds=[100]):
            return 몬스터출현02_생성랜덤01(self.ctx)


# 첫번째 꼬마 찾기 랜덤 스테이트 종료
# 두번째 꼬마 찾기 전에 전투용 몬스터 미리 스폰
class 몬스터출현02_생성랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 몬스터출현02_1번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현02_2번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현02_3번생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현02_4번생성(self.ctx)


class 몬스터출현02_1번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[9223,9224,9225,921,922,924,925,927,928], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 두명패트롤01(self.ctx)


class 몬스터출현02_2번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[9221,9223,9225,920,922,924,925,926,929], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 두명패트롤01(self.ctx)


class 몬스터출현02_3번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[9221,9222,9224,920,922,924,925,926,928], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 두명패트롤01(self.ctx)


class 몬스터출현02_4번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[9222,9223,9225,922,923,925,926,927,929], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 두명패트롤01(self.ctx)


class 두명패트롤01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1003')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9016, spawnIds=[100]):
            return 두번째덤불등장01(self.ctx)


class 두번째덤불등장01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003312, textId=20003312) # 가이드 : 스킬을 사용해서 덤불을 없애 주세요.
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__24$', arg4=3, arg5=0)
        self.create_monster(spawnIds=[91003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[91003]):
            return 두번째덤불제거01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003312)
        self.set_effect(triggerIds=[777402], visible=True) # 덤불 제거02 사운드


class 두번째덤불제거01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=93330, visible=True, initialSequence='Dead_A') # 첫번째장벽 덤불
        self.set_mesh(triggerIds=[90003], visible=False, arg3=0, delay=0, scale=0) # 4th barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째꼬마찾기시작(self.ctx)


class 두번째꼬마찾기시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__25$', arg4=3, arg5=0)
        self.set_effect(triggerIds=[777402], visible=False) # 덤불 제거02 사운드
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1004')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9005, spawnIds=[100]):
            return 두번째몬스터발견01(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=93330, visible=False, initialSequence='Dead_A') # 첫번째장벽 덤불


class 두번째몬스터발견01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__30$', arg4=2, arg5=0)
        self.set_agent(triggerIds=[13001], visible=False) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(triggerIds=[13002], visible=False) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(triggerIds=[13003], visible=False) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(triggerIds=[13004], visible=False) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(triggerIds=[13005], visible=False) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_agent(triggerIds=[13006], visible=False) # 두번째 전투 전에 몬스터 길  막기 해제
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__31$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[9221,9222,9223,9224,9225,920,921,922,923,924,925,926,927,928,929]):
            return 두번째꼬마랜덤(self.ctx)


class 두번째꼬마랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 두번째힌트발견01(self.ctx)
        if self.random_condition(rate=20):
            return 두번째힌트발견02(self.ctx)
        if self.random_condition(rate=20):
            return 두번째힌트발견03(self.ctx)
        if self.random_condition(rate=20):
            return 두번째힌트발견04(self.ctx)
        if self.random_condition(rate=20):
            return 두번째힌트발견05(self.ctx)


# 두번째힌트발견01 - 10000771, 301, 311
class 두번째힌트발견01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_997')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2013')
        self.set_random_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018], visible=True, meshCount=18, arg4=50, delay=50) # 2nd Hint ON
        self.set_effect(triggerIds=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 두번째힌트수색01(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 두번째힌트수색01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[311], animationEffect=False)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__32$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9301]):
            return 두번째꼬마도움01(self.ctx)


class 두번째꼬마도움01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=311, script='$02000331_BF__Seeker01__33$', arg4=2, arg5=0)
        self.set_interact_object(triggerIds=[10000771], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마발견01(self.ctx)


class 두번째꼬마발견01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000771], stateValue=0):
            return 두번째꼬마구출01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003313)
        self.set_interact_object(triggerIds=[10000771], state=2)


class 두번째꼬마구출01(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=311, addSpawnId=301)
        self.set_conversation(type=1, spawnId=301, script='$02000331_BF__Seeker01__38$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 두번째꼬마이동01(self.ctx)


class 두번째꼬마이동01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_3301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마만남01(self.ctx)


class 두번째꼬마만남01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=301, script='$02000331_BF__Seeker01__39$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마대화01(self.ctx)


class 두번째꼬마대화01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__40$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9006, spawnIds=[301]):
            return 두번째꼬마교체딜레이01(self.ctx)


class 두번째꼬마교체딜레이01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__41$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째꼬마교체01(self.ctx)


class 두번째꼬마교체01(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=301, addSpawnId=300)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_996')
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__42$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9007, spawnIds=[100]):
            return 세명패트롤01(self.ctx)


# 두번째힌트발견02 - 10000772, 302, 312
class 두번째힌트발견02(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_997')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2013')
        self.set_random_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116], visible=True, meshCount=16, arg4=50, delay=50) # 2nd Hint ON
        self.set_effect(triggerIds=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 두번째힌트수색02(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 두번째힌트수색02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[312], animationEffect=False)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__32$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9302]):
            return 두번째꼬마도움02(self.ctx)


class 두번째꼬마도움02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=312, script='$02000331_BF__Seeker01__34$', arg4=2, arg5=0)
        self.set_interact_object(triggerIds=[10000772], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마발견02(self.ctx)


class 두번째꼬마발견02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000772], stateValue=0):
            return 두번째꼬마구출02(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10000772], state=2)
        self.hide_guide_summary(entityId=20003313)


class 두번째꼬마구출02(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=312, addSpawnId=302)
        self.set_conversation(type=1, spawnId=302, script='$02000331_BF__Seeker01__43$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 두번째꼬마이동02(self.ctx)


class 두번째꼬마이동02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_3302')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마만남02(self.ctx)


class 두번째꼬마만남02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=302, script='$02000331_BF__Seeker01__44$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마대화02(self.ctx)


class 두번째꼬마대화02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__45$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9006, spawnIds=[302]):
            return 두번째꼬마교체딜레이02(self.ctx)


class 두번째꼬마교체딜레이02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__46$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째꼬마교체02(self.ctx)


class 두번째꼬마교체02(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=302, addSpawnId=300)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_996')
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__47$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9007, spawnIds=[100]):
            return 세명패트롤01(self.ctx)


# 두번째힌트발견03 - 10000773, 303, 313
class 두번째힌트발견03(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_997')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2013')
        self.set_random_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=True, meshCount=21, arg4=50, delay=50) # 2nd Hint ON
        self.set_effect(triggerIds=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 두번째힌트수색03(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 두번째힌트수색03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[313], animationEffect=False)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__32$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9303]):
            return 두번째꼬마도움03(self.ctx)


class 두번째꼬마도움03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=313, script='$02000331_BF__Seeker01__35$', arg4=2, arg5=0)
        self.set_interact_object(triggerIds=[10000773], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마발견03(self.ctx)


class 두번째꼬마발견03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000773], stateValue=0):
            return 두번째꼬마구출03(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10000773], state=2)
        self.hide_guide_summary(entityId=20003313)


class 두번째꼬마구출03(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=313, addSpawnId=303)
        self.set_conversation(type=1, spawnId=303, script='$02000331_BF__Seeker01__48$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 두번째꼬마이동03(self.ctx)


class 두번째꼬마이동03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=303, patrolName='MS2PatrolData_3303')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마만남03(self.ctx)


class 두번째꼬마만남03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=303, script='$02000331_BF__Seeker01__49$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마대화03(self.ctx)


class 두번째꼬마대화03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__50$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9006, spawnIds=[303]):
            return 두번째꼬마교체딜레이03(self.ctx)


class 두번째꼬마교체딜레이03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__51$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마교체03(self.ctx)


class 두번째꼬마교체03(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=303, addSpawnId=300)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_996')
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__52$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9007, spawnIds=[100]):
            return 세명패트롤01(self.ctx)


# 두번째힌트발견04 - 10000774, 304, 314
class 두번째힌트발견04(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_997')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2013')
        self.set_random_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318], visible=True, meshCount=18, arg4=50, delay=50) # 2nd Hint ON
        self.set_effect(triggerIds=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 두번째힌트수색04(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 두번째힌트수색04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[314], animationEffect=False)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__32$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9304]):
            return 두번째꼬마도움04(self.ctx)


class 두번째꼬마도움04(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000774], state=1)
        self.set_conversation(type=1, spawnId=314, script='$02000331_BF__Seeker01__36$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마발견04(self.ctx)


class 두번째꼬마발견04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000774], stateValue=0):
            return 두번째꼬마구출04(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10000774], state=2)
        self.hide_guide_summary(entityId=20003313)


class 두번째꼬마구출04(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=314, addSpawnId=304)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마이동04(self.ctx)


class 두번째꼬마이동04(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=304, patrolName='MS2PatrolData_3304')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마만남04(self.ctx)


class 두번째꼬마만남04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=304, script='$02000331_BF__Seeker01__54$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마대화04(self.ctx)


class 두번째꼬마대화04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__55$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9006, spawnIds=[304]):
            return 두번째꼬마교체딜레이04(self.ctx)


class 두번째꼬마교체딜레이04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__56$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째꼬마교체04(self.ctx)


class 두번째꼬마교체04(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=304, addSpawnId=300)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_996')
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__57$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9007, spawnIds=[100]):
            return 세명패트롤01(self.ctx)


# 두번째힌트발견05 - 10000775, 305, 315
class 두번째힌트발견05(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_997')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2013')
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__800$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.set_random_mesh(triggerIds=[3401,3402,3403,3404,3405,3406,3407,3408,3409,3410,3411,3412,3413,3414,3415,3416,3417,3418,3419], visible=True, meshCount=19, arg4=50, delay=50) # 2nd Hint ON
        self.set_effect(triggerIds=[777502], visible=True) # 발자국 나타남02 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 두번째힌트수색05(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003313, textId=20003313) # 가이드 : 발자국을 따라가서 친구를 찾아 보세요.


class 두번째힌트수색05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[315], animationEffect=False)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__32$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9305]):
            return 두번째꼬마도움05(self.ctx)


class 두번째꼬마도움05(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000775], state=1)
        self.set_conversation(type=1, spawnId=315, script='$02000331_BF__Seeker01__37$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 두번째꼬마발견05(self.ctx)


class 두번째꼬마발견05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000775], stateValue=0):
            return 두번째꼬마구출05(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10000775], state=2)
        self.hide_guide_summary(entityId=20003313)


class 두번째꼬마구출05(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=315, addSpawnId=305)
        self.set_conversation(type=1, spawnId=305, script='$02000331_BF__Seeker01__58$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마이동05(self.ctx)


class 두번째꼬마이동05(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=305, patrolName='MS2PatrolData_3305')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마만남05(self.ctx)


class 두번째꼬마만남05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=305, script='$02000331_BF__Seeker01__59$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째꼬마대화05(self.ctx)


class 두번째꼬마대화05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__60$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9006, spawnIds=[305]):
            return 두번째꼬마교체딜레이05(self.ctx)


class 두번째꼬마교체딜레이05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__61$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째꼬마교체05(self.ctx)


class 두번째꼬마교체05(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=305, addSpawnId=300)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_996')
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__62$', arg4=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9007, spawnIds=[100]):
            return 세명패트롤01(self.ctx)


# 두번째 꼬마 찾기 랜덤 스테이트 종료
class 세명패트롤01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1005')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2004')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9008, spawnIds=[100]):
            return 세명패트롤02(self.ctx)


class 세명패트롤02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__70$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세번째덤불등장01(self.ctx)


# 세명 패트롤 하다가 덩굴에 막힘
class 세번째덤불등장01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003312, textId=20003312) # 가이드 : 스킬을 사용해서 덤불을 없애 주세요.
        self.create_monster(spawnIds=[91004], animationEffect=False) # 3다시1 꽃덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[91004]):
            return 세번째덤불등장02(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[777403], visible=True) # 덤불 제거03 사운드


class 세번째덤불등장02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1006')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2005')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3003')
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__71$', arg4=2, arg5=0)
        self.create_monster(spawnIds=[91005], animationEffect=False) # 3다시2 꽃덤불
        self.set_mesh(triggerIds=[90004], visible=False, arg3=0, delay=0, scale=0) # 4th barrier OFF
        self.set_actor(triggerId=94440, visible=True, initialSequence='Dead_A') # 첫번째장벽 덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[91005]):
            return 세번째덤불등장03(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003312)
        self.set_effect(triggerIds=[777404], visible=True) # 덤불 제거04 사운드


class 세번째덤불등장03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__72$', arg4=2, arg5=0)
        self.set_mesh(triggerIds=[90005], visible=False, arg3=0, delay=0, scale=0) # 5th barrier OFF
        self.set_actor(triggerId=94450, visible=True, initialSequence='Dead_A') # 첫번째장벽 덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세번째꼬마찾기시작(self.ctx)


class 세번째꼬마찾기시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[777403], visible=False) # 덤불 제거03 사운드
        self.set_effect(triggerIds=[777404], visible=False) # 덤불 제거04 사운드
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__73$', arg4=2, arg5=0)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1016')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2015')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3013')
        self.set_actor(triggerId=94440, visible=False, initialSequence='Dead_A') # 첫번째장벽 덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 꼬마셋대화연출01(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=94450, visible=False, initialSequence='Dead_A') # 첫번째장벽 덤불


class 꼬마셋대화연출01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__74$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 세명패트롤03(self.ctx)


class 세명패트롤03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9009, spawnIds=[100]):
            return 세번째스위치랜덤(self.ctx)


# 고립된 세번째 꼬마 발견, 세번째스위치 랜덤
class 세번째스위치랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 세번째스위치출현01(self.ctx)
        if self.random_condition(rate=20):
            return 세번째스위치출현02(self.ctx)
        if self.random_condition(rate=20):
            return 세번째스위치출현03(self.ctx)
        if self.random_condition(rate=20):
            return 세번째스위치출현04(self.ctx)
        if self.random_condition(rate=20):
            return 세번째스위치출현05(self.ctx)


# 세번째스위치01 - 10000784
class 세번째스위치출현01(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000784], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 고립연출시작01(self.ctx)


class 고립연출시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(triggerId=804, enable=True)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1007')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 고립연출종료01(self.ctx)


class 고립연출종료01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내01_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 구출안내01_01(self.ctx)


class 구출안내01_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 구출안내01_02(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.


class 구출안내01_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__80$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내01_03(self.ctx)


class 구출안내01_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__81$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내01_04(self.ctx)


class 구출안내01_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__82$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000784], stateValue=0):
            return 딜레이(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


# 세번째스위치02 - 10000792
class 세번째스위치출현02(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000792], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 고립연출시작02(self.ctx)


class 고립연출시작02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(triggerId=804, enable=True)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1007')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 고립연출종료02(self.ctx)


class 고립연출종료02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내02_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 구출안내02_01(self.ctx)


class 구출안내02_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 구출안내02_02(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.


class 구출안내02_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__80$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내02_03(self.ctx)


class 구출안내02_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__81$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내02_04(self.ctx)


class 구출안내02_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__82$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000792], stateValue=0):
            return 딜레이(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


# 세번째스위치03 - 10000793
class 세번째스위치출현03(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000793], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 고립연출시작03(self.ctx)


class 고립연출시작03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(triggerId=804, enable=True)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1007')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 고립연출종료03(self.ctx)


class 고립연출종료03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내03_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 구출안내03_01(self.ctx)


class 구출안내03_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 구출안내03_02(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.


class 구출안내03_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__80$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내03_03(self.ctx)


class 구출안내03_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__81$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내03_04(self.ctx)


class 구출안내03_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__82$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000793], stateValue=0):
            return 딜레이(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


# 세번째스위치04 - 10000794
class 세번째스위치출현04(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000794], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 고립연출시작04(self.ctx)


class 고립연출시작04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(triggerId=804, enable=True)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1007')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 고립연출종료04(self.ctx)


class 고립연출종료04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내04_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 구출안내04_01(self.ctx)


class 구출안내04_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 구출안내04_02(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.


class 구출안내04_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__80$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내04_03(self.ctx)


class 구출안내04_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__81$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내04_04(self.ctx)


class 구출안내04_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__82$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000794], stateValue=0):
            return 딜레이(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


# 세번째스위치05 - 10000795
class 세번째스위치출현05(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000795], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 고립연출시작05(self.ctx)


class 고립연출시작05(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__901$')
        self.select_camera(triggerId=804, enable=True)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1007')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2006')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3004')
        self.set_skip(state=고립연출종료05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 고립연출종료05(self.ctx)


class 고립연출종료05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=804, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=구출안내05_01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 구출안내05_01(self.ctx)


class 구출안내05_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__802$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 구출안내05_02(self.ctx)

    def on_exit(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.


class 구출안내05_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__80$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내05_03(self.ctx)


class 구출안내05_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__81$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 구출안내05_04(self.ctx)


class 구출안내05_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__82$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000795], stateValue=0):
            return 딜레이(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=401, addSpawnId=400)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 세번째꼬마탈출(self.ctx)


class 세번째꼬마탈출(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=400, script='$02000331_BF__Seeker01__83$', arg4=2, arg5=0)
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_4001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9010, spawnIds=[400]):
            return 세번째꼬마만남01(self.ctx)


class 세번째꼬마만남01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1008')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2007')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3005')
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__84$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세번째꼬마만남02(self.ctx)


class 세번째꼬마만남02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=400, script='$02000331_BF__Seeker01__85$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세번째꼬마만남03(self.ctx)


class 세번째꼬마만남03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__86$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 네명패트롤01(self.ctx)


# 고립된 세번째 꼬마 구출 완료
class 네명패트롤01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__87$', arg4=2, arg5=0)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1009')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9011, spawnIds=[100]):
            return 네명패트롤02(self.ctx)


class 네명패트롤02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2008')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3006')
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_4002')
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__88$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9017, spawnIds=[100]):
            return 네번째덤불등장01(self.ctx)


# 네명 패트롤 하다가 세번째 덩굴에 막힘
class 네번째덤불등장01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003312, textId=20003312) # 가이드 : 스킬을 사용해서 덤불을 없애 주세요.
        self.create_monster(spawnIds=[91006], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[91006]):
            return 네번째덤불제거01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003312)
        self.set_effect(triggerIds=[777405], visible=True) # 덤불 제거05 사운드


class 네번째덤불제거01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=96660, visible=True, initialSequence='Dead_A') # 첫번째장벽 덤불
        self.set_mesh(triggerIds=[90006], visible=False, arg3=0, delay=0, scale=0) # 7th barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 네번째꼬마찾기시작(self.ctx)


class 네번째꼬마찾기시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='401', seconds=2)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__89$', arg4=2, arg5=0)
        self.set_effect(triggerIds=[777405], visible=False) # 덤불 제거05 사운드
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1010')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2009')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3007')
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_4003')
        self.set_actor(triggerId=96660, visible=False, initialSequence='Dead_A') # 첫번째장벽 덤불

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9013, spawnIds=[100]):
            return 몬스터출현05_꼬마생성(self.ctx)


# 네번째 꼬마 쫓기는 웨이브 시작
class 몬스터출현05_꼬마생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[500], animationEffect=False)
        self.move_npc(spawnId=500, patrolName='MS2PatrolData_5001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현05_생성랜덤01(self.ctx)


class 몬스터출현05_생성랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 몬스터출현05_1번대장생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_2번대장생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_3번대장생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_4번대장생성(self.ctx)


class 몬스터출현05_1번대장생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[991], animationEffect=False)
        self.move_npc(spawnId=991, patrolName='MS2PatrolData_905')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 몬스터출현05_생성랜덤02(self.ctx)


class 몬스터출현05_2번대장생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[992], animationEffect=False)
        self.move_npc(spawnId=992, patrolName='MS2PatrolData_905')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 몬스터출현05_생성랜덤02(self.ctx)


class 몬스터출현05_3번대장생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[992], animationEffect=False)
        self.move_npc(spawnId=992, patrolName='MS2PatrolData_905')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 몬스터출현05_생성랜덤02(self.ctx)


class 몬스터출현05_4번대장생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[991], animationEffect=False)
        self.move_npc(spawnId=991, patrolName='MS2PatrolData_905')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 몬스터출현05_생성랜덤02(self.ctx)


class 몬스터출현05_생성랜덤02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 몬스터출현05_1번자코생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_2번자코생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_3번자코생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_4번자코생성(self.ctx)


class 몬스터출현05_1번자코생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5001', seconds=1)
        self.create_monster(spawnIds=[930], animationEffect=False)
        self.move_npc(spawnId=930, patrolName='MS2PatrolData_901')
        self.create_monster(spawnIds=[935], animationEffect=False)
        self.move_npc(spawnId=935, patrolName='MS2PatrolData_904')
        self.create_monster(spawnIds=[937], animationEffect=False)
        self.move_npc(spawnId=937, patrolName='MS2PatrolData_906')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5001'):
            return 몬스터출현05_생성랜덤03(self.ctx)


class 몬스터출현05_2번자코생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5002', seconds=1)
        self.create_monster(spawnIds=[931], animationEffect=False)
        self.move_npc(spawnId=931, patrolName='MS2PatrolData_902')
        self.create_monster(spawnIds=[936], animationEffect=False)
        self.move_npc(spawnId=936, patrolName='MS2PatrolData_901')
        self.create_monster(spawnIds=[937], animationEffect=False)
        self.move_npc(spawnId=937, patrolName='MS2PatrolData_907')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5002'):
            return 몬스터출현05_생성랜덤03(self.ctx)


class 몬스터출현05_3번자코생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5003', seconds=1)
        self.create_monster(spawnIds=[932], animationEffect=False)
        self.move_npc(spawnId=932, patrolName='MS2PatrolData_903')
        self.create_monster(spawnIds=[938], animationEffect=False)
        self.move_npc(spawnId=938, patrolName='MS2PatrolData_907')
        self.create_monster(spawnIds=[936], animationEffect=False)
        self.move_npc(spawnId=936, patrolName='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5003'):
            return 몬스터출현05_생성랜덤03(self.ctx)


class 몬스터출현05_4번자코생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5004', seconds=1)
        self.create_monster(spawnIds=[932], animationEffect=False)
        self.move_npc(spawnId=932, patrolName='MS2PatrolData_905')
        self.create_monster(spawnIds=[934], animationEffect=False)
        self.move_npc(spawnId=934, patrolName='MS2PatrolData_903')
        self.create_monster(spawnIds=[938], animationEffect=False)
        self.move_npc(spawnId=938, patrolName='MS2PatrolData_906')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5004'):
            return 몬스터출현05_생성랜덤03(self.ctx)


class 몬스터출현05_생성랜덤03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 몬스터출현05_5번대장생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_6번대장생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_7번대장생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_8번대장생성(self.ctx)


class 몬스터출현05_5번대장생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[991], animationEffect=False)
        self.move_npc(spawnId=991, patrolName='MS2PatrolData_904')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현05_생성랜덤04(self.ctx)


class 몬스터출현05_6번대장생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[992], animationEffect=False)
        self.move_npc(spawnId=992, patrolName='MS2PatrolData_904')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현05_생성랜덤04(self.ctx)


class 몬스터출현05_7번대장생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[993], animationEffect=False)
        self.move_npc(spawnId=993, patrolName='MS2PatrolData_904')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현05_생성랜덤04(self.ctx)


class 몬스터출현05_8번대장생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[994], animationEffect=False)
        self.move_npc(spawnId=994, patrolName='MS2PatrolData_904')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현05_생성랜덤04(self.ctx)


class 몬스터출현05_생성랜덤04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 몬스터출현05_5번자코생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_6번자코생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_7번자코생성(self.ctx)
        if self.random_condition(rate=25):
            return 몬스터출현05_8번자코생성(self.ctx)


class 몬스터출현05_5번자코생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[930], animationEffect=False)
        self.move_npc(spawnId=930, patrolName='MS2PatrolData_902')
        self.create_monster(spawnIds=[935], animationEffect=False)
        self.move_npc(spawnId=935, patrolName='MS2PatrolData_905')
        self.create_monster(spawnIds=[937], animationEffect=False)
        self.move_npc(spawnId=937, patrolName='MS2PatrolData_909')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 추격연출시작01(self.ctx)


class 몬스터출현05_6번자코생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[931], animationEffect=False)
        self.move_npc(spawnId=931, patrolName='MS2PatrolData_901')
        self.create_monster(spawnIds=[934], animationEffect=False)
        self.move_npc(spawnId=934, patrolName='MS2PatrolData_909')
        self.create_monster(spawnIds=[937], animationEffect=False)
        self.move_npc(spawnId=937, patrolName='MS2PatrolData_907')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 추격연출시작01(self.ctx)


class 몬스터출현05_7번자코생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[932], animationEffect=False)
        self.move_npc(spawnId=932, patrolName='MS2PatrolData_903')
        self.create_monster(spawnIds=[935], animationEffect=False)
        self.move_npc(spawnId=935, patrolName='MS2PatrolData_904')
        self.create_monster(spawnIds=[936], animationEffect=False)
        self.move_npc(spawnId=936, patrolName='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 추격연출시작01(self.ctx)


class 몬스터출현05_8번자코생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[932], animationEffect=False)
        self.move_npc(spawnId=932, patrolName='MS2PatrolData_906')
        self.create_monster(spawnIds=[934], animationEffect=False)
        self.move_npc(spawnId=934, patrolName='MS2PatrolData_901')
        self.create_monster(spawnIds=[937], animationEffect=False)
        self.move_npc(spawnId=937, patrolName='MS2PatrolData_907')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 추격연출시작01(self.ctx)


class 추격연출시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7776], visible=True) # 추격 소음01 사운드
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__902$')
        self.select_camera(triggerId=800, enable=True)
        self.set_skip(state=추격연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 추격연출종료01(self.ctx)


class 추격연출종료01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__803$', arg3='2000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.select_camera(triggerId=800, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__90$', arg4=2)
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__91$', arg4=2)
        self.set_conversation(type=1, spawnId=500, script='$02000331_BF__Seeker01__92$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[930,931,932,933,934,935,936,937,938,991,992,993,994]):
            return 네번째꼬마만남01(self.ctx)


class 네번째꼬마만남01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7776], visible=False) # 추격 소음01 사운드
        self.set_conversation(type=1, spawnId=500, script='$02000331_BF__Seeker01__93$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 네번째꼬마만남02(self.ctx)


class 네번째꼬마만남02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__94$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 네번째꼬마만남03(self.ctx)


class 네번째꼬마만남03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__95$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 네번째꼬마만남04(self.ctx)


class 네번째꼬마만남04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=400, script='$02000331_BF__Seeker01__96$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다섯명패트롤01(self.ctx)


class 다섯명패트롤01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__97$', arg4=2, arg5=0)
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9014, spawnIds=[100]):
            return 다섯명패트롤02(self.ctx)


class 다섯명패트롤02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2010')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3008')
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_4004')
        self.move_npc(spawnId=500, patrolName='MS2PatrolData_5002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9015, spawnIds=[100]):
            return 두번째무너짐연출시작01(self.ctx)


class 두번째무너짐연출시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__903$')
        self.select_camera(triggerId=806, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 두번째다리붕괴02(self.ctx)


class 두번째다리붕괴02(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,10030,10031,10032,10033], visible=False, meshCount=14, arg4=100, delay=100)
        self.set_effect(triggerIds=[777803], visible=True) # 길 없어짐02 사운드 / 막힌 길
        self.set_agent(triggerIds=[15000], visible=True) # 끊어진 다리 길 막기
        self.set_agent(triggerIds=[15001], visible=True) # 끊어진 다리 길 막기
        self.set_agent(triggerIds=[15002], visible=True) # 끊어진 다리 길 막기
        self.set_skip(state=두번째무너짐연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 두번째무너짐연출종료01(self.ctx)


class 두번째무너짐연출종료01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=806, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_skip(state=술래말풍선06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 술래말풍선06(self.ctx)


class 술래말풍선06(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[777803], visible=False) # 길 없어짐02 사운드 / 막힌 길
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1012')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 술래말풍선07(self.ctx)


class 술래말풍선07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__100$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=200, script='$02000331_BF__Seeker01__101$', arg4=2, arg5=1)
        self.move_npc(spawnId=500, patrolName='MS2PatrolData_5003')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3009')
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_4005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 술래말풍선08(self.ctx)


class 술래말풍선08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=500, script='$02000331_BF__Seeker01__102$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 술래말풍선09(self.ctx)


class 술래말풍선09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__103$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 술래말풍선10(self.ctx)


class 술래말풍선10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=400, script='$02000331_BF__Seeker01__104$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=300, script='$02000331_BF__Seeker01__105$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 외다리생성랜덤(self.ctx)


# 다섯번째  외다리 생성 스위치 랜덤
class 외다리생성랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 외다리스위치출현01(self.ctx)
        if self.random_condition(rate=20):
            return 외다리스위치출현02(self.ctx)
        if self.random_condition(rate=20):
            return 외다리스위치출현03(self.ctx)
        if self.random_condition(rate=20):
            return 외다리스위치출현04(self.ctx)
        if self.random_condition(rate=20):
            return 외다리스위치출현05(self.ctx)


# 외다리스위치출현01 -  10000785
class 외다리스위치출현01(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000785], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(triggerIds=[10000785], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 외다리스위치반응01(self.ctx)


class 외다리스위치반응01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000785]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


# 외다리스위치출현02 -  10000796
class 외다리스위치출현02(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000796], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(triggerIds=[10000796], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 외다리스위치반응02(self.ctx)


class 외다리스위치반응02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000796]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


# 외다리스위치출현03 -  10000797
class 외다리스위치출현03(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000797], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(triggerIds=[10000797], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 외다리스위치반응03(self.ctx)


class 외다리스위치반응03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000797]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


# 외다리스위치출현04 -  10000798
class 외다리스위치출현04(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000798], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(triggerIds=[10000798], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 외다리스위치반응04(self.ctx)


class 외다리스위치반응04(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000798]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


# 외다리스위치출현05 -  10000799
class 외다리스위치출현05(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000799], state=0) # 외다리 생성하는 레버01 나타남
        self.set_interact_object(triggerIds=[10000799], state=1) # 외다리 생성하는 레버01 나타남
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__804$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 외다리스위치반응05(self.ctx)


class 외다리스위치반응05(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003314, textId=20003314) # 가이드 : 주변에서 레버를 찾아 당겨 보세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000799]):
            return 외다리생성시작01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003314)


class 외다리생성시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[90008], visible=False, arg3=0, delay=0, scale=0) # 9th barrier OFF
        self.set_effect(triggerIds=[777702], visible=True) # 길 나타남02 사운드 / 외다리
        self.set_random_mesh(triggerIds=[10040,10041,10042,10043,10044], visible=True, meshCount=5, arg4=150, delay=150) # 3rd bridge ON

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 다리건너갈준비01(self.ctx)


class 다리건너갈준비01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__805$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 다리건너갈준비02(self.ctx)


class 다리건너갈준비02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__110$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[99992]):
            return 다리건너가기01(self.ctx)
        if self.user_detected(boxIds=[99993]):
            return 다리건너가기01(self.ctx)


class 다리건너가기01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_1014')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_2014')
        self.move_npc(spawnId=300, patrolName='MS2PatrolData_3010')
        self.move_npc(spawnId=400, patrolName='MS2PatrolData_4006')
        self.move_npc(spawnId=500, patrolName='MS2PatrolData_5004')
        self.set_conversation(type=1, spawnId=100, script='$02000331_BF__Seeker01__111$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다리건너가기02(self.ctx)


class 다리건너가기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[99996]):
            return 다리건너가기03(self.ctx)


class 다리건너가기03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=610, script='$02000331_BF__Seeker01__112$', arg4=3, arg5=0)
        self.set_mesh(triggerIds=[90008], visible=True, arg3=0, delay=0, scale=0) # 9th barrier ON

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 다리건너가기04(self.ctx)


class 다리건너가기04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9018, spawnIds=[300]):
            return 보스등장연출시작01(self.ctx)


class 보스등장연출시작01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[990], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__904$')
        self.set_effect(triggerIds=[777901], visible=True) # KaseMu Voice01
        self.select_camera(triggerId=808, enable=True)
        self.set_skip(state=보스등장연출중01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보스등장연출중01(self.ctx)


class 보스등장연출중01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__905$')
        self.set_skip(state=보스등장연출중01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보스등장연출중01Skip(self.ctx)


class 보스등장연출중01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 보스등장연출중02(self.ctx)


class 보스등장연출중02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__906$')
        self.change_monster(removeSpawnId=100, addSpawnId=601) # 디펜스용 NPC로 교체 메린
        self.change_monster(removeSpawnId=200, addSpawnId=602) # 디펜스용 NPC로 교체 이지
        self.change_monster(removeSpawnId=300, addSpawnId=603) # 디펜스용 NPC로 교체 플린
        self.change_monster(removeSpawnId=400, addSpawnId=604) # 디펜스용 NPC로 교체 스틴
        self.change_monster(removeSpawnId=500, addSpawnId=605) # 디펜스용 NPC로 교체 토리
        self.select_camera(triggerId=809, enable=True)
        self.set_skip(state=보스등장연출중02Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스등장연출중02Skip(self.ctx)


class 보스등장연출중02Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 보스등장연출중03(self.ctx)


class 보스등장연출중03(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[10040,10041,10042,10043,10044], visible=False, meshCount=5, arg4=150, delay=150) # 3rd bridge OFF
        self.set_effect(triggerIds=[777802], visible=True) # 길 없어짐02 사운드 /  외다리
        self.set_agent(triggerIds=[16000], visible=True) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16001], visible=True) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16002], visible=True) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16003], visible=True) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16004], visible=True) # 새로운 다리 길 막기
        self.set_skip(state=보스등장연출중03Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스등장연출중03Skip(self.ctx)


class 보스등장연출중03Skip(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 보스등장연출중04(self.ctx)


class 보스등장연출중04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=809, enable=False)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__907$')
        self.set_effect(triggerIds=[777901], visible=False) # KaseMu Voice01
        self.set_effect(triggerIds=[777902], visible=True) # KaseMu Voice02
        self.set_skip(state=보스등장연출끝01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보스등장연출끝01(self.ctx)


class 보스등장연출끝01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=808, enable=False)
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[777802], visible=False) # 길 없어짐02 사운드 /  외다리
        self.set_user_value(triggerId=15, key='SecondBridgeOff', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마지막웨이브알림01(self.ctx)


class 마지막웨이브알림01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__806$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 몬스터출현06_생성랜덤01(self.ctx)


# 마지막 웨이브 : 첫 번째 소환 : 근거리4/근거리4
class 몬스터출현06_생성랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 몬스터출현06_1번생성(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_2번생성(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_3번생성(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_4번생성(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_5번생성(self.ctx)


class 몬스터출현06_1번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[940,941,950,951], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_생성랜덤02(self.ctx)


class 몬스터출현06_2번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[942,943,952,953], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_생성랜덤02(self.ctx)


class 몬스터출현06_3번생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6003', seconds=1)
        self.create_monster(spawnIds=[944,945,954,955], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_생성랜덤02(self.ctx)


class 몬스터출현06_4번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[946,947,956,957], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_생성랜덤02(self.ctx)


class 몬스터출현06_5번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[948,949,958,959], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_생성랜덤02(self.ctx)


# 마지막 웨이브 : 두 번째 소환
class 몬스터출현06_생성랜덤02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 몬스터출현06_6번생성(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_7번생성(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_8번생성(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_9번생성(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_10번생성(self.ctx)


class 몬스터출현06_6번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[960,961,962,963], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 몬스터출현06_7번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[962,963,964,965], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 몬스터출현06_8번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[964,965,966,967], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 몬스터출현06_9번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[966,967,968,969], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 몬스터출현06_10번생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[968,969,960,961], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 두번째웨이브대기(self.ctx)


class 두번째웨이브대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 몬스터출현06_생성랜덤03(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 : 원거리4 근거리12
class 몬스터출현06_생성랜덤03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=20):
            return 몬스터출현06_11번생성_01(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_12번생성_01(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_13번생성_01(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_14번생성_01(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_15번생성_01(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 : 패턴1 : 근2-2-3-2-3-2, 원3,5빼고
class 몬스터출현06_11번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[940,941,971], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_11번생성_02(self.ctx)


class 몬스터출현06_11번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[950,951,970], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_11번생성_03(self.ctx)


class 몬스터출현06_11번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[960,961,962], animationEffect=False) # 원거리없음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_11번생성_04(self.ctx)


class 몬스터출현06_11번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[945,946,976], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_11번생성_05(self.ctx)


class 몬스터출현06_11번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[955,956,957], animationEffect=False) # 원거리없음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 몬스터출현06_11번생성_06(self.ctx)


class 몬스터출현06_11번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[965,966,975], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 :  패턴2  : 근2-3-2-3-2-2, 원2,5빼고
class 몬스터출현06_12번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[958,959,978], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_12번생성_02(self.ctx)


class 몬스터출현06_12번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[968,969,960], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_12번생성_03(self.ctx)


class 몬스터출현06_12번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[948,949,979], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_12번생성_04(self.ctx)


class 몬스터출현06_12번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[943,944,945,975], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_12번생성_05(self.ctx)


class 몬스터출현06_12번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[953,954], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_12번생성_06(self.ctx)


class 몬스터출현06_12번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[964,965,974], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 :  패턴3 : 근2-3-3-2-2-2, 원1,6빼고
class 몬스터출현06_13번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[946,947], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_13번생성_02(self.ctx)


class 몬스터출현06_13번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[955,956,957,976], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_13번생성_03(self.ctx)


class 몬스터출현06_13번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[965,966,967,977], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_13번생성_04(self.ctx)


class 몬스터출현06_13번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[969,960,979], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_13번생성_05(self.ctx)


class 몬스터출현06_13번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[949,940,970], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_13번생성_06(self.ctx)


class 몬스터출현06_13번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[950,959], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 :  패턴4 : 근2-3-3-2-2-2, 원2,3빼고
class 몬스터출현06_14번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[941,942,972], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_14번생성_02(self.ctx)


class 몬스터출현06_14번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[961,962,963], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_14번생성_03(self.ctx)


class 몬스터출현06_14번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[951,952,953], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_14번생성_04(self.ctx)


class 몬스터출현06_14번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[964,965,974], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_14번생성_05(self.ctx)


class 몬스터출현06_14번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[944,946,975], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_14번생성_06(self.ctx)


class 몬스터출현06_14번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[955,956,976], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 2방향 순차적 소환 :  패턴5  : 근2-3-2-2-3-2, 원3,6빼고
class 몬스터출현06_15번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[948,949,979], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_15번생성_02(self.ctx)


class 몬스터출현06_15번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[968,969,960,978], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_15번생성_03(self.ctx)


class 몬스터출현06_15번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[948,949], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_15번생성_04(self.ctx)


class 몬스터출현06_15번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[963,964,973], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_15번생성_05(self.ctx)


class 몬스터출현06_15번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[953,954,955,974], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_15번생성_06(self.ctx)


class 몬스터출현06_15번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[943,944], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 몬스터출현06_생성랜덤04(self.ctx)


# 마지막 웨이브 : 전방향 순차적 소환 : 근거리4 원거리 1/ 근거리5 원거리2/ 근거리4 원거리 1/ 근거리5 원거리2
class 몬스터출현06_생성랜덤04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 몬스터출현06_16번생성_01(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_17번생성_01(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_18번생성_01(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_19번생성_01(self.ctx)
        if self.random_condition(rate=20):
            return 몬스터출현06_20번생성_01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴1 : 근거리4 원거리1/ 근거리5 원거리2/ 근거리4 원거리 1/ 근거리5 원거리2
class 몬스터출현06_16번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[941,942,971], animationEffect=False) # 근거리4 원거리1 , 123

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_16번생성_02(self.ctx)


class 몬스터출현06_16번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[951,953], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_16번생성_03(self.ctx)


class 몬스터출현06_16번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[954,955,956,986], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_16번생성_04(self.ctx)


class 몬스터출현06_16번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[964,965,985], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_16번생성_05(self.ctx)


class 몬스터출현06_16번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[953,954], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_16번생성_06(self.ctx)


class 몬스터출현06_16번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[964,965,974], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_16번생성_07(self.ctx)


class 몬스터출현06_16번생성_07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[947,948,949,988], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_16번생성_08(self.ctx)


class 몬스터출현06_16번생성_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[967,968,987], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴2 : 근거리4 원거리1/ 근거리5 원거리2/ 근거리4 원거리 1/ 근거리5 원거리2
class 몬스터출현06_17번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[954,955,956,986], animationEffect=False) # 근거리5 원거리2 ,456

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_17번생성_02(self.ctx)


class 몬스터출현06_17번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[964,965,985], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_17번생성_03(self.ctx)


class 몬스터출현06_17번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[941,942,971], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_17번생성_04(self.ctx)


class 몬스터출현06_17번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[951,953], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_17번생성_05(self.ctx)


class 몬스터출현06_17번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[947,948,949,988], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_17번생성_06(self.ctx)


class 몬스터출현06_17번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[967,968,987], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_17번생성_07(self.ctx)


class 몬스터출현06_17번생성_07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[953,954], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_17번생성_08(self.ctx)


class 몬스터출현06_17번생성_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[964,965,974], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴3 : 근거리4 원거리1/ 근거리5 원거리2/ 근거리4 원거리 1/ 근거리5 원거리2
class 몬스터출현06_18번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[959,958], animationEffect=False) # 근거리4 원거리1 , 890

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_18번생성_02(self.ctx)


class 몬스터출현06_18번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[949,940,970], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_18번생성_03(self.ctx)


class 몬스터출현06_18번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[953,954,955,983], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_18번생성_04(self.ctx)


class 몬스터출현06_18번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[943,945,984], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_18번생성_05(self.ctx)


class 몬스터출현06_18번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[961,962], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_18번생성_06(self.ctx)


class 몬스터출현06_18번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[952,953,972], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_18번생성_07(self.ctx)


class 몬스터출현06_18번생성_07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[945,946,947,985], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_18번생성_08(self.ctx)


class 몬스터출현06_18번생성_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[966,967,986], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴4 : 근거리5 원거리1/ 근거리4 원거리2/ 근거리5 원거리 1/ 근거리4 원거리2
class 몬스터출현06_19번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[943,944,945,974], animationEffect=False) # 근거리5 원거리1 , 345

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_19번생성_02(self.ctx)


class 몬스터출현06_19번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[963,965], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_19번생성_03(self.ctx)


class 몬스터출현06_19번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[951,950,980], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_19번생성_04(self.ctx)


class 몬스터출현06_19번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[941,942,981], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_19번생성_05(self.ctx)


class 몬스터출현06_19번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[957,958], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_19번생성_06(self.ctx)


class 몬스터출현06_19번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[966,968,977], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_19번생성_07(self.ctx)


class 몬스터출현06_19번생성_07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[948,949,989], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_19번생성_08(self.ctx)


class 몬스터출현06_19번생성_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[959,958,988], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


# 마지막 웨이브 : 4방향 순차적 소환 :  패턴5 : 근거리5 원거리1/ 근거리4 원거리2/ 근거리5 원거리 1/ 근거리4 원거리2
class 몬스터출현06_20번생성_01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[967,968,969], animationEffect=False) # 근거리5 원거리1 , 789

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_20번생성_02(self.ctx)


class 몬스터출현06_20번생성_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[957,959,978], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_20번생성_03(self.ctx)


class 몬스터출현06_20번생성_03(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[953,954,984], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_20번생성_04(self.ctx)


class 몬스터출현06_20번생성_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[943,944,983], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_20번생성_05(self.ctx)


class 몬스터출현06_20번생성_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[951,952,950], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_20번생성_06(self.ctx)


class 몬스터출현06_20번생성_06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[962,961,970], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터출현06_20번생성_07(self.ctx)


class 몬스터출현06_20번생성_07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[946,947,986], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터출현06_20번생성_08(self.ctx)


class 몬스터출현06_20번생성_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[955,956,985], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989]):
            return 보스전투_준비01(self.ctx)


class 보스전투_준비01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보스전투_준비02(self.ctx)


class 보스전투_준비02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=811, enable=True)
        self.set_skip(state=보스전투_준비04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보스전투_준비03(self.ctx)


class 보스전투_준비03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__908$')
        self.set_effect(triggerIds=[777902], visible=False) # KaseMu Voice02
        self.set_effect(triggerIds=[777903], visible=True) # KaseMu Voice03

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보스전투_준비04(self.ctx)


class 보스전투_준비04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=811, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스전투_시작01(self.ctx)


class 보스전투_시작01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[990])
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__807$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드
        self.create_monster(spawnIds=[999], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[999]):
            return 보스도망준비01(self.ctx)


class 보스도망준비01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보스도망연출01(self.ctx)


class 보스도망연출01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1000], animationEffect=False)
        self.set_interact_object(triggerIds=[10000776], state=0) # 마지막꼬마 CAGE 열수있는 철창 켜기
        self.set_interact_object(triggerIds=[10000776], state=1) # 마지막꼬마 CAGE 열수있는 철창 켜기
        self.set_actor(triggerId=97770, visible=False, initialSequence='Closed') # 마지막꼬마 CAGE 액터 감추기
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__909$')
        self.select_camera(triggerId=812, enable=True)
        self.set_skip(state=보스도망연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보스도망연출02(self.ctx)


class 보스도망연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3, script='$02000331_BF__Seeker01__910$')
        self.set_effect(triggerIds=[777903], visible=False) # KaseMu Voice03
        self.set_effect(triggerIds=[777904], visible=True) # KaseMu Voice04
        self.set_skip(state=보스도망연출03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스도망연출03(self.ctx)


class 보스도망연출03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=812, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.change_monster(removeSpawnId=610, addSpawnId=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스전투_끝01(self.ctx)


class 보스전투_끝01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000331_BF__Seeker01__808$', arg3='3000', arg4='0')
        self.set_conversation(type=1, spawnId=600, script='$02000331_BF__Seeker01__120$', arg4=2, arg5=1)
        self.destroy_monster(spawnIds=[1000])
        self.set_effect(triggerIds=[7771], visible=True) # UI  메시지 알림 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마지막연출_준비01(self.ctx)


class 마지막연출_준비01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003315, textId=20003315) # 가이드 : 갇혀 있는 리안을 구해 주세요.

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000776]):
            return 마지막연출_포털출현01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20003315)
        self.set_interact_object(triggerIds=[10000776], state=0) # 마지막꼬마 CAGE 열수있는 철창 켜기


class 마지막연출_포털출현01(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=7, arg2='$02000331_BF__Seeker01__809$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마지막연출_포털출현02(self.ctx)


class 마지막연출_포털출현02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=600, patrolName='MS2PatrolData_6001')
        self.set_effect(triggerIds=[777904], visible=False) # KaseMu Voice04

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마지막연출_포털출현03(self.ctx)


class 마지막연출_포털출현03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=600, script='$02000331_BF__Seeker01__130$', arg4=2, arg5=0)
        self.set_effect(triggerIds=[99999], visible=True) # 치유 이펙트
        self.set_effect(triggerIds=[7772], visible=True) # 치유 사운드

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9020, spawnIds=[600]):
            return 마지막연출_포털출현04(self.ctx)


class 마지막연출_포털출현04(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[99999], visible=False) # 치유 이펙트
        self.change_monster(removeSpawnId=601, addSpawnId=110)
        self.change_monster(removeSpawnId=602, addSpawnId=210)
        self.change_monster(removeSpawnId=603, addSpawnId=310)
        self.change_monster(removeSpawnId=604, addSpawnId=410)
        self.change_monster(removeSpawnId=605, addSpawnId=510)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마지막연출_시작01(self.ctx)


class 마지막연출_시작01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=410, patrolName='MS2PatrolData_4007')
        self.move_npc(spawnId=510, patrolName='MS2PatrolData_5005')
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_1015')
        self.move_npc(spawnId=210, patrolName='MS2PatrolData_2012')
        self.move_npc(spawnId=310, patrolName='MS2PatrolData_3011')
        self.move_npc(spawnId=600, patrolName='MS2PatrolData_6002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마지막연출_시작02(self.ctx)


class 마지막연출_시작02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=110, script='$02000331_BF__Seeker01__131$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=310, script='$02000331_BF__Seeker01__132$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=410, script='$02000331_BF__Seeker01__133$', arg4=2, arg5=4)
        self.set_conversation(type=1, spawnId=600, script='$02000331_BF__Seeker01__136$', arg4=2, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 던전클리어01(self.ctx)


class 던전클리어01(trigger_api.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[90090,90091,90092,90093,90094,90095,90096,90097,90098,90099], visible=False, meshCount=10, arg4=100, delay=100) # 클리어포털 나타남
        self.change_monster(removeSpawnId=110, addSpawnId=111) # Quest Npc 교체

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 퇴장시작01(self.ctx)

    def on_exit(self):
        self.dungeon_clear()
        self.set_achievement(triggerId=99998, type='trigger', achieve='ClearHideandSeek') # ClearHideandSeek 퀘스트
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 클리어포털 나타남


class 퇴장시작01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=210, script='$02000331_BF__Seeker01__134$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=510, script='$02000331_BF__Seeker01__135$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=111, script='$02000331_BF__Seeker01__137$', arg4=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[11000], visible=False) # 입구로 되돌아 가는 길 막기
        self.set_agent(triggerIds=[11001], visible=False) # 입구로 되돌아 가는 길 막기
        self.set_agent(triggerIds=[15000], visible=False) # 끊어진 다리 길 막기
        self.set_agent(triggerIds=[15001], visible=False) # 끊어진 다리 길 막기
        self.set_agent(triggerIds=[15002], visible=False) # 끊어진 다리 길 막기
        self.set_agent(triggerIds=[16000], visible=False) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16001], visible=False) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16002], visible=False) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16003], visible=False) # 새로운 다리 길 막기
        self.set_agent(triggerIds=[16004], visible=False) # 새로운 다리 길 막기


initial_state = 대기
