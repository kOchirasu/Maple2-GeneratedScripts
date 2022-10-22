""" trigger/02000313_bf/bossspawn.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=13, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        set_ladder(triggerIds=[4001], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4002], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4003], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4004], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4005], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4006], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4007], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4008], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4101], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4102], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4103], visible=False, animationEffect=False)
        set_ladder(triggerIds=[4104], visible=False, animationEffect=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1099], arg2=False)
        create_monster(spawnIds=[1101,1102,1103,1104,1105,1106,1107,1108], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[15]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작()

state.DungeonStart = DungeonStart


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015], visible=True, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[2001], arg2=False)
        select_camera(triggerId=30000, enable=True)
        set_effect(triggerIds=[5002], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=차전투시작1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차전투시작1()

    def on_exit(self):
        select_camera(triggerId=30000, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 차전투시작1(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031300, textId=20031300, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 차전투시작2_1()


class 차전투시작2_1(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031301, textId=20031301, duration=4000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 차NPC이동1()


class 차NPC이동1(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=10101, spawnIds=[1001]):
            destroy_monster(spawnIds=[1001])
            create_monster(spawnIds=[1002], arg2=False)
            return 차전투대기2()


class 차전투대기2(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031302, textId=20031302, duration=4000)
        create_monster(spawnIds=[2002], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10102]):
            return 차전투딜레이2()
        if monster_in_combat(boxIds=[2002]):
            return 차전투딜레이2()


class 차전투딜레이2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차전투시작2()


class 차전투시작2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1002])
        create_monster(spawnIds=[1003], arg2=False)
        set_ladder(triggerIds=[4001], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4002], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4003], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4004], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4005], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4006], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4007], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4008], visible=True, animationEffect=True)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            return 차NPC이동2()


class 차NPC이동2(state.State):
    def on_enter(self):
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003B')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=10104, spawnIds=[1003]):
            destroy_monster(spawnIds=[1003])
            create_monster(spawnIds=[1004], arg2=False)
            return 차전투대기3()


class 차전투대기3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003], arg2=False)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031302, textId=20031302, duration=4000)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10103]):
            return 차전투딜레이3()
        if monster_in_combat(boxIds=[2003]):
            return 차전투딜레이3()


class 차전투딜레이3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차전투시작3()


class 차전투시작3(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1004])
        create_monster(spawnIds=[1005], arg2=False)
        set_ladder(triggerIds=[4101], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4102], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4103], visible=True, animationEffect=True)
        set_ladder(triggerIds=[4104], visible=True, animationEffect=True)
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2003]):
            return 보스등장연출()


class 보스등장연출(state.State):
    def on_enter(self):
        select_camera(triggerId=30001, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 보스등장연출2()


class 보스등장연출2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1099])
        destroy_monster(spawnIds=[1005])
        create_monster(spawnIds=[2099], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 보스등장연출3()


class 보스등장연출3(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1101, sequenceName='Dead_A', duration=9000)
        set_npc_emotion_loop(spawnId=1102, sequenceName='Dead_A', duration=9000)
        set_npc_emotion_loop(spawnId=1103, sequenceName='Dead_A', duration=9000)
        set_npc_emotion_loop(spawnId=1104, sequenceName='Dead_A', duration=9000)
        set_npc_emotion_loop(spawnId=1105, sequenceName='Dead_A', duration=9000)
        set_npc_emotion_loop(spawnId=1106, sequenceName='Dead_A', duration=9000)
        set_npc_emotion_loop(spawnId=1107, sequenceName='Dead_A', duration=9000)
        set_npc_emotion_loop(spawnId=1108, sequenceName='Dead_A', duration=9000)
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325], visible=True, arg3=0, arg4=0, arg5=0)
        set_skip(state=보스전투시작)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보스전투시작()

    def on_exit(self):
        select_camera(triggerId=30001, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[1101,1102,1103,1104,1105,1106,1107,1108])
        set_npc_emotion_loop(spawnId=1005, sequenceName='Dead_Idle_A', duration=1E+16)
        set_effect(triggerIds=[5002], visible=False)


class 보스전투시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031303, textId=20031303, duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 보스전투시작2()


class 보스전투시작2(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031304, textId=20031304, duration=6000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 퀘스트체크()


class 퀘스트체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 종료()
        if not is_dungeon_room():
            return 퀘스트코드확인()


class 종료(state.State):
    def on_enter(self):
        dungeon_clear()
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=13, visible=True, enabled=True, minimapVisible=True)


class 퀘스트코드확인(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9997], questIds=[10003105], questStates=[2]):
            return 퀘스트연출_시작()
        if quest_user_detected(boxIds=[9998], questIds=[10003105], questStates=[2]):
            return 퀘스트연출_시작()
        if quest_user_detected(boxIds=[9999], questIds=[10003105], questStates=[2]):
            return 퀘스트연출_시작()


class 퀘스트연출_시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__43$', arg3=False)
        create_monster(spawnIds=[205], arg2=True) # 바야르
        create_monster(spawnIds=[202], arg2=True) # 무파사
        create_monster(spawnIds=[203], arg2=True) # 구르는천둥
        create_monster(spawnIds=[204], arg2=True) # 시끄러운 주먹
        move_user(mapId=2000313, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 퀘스트연출_상황보여주기_01()


class 퀘스트연출_상황보여주기_01(state.State):
    def on_enter(self):
        set_scene_skip(state=퀘스트연출끝_이동, arg2='exit')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=30000, enable=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, msg='$02000313_BF__BOSSSPAWN__44$', duration=3000)
        add_cinematic_talk(npcId=11003392, msg='$02000313_BF__BOSSSPAWN__45$', duration=3000)
        set_npc_emotion_loop(spawnId=205, sequenceName='Stun_A', duration=160000000)
        set_npc_emotion_loop(spawnId=203, sequenceName='Attack_Idle_A', duration=160000000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_02()


class 퀘스트연출_상황보여주기_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)
        set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        face_emotion(spawnId=203, emotionName='Trigger_Sad')
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__46$', duration=3000)
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__47$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_03()


class 퀘스트연출_상황보여주기_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        set_npc_emotion_loop(spawnId=203, sequenceName='Attack_Idle_A', duration=1E+09)
        set_npc_emotion_sequence(spawnId=204, sequenceName='Talk_A,Bore_B')
        set_effect(triggerIds=[5001], visible=False)
        add_cinematic_talk(npcId=11003454, msg='$02000313_BF__BOSSSPAWN__48$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_04_1()


class 퀘스트연출_상황보여주기_04_1(state.State):
    def on_enter(self):
        face_emotion(spawnId=203, emotionName='Trigger_Danger')
        add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__49$', duration=3000)
        add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__50$', duration=3000)
        add_cinematic_talk(npcId=11003454, msg='$02000313_BF__BOSSSPAWN__51$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 퀘스트연출_상황보여주기_04_2()


class 퀘스트연출_상황보여주기_04_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011], returnView=False)
        set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        add_cinematic_talk(npcId=0, msg='$02000313_BF__BOSSSPAWN__52$', duration=3000)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__53$', duration=3000)
        create_monster(spawnIds=[201], arg2=True) # 붉은늑대심장
        add_balloon_talk(spawnId=0, msg='$02000313_BF__BOSSSPAWN__54$', duration=2000, delayTick=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_04()


class 퀘스트연출_상황보여주기_04(state.State):
    def on_enter(self):
        face_emotion(spawnId=201, emotionName='Talk')
        set_npc_emotion_loop(spawnId=201, sequenceName='Idle_A', duration=1E+09)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 퀘스트연출_상황보여주기_05()


class 퀘스트연출_상황보여주기_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013], returnView=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_9991')
        add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__55$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_06()


class 퀘스트연출_상황보여주기_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013], returnView=False)
        set_npc_emotion_loop(spawnId=201, sequenceName='Idle_A', duration=1E+09)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__56$', duration=3000)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__57$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_07()


class 퀘스트연출_상황보여주기_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__58$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_08()


class 퀘스트연출_상황보여주기_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4018], returnView=False)
        set_npc_emotion_loop(spawnId=201, sequenceName='Idle_A', duration=1E+09)
        set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        move_npc(spawnId=202, patrolName='MS2PatrolData_9994')
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__15$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_09()


class 퀘스트연출_상황보여주기_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013], returnView=False)
        set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=1E+09)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__59$', duration=3000)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__60$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_10()


class 퀘스트연출_상황보여주기_10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        move_npc(spawnId=202, patrolName='MS2PatrolData_9995')
        add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__61$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$02000313_BF__BOSSSPAWN__62$', duration=3000)
        set_npc_emotion_sequence(spawnId=204, sequenceName='Talk_A')
        set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_01_C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_10_1()


class 퀘스트연출_상황보여주기_10_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013], returnView=False)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__63$', duration=3000)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__64$', duration=3000)
        set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=1E+09)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__65$', duration=3000)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__66$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$02000313_BF__BOSSSPAWN__67$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 퀘스트연출_상황보여주기_11()


class 퀘스트연출_상황보여주기_11(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='ChatUp_A')
        face_emotion(spawnId=201, emotionName='Trigger_Proud')
        move_npc(spawnId=202, patrolName='MS2PatrolData_9996')
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__68$', duration=4000)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__69$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 퀘스트연출_상황보여주기_11_1()


class 퀘스트연출_상황보여주기_11_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__70$', duration=3000)
        set_npc_emotion_loop(spawnId=203, sequenceName='Sit_Down_A', duration=10000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_11_2()


class 퀘스트연출_상황보여주기_11_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4018], returnView=False)
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__71$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_11_3()


class 퀘스트연출_상황보여주기_11_3(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        face_emotion(spawnId=201, emotionName='Trigger_Sad')
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__72$', duration=3000)
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__73$', duration=3000)
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__74$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 퀘스트연출_상황보여주기_11_4_1()


class 퀘스트연출_상황보여주기_11_4_1(state.State):
    def on_enter(self):
        face_emotion(spawnId=201, emotionName='Trigger_Proud')
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__75$', duration=6060)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6060):
            return 퀘스트연출_상황보여주기_11_4()


class 퀘스트연출_상황보여주기_11_4(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4019], returnView=False)
        set_npc_emotion_sequence(spawnId=202, sequenceName='Attack_01_A')
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__76$', duration=4000)
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__77$', duration=4000)
        set_skip(state=퀘스트연출_마지막전투_04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 퀘스트연출_상황보여주기_12()


class 퀘스트연출_상황보여주기_12(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__78$', duration=3000)
        face_emotion(spawnId=203, emotionName='Trigger_Embarrassed')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_13()


class 퀘스트연출_상황보여주기_13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4018], returnView=False)
        visible_my_pc(isVisible=False)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A')
        set_npc_emotion_sequence(spawnId=202, sequenceName='Attack_01_C')
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__79$', duration=3000)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__80$', duration=3000)
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__81$', duration=3000)
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        destroy_monster(spawnIds=[203]) # 구르는천둥
        destroy_monster(spawnIds=[204]) # 시끄러운 주먹

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 퀘스트연출_마지막전투_01()


class 퀘스트연출_마지막전투_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4020], returnView=False)
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_npc_emotion_sequence(spawnId=205, sequenceName='Attack_04_G')
        add_cinematic_talk(npcId=11003392, msg='$02000313_BF__BOSSSPAWN__82$', duration=1500)
        set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 퀘스트연출_마지막전투_02()


class 퀘스트연출_마지막전투_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4017], returnView=False)
        visible_my_pc(isVisible=False)
        add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__83$', duration=3000)
        add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__84$', duration=3000)
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_npc_emotion_sequence(spawnId=205, sequenceName='Attack_02_H')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 퀘스트연출_마지막전투_03()


class 퀘스트연출_마지막전투_03(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_9993')
        move_npc(spawnId=202, patrolName='MS2PatrolData_9992')
        set_npc_emotion_sequence(spawnId=205, sequenceName='Attack_04_G')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트연출_마지막전투_03_1()


class 퀘스트연출_마지막전투_03_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4017], returnView=False)
        set_effect(triggerIds=[5001], visible=True)
        set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_npc_emotion_sequence(spawnId=205, sequenceName='Dead_A')
        set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_01_B')
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5005], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 퀘스트연출_마지막전투_04()


class 퀘스트연출_마지막전투_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[201])
        destroy_monster(spawnIds=[202])
        destroy_monster(spawnIds=[205])
        create_monster(spawnIds=[206], arg2=True)
        create_monster(spawnIds=[207], arg2=True)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_npc_emotion_loop(spawnId=206, sequenceName='Dead_A', duration=1000000)
        set_npc_emotion_loop(spawnId=207, sequenceName='Dead_B', duration=1000000)
        face_emotion(spawnId=206, emotionName='Trigger_Dead')
        face_emotion(spawnId=207, emotionName='Trigger_Dead')
        set_effect(triggerIds=[5006], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 퀘스트연출_마지막전투_05()


class 퀘스트연출_마지막전투_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_onetime_effect(id=3, enable=True, path='BG\weather\Eff_monochrome_03.xml')
        select_camera_path(pathIds=[4021,4022], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트연출_마지막전투_06()


class 퀘스트연출_마지막전투_06(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_onetime_effect(id=3, enable=False, path='BG\weather\Eff_monochrome_03.xml')
        set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__85$', arg3=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 퀘스트연출_마지막전투_07()


class 퀘스트연출_마지막전투_07(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__86$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트연출_마지막전투_08()


class 퀘스트연출_마지막전투_08(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트연출끝_이동()


class 퀘스트연출끝_이동(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        move_user(mapId=52010032, portalId=3)


