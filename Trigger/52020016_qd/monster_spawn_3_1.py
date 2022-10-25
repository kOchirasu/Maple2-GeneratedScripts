""" trigger/52020016_qd/monster_spawn_3_1.xml """
import common


class 체력조건(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn_phase_3', value=1):
            return 전투페이즈(self.ctx)


class 전투페이즈(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4000201], animationEffect=False)
        self.create_monster(spawnIds=[4000202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 전투페이즈_2(self.ctx)


class 전투페이즈_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[4000301], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 전투페이즈_2_대사(self.ctx)


class 전투페이즈_2_대사(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=4000301, script='하하하!!내가 돌아왔다!', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 끝(self.ctx)


class 끝(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='카...카트반? 어떻게?!', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4000301]):
            return 대화(self.ctx)

    def on_exit(self):
        self.set_ambient_light(primary=[0,0,0])
        self.set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])


class 대화(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.set_conversation(type=2, spawnId=4000201, script='제법이군요! 그렇다면 이건 어떤가요?', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 조디등장_1(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[4000401], animationEffect=False)


class 조디등장_1(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4000401, patrolName='MS2PatrolData0_4000401_1')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 조디등장_2(self.ctx)

    def on_exit(self):
        self.select_camera_path(pathIds=[2000001], returnView=False)


class 조디등장_2(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=0, script='!!!!!!!??????', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=0, script='조...조디?!', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=0, script='조디...살아있었던거야?', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=300001, script='헤헤...오랫만에 뵙네요. 보고싶었어요.', arg4=5)
        self.set_conversation(type=2, spawnId=300001, script='그런데 저를...왜 죽게 내버려 두었나요?', arg4=5)
        self.set_conversation(type=2, spawnId=0, script='그...그게 아니야!!', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=300001, script='당신을...저주해요..가만두지 않겠어요!!', arg4=5)
        self.set_conversation(type=2, spawnId=0, script='아...안돼 그만둬!! 조디!!', arg4=3, arg5=0)
        self.set_skip(state=마지막전투)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return 마지막전투(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[4000401], arg2=False)
        self.select_camera_path(pathIds=[2000001], returnView=True)


class 마지막전투(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.destroy_monster(spawnIds=[4000401])
        self.set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마지막전투_2(self.ctx)


class 마지막전투_2(common.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[180,180,149])
        self.set_directional_light(diffuseColor=[219,204,182], specularColor=[219,204,182])
        self.set_portal(portalId=95, visible=True, enable=True)
        self.set_user_value(triggerId=911, key='respawn_phase_4', value=1)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[4000402]):
            return 마지막전투_3(self.ctx)


class 마지막전투_3(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=912, key='respawn_phase_4', value=1)
        self.set_user_value(triggerId=913, key='respawn_phase_4', value=1)

    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 마지막전투_4(self.ctx)


class 마지막전투_4(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=914, key='respawn_phase_4', value=1)
        self.set_user_value(triggerId=915, key='respawn_phase_4', value=1)
        self.set_user_value(triggerId=916, key='respawn_phase_4', value=1)
        self.set_conversation(type=1, spawnId=0, script='조디!! 제발 맘춰!!', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 마지막전투_5(self.ctx)


class 마지막전투_5(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=917, key='respawn_phase_4', value=1)
        self.set_user_value(triggerId=918, key='respawn_phase_4', value=1)
        self.set_user_value(triggerId=919, key='respawn_phase_4', value=1)
        self.set_user_value(triggerId=920, key='respawn_phase_4', value=1)

    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 긴급대화_2(self.ctx)

    def on_exit(self):
        self.set_achievement(type='trigger', achieve='DollMaster')


class 긴급대화_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Disappoint_A','Emotion_Disappoint_Idle_A'])
        self.set_conversation(type=1, spawnId=0, script='이젠...더이상은...힘들어....', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 긴급대화_3(self.ctx)


class 긴급대화_3(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마지막_연출(self.ctx)


class 마지막_연출(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[400001], animationEffect=False)
        self.create_monster(spawnIds=[400002], animationEffect=False)
        self.create_monster(spawnIds=[400003], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=400001, sequenceName='Attack_Idle_A', duration=100000000)
        self.set_npc_emotion_loop(spawnId=400002, sequenceName='Attack_Idle_A', duration=100000000)
        self.set_npc_emotion_loop(spawnId=400003, sequenceName='Attack_Idle_A', duration=100000000)
        self.move_user(mapId=52020016, portalId=97)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마지막_연출_2(self.ctx)

    def on_exit(self):
        self.set_pc_emotion_loop(sequenceName='Emotion_Disappoint_Idle_A', duration=100000000)


class 마지막_연출_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(pathIds=[2000005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마지막_연출_3(self.ctx)


class 마지막_연출_3(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[320001], animationEffect=False)
        self.move_npc(spawnId=320001, patrolName='MS2PatrolData0_320001_1')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마지막_연출_4(self.ctx)


class 마지막_연출_4(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=320001, script='하하하하! 느껴지시나요? 나와 당신의 높이가!!', arg4=5)
        self.set_conversation(type=2, spawnId=0, script='헉헉...제발 그만둬!!', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=320001, script='이 몽환의 무대 안에서는 어떠한 존재라도 저를 이길 수 없습니다!', arg4=5)
        self.set_conversation(type=2, spawnId=320001, script='그럼 이제 마무리를 지어 볼까요?', arg4=5)
        self.set_skip(state=마지막_연출_4_2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=17000):
            return 마지막_연출_4_2(self.ctx)


class 마지막_연출_4_2(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000006], returnView=False)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return 마지막_연출_4_3(self.ctx)


class 마지막_연출_4_3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[410001], animationEffect=False)
        self.create_monster(spawnIds=[410002], animationEffect=False)
        self.create_monster(spawnIds=[410003], animationEffect=False)
        self.create_monster(spawnIds=[410004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return 마지막_연출_5(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[420001], animationEffect=False)
        self.create_monster(spawnIds=[420002], animationEffect=False)
        self.create_monster(spawnIds=[420003], animationEffect=False)
        self.create_monster(spawnIds=[420004], animationEffect=False)
        self.create_monster(spawnIds=[420005], animationEffect=False)
        self.create_monster(spawnIds=[420006], animationEffect=False)
        self.create_monster(spawnIds=[420007], animationEffect=False)


class 마지막_연출_5(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=900):
            return 유저이동(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=4)


class 유저이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020032, portalId=6001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return None


initial_state = 체력조건
