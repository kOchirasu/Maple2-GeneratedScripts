""" trigger/52000023_qd/main01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 종이문서 발견 사운드 이펙트
        self.set_effect(triggerIds=[6001], visible=False) # Ishura Voice 00001274
        self.set_effect(triggerIds=[6002], visible=False) # Ishura Voice 00001275
        self.set_effect(triggerIds=[6003], visible=False) # Ishura Voice 00001276
        self.set_effect(triggerIds=[6004], visible=False) # Ishura Voice 00001277
        self.set_effect(triggerIds=[6005], visible=False) # Ishura Voice 00001278
        self.set_effect(triggerIds=[6006], visible=False) # Ishura Voice 00001279
        self.set_effect(triggerIds=[6007], visible=False) # Ishura Voice 00001280
        self.set_effect(triggerIds=[6008], visible=False) # Ishura Voice 00001281
        self.set_effect(triggerIds=[6009], visible=False) # Ishura Voice 00001282
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8100], visible=False)
        self.set_agent(triggerIds=[8101], visible=False)
        self.set_agent(triggerIds=[8102], visible=False)
        self.set_agent(triggerIds=[8103], visible=False)
        self.set_agent(triggerIds=[8104], visible=False)
        self.set_agent(triggerIds=[8105], visible=False)
        self.set_agent(triggerIds=[8106], visible=False)
        self.set_agent(triggerIds=[8107], visible=False)
        self.set_agent(triggerIds=[8108], visible=False)
        self.set_agent(triggerIds=[8109], visible=False)
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000617], state=0)
        self.set_interact_object(triggerIds=[10000618], state=0)
        self.set_interact_object(triggerIds=[10000619], state=0)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[20002230], questStates=[1]):
            return 연출준비(self.ctx)


class 연출준비(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8100], visible=True)
        self.set_agent(triggerIds=[8101], visible=True)
        self.set_agent(triggerIds=[8102], visible=True)
        self.set_agent(triggerIds=[8103], visible=True)
        self.set_agent(triggerIds=[8104], visible=True)
        self.set_agent(triggerIds=[8105], visible=True)
        self.set_agent(triggerIds=[8106], visible=True)
        self.set_agent(triggerIds=[8107], visible=True)
        self.set_agent(triggerIds=[8108], visible=True)
        self.set_agent(triggerIds=[8109], visible=True)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 유저이동01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 유저이동01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 유저이동02(self.ctx)


class 유저이동02(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_100')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 유저이동03(self.ctx)


class 유저이동03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투준비01(self.ctx)


class 전투준비01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True) # Ishura Voice 00001274
        self.set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__0$', arg4=6, arg5=0) # 음성코드 	00001274
        self.set_skip(state=전투준비02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 전투준비02(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 전투준비02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=False) # Ishura Voice 00001274
        self.set_effect(triggerIds=[6002], visible=True) # Ishura Voice 00001275
        self.set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__1$', arg4=4, arg5=0) # 음성코드 	00001275
        self.set_skip(state=전투시작)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투시작(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 전투시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=603, enable=False)
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8100], visible=False)
        self.set_agent(triggerIds=[8101], visible=False)
        self.set_agent(triggerIds=[8102], visible=False)
        self.set_agent(triggerIds=[8103], visible=False)
        self.set_agent(triggerIds=[8104], visible=False)
        self.set_agent(triggerIds=[8105], visible=False)
        self.set_agent(triggerIds=[8106], visible=False)
        self.set_agent(triggerIds=[8107], visible=False)
        self.set_agent(triggerIds=[8108], visible=False)
        self.set_agent(triggerIds=[8109], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[901,902,903,904,905,906,907,908,909,910]):
            return 대화준비01(self.ctx)


class 대화준비01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=False) # Ishura Voice 00001275
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대화준비02(self.ctx)


class 대화준비02(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_200')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9002]):
            return 대화준비03(self.ctx)


class 대화준비03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이슈라대화01(self.ctx)


class 이슈라대화01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=True) # Ishura Voice 00001276
        self.set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__2$', arg4=8, arg5=0) # 음성코드 	00001276
        self.set_skip(state=이슈라대화02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 이슈라대화02(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 이슈라대화02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=False) # Ishura Voice 00001276
        self.set_effect(triggerIds=[6004], visible=True) # Ishura Voice 00001277
        self.set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__3$', arg4=8, arg5=0) # 음성코드 	00001277
        self.set_skip(state=이슈라대화03)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 이슈라대화03(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 이슈라대화03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6004], visible=False) # Ishura Voice 00001277
        self.set_effect(triggerIds=[6005], visible=True) # Ishura Voice 00001278
        self.set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__4$', arg4=7, arg5=0) # 음성코드 	00001278
        self.set_skip(state=이슈라대화04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 이슈라대화04(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 이슈라대화04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6005], visible=False) # Ishura Voice 00001278
        self.set_effect(triggerIds=[6006], visible=True) # Ishura Voice 00001279
        self.set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__5$', arg4=6, arg5=0) # 음성코드 	00001279
        self.set_skip(state=수색준비)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 수색준비(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 수색준비(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6006], visible=False) # Ishura Voice 00001279
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.set_interact_object(triggerIds=[10000617], state=1)
        self.set_interact_object(triggerIds=[10000618], state=1)
        self.set_interact_object(triggerIds=[10000619], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 수색시작(self.ctx)


class 수색시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=25200231, textId=25200231)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_101')

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000617], stateValue=0):
            return 수색종료01(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[5001], visible=True) # 종이문서 발견 사운드 이펙트
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0)


class 수색종료01(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000618], state=0)
        self.set_interact_object(triggerIds=[10000619], state=0)
        self.hide_guide_summary(entityId=25200231)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 수색종료02(self.ctx)


class 수색종료02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_104')
        self.set_effect(triggerIds=[6007], visible=True) # Ishura Voice 00001280
        self.set_conversation(type=1, spawnId=103, script='$52000023_QD__MAIN01__6$', arg4=3, arg5=0) # 음성코드 	00001280

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 정리준비01(self.ctx)


class 정리준비01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        self.select_camera(triggerId=604, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9003, spawnIds=[103]):
            return 정리준비02(self.ctx)


class 정리준비02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6007], visible=False) # Ishura Voice 00001280

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 정리대화01(self.ctx)


class 정리대화01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6008], visible=True) # Ishura Voice 00001281
        self.set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__7$', arg4=9, arg5=0) # 음성코드 	00001281
        self.set_skip(state=정리대화02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 정리대화02(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 정리대화02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6008], visible=False) # Ishura Voice 00001281
        self.set_effect(triggerIds=[6009], visible=True) # Ishura Voice 00001282
        self.set_conversation(type=2, spawnId=11001244, script='$52000023_QD__MAIN01__8$', arg4=5, arg5=0) # 음성코드 	00001282
        self.set_skip(state=퇴장준비)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 퇴장준비(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk()


class 퇴장준비(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=604, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 퇴장중(self.ctx)


class 퇴장중(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9900, type='trigger', achieve='MeetAgain_Ishura')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_103')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9004, spawnIds=[103]):
            return 퇴장완료(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[103])


class 퇴장완료(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6009], visible=False) # Ishura Voice 00001282


initial_state = 대기
