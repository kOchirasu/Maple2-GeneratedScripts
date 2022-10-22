""" trigger/02020145_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        set_effect(triggerIds=[200031,200032,200033,200034,200035], visible=False) # triggerbox 1002 풀밭 안내 화살표 끄기
        set_effect(triggerIds=[200001,200002,200003,200004,200005], visible=False) # triggerbox 1003 라펜턴드 안내 화살표 끄기
        set_effect(triggerIds=[200021,200022,200023,200024,200025], visible=False) # triggerbox 1004 화염 안내 화살표 끄기
        set_effect(triggerIds=[200011,200012,200013,200014,200015], visible=False) # triggerbox 1005 얼음 안내 화살표 끄기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1007]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        remove_buff(boxId=1006, skillId=70002151, arg3=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1007]):
            return 보스전_시작()


class 보스전_시작(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__0$', duration=5684, voice='ko/Npc/00002201')
        create_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5684):
            return 조명변경()


class 조명변경(state.State):
    def on_enter(self):
        set_ambient_light(primary=[52,48,38])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])
        add_buff(boxIds=[101], skillId=62100014, level=1, arg4=True)
        add_buff(boxIds=[1001], skillId=75000001, level=1) # 캐릭터 밝히기
        create_monster(spawnIds=[121,123,125,131,132,133])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 보스전_성공()
        if wait_tick(waitTick=6000):
            return 페이드인()


class 페이드인(state.State):
    def on_enter(self):
        npc_remove_additional_effect(spawnId=101, additionalEffectId=62100014) # 위에 걸린 62100014 : 렌듀비앙 어둠의 기운 삭제

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조명리셋()


class 조명리셋(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02020111_BF__MOVEMENT_01__1$', arg4=3, arg5=0) # 하하핫, 제법이군... 끝까지 한번 버텨봐라!!
        destroy_monster(spawnIds=[121,122,123,124,125,131,132,133,134])
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        add_buff(boxIds=[1001], skillId=75000002, level=1)
        add_buff(boxIds=[1002], skillId=75000002, level=1)
        add_buff(boxIds=[1003], skillId=75000002, level=1)
        add_buff(boxIds=[1004], skillId=75000002, level=1)
        add_buff(boxIds=[1005], skillId=75000002, level=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 보스전_성공()
        if wait_tick(waitTick=15000):
            return 조건확인()


class 조건확인(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 보스전_성공()
        if check_npc_hp(compare='higherEqual', value=50, spawnId=101, isRelative=True):
            return 조명변경()
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=101, isRelative=True):
            return 조건추가()


class 조건추가(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 보스전_성공()


class 보스전_성공(state.State):
    def on_enter(self):
        set_achievement(type='trigger', achieve='ClearBlueLapenta_Quest')
        side_npc_talk(type='talk', npcId=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__1$', duration=3176, voice='ko/Npc/00002202') # 크윽.....네놈들.... 두고보자!!
        destroy_monster(spawnIds=[121,122,123,124,125,131,132,133,134])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3176):
            return 조명리셋2()


class 조명리셋2(state.State):
    def on_enter(self):
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        add_buff(boxIds=[1001], skillId=75000002, level=1)
        add_buff(boxIds=[1002], skillId=75000002, level=1)
        add_buff(boxIds=[1003], skillId=75000002, level=1)
        add_buff(boxIds=[1004], skillId=75000002, level=1)
        add_buff(boxIds=[1005], skillId=75000002, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_achievement(type='trigger', achieve='ClearBlueLapenta_Quest')
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)


