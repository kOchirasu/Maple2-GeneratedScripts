""" trigger/52000048_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], animationEffect=False)
        self.create_monster(spawnIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110], animationEffect=False)
        self.create_monster(spawnIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210], animationEffect=False)
        self.create_monster(spawnIds=[2001])
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[600], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1102, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1103, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1104, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1105, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1106, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1107, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1108, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1109, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1110, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1006, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1008, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1009, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1010, patrolName='MS2PatrolData_B')
        self.move_npc(spawnId=1201, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1202, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1203, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1204, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1205, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1206, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1207, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1208, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1209, patrolName='MS2PatrolData_C')
        self.move_npc(spawnId=1210, patrolName='MS2PatrolData_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 칸두라이동(self.ctx)


class 칸두라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_K1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            self.set_npc_emotion_sequence(spawnId=2001, sequenceName='Attack_01_A')
            return 칸두라이동2(self.ctx)


class 칸두라이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.move_npc(spawnId=2001, patrolName='MS2PatrolData_K2')
            return 카메라이동대기(self.ctx)


class 카메라이동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 카메라이동2(self.ctx)


class 카메라이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=303, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 라오즈등장(self.ctx)


class 라오즈등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[601], visible=True)
        self.create_monster(spawnIds=[2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return PC말풍선(self.ctx)


class PC말풍선(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_PC')
        self.set_conversation(type=1, spawnId=0, script='$52000048_QD__MAIN__0$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 라오즈대사01(self.ctx)


class 라오즈대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001768, script='$52000048_QD__MAIN__1$', arg4=3)
        self.set_skip(state=라오즈대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라오즈대사02(self.ctx)


class 라오즈대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 라오즈대사02(self.ctx)


class 라오즈대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001768, script='$52000048_QD__MAIN__2$', arg4=6)
        self.set_skip(state=라오즈대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 라오즈대사03(self.ctx)


class 라오즈대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 라오즈대사03(self.ctx)


class 라오즈대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=304, enable=True)
        self.set_conversation(type=2, spawnId=11001768, script='$52000048_QD__MAIN__3$', arg4=6)
        self.set_skip(state=라오즈대사03스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 퀘스트완료(self.ctx)


class 라오즈대사03스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 퀘스트완료(self.ctx)


class 퀘스트완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=101, type='trigger', achieve='MessageThroughAnimar')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=304, enable=False)
        self.move_user(mapId=52000050, portalId=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
