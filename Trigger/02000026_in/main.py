""" trigger/02000026_in/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102])
        set_mesh(triggerIds=[4001,4002], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[3]):
            return 조건체크01()
        if quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[2]):
            return 아노스있음01()
        if quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[1]):
            return 아노스만남연출대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001567], questStates=[3]):
            return 대기조건01()
        if quest_user_detected(boxIds=[9000], questIds=[50001567], questStates=[2]):
            return 대기조건01()
        if quest_user_detected(boxIds=[9000], questIds=[50001567], questStates=[1]):
            return 기본상태()


class 대기조건01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[1]):
            return 아노스만남연출시작()
        if not quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[1]):
            return start()


class 조건체크01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001569], questStates=[1]):
            return 아노스있음01()
        if not quest_user_detected(boxIds=[9000], questIds=[50001569], questStates=[1]):
            return 조건체크02()


class 조건체크02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001573], questStates=[3]):
            return 기본상태()
        if quest_user_detected(boxIds=[9000], questIds=[50001568,50001569,50001570,50001571,50001572,50001573], questStates=[2]):
            return 아노스있음01()


class 기본상태(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return start()


class 아노스있음01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        set_mesh(triggerIds=[4001,4002], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 아노스만남연출대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        set_mesh(triggerIds=[4001,4002], visible=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            move_user_path(patrolName='MS2PatrolData_PC_00')
            return 아노스만남연출시작()


class 아노스만남연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8000], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 아노스등장()


class 아노스등장(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_00')
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__0$', arg4=4, arg5=0)
        set_scene_skip(state=아노스만남_스킵완료, arg2='nextState') # setsceneskip 1 set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아노스이동01()


class 아노스이동01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_01')
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__1$', arg4=3, arg5=0)
        # <action name="스킵을설정한다" arg1="아노스만남_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3239):
            return 아노스이동02()


class 아노스이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_02')
        # <action name="스킵을설정한다" arg1="아노스만남_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아노스이동03()


class 아노스이동03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__2$', arg4=3, arg5=0)
        set_npc_emotion_sequence(spawnId=101, sequenceName='ChatUp_A')
        # <action name="스킵을설정한다" arg1="아노스만남_스킵완료"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4623):
            return 아노스대사01()


class 아노스대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__3$', arg4=4, arg5=0)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        set_skip(state=아노스대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라이동_라딘01()


class 아노스대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 카메라이동_라딘01()


class 카메라이동_라딘01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라딘대사01()


class 라딘대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000264, script='$02000026_IN__MAIN__4$', arg4=3, arg5=0)
        set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_A')
        set_skip(state=라딘대사01_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4623):
            return 아노스대사02()


class 라딘대사01_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아노스대사02()


class 아노스대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4000)
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__5$', arg4=4, arg5=0)
        set_skip(state=아노스대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4519):
            return 라딘대사02()


class 아노스대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 라딘대사02()


class 라딘대사02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='ChatUP_A')
        # <action name="SetNpcEmotionLoop" arg1="103" arg2="ChatUP_A" arg3="4000"/>
        set_conversation(type=2, spawnId=11000264, script='$02000026_IN__MAIN__6$', arg4=4, arg5=0)
        set_skip(state=라딘대사02_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4780):
            return 카메라이동_아노스01()


class 라딘대사02_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 카메라이동_아노스01()


class 카메라이동_아노스01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아노스대사03()


class 아노스대사03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='ChatUp_A')
        # <action name="SetNpcEmotionLoop" arg1="102" arg2="ChatUp_A" arg3="3000" />
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__7$', arg4=3, arg5=0)
        set_skip(state=아노스대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6817):
            return 아노스대사04()


class 아노스대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아노스대사04()


class 아노스대사04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__8$', arg4=3, arg5=0)
        move_user_path(patrolName='MS2PatrolData_PC_01')
        set_skip(state=아노스대사04_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라딘대사03()


class 아노스대사04_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 라딘대사03()


class 라딘대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        set_conversation(type=2, spawnId=11000264, script='$02000026_IN__MAIN__9$', arg4=4, arg5=0)
        set_skip(state=라딘대사03_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return PC안녕()


class 라딘대사03_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return PC안녕()


class PC안녕(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Hello_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아노스대사05()


class 아노스대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__10$', arg4=3, arg5=0)
        set_skip(state=아노스대사05_skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3343):
            return 아노스대사06()


class 아노스대사05_skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 아노스대사06()


class 아노스대사06(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=3000)
        set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__11$', arg4=3, arg5=0)
        show_caption(type='NameCaption', title='$02000026_IN__MAIN__12$', desc='$02000026_IN__MAIN__13$', align='centerLeft', offsetRateX=0.05, offsetRateY=0.15, duration=5000, scale=2)
        set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출종료()


class 아노스만남_스킵완료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[101,102])
        create_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        set_achievement(triggerId=9000, type='trigger', achieve='MeetAnos')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    pass


