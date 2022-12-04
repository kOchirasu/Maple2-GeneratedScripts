""" trigger/02010054_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_gravity(gravity=-9.8)
        self.set_interact_object(triggerIds=[10000856], state=2)
        self.set_interact_object(triggerIds=[10000857], state=2)
        self.set_interact_object(triggerIds=[10000858], state=2)
        self.set_interact_object(triggerIds=[10000859], state=2)
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3315,3316,3317,3318,3319,3320,3321], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3130,3131,3132,3133,3134,3135,3136], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615,3616,3617,3618,3619,3620], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3330], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[600], visible=True)
        self.set_effect(triggerIds=[6000], visible=False)
        self.set_effect(triggerIds=[6001], visible=False)
        self.set_effect(triggerIds=[6002], visible=False)
        self.set_effect(triggerIds=[6003], visible=False)
        self.set_effect(triggerIds=[6004], visible=False)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_effect(triggerIds=[607], visible=True)
        self.set_effect(triggerIds=[608], visible=True)
        self.set_effect(triggerIds=[609], visible=True)
        self.set_effect(triggerIds=[612], visible=True)
        self.set_effect(triggerIds=[613], visible=True)
        self.set_effect(triggerIds=[614], visible=True)
        self.set_effect(triggerIds=[615], visible=True)
        self.set_effect(triggerIds=[616], visible=True)
        self.set_effect(triggerIds=[620], visible=False)
        self.set_effect(triggerIds=[621], visible=False)
        self.set_effect(triggerIds=[622], visible=False)
        self.set_effect(triggerIds=[625], visible=True)
        self.set_effect(triggerIds=[626], visible=True)
        self.set_effect(triggerIds=[627], visible=True)
        self.set_effect(triggerIds=[628], visible=True)
        self.set_effect(triggerIds=[629], visible=True)
        self.create_monster(spawnIds=[2099], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.select_camera(triggerId=301, enable=True)
        self.set_skip(state=인트로연출스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출해제(self.ctx)


class 연출해제(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return 시작(self.ctx)


class 인트로연출스킵(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            self.remove_buff(boxId=199, skillId=70000107)
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_buff(boxId=199, skillId=70000107)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20105407, textId=20105407, duration=3500)
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[6000], visible=False)
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[2001,2002,2003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 반응대기01(self.ctx)


class 반응대기01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20105401, textId=20105401)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10000856], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000856], stateValue=0):
            self.hide_guide_summary(entityId=20105401)
            self.set_gravity(gravity=-39)
            return 반응대기02(self.ctx)


class 반응대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000860,10000861], stateValue=0):
            self.set_event_ui(type=1, arg2='$02010054_BF__MAIN__1$', arg3='5000', arg4='0')
            self.set_interact_object(triggerIds=[10000858], state=1)
            return 반응대기03(self.ctx)


class 반응대기03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000858], stateValue=0):
            self.set_effect(triggerIds=[607], visible=False)
            self.set_effect(triggerIds=[608], visible=False)
            self.set_effect(triggerIds=[609], visible=False)
            self.set_effect(triggerIds=[6001], visible=False)
            self.set_effect(triggerIds=[6002], visible=True)
            self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222], visible=True, arg3=0, delay=50, scale=1)
            self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123], visible=True, arg3=0, delay=50, scale=1)
            self.set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615,3616,3617,3618,3619,3620], visible=True, arg3=0, delay=50, scale=1)
            self.set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520], visible=True, arg3=0, delay=50, scale=1)
            self.create_monster(spawnIds=[2011,2014,2015,2020,2021], animationEffect=False)
            self.set_gravity(gravity=-9.8)
            return 인원체크(self.ctx)


class 인원체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_max_user_count(value=1):
            return 반응둘중하나만(self.ctx)
        if self.wait_tick(waitTick=100):
            return 반응둘다01(self.ctx)


class 반응둘다01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000884,10000885], stateValue=0):
            return 반응대기05(self.ctx)


class 반응둘중하나만(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000884], stateValue=0):
            return 반응대기05(self.ctx)
        if self.object_interacted(interactIds=[10000885], stateValue=0):
            return 반응대기05(self.ctx)


class 반응대기05(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000857], state=1)
        self.set_interact_object(triggerIds=[10000859], state=1)
        self.show_guide_summary(entityId=20105401, textId=20105401)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000857], stateValue=0):
            self.hide_guide_summary(entityId=20105401)
            self.set_gravity(gravity=-39)
            return 별생성(self.ctx)


class 별생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3315,3316,3317,3318,3319,3320,3321], visible=True, arg3=0, delay=500, scale=3)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.set_mesh(triggerIds=[3315,3316,3317,3318,3319,3320,3321], visible=False, arg3=0, delay=900, scale=2)
            return 반응대기06(self.ctx)


class 반응대기06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000859], stateValue=0):
            self.set_mesh(triggerIds=[3330], visible=True, arg3=0, delay=0, scale=3)
            self.set_portal(portalId=10, visible=False, enable=True, minimapVisible=False)
            self.set_gravity(gravity=-9.8)
            return 중간보스소환(self.ctx)


class 중간보스소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2098], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2098]):
            self.set_effect(triggerIds=[6003], visible=False)
            return 골렘소환대기(self.ctx)


class 골렘소환대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[612], visible=False)
        self.set_effect(triggerIds=[613], visible=False)
        self.set_effect(triggerIds=[614], visible=False)
        self.set_effect(triggerIds=[615], visible=False)
        self.set_effect(triggerIds=[616], visible=False)
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[107]):
            return 골렘소환(self.ctx)


class 골렘소환(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[620], visible=True)
        self.create_monster(spawnIds=[2024], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 골렘소환2(self.ctx)


class 골렘소환2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[621], visible=True)
        self.create_monster(spawnIds=[2025], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 골렘소환3(self.ctx)


class 골렘소환3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[622], visible=True)
        self.create_monster(spawnIds=[2026], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2024,2025,2026]):
            return 그라즈나전투(self.ctx)


class 그라즈나전투(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[625], visible=False)
        self.set_effect(triggerIds=[626], visible=False)
        self.set_effect(triggerIds=[627], visible=False)
        self.set_effect(triggerIds=[628], visible=False)
        self.set_effect(triggerIds=[629], visible=False)
        self.set_effect(triggerIds=[6004], visible=False)
        self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3130,3131,3132,3133,3134,3135,3136], visible=True, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_timer(timerId='4', seconds=4)
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
