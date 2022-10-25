""" trigger/02020145_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[183,189,201])
        self.set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        self.set_effect(triggerIds=[200031,200032,200033,200034,200035], visible=False) # triggerbox 1002 풀밭 안내 화살표 끄기
        self.set_effect(triggerIds=[200001,200002,200003,200004,200005], visible=False) # triggerbox 1003 라펜턴드 안내 화살표 끄기
        self.set_effect(triggerIds=[200021,200022,200023,200024,200025], visible=False) # triggerbox 1004 화염 안내 화살표 끄기
        self.set_effect(triggerIds=[200011,200012,200013,200014,200015], visible=False) # triggerbox 1005 얼음 안내 화살표 끄기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1007]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=1006, skillId=70002151, isPlayer=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1007]):
            return 보스전_시작(self.ctx)


class 보스전_시작(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__0$', duration=5684, voice='ko/Npc/00002201')
        self.create_monster(spawnIds=[101])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5684):
            return 조명변경(self.ctx)


class 조명변경(common.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[52,48,38])
        self.set_directional_light(diffuseColor=[0,0,0], specularColor=[206,174,84])
        self.add_buff(boxIds=[101], skillId=62100014, level=1, isPlayer=True)
        self.add_buff(boxIds=[1001], skillId=75000001, level=1) # 캐릭터 밝히기
        self.create_monster(spawnIds=[121,123,125,131,132,133])

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 보스전_성공(self.ctx)
        if self.wait_tick(waitTick=6000):
            return 페이드인(self.ctx)


class 페이드인(common.Trigger):
    def on_enter(self):
        self.npc_remove_additional_effect(spawnId=101, additionalEffectId=62100014) # 위에 걸린 62100014 : 렌듀비앙 어둠의 기운 삭제

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 조명리셋(self.ctx)


class 조명리셋(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$02020111_BF__MOVEMENT_01__1$', arg4=3, arg5=0) # 하하핫, 제법이군... 끝까지 한번 버텨봐라!!
        self.destroy_monster(spawnIds=[121,122,123,124,125,131,132,133,134])
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_ambient_light(primary=[183,189,201])
        self.set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        self.add_buff(boxIds=[1001], skillId=75000002, level=1)
        self.add_buff(boxIds=[1002], skillId=75000002, level=1)
        self.add_buff(boxIds=[1003], skillId=75000002, level=1)
        self.add_buff(boxIds=[1004], skillId=75000002, level=1)
        self.add_buff(boxIds=[1005], skillId=75000002, level=1)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 보스전_성공(self.ctx)
        if self.wait_tick(waitTick=15000):
            return 조건확인(self.ctx)


class 조건확인(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 보스전_성공(self.ctx)
        if self.check_npc_hp(compare='higherEqual', value=50, spawnId=101, isRelative=True):
            return 조명변경(self.ctx)
        if self.check_npc_hp(compare='lowerEqual', value=50, spawnId=101, isRelative=True):
            return 조건추가(self.ctx)


class 조건추가(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 보스전_성공(self.ctx)


class 보스전_성공(common.Trigger):
    def on_enter(self):
        self.set_achievement(type='trigger', achieve='ClearBlueLapenta_Quest')
        self.side_npc_talk(type='talk', npcId=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__1$', duration=3176, voice='ko/Npc/00002202') # 크윽.....네놈들.... 두고보자!!
        self.destroy_monster(spawnIds=[121,122,123,124,125,131,132,133,134])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3176):
            return 조명리셋2(self.ctx)


class 조명리셋2(common.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[183,189,201])
        self.set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])
        self.add_buff(boxIds=[1001], skillId=75000002, level=1)
        self.add_buff(boxIds=[1002], skillId=75000002, level=1)
        self.add_buff(boxIds=[1003], skillId=75000002, level=1)
        self.add_buff(boxIds=[1004], skillId=75000002, level=1)
        self.add_buff(boxIds=[1005], skillId=75000002, level=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_achievement(type='trigger', achieve='ClearBlueLapenta_Quest')
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
