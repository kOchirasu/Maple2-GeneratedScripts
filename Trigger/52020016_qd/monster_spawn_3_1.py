""" trigger/52020016_qd/monster_spawn_3_1.xml """
from common import *
import state


class 체력조건(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='respawn_phase_3', value=1):
            return 전투페이즈()


class 전투페이즈(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4000201], arg2=False)
        create_monster(spawnIds=[4000202], arg2=False)

    def on_tick(self) -> state.State:
        if all_of():
            return 전투페이즈_2()


class 전투페이즈_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4000301], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 전투페이즈_2_대사()


class 전투페이즈_2_대사(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=4000301, script='하하하!!내가 돌아왔다!', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='카...카트반? 어떻게?!', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4000301]):
            return 대화()

    def on_exit(self):
        set_ambient_light(primary=[0,0,0])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])


class 대화(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        set_conversation(type=2, spawnId=4000201, script='제법이군요! 그렇다면 이건 어떤가요?', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조디등장_1()

    def on_exit(self):
        create_monster(spawnIds=[4000401], arg2=False)


class 조디등장_1(state.State):
    def on_enter(self):
        move_npc(spawnId=4000401, patrolName='MS2PatrolData0_4000401_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 조디등장_2()

    def on_exit(self):
        select_camera_path(pathIds=[2000001], returnView=False)


class 조디등장_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=0, script='!!!!!!!??????', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=0, script='조...조디?!', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=0, script='조디...살아있었던거야?', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=300001, script='헤헤...오랫만에 뵙네요. 보고싶었어요.', arg4=5)
        set_conversation(type=2, spawnId=300001, script='그런데 저를...왜 죽게 내버려 두었나요?', arg4=5)
        set_conversation(type=2, spawnId=0, script='그...그게 아니야!!', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=300001, script='당신을...저주해요..가만두지 않겠어요!!', arg4=5)
        set_conversation(type=2, spawnId=0, script='아...안돼 그만둬!! 조디!!', arg4=3, arg5=0)
        set_skip(state=마지막전투)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=32000):
            return 마지막전투()

    def on_exit(self):
        destroy_monster(spawnIds=[4000401], arg2=False)
        select_camera_path(pathIds=[2000001], returnView=True)


class 마지막전투(state.State):
    def on_enter(self):
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)
        destroy_monster(spawnIds=[4000401])
        set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마지막전투_2()


class 마지막전투_2(state.State):
    def on_enter(self):
        set_ambient_light(primary=[180,180,149])
        set_directional_light(diffuseColor=[219,204,182], specularColor=[219,204,182])
        set_portal(portalId=95, visible=True, enabled=True)
        set_user_value(triggerId=911, key='respawn_phase_4', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[4000402]):
            return 마지막전투_3()


class 마지막전투_3(state.State):
    def on_enter(self):
        set_user_value(triggerId=912, key='respawn_phase_4', value=1)
        set_user_value(triggerId=913, key='respawn_phase_4', value=1)

    def on_tick(self) -> state.State:
        if all_of():
            return 마지막전투_4()


class 마지막전투_4(state.State):
    def on_enter(self):
        set_user_value(triggerId=914, key='respawn_phase_4', value=1)
        set_user_value(triggerId=915, key='respawn_phase_4', value=1)
        set_user_value(triggerId=916, key='respawn_phase_4', value=1)
        set_conversation(type=1, spawnId=0, script='조디!! 제발 맘춰!!', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if all_of():
            return 마지막전투_5()


class 마지막전투_5(state.State):
    def on_enter(self):
        set_user_value(triggerId=917, key='respawn_phase_4', value=1)
        set_user_value(triggerId=918, key='respawn_phase_4', value=1)
        set_user_value(triggerId=919, key='respawn_phase_4', value=1)
        set_user_value(triggerId=920, key='respawn_phase_4', value=1)

    def on_tick(self) -> state.State:
        if all_of():
            return 긴급대화_2()

    def on_exit(self):
        set_achievement(type='trigger', achieve='DollMaster')


class 긴급대화_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Disappoint_A','Emotion_Disappoint_Idle_A'])
        set_conversation(type=1, spawnId=0, script='이젠...더이상은...힘들어....', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 긴급대화_3()


class 긴급대화_3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마지막_연출()


class 마지막_연출(state.State):
    def on_enter(self):
        create_monster(spawnIds=[400001], arg2=False)
        create_monster(spawnIds=[400002], arg2=False)
        create_monster(spawnIds=[400003], arg2=False)
        set_npc_emotion_loop(spawnId=400001, sequenceName='Attack_Idle_A', duration=100000000)
        set_npc_emotion_loop(spawnId=400002, sequenceName='Attack_Idle_A', duration=100000000)
        set_npc_emotion_loop(spawnId=400003, sequenceName='Attack_Idle_A', duration=100000000)
        move_user(mapId=52020016, portalId=97)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마지막_연출_2()

    def on_exit(self):
        set_pc_emotion_loop(sequenceName='Emotion_Disappoint_Idle_A', duration=100000000)


class 마지막_연출_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera_path(pathIds=[2000005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마지막_연출_3()


class 마지막_연출_3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[320001], arg2=False)
        move_npc(spawnId=320001, patrolName='MS2PatrolData0_320001_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 마지막_연출_4()


class 마지막_연출_4(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=320001, script='하하하하! 느껴지시나요? 나와 당신의 높이가!!', arg4=5)
        set_conversation(type=2, spawnId=0, script='헉헉...제발 그만둬!!', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=320001, script='이 몽환의 무대 안에서는 어떠한 존재라도 저를 이길 수 없습니다!', arg4=5)
        set_conversation(type=2, spawnId=320001, script='그럼 이제 마무리를 지어 볼까요?', arg4=5)
        set_skip(state=마지막_연출_4_2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=17000):
            return 마지막_연출_4_2()


class 마지막_연출_4_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000006], returnView=False)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 마지막_연출_4_3()


class 마지막_연출_4_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[410001], arg2=False)
        create_monster(spawnIds=[410002], arg2=False)
        create_monster(spawnIds=[410003], arg2=False)
        create_monster(spawnIds=[410004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 마지막_연출_5()

    def on_exit(self):
        create_monster(spawnIds=[420001], arg2=False)
        create_monster(spawnIds=[420002], arg2=False)
        create_monster(spawnIds=[420003], arg2=False)
        create_monster(spawnIds=[420004], arg2=False)
        create_monster(spawnIds=[420005], arg2=False)
        create_monster(spawnIds=[420006], arg2=False)
        create_monster(spawnIds=[420007], arg2=False)


class 마지막_연출_5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=900):
            return 유저이동()

    def on_exit(self):
        set_cinematic_ui(type=4)


class 유저이동(state.State):
    def on_enter(self):
        move_user(mapId=52020032, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return None


