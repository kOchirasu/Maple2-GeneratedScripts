""" trigger/02000313_bf/bossspawn.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.set_ladder(triggerIds=[4001], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4002], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4003], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4004], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4005], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4006], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4007], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4008], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4101], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4102], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4103], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[4104], visible=False, animationEffect=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1099], animationEffect=False)
        self.create_monster(spawnIds=[1101,1102,1103,1104,1105,1106,1107,1108], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[15]):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015], visible=True, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.select_camera(triggerId=30000, enable=True)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=차전투시작1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 차전투시작1(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=30000, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 차전투시작1(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031300, textId=20031300, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 차전투시작2_1(self.ctx)


class 차전투시작2_1(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031301, textId=20031301, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 차NPC이동1(self.ctx)


class 차NPC이동1(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=10101, spawnIds=[1001]):
            self.destroy_monster(spawnIds=[1001])
            self.create_monster(spawnIds=[1002], animationEffect=False)
            return 차전투대기2(self.ctx)


class 차전투대기2(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031302, textId=20031302, duration=4000)
        self.create_monster(spawnIds=[2002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10102]):
            return 차전투딜레이2(self.ctx)
        if self.monster_in_combat(boxIds=[2002]):
            return 차전투딜레이2(self.ctx)


class 차전투딜레이2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차전투시작2(self.ctx)


class 차전투시작2(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1002])
        self.create_monster(spawnIds=[1003], animationEffect=False)
        self.set_ladder(triggerIds=[4001], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4002], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4003], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4004], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4005], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4006], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4007], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4008], visible=True, animationEffect=True)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2002]):
            return 차NPC이동2(self.ctx)


class 차NPC이동2(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003B')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=10104, spawnIds=[1003]):
            self.destroy_monster(spawnIds=[1003])
            self.create_monster(spawnIds=[1004], animationEffect=False)
            return 차전투대기3(self.ctx)


class 차전투대기3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2003], animationEffect=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031302, textId=20031302, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10103]):
            return 차전투딜레이3(self.ctx)
        if self.monster_in_combat(boxIds=[2003]):
            return 차전투딜레이3(self.ctx)


class 차전투딜레이3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차전투시작3(self.ctx)


class 차전투시작3(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1004])
        self.create_monster(spawnIds=[1005], animationEffect=False)
        self.set_ladder(triggerIds=[4101], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4102], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4103], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[4104], visible=True, animationEffect=True)
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2003]):
            return 보스등장연출(self.ctx)


class 보스등장연출(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=30001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 보스등장연출2(self.ctx)


class 보스등장연출2(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1099])
        self.destroy_monster(spawnIds=[1005])
        self.create_monster(spawnIds=[2099], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 보스등장연출3(self.ctx)


class 보스등장연출3(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=1101, sequenceName='Dead_A', duration=9000)
        self.set_npc_emotion_loop(spawnId=1102, sequenceName='Dead_A', duration=9000)
        self.set_npc_emotion_loop(spawnId=1103, sequenceName='Dead_A', duration=9000)
        self.set_npc_emotion_loop(spawnId=1104, sequenceName='Dead_A', duration=9000)
        self.set_npc_emotion_loop(spawnId=1105, sequenceName='Dead_A', duration=9000)
        self.set_npc_emotion_loop(spawnId=1106, sequenceName='Dead_A', duration=9000)
        self.set_npc_emotion_loop(spawnId=1107, sequenceName='Dead_A', duration=9000)
        self.set_npc_emotion_loop(spawnId=1108, sequenceName='Dead_A', duration=9000)
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325], visible=True, arg3=0, delay=0, scale=0)
        self.set_skip(state=보스전투시작)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스전투시작(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=30001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[1101,1102,1103,1104,1105,1106,1107,1108])
        self.set_npc_emotion_loop(spawnId=1005, sequenceName='Dead_Idle_A', duration=1E+16)
        self.set_effect(triggerIds=[5002], visible=False)


class 보스전투시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031303, textId=20031303, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 보스전투시작2(self.ctx)


class 보스전투시작2(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031304, textId=20031304, duration=6000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.is_dungeon_room():
            return 종료(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트코드확인(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=True)


class 퀘스트코드확인(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9997], questIds=[10003105], questStates=[2]):
            return 퀘스트연출_시작(self.ctx)
        if self.quest_user_detected(boxIds=[9998], questIds=[10003105], questStates=[2]):
            return 퀘스트연출_시작(self.ctx)
        if self.quest_user_detected(boxIds=[9999], questIds=[10003105], questStates=[2]):
            return 퀘스트연출_시작(self.ctx)


class 퀘스트연출_시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__43$', arg3=False)
        self.create_monster(spawnIds=[205], animationEffect=True) # 바야르
        self.create_monster(spawnIds=[202], animationEffect=True) # 무파사
        self.create_monster(spawnIds=[203], animationEffect=True) # 구르는천둥
        self.create_monster(spawnIds=[204], animationEffect=True) # 시끄러운 주먹
        self.move_user(mapId=2000313, portalId=6001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 퀘스트연출_상황보여주기_01(self.ctx)


class 퀘스트연출_상황보여주기_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=퀘스트연출끝_이동, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=30000, enable=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=0, msg='$02000313_BF__BOSSSPAWN__44$', duration=3000)
        self.add_cinematic_talk(npcId=11003392, msg='$02000313_BF__BOSSSPAWN__45$', duration=3000)
        self.set_npc_emotion_loop(spawnId=205, sequenceName='Stun_A', duration=160000000)
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Attack_Idle_A', duration=160000000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_02(self.ctx)


class 퀘스트연출_상황보여주기_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4012], returnView=False)
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        self.face_emotion(spawnId=203, emotionName='Trigger_Sad')
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__46$', duration=3000)
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__47$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_03(self.ctx)


class 퀘스트연출_상황보여주기_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Attack_Idle_A', duration=1E+09)
        self.set_npc_emotion_sequence(spawnId=204, sequenceName='Talk_A,Bore_B')
        self.set_effect(triggerIds=[5001], visible=False)
        self.add_cinematic_talk(npcId=11003454, msg='$02000313_BF__BOSSSPAWN__48$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_04_1(self.ctx)


class 퀘스트연출_상황보여주기_04_1(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=203, emotionName='Trigger_Danger')
        self.add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__49$', duration=3000)
        self.add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__50$', duration=3000)
        self.add_cinematic_talk(npcId=11003454, msg='$02000313_BF__BOSSSPAWN__51$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 퀘스트연출_상황보여주기_04_2(self.ctx)


class 퀘스트연출_상황보여주기_04_2(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4011], returnView=False)
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.add_cinematic_talk(npcId=0, msg='$02000313_BF__BOSSSPAWN__52$', duration=3000)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__53$', duration=3000)
        self.create_monster(spawnIds=[201], animationEffect=True) # 붉은늑대심장
        self.add_balloon_talk(spawnId=0, msg='$02000313_BF__BOSSSPAWN__54$', duration=2000, delayTick=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_04(self.ctx)


class 퀘스트연출_상황보여주기_04(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=201, emotionName='Talk')
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Idle_A', duration=1E+09)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 퀘스트연출_상황보여주기_05(self.ctx)


class 퀘스트연출_상황보여주기_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4013], returnView=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_9991')
        self.add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__55$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_06(self.ctx)


class 퀘스트연출_상황보여주기_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4013], returnView=False)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Idle_A', duration=1E+09)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__56$', duration=3000)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__57$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_07(self.ctx)


class 퀘스트연출_상황보여주기_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__58$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_08(self.ctx)


class 퀘스트연출_상황보여주기_08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4018], returnView=False)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Idle_A', duration=1E+09)
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_9994')
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__15$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_09(self.ctx)


class 퀘스트연출_상황보여주기_09(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4013], returnView=False)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=1E+09)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__59$', duration=3000)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__60$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_10(self.ctx)


class 퀘스트연출_상황보여주기_10(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_9995')
        self.add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__61$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$02000313_BF__BOSSSPAWN__62$', duration=3000)
        self.set_npc_emotion_sequence(spawnId=204, sequenceName='Talk_A')
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_01_C')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트연출_상황보여주기_10_1(self.ctx)


class 퀘스트연출_상황보여주기_10_1(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4013], returnView=False)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__63$', duration=3000)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__64$', duration=3000)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Attack_Idle_A', duration=1E+09)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__65$', duration=3000)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__66$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$02000313_BF__BOSSSPAWN__67$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 퀘스트연출_상황보여주기_11(self.ctx)


class 퀘스트연출_상황보여주기_11(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='ChatUp_A')
        self.face_emotion(spawnId=201, emotionName='Trigger_Proud')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_9996')
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__68$', duration=4000)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__69$', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 퀘스트연출_상황보여주기_11_1(self.ctx)


class 퀘스트연출_상황보여주기_11_1(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__70$', duration=3000)
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Sit_Down_A', duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_11_2(self.ctx)


class 퀘스트연출_상황보여주기_11_2(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4018], returnView=False)
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__71$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_11_3(self.ctx)


class 퀘스트연출_상황보여주기_11_3(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        self.face_emotion(spawnId=201, emotionName='Trigger_Sad')
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__72$', duration=3000)
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__73$', duration=3000)
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__74$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 퀘스트연출_상황보여주기_11_4_1(self.ctx)


class 퀘스트연출_상황보여주기_11_4_1(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=201, emotionName='Trigger_Proud')
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__75$', duration=6060)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6060):
            return 퀘스트연출_상황보여주기_11_4(self.ctx)


class 퀘스트연출_상황보여주기_11_4(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4019], returnView=False)
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Attack_01_A')
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__76$', duration=4000)
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__77$', duration=4000)
        self.set_skip(state=퀘스트연출_마지막전투_04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 퀘스트연출_상황보여주기_12(self.ctx)


class 퀘스트연출_상황보여주기_12(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.add_cinematic_talk(npcId=11003387, msg='$02000313_BF__BOSSSPAWN__78$', duration=3000)
        self.face_emotion(spawnId=203, emotionName='Trigger_Embarrassed')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 퀘스트연출_상황보여주기_13(self.ctx)


class 퀘스트연출_상황보여주기_13(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4018], returnView=False)
        self.visible_my_pc(isVisible=False)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Attack_01_C')
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__79$', duration=3000)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__80$', duration=3000)
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__81$', duration=3000)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.destroy_monster(spawnIds=[203]) # 구르는천둥
        self.destroy_monster(spawnIds=[204]) # 시끄러운 주먹

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 퀘스트연출_마지막전투_01(self.ctx)


class 퀘스트연출_마지막전투_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4020], returnView=False)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Attack_04_G')
        self.add_cinematic_talk(npcId=11003392, msg='$02000313_BF__BOSSSPAWN__82$', duration=1500)
        self.set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 퀘스트연출_마지막전투_02(self.ctx)


class 퀘스트연출_마지막전투_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4017], returnView=False)
        self.visible_my_pc(isVisible=False)
        self.add_cinematic_talk(npcId=11003393, msg='$02000313_BF__BOSSSPAWN__83$', duration=3000)
        self.add_cinematic_talk(npcId=11003407, msg='$02000313_BF__BOSSSPAWN__84$', duration=3000)
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Attack_02_H')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return 퀘스트연출_마지막전투_03(self.ctx)


class 퀘스트연출_마지막전투_03(common.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_9993')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_9992')
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Attack_04_G')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트연출_마지막전투_03_1(self.ctx)


class 퀘스트연출_마지막전투_03_1(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4017], returnView=False)
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawnId=205, sequenceName='Dead_A')
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Attack_01_B')
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5005], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 퀘스트연출_마지막전투_04(self.ctx)


class 퀘스트연출_마지막전투_04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[201])
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[205])
        self.create_monster(spawnIds=[206], animationEffect=True)
        self.create_monster(spawnIds=[207], animationEffect=True)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_npc_emotion_loop(spawnId=206, sequenceName='Dead_A', duration=1000000)
        self.set_npc_emotion_loop(spawnId=207, sequenceName='Dead_B', duration=1000000)
        self.face_emotion(spawnId=206, emotionName='Trigger_Dead')
        self.face_emotion(spawnId=207, emotionName='Trigger_Dead')
        self.set_effect(triggerIds=[5006], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 퀘스트연출_마지막전투_05(self.ctx)


class 퀘스트연출_마지막전투_05(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_onetime_effect(id=3, enable=True, path='BG\weather\Eff_monochrome_03.xml')
        self.select_camera_path(pathIds=[4021,4022], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트연출_마지막전투_06(self.ctx)


class 퀘스트연출_마지막전투_06(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG\weather\Eff_monochrome_03.xml')
        self.set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__85$', arg3=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 퀘스트연출_마지막전투_07(self.ctx)


class 퀘스트연출_마지막전투_07(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__86$', arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트연출_마지막전투_08(self.ctx)


class 퀘스트연출_마지막전투_08(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트연출끝_이동(self.ctx)


class 퀘스트연출끝_이동(common.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=True)
        self.move_user(mapId=52010032, portalId=3)


initial_state = 시작대기중
