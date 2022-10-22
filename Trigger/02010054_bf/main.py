""" trigger/02010054_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 준비(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_gravity(gravity=-9.8)
        set_interact_object(triggerIds=[10000856], state=2)
        set_interact_object(triggerIds=[10000857], state=2)
        set_interact_object(triggerIds=[10000858], state=2)
        set_interact_object(triggerIds=[10000859], state=2)
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3003], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3315,3316,3317,3318,3319,3320,3321], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3130,3131,3132,3133,3134,3135,3136], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615,3616,3617,3618,3619,3620], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3330], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[600], visible=True)
        set_effect(triggerIds=[6000], visible=False)
        set_effect(triggerIds=[6001], visible=False)
        set_effect(triggerIds=[6002], visible=False)
        set_effect(triggerIds=[6003], visible=False)
        set_effect(triggerIds=[6004], visible=False)
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[607], visible=True)
        set_effect(triggerIds=[608], visible=True)
        set_effect(triggerIds=[609], visible=True)
        set_effect(triggerIds=[612], visible=True)
        set_effect(triggerIds=[613], visible=True)
        set_effect(triggerIds=[614], visible=True)
        set_effect(triggerIds=[615], visible=True)
        set_effect(triggerIds=[616], visible=True)
        set_effect(triggerIds=[620], visible=False)
        set_effect(triggerIds=[621], visible=False)
        set_effect(triggerIds=[622], visible=False)
        set_effect(triggerIds=[625], visible=True)
        set_effect(triggerIds=[626], visible=True)
        set_effect(triggerIds=[627], visible=True)
        set_effect(triggerIds=[628], visible=True)
        set_effect(triggerIds=[629], visible=True)
        create_monster(spawnIds=[2099], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)
        select_camera(triggerId=301, enable=True)
        set_skip(state=인트로연출스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출해제()

state.DungeonStart = DungeonStart


class 연출해제(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            return 시작()


class 인트로연출스킵(state.State):
    def on_enter(self):
        set_skip()
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            remove_buff(boxId=199, skillId=70000107)
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_skip()
        remove_buff(boxId=199, skillId=70000107)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20105407, textId=20105407, duration=3500)
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[6000], visible=False)
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[2001,2002,2003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 반응대기01()


class 반응대기01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20105401, textId=20105401)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_interact_object(triggerIds=[10000856], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000856], arg2=0):
            hide_guide_summary(entityId=20105401)
            set_gravity(gravity=-39)
            return 반응대기02()


class 반응대기02(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000860,10000861], arg2=0):
            set_event_ui(type=1, arg2='$02010054_BF__MAIN__1$', arg3='5000', arg4='0')
            set_interact_object(triggerIds=[10000858], state=1)
            return 반응대기03()


class 반응대기03(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000858], arg2=0):
            set_effect(triggerIds=[607], visible=False)
            set_effect(triggerIds=[608], visible=False)
            set_effect(triggerIds=[609], visible=False)
            set_effect(triggerIds=[6001], visible=False)
            set_effect(triggerIds=[6002], visible=True)
            set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222], visible=True, arg3=0, arg4=50, arg5=1)
            set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123], visible=True, arg3=0, arg4=50, arg5=1)
            set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615,3616,3617,3618,3619,3620], visible=True, arg3=0, arg4=50, arg5=1)
            set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513,3514,3515,3516,3517,3518,3519,3520], visible=True, arg3=0, arg4=50, arg5=1)
            create_monster(spawnIds=[2011,2014,2015,2020,2021], arg2=False)
            set_gravity(gravity=-9.8)
            return 인원체크()


class 인원체크(state.State):
    def on_tick(self) -> state.State:
        if dungeon_max_user_count(value=1):
            return 반응둘중하나만()
        if wait_tick(waitTick=100):
            return 반응둘다01()


class 반응둘다01(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000884,10000885], arg2=0):
            return 반응대기05()


class 반응둘중하나만(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000884], arg2=0):
            return 반응대기05()
        if object_interacted(interactIds=[10000885], arg2=0):
            return 반응대기05()


class 반응대기05(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000857], state=1)
        set_interact_object(triggerIds=[10000859], state=1)
        show_guide_summary(entityId=20105401, textId=20105401)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000857], arg2=0):
            hide_guide_summary(entityId=20105401)
            set_gravity(gravity=-39)
            return 별생성()


class 별생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3315,3316,3317,3318,3319,3320,3321], visible=True, arg3=0, arg4=500, arg5=3)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            set_mesh(triggerIds=[3315,3316,3317,3318,3319,3320,3321], visible=False, arg3=0, arg4=900, arg5=2)
            return 반응대기06()


class 반응대기06(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000859], arg2=0):
            set_mesh(triggerIds=[3330], visible=True, arg3=0, arg4=0, arg5=3)
            set_portal(portalId=10, visible=False, enabled=True, minimapVisible=False)
            set_gravity(gravity=-9.8)
            return 중간보스소환()


class 중간보스소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2098], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2098]):
            set_effect(triggerIds=[6003], visible=False)
            return 골렘소환대기()


class 골렘소환대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[612], visible=False)
        set_effect(triggerIds=[613], visible=False)
        set_effect(triggerIds=[614], visible=False)
        set_effect(triggerIds=[615], visible=False)
        set_effect(triggerIds=[616], visible=False)
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return 골렘소환()


class 골렘소환(state.State):
    def on_enter(self):
        set_effect(triggerIds=[620], visible=True)
        create_monster(spawnIds=[2024], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 골렘소환2()


class 골렘소환2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[621], visible=True)
        create_monster(spawnIds=[2025], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 골렘소환3()


class 골렘소환3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[622], visible=True)
        create_monster(spawnIds=[2026], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2024,2025,2026]):
            return 그라즈나전투()


class 그라즈나전투(state.State):
    def on_enter(self):
        set_effect(triggerIds=[625], visible=False)
        set_effect(triggerIds=[626], visible=False)
        set_effect(triggerIds=[627], visible=False)
        set_effect(triggerIds=[628], visible=False)
        set_effect(triggerIds=[629], visible=False)
        set_effect(triggerIds=[6004], visible=False)
        set_mesh(triggerIds=[3003], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 종료딜레이()


class 종료딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3130,3131,3132,3133,3134,3135,3136], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_timer(timerId='4', seconds=4)
        dungeon_clear()

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 종료()


class 종료(state.State):
    pass


