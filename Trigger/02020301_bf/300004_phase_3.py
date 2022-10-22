""" trigger/02020301_bf/300004_phase_3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[200011,200012,200013,200014,200015,200016,200017,200018], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='AI_Phase', value=3):
            return 패이즈_3_시작()


class 패이즈_3_시작(state.State):
    def on_enter(self):
        add_buff(boxIds=[1003], skillId=62100168, level=1) # 포탑 기절 이뮨
        destroy_monster(spawnIds=[701])
        destroy_monster(spawnIds=[702])
        destroy_monster(spawnIds=[703])
        destroy_monster(spawnIds=[704])
        destroy_monster(spawnIds=[705])
        destroy_monster(spawnIds=[706])
        set_user_value(triggerId=3000032, key='Phase_2_Interect_02', value=0)
        set_user_value(triggerId=3000033, key='Phase_2_Interect_03', value=0)
        set_user_value(triggerId=3000034, key='Phase_2_Interect_04', value=0)
        set_user_value(triggerId=3000035, key='Phase_2_Interect_05', value=0)
        set_user_value(triggerId=3000036, key='Phase_2_Interect_06', value=0)
        set_user_value(triggerId=3000037, key='Phase_2_Interect_07', value=0)
        remove_buff(boxId=1001, skillId=73000004, arg3=True)
        set_user_value(triggerId=3000031, key='Phase_2_Interect_01', value=0) # 아르케온 탈것 인터렉트 제거
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300004_PHASE_3__0$', duration=3176)
        side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$02020301_BF__300004_PHASE_3__1$', duration=3176)
        set_user_value(key='AI_Phase', value=0)
        set_visible_breakable_object(triggerIds=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184], arg2=True)
        set_visible_breakable_object(triggerIds=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164], arg2=True)
        set_breakable(triggerIds=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184], enabled=True) # 좌우 이동 엘리베이터 동작
        set_breakable(triggerIds=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164], enabled=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 엘리베이터_도착()


class 엘리베이터_도착(state.State):
    def on_enter(self):
        set_user_value(key='AI_Phase', value=0)
        set_visible_breakable_object(triggerIds=[5351,5352,5353,5354,5355,5356,5357,5358,5359,5360,5361,5362,5363,5364], arg2=True) # 좌우 이동 엘리베이터  도착 후 재생
        set_visible_breakable_object(triggerIds=[5371,5372,5373,5374,5375,5376,5377,5378,5379,5380,5381,5382,5383,5384], arg2=True)
        set_breakable(triggerIds=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184], enabled=False) # 좌우 이동 엘리베이터 멈춤 후, 숨기기
        set_breakable(triggerIds=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164], enabled=False)
        set_visible_breakable_object(triggerIds=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184], arg2=False)
        set_visible_breakable_object(triggerIds=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포탑_생성()


class 포탑_생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[512], arg2=True) # 포탑 소환
        create_monster(spawnIds=[511], arg2=True)
        set_user_value(triggerId=3000041, key='Phase_3_Interect_01', value=1) # 포탑 발사 트리거로 명령
        set_user_value(triggerId=3000042, key='Phase_3_Interect_02', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 가이드()


class 가이드(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020301_BF__300004_PHASE_3__2$', arg3='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return None # Missing State: 엘리베이터_대기


