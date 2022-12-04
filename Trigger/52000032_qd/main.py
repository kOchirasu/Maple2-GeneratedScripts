""" trigger/52000032_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=False, initialSequence='Idle_A')
        self.set_mesh(triggerIds=[3001,3002,3003], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3004], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3005], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_effect(triggerIds=[604], visible=False)
        self.set_effect(triggerIds=[605], visible=False)
        self.set_effect(triggerIds=[606], visible=False)
        self.set_effect(triggerIds=[607], visible=False)
        self.set_effect(triggerIds=[608], visible=False)
        self.set_effect(triggerIds=[609], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,2001], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 홀슈타트변신(self.ctx)


class 홀슈타트변신(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2001])
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.set_effect(triggerIds=[601], visible=False)
        # action name="메쉬를설정한다" arg1="3001-3003" arg2="0" arg3="0" arg4="0" arg5="2" /
        self.set_effect(triggerIds=[605], visible=True)
        self.add_buff(boxIds=[2002], skillId=71000005, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 유페리아대사01(self.ctx)


class 유페리아대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=True, initialSequence='Idle_A')
        self.select_camera(triggerId=3022, enable=True)
        self.set_effect(triggerIds=[606], visible=True)
        self.set_conversation(type=2, spawnId=11001564, script='$52000032_QD__MAIN__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 유페리아돌진(self.ctx)


class 유페리아돌진(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 카메라전환(self.ctx)


class 카메라전환(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=303, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 이슈라돌진(self.ctx)


class 이슈라돌진(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=True)
        self.select_camera(triggerId=3033, enable=True)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=550):
            return 홀슈타트어택(self.ctx)


class 홀슈타트어택(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            self.set_effect(triggerIds=[604], visible=True)
            self.set_effect(triggerIds=[602], visible=True)
            return 화면전환대기(self.ctx)


class 화면전환대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            self.destroy_monster(spawnIds=[1001,1003])
            return 홀슈타트대사01(self.ctx)


class 홀슈타트대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3034, enable=True)
        self.set_conversation(type=2, spawnId=11001231, script='$52000032_QD__MAIN__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 홀슈타트이동(self.ctx)


class 홀슈타트이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[2002]):
            return 홀슈타트소멸(self.ctx)


class 홀슈타트소멸(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1101,1102], animationEffect=False)
        self.destroy_monster(spawnIds=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=False, initialSequence='Idle_A')
        self.create_monster(spawnIds=[2099], animationEffect=False)
        # action name="카메라를선택한다" arg1="304" arg2="1"/

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101], jobCode=1):
            return 투입대사10(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=10):
            return 투입대사10(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=20):
            return 투입대사20(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=30):
            return 투입대사30(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=40):
            return 투입대사40(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=50):
            return 투입대사50(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=60):
            return 투입대사60(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=70):
            return 투입대사70(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=80):
            return 투입대사80(self.ctx)
        if self.user_detected(boxIds=[101], jobCode=90):
            return 투입대사90(self.ctx)


class 투입대사10(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__2$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11000076, script='$52000032_QD__MAIN__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사20(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__4$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001581, script='$52000032_QD__MAIN__5$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사30(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__6$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 투입대사30_1(self.ctx)


class 투입대사30_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[608], visible=True)
        self.set_conversation(type=2, spawnId=11000032, script='$52000032_QD__MAIN__7$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사40(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__8$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001578, script='$52000032_QD__MAIN__9$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사50(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__10$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11000015, script='$52000032_QD__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사60(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__12$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001583, script='$52000032_QD__MAIN__13$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사70(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__14$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001586, script='$52000032_QD__MAIN__15$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사80(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__16$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001584, script='$52000032_QD__MAIN__17$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 투입대사90(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__18$', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__19$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 누타만전투(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 누타만전투(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 누타만전투종료(self.ctx)


class 누타만전투종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=305, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 렌듀비앙대사01(self.ctx)


class 렌듀비앙대사01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1103,1104], animationEffect=False)
        self.select_camera(triggerId=304, enable=True)
        self.set_conversation(type=2, spawnId=11001575, script='$52000032_QD__MAIN__20$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 유페리아대사_흐느낌(self.ctx)


class 유페리아대사_흐느낌(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[607], visible=True)
        self.set_conversation(type=2, spawnId=11001576, script='$52000032_QD__MAIN__21$', arg4=8, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8500):
            return 아노스대사01(self.ctx)


class 아노스대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[609], visible=True)
        self.set_conversation(type=2, spawnId=11000032, script='$52000032_QD__MAIN__22$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 렌듀비앙대사02(self.ctx)


class 렌듀비앙대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001230, script='$52000032_QD__MAIN__23$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 렌듀비앙이동(self.ctx)


class 렌듀비앙이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1103, patrolName='MS2PatrolData_1103_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 렌듀비앙캐스팅(self.ctx)


class 렌듀비앙캐스팅(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1103], skillId=71000004, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3004], visible=True, arg3=0, delay=0, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)

    def on_exit(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='ClearNutaman')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=2000023, portalId=100)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
