""" trigger/52100001_qd/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 퀘스트체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[1]):
            return 대기()
        if quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[2]):
            return 퀘스트완료가능이거나완료1()
        if quest_user_detected(boxIds=[199], questIds=[50100060], questStates=[3]):
            return 퀘스트완료가능이거나완료1()


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10001108], state=2)
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3901,3902,3903,3904], visible=True, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1099,2094,2095,2096,2097,2098,2099], arg2=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_skip(state=연출종료)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=300, enable=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 부선장대사01()

state.DungeonStart = DungeonStart


class 부선장대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=24003011, script='$02000391_BF__MAIN__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 해적이동01()


class 해적이동01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2099, script='$02000391_BF__MAIN__1$', arg4=3, arg5=0)
        set_npc_emotion_sequence(spawnId=1099, sequenceName='Attack_01_C')
        select_camera(triggerId=301, enable=True)
        move_npc(spawnId=2094, patrolName='MS2PatrolData_2094A')
        move_npc(spawnId=2095, patrolName='MS2PatrolData_2095A')
        move_npc(spawnId=2096, patrolName='MS2PatrolData_2096A')
        move_npc(spawnId=2097, patrolName='MS2PatrolData_2097A')
        move_npc(spawnId=2098, patrolName='MS2PatrolData_2098A')
        move_npc(spawnId=2099, patrolName='MS2PatrolData_2099A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라302()


class 카메라302(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 부선장대사03()


class 부선장대사03(state.State):
    def on_enter(self):
        select_camera(triggerId=303, enable=True)
        set_conversation(type=2, spawnId=24003011, script='$02000391_BF__MAIN__2$', arg4=4, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4858):
            return 세이렌대사01()


class 세이렌대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=309, enable=True)
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000391_BF__MAIN__3$', align='left', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4179):
            return 카메라310()


class 카메라310(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='Dungeon_Siren_Harp01')
        set_npc_emotion_sequence(spawnId=1098, sequenceName='Attack_01_D')
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000391_BF__MAIN__4$', align='left', duration=3000)
        set_npc_emotion_sequence(spawnId=1099, sequenceName='Attack_01_D')
        select_camera(triggerId=310, enable=True)
        set_effect(triggerIds=[603], visible=True)
        add_buff(boxIds=[2094], skillId=70000055, level=1, arg4=True)
        add_buff(boxIds=[2095], skillId=70000055, level=1, arg4=True)
        add_buff(boxIds=[2096], skillId=70000055, level=1, arg4=True)
        add_buff(boxIds=[2097], skillId=70000055, level=1, arg4=True)
        add_buff(boxIds=[2098], skillId=70000055, level=1, arg4=True)
        add_buff(boxIds=[2099], skillId=70000055, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라304()


class 카메라304(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2099, script='$02000391_BF__MAIN__5$', arg4=3, arg5=0)
        set_npc_emotion_sequence(spawnId=1099, sequenceName='Attack_01_I')
        select_camera(triggerId=304, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1300):
            destroy_monster(spawnIds=[1099])
            return 딜레이01()


class 딜레이01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라305()


class 카메라305(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=False)
        destroy_monster(spawnIds=[2094,2095,2096,2097,2098,2099])
        create_monster(spawnIds=[2100], arg2=False)
        create_monster(spawnIds=[1098], arg2=False)
        select_camera(triggerId=305, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 세이렌연주02()


class 세이렌연주02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000391_BF__MAIN__6$', align='left', duration=5000)
        play_system_sound_in_box(sound='Dungeon_Siren_Harp01')
        set_npc_emotion_sequence(spawnId=1098, sequenceName='Attack_01_D')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 물큐브제거()


class 물큐브제거(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 세이렌이동()


class 세이렌이동(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003888, illustId='Celine_normal', msg='$02000391_BF__MAIN__7$', align='left', duration=3500)
        select_camera(triggerId=306, enable=True)
        move_npc(spawnId=1098, patrolName='MS2PatrolData_1098A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 카메라307()


class 카메라307(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1098])
        select_camera(triggerId=307, enable=True)
        set_conversation(type=2, spawnId=24003011, script='$02000391_BF__MAIN__8$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라308()


class 카메라308(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011], isAutoTargeting=False)
        select_camera(triggerId=308, enable=True)
        set_npc_emotion_sequence(spawnId=2100, sequenceName='Attack_01_A')
        set_conversation(type=1, spawnId=2100, script='$02000391_BF__MAIN__9$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 암전()


class 암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_skip()
        set_effect(triggerIds=[603], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3901,3902,3903,3904], visible=False, arg3=0, arg4=0, arg5=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2) # action name="카메라를선택한다" arg1="306" arg2="0"/
        reset_camera(interpolationTime=0)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011])
            destroy_monster(spawnIds=[1098,1099,2094,2095,2096,2097,2098,2099,2100])
            return 룸체크()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 던전시작()
        if not is_dungeon_room():
            return 퀘스트던전시작()


class 던전시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2199], arg2=False)
        spawn_npc_range(rangeIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011], isAutoTargeting=False)
        spawn_npc_range(rangeIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016], isAutoTargeting=False)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039101, textId=20039101, duration=3000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2199]):
            return 사망딜레이()


class 퀘스트던전시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2299], arg2=False)
        spawn_npc_range(rangeIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011], isAutoTargeting=False)
        spawn_npc_range(rangeIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016], isAutoTargeting=False)
        show_guide_summary(entityId=20039101, textId=20039101, duration=3000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2299]):
            return 사망딜레이()


class 사망딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011])
            return 오브젝트카메라()


class 오브젝트카메라(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_skip(state=하프반응대기)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[601], visible=True)
        select_camera(triggerId=307, enable=True)
        set_interact_object(triggerIds=[10001108], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 하프반응대기()


class 하프반응대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_skip()
        reset_camera(interpolationTime=0)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039102, textId=20039102, duration=3000) # action name="카메라를선택한다" arg1="307" arg2="0"/

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001108], arg2=0):
            play_system_sound_in_box(sound='Dungeon_Siren_Harp01')
            set_effect(triggerIds=[601], visible=False)
            return 연주딜레이()


class 연주딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 물큐브제거2()


class 물큐브제거2(state.State):
    def on_enter(self):
        set_skip(state=종료)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[602], visible=True)
        select_camera(triggerId=305, enable=True)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201], visible=False, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=2, visible=False, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 종료()


class 퀘스트완료가능이거나완료1(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10001108], state=2)
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3901,3902,3903,3904], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트완료가능이거나완료2()


class 퀘스트완료가능이거나완료2(state.State):
    def on_enter(self):
        set_skip(state=종료)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158,3159,3160,3161,3162,3163,3164,3165,3166,3167,3168,3169,3170,3171,3172,3173,3174,3175,3176,3177,3178,3179,3180,3181,3182,3183,3184,3185,3186,3187,3188,3189,3190,3191,3192,3193,3194,3195,3196,3197,3198,3199,3200,3201], visible=False, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=2, visible=False, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[602], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039103, textId=20039103)
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)


