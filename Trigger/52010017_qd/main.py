""" trigger/52010017_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(triggerIds=[401], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[402], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[403], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[404], visible=False, animationEffect=False, animationDelay=0)
        self.set_ladder(triggerIds=[405], visible=False, animationEffect=False, animationDelay=0)
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3003], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3004], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3005], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3006], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3007], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3008], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[102], questIds=[10002851], questStates=[1]):
            self.create_monster(spawnIds=[1002], animationEffect=False)
            self.create_monster(spawnIds=[1003], animationEffect=False)
            self.create_monster(spawnIds=[1004], animationEffect=False)
            self.create_monster(spawnIds=[2001], animationEffect=True)
            return 카메라연출01(self.ctx)


class 카메라연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 미카대사01(self.ctx)


class 미카대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1001])
        self.create_monster(spawnIds=[1005], animationEffect=False)
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005')
        self.set_ladder(triggerIds=[401], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[402], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[403], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[404], visible=True, animationEffect=True, animationDelay=0)
        self.set_ladder(triggerIds=[405], visible=True, animationEffect=True, animationDelay=0)
        self.set_conversation(type=2, spawnId=11001285, script='$52010017_QD__MAIN__0$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 체크포인트01(self.ctx)


class 체크포인트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            self.create_monster(spawnIds=[2002], animationEffect=True)
            return 카메라연출02(self.ctx)


class 카메라연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 미카대사02(self.ctx)


class 미카대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001285, script='$52010017_QD__MAIN__1$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.select_camera(triggerId=302, enable=False)
            return 체크포인트02(self.ctx)


class 체크포인트02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_A')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2002]):
            return 미키이동01(self.ctx)


class 미키이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_A2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[1005]):
            return 오브젝트01(self.ctx)


class 오브젝트01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)
            return 카메라연출03(self.ctx)


class 카메라연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 타라대사01(self.ctx)


class 타라대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001218, script='$52010017_QD__MAIN__2$', arg4=2)
        self.select_camera(triggerId=303, enable=True)
        self.create_monster(spawnIds=[2003], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 체크포인트03(self.ctx)


class 체크포인트03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=303, enable=False)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_B')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_B')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_B')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2003]):
            return 미키이동02(self.ctx)


class 미키이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_B2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=104, spawnIds=[1005]):
            return 오브젝트02(self.ctx)


class 오브젝트02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_mesh(triggerIds=[3003], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3004], visible=True, arg3=0, delay=0, scale=0)
            return 카메라연출04(self.ctx)


class 카메라연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 둔바대사01(self.ctx)


class 둔바대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=304, enable=True)
        self.set_conversation(type=2, spawnId=11001217, script='$52010017_QD__MAIN__3$', arg4=2)
        self.create_monster(spawnIds=[2004], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 체크포인트04(self.ctx)


class 체크포인트04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=304, enable=False)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_C')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_C')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_C')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2004]):
            return 미키이동03(self.ctx)


class 미키이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_C2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=105, spawnIds=[1005]):
            return 오브젝트03(self.ctx)


class 오브젝트03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_mesh(triggerIds=[3005], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3006], visible=True, arg3=0, delay=0, scale=0)
            return 카메라연출05(self.ctx)


class 카메라연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 스타츠대사01(self.ctx)


class 스타츠대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=305, enable=True)
        self.set_conversation(type=2, spawnId=11001292, script='$52010017_QD__MAIN__4$', arg4=2)
        self.create_monster(spawnIds=[2005], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 체크포인트05(self.ctx)


class 체크포인트05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=305, enable=False)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_D')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_D')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_D')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2005]):
            return 미키이동04(self.ctx)


class 미키이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_D2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=106, spawnIds=[1005]):
            return 오브젝트04(self.ctx)


class 오브젝트04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_mesh(triggerIds=[3007], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3008], visible=True, arg3=0, delay=0, scale=0)
            return 카메라연출06(self.ctx)


class 카메라연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_D3')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 미카대사03(self.ctx)


class 미카대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001285, script='$52010017_QD__MAIN__5$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 미카대사04(self.ctx)


class 미카대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001285, script='$52010017_QD__MAIN__6$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 이동대기(self.ctx)


class 이동대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=110, type='trigger', achieve='Getalllamestone')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.move_user(mapId=2010034, portalId=3, boxId=110)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
