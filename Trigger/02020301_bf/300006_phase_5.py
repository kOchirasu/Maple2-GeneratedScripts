""" trigger/02020301_bf/300006_phase_5.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='AI_Phase', value=5):
            return 패이즈_5_시작()


class 패이즈_5_시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111])
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300006_PHASE_5__0$', duration=3176)
        set_effect(triggerIds=[200021,200022,200023,200024,200025,200026,200027,200028], visible=False)
        set_user_value(key='AI_Phase', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Portal_On_04', value=1):
            return 포탈_오픈_대기()


class 포탈_오픈_대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포탈_오픈()


class 포탈_오픈(state.State):
    def on_enter(self):
        set_user_value(triggerId=3000051, key='Phase_4_Interect_01', value=0) # 페이즈4 장치 삭제
        set_user_value(triggerId=3000052, key='Phase_4_Interect_02', value=0)
        set_user_value(triggerId=3000053, key='Phase_4_Interect_03', value=0)
        set_user_value(triggerId=3000054, key='Phase_4_Interect_04', value=0)
        set_effect(triggerIds=[200001,200002,200003,200004,200005,200006,200007,200008], visible=False)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300006_PHASE_5__1$', duration=3176)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1002]):
            return 엘리베이터_동작_대기()


class 엘리베이터_동작_대기(state.State):
    def on_enter(self):
        set_ai_extra_data(key='Last_Phase', value=1, isModify=False)
        set_user_value(triggerId=3000051, key='Phase_4_Interect_01', value=0) # 초고속 플레이에 인해 트리거가 제거 되지 않는 문제를 항번더 입력
        set_user_value(triggerId=3000052, key='Phase_4_Interect_02', value=0)
        set_user_value(triggerId=3000053, key='Phase_4_Interect_03', value=0)
        set_user_value(triggerId=3000054, key='Phase_4_Interect_04', value=0)
        set_effect(triggerIds=[200001,200002,200003,200004,200005,200006,200007,200008], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 택스트_1()


class 택스트_1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300006_PHASE_5__2$', duration=3176)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 택스트_2()


class 택스트_2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_normal', script='$02020301_BF__300006_PHASE_5__3$', duration=3176)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 엘리베이터_동작()


class 엘리베이터_동작(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410], enabled=True) # 5페이즈 상하 엘리베이터 동작
        set_breakable(triggerIds=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420], enabled=True)
        set_breakable(triggerIds=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430], enabled=True)
        set_breakable(triggerIds=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440], enabled=True)
        set_visible_breakable_object(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410], arg2=True) # 5페이즈 상하 엘리베이터 동작 보이기
        set_visible_breakable_object(triggerIds=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420], arg2=True)
        set_visible_breakable_object(triggerIds=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430], arg2=True)
        set_visible_breakable_object(triggerIds=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 엘리베이터_도착()


class 엘리베이터_도착(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512,5513,5514,5515,5516,5517,5518,5519,5520,5521,5522,5523,5524,5525,5526,5527,5528,5529,5530,5531,5532,5533,5534,5535,5536,5537,5538,5539,5540], arg2=True) # 5페이즈 상하 엘리베이터 도착 나타나기
        set_breakable(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410], enabled=False) # 5페이즈 상하 엘리베이터 멈춤
        set_breakable(triggerIds=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420], enabled=False)
        set_breakable(triggerIds=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430], enabled=False)
        set_breakable(triggerIds=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440], enabled=False)
        set_visible_breakable_object(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410], arg2=False) # 5페이즈 상하 엘리베이터 동작 숨기기
        set_visible_breakable_object(triggerIds=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420], arg2=False)
        set_visible_breakable_object(triggerIds=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430], arg2=False)
        set_visible_breakable_object(triggerIds=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아르케온_탈것_생성()


class 아르케온_탈것_생성(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020301_BF__300006_PHASE_5__4$', arg3='4000')
        set_user_value(triggerId=3000061, key='Phase_5_Interect_01', value=1) # 아르케온 탈것 페이즈로 이동
        set_user_value(triggerId=3000062, key='Phase_5_Interect_02', value=1)
        set_user_value(triggerId=3000063, key='Phase_5_Interect_03', value=1)
        set_user_value(triggerId=3000064, key='Phase_5_Interect_04', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 길막열기()


class 길막열기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5641,5642,5643,5644], visible=False) # 4페이즈 상하좌우 엘리베이터 길막 열기
        set_agent(triggerIds=[1810000,1810001,1810002,1810003,1810004,1810005,1810006,1810007,1810008,1810009,1810010,1810011], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 아르케온_탈것_리셋()


class 아르케온_탈것_리셋(state.State):
    def on_enter(self):
        set_user_value(triggerId=3000061, key='Phase_5_Interect_01', value=0) # 아르케온 탈것 리셋
        set_user_value(triggerId=3000062, key='Phase_5_Interect_02', value=0)
        set_user_value(triggerId=3000063, key='Phase_5_Interect_03', value=0)
        set_user_value(triggerId=3000064, key='Phase_5_Interect_04', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return None # Missing State: 게임_종료


