""" trigger/02000026_in/main.xml """
import common


class start(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102])
        self.set_mesh(triggerIds=[4001,4002], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[3]):
            return 조건체크01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[2]):
            return 아노스있음01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[1]):
            return 아노스만남연출대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001567], questStates=[3]):
            return 대기조건01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001567], questStates=[2]):
            return 대기조건01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001567], questStates=[1]):
            return 기본상태(self.ctx)


class 대기조건01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[1]):
            return 아노스만남연출시작(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001568], questStates=[1]):
            return start(self.ctx)


class 조건체크01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001569], questStates=[1]):
            return 아노스있음01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001569], questStates=[1]):
            return 조건체크02(self.ctx)


class 조건체크02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001573], questStates=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001568,50001569,50001570,50001571,50001572,50001573], questStates=[2]):
            return 아노스있음01(self.ctx)


class 기본상태(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return start(self.ctx)


class 아노스있음01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_mesh(triggerIds=[4001,4002], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 아노스만남연출대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_mesh(triggerIds=[4001,4002], visible=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            self.move_user_path(patrolName='MS2PatrolData_PC_00')
            return 아노스만남연출시작(self.ctx)


class 아노스만남연출시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8000], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 아노스등장(self.ctx)


class 아노스등장(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_00')
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__0$', arg4=4, arg5=0)
        self.set_scene_skip(state=아노스만남_스킵완료, action='nextState') # setsceneskip 1 set

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아노스이동01(self.ctx)


class 아노스이동01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_01')
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__1$', arg4=3, arg5=0)
        # <action name="스킵을설정한다" arg1="아노스만남_스킵완료"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3239):
            return 아노스이동02(self.ctx)


class 아노스이동02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_02')
        # <action name="스킵을설정한다" arg1="아노스만남_스킵완료"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아노스이동03(self.ctx)


class 아노스이동03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__2$', arg4=3, arg5=0)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='ChatUp_A')
        # <action name="스킵을설정한다" arg1="아노스만남_스킵완료"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4623):
            return 아노스대사01(self.ctx)


class 아노스대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__3$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=아노스대사01_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라이동_라딘01(self.ctx)


class 아노스대사01_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 카메라이동_라딘01(self.ctx)


class 카메라이동_라딘01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라딘대사01(self.ctx)


class 라딘대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000264, script='$02000026_IN__MAIN__4$', arg4=3, arg5=0)
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_A')
        self.set_skip(state=라딘대사01_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4623):
            return 아노스대사02(self.ctx)


class 라딘대사01_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 아노스대사02(self.ctx)


class 아노스대사02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4000)
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__5$', arg4=4, arg5=0)
        self.set_skip(state=아노스대사02_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4519):
            return 라딘대사02(self.ctx)


class 아노스대사02_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 라딘대사02(self.ctx)


class 라딘대사02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='ChatUP_A')
        # <action name="SetNpcEmotionLoop" arg1="103" arg2="ChatUP_A" arg3="4000"/>
        self.set_conversation(type=2, spawnId=11000264, script='$02000026_IN__MAIN__6$', arg4=4, arg5=0)
        self.set_skip(state=라딘대사02_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4780):
            return 카메라이동_아노스01(self.ctx)


class 라딘대사02_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 카메라이동_아노스01(self.ctx)


class 카메라이동_아노스01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아노스대사03(self.ctx)


class 아노스대사03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='ChatUp_A')
        # <action name="SetNpcEmotionLoop" arg1="102" arg2="ChatUp_A" arg3="3000" />
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__7$', arg4=3, arg5=0)
        self.set_skip(state=아노스대사03_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6817):
            return 아노스대사04(self.ctx)


class 아노스대사03_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 아노스대사04(self.ctx)


class 아노스대사04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__8$', arg4=3, arg5=0)
        self.move_user_path(patrolName='MS2PatrolData_PC_01')
        self.set_skip(state=아노스대사04_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라딘대사03(self.ctx)


class 아노스대사04_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 라딘대사03(self.ctx)


class 라딘대사03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        self.set_conversation(type=2, spawnId=11000264, script='$02000026_IN__MAIN__9$', arg4=4, arg5=0)
        self.set_skip(state=라딘대사03_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return PC안녕(self.ctx)


class 라딘대사03_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return PC안녕(self.ctx)


class PC안녕(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Hello_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사05(self.ctx)


class 아노스대사05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__10$', arg4=3, arg5=0)
        self.set_skip(state=아노스대사05_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3343):
            return 아노스대사06(self.ctx)


class 아노스대사05_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 아노스대사06(self.ctx)


class 아노스대사06(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=3000)
        self.set_conversation(type=2, spawnId=11003313, script='$02000026_IN__MAIN__11$', arg4=3, arg5=0)
        self.show_caption(type='NameCaption', title='$02000026_IN__MAIN__12$', desc='$02000026_IN__MAIN__13$', align='centerLeft', offsetRateX=0.05, offsetRateY=0.15, duration=5000, scale=2)
        self.set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연출종료(self.ctx)


class 아노스만남_스킵완료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[101,102])
        self.create_monster(spawnIds=[102])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_achievement(triggerId=9000, type='trigger', achieve='MeetAnos')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = start
