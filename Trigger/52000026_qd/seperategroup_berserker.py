""" trigger/52000026_qd/seperategroup_berserker.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=10000, enable=False) # TriaAttack
        self.set_effect(triggerIds=[5000], visible=False) # LeftDoorOpen
        self.set_effect(triggerIds=[5001], visible=False) # LeftDoorClose
        self.set_effect(triggerIds=[5002], visible=False) # RightDoorOpen
        self.set_effect(triggerIds=[5003], visible=False) # RightDoorClose
        self.set_effect(triggerIds=[5004], visible=False) # blastjump
        self.set_effect(triggerIds=[6001], visible=False) # Asimov Voice 00000553 / everytime
        self.set_effect(triggerIds=[6002], visible=False) # Asimov Voice 00001338 / everytime
        self.set_effect(triggerIds=[6003], visible=False) # Asimov Voice 00001339 / everytime
        self.set_effect(triggerIds=[6004], visible=False) # Asimov Voice 00001340 / everytime
        self.set_effect(triggerIds=[6005], visible=False) # Asimov Voice 00001341 / in case RuneBlader, Berserker, Priest, Wizard
        self.set_effect(triggerIds=[6006], visible=False) # Asimov Voice 00001342 / in case RuneBlader, Wizard
        self.set_effect(triggerIds=[6007], visible=False) # Asimov Voice 00000561 / in case Berserker
        self.set_effect(triggerIds=[6101], visible=False) # Ishura Voice 00001291 / only RB
        self.set_effect(triggerIds=[6102], visible=False) # Ishura Voice 00001292 / everytime
        self.set_effect(triggerIds=[6103], visible=False) # Ishura Voice 00001293 / only RB
        self.set_effect(triggerIds=[6104], visible=False) # Ishura Voice 00001155 / in case Assassin, Berserker, Heavygunner, Knight, Priest, Ranger, Thief, Wizard
        self.set_effect(triggerIds=[6105], visible=False) # Ishura Voice 00001159 / in case Assassin, Berserker, Heavygunner, Knight, Priest, Ranger, Thief, Wizard

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002963], questStates=[1], jobCode=20):
            return 연출준비01(self.ctx)


class 연출준비01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=3000, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출준비02(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출준비02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 유저이동01(self.ctx)


class 유저이동01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3001, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6500):
            return 차입장01_1(self.ctx)


class 차입장01_1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,201], animationEffect=True)
        self.set_effect(triggerIds=[5000], visible=True) # LeftDoorOpen
        self.move_user_path(patrolName='MS2PatrolData_2001')
        self.select_camera(triggerId=3002, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차입장02_1(self.ctx)


class 차입장02_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # LeftDoorClose
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        self.select_camera_path(pathIds=[3003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장03_1(self.ctx)


class 차입장03_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000601, script='$52000026_QD__SEPERATEGROUP_BERSERKER__0$', arg4=3, arg5=0)
        self.set_skip(state=차입장01_2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장01_2(self.ctx)


class 차입장01_2(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[5002], visible=True) # RightDoorOpen
        self.select_camera(triggerId=3100, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차입장02_2(self.ctx)


class 차입장02_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301], animationEffect=True)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        self.move_user_path(patrolName='MS2PatrolData_2002')
        self.set_effect(triggerIds=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 차입장03_2(self.ctx)


class 차입장03_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401], animationEffect=True)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차입장04_2(self.ctx)


class 차입장04_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6104], visible=True) # 음성 코드 00001155
        self.set_conversation(type=2, spawnId=11001244, script='$52000026_QD__SEPERATEGROUP_BERSERKER__1$', arg4=3, arg5=0) # 음성 코드 00001155
        self.set_skip(state=차입장05_2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차입장05_2(self.ctx)


class 차입장05_2(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 차입장06_2(self.ctx)


class 차입장06_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001244, script='$52000026_QD__SEPERATEGROUP_BERSERKER__2$', arg4=4, arg5=0)
        self.set_skip(state=차입장07_2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장07_2(self.ctx)


class 차입장07_2(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[6101], visible=False) # Ishura Voice 00001291
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_302')
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_402')
        self.move_user_path(patrolName='MS2PatrolData_2003')
        self.select_camera(triggerId=3101, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차입장01_3(self.ctx)


class 차입장01_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # RightDoorOpen
        self.create_monster(spawnIds=[501], animationEffect=True)
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_501')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 차입장02_3(self.ctx)


class 차입장02_3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[601], animationEffect=True)
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_601')
        self.set_effect(triggerIds=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장03_3(self.ctx)


class 차입장03_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3102, enable=True)
        self.set_effect(triggerIds=[6001], visible=True) # Asimov Voice 00000553
        self.set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_BERSERKER__3$', arg4=7, arg5=0) # 음성 코드 00000553
        self.set_skip(state=차입장01_4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 차입장01_4(self.ctx)


class 차입장01_4(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[6001], visible=False) # Asimov Voice 00000553
        self.select_camera(triggerId=3200, enable=True)
        self.set_effect(triggerIds=[5002], visible=True) # RightDoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 차입장02_4(self.ctx)


class 차입장02_4(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3210, enable=True)
        self.create_monster(spawnIds=[701], animationEffect=True)
        self.move_npc(spawnId=701, patrolName='MS2PatrolData_701')
        self.set_effect(triggerIds=[5003], visible=True) # RightDoorClose

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차입장03_4(self.ctx)


class 차입장03_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001581, script='$52000026_QD__SEPERATEGROUP_BERSERKER__4$', arg4=3, arg5=0)
        self.set_skip(state=차입장04_4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차입장04_4(self.ctx)


class 차입장04_4(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 차입장05_4(self.ctx)


class 차입장05_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001581, script='$52000026_QD__SEPERATEGROUP_BERSERKER__5$', arg4=4, arg5=0)
        self.set_skip(state=차입장06_4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장06_4(self.ctx)


class 차입장06_4(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=3201, enable=True)
        self.create_monster(spawnIds=[801], animationEffect=True)
        self.move_npc(spawnId=801, patrolName='MS2PatrolData_801')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차입장07_4(self.ctx)


class 차입장07_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000076, script='$52000026_QD__SEPERATEGROUP_BERSERKER__6$', arg4=4, arg5=0)
        self.set_skip(state=차입장08_4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장08_4(self.ctx)


class 차입장08_4(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차입장01_5(self.ctx)


class 차입장01_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5004], visible=True) # blastjump

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차입장02_5(self.ctx)


class 차입장02_5(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=701, patrolName='MS2PatrolData_702')
        self.select_camera(triggerId=3300, enable=True)
        self.create_monster(spawnIds=[901], animationEffect=True)
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_901')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차입장03_5(self.ctx)


class 차입장03_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001583, script='$52000026_QD__SEPERATEGROUP_BERSERKER__7$', arg4=3, arg5=0)
        self.set_skip(state=차입장04_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장04_5(self.ctx)


class 차입장04_5(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=3301, enable=True)
        self.create_monster(spawnIds=[1001], animationEffect=True)
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차입장05_5(self.ctx)


class 차입장05_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001584, script='$52000026_QD__SEPERATEGROUP_BERSERKER__8$', arg4=4, arg5=0)
        self.set_skip(state=차입장06_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장06_5(self.ctx)


class 차입장06_5(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=3302, enable=True)
        self.create_monster(spawnIds=[1101], animationEffect=True)
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_1101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차입장07_5(self.ctx)


class 차입장07_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000015, script='$52000026_QD__SEPERATEGROUP_BERSERKER__9$', arg4=3, arg5=0)
        self.set_skip(state=차입장08_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 차입장08_5(self.ctx)


class 차입장08_5(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[5002], visible=True) # RightDoorOpen
        self.select_camera(triggerId=3303, enable=True)
        self.create_monster(spawnIds=[1201], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 차입장09_5(self.ctx)


class 차입장09_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True) # RightDoorClose
        self.move_npc(spawnId=1201, patrolName='MS2PatrolData_1201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 차입장10_5(self.ctx)


class 차입장10_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001586, script='$52000026_QD__SEPERATEGROUP_BERSERKER__10$', arg4=3, arg5=0)
        self.set_skip(state=차입장11_5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 차입장11_5(self.ctx)


class 차입장11_5(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=3304, enable=True)
        self.move_npc(spawnId=801, patrolName='MS2PatrolData_802')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 차입장12_5(self.ctx)


class 차입장12_5(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000076, script='$52000026_QD__SEPERATEGROUP_BERSERKER__11$', arg4=3, arg5=0)
        self.set_skip(state=입장완료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 입장완료01(self.ctx)


class 입장완료01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_sound(triggerId=10000, enable=True) # TriaAttack
        self.select_camera_path(pathIds=[3400,3401,3402,3403], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정렬01(self.ctx)


class 정렬01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=True) # Asimov Voice 00001338
        self.set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_BERSERKER__12$', arg4=5, arg5=0) # 음성 코드 00001338
        self.set_skip(state=정렬02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 정렬02(self.ctx)


class 정렬02(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_502')
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_602')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 정렬03(self.ctx)


class 정렬03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1002')
        self.move_npc(spawnId=1201, patrolName='MS2PatrolData_1202')
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_902')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 정렬04(self.ctx)


class 정렬04(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2004')
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_303')
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_403')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 정렬05(self.ctx)


class 정렬05(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_103')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_203')
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_1102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 정렬06(self.ctx)


class 정렬06(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6002], visible=False) # Asimov Voice 00001338
        self.move_npc(spawnId=701, patrolName='MS2PatrolData_703')
        self.move_npc(spawnId=801, patrolName='MS2PatrolData_803')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 본론01(self.ctx)


class 본론01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=True) # Asimov Voice 00001339
        self.set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_BERSERKER__13$', arg4=10, arg5=0) # 음성 코드 00001339
        self.set_skip(state=본론02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 본론02(self.ctx)


class 본론02(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 본론03(self.ctx)


class 본론03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=False) # Asimov Voice 00001339
        self.set_effect(triggerIds=[6004], visible=True) # Asimov Voice 00001340
        self.set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_BERSERKER__14$', arg4=6, arg5=0) # 음성 코드 00001340
        self.set_skip(state=본론04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 본론04(self.ctx)


class 본론04(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[6004], visible=False) # Asimov Voice 00001340
        self.select_camera(triggerId=3500, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 본론05(self.ctx)


class 본론05(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_304')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 본론06(self.ctx)


class 본론06(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_2005')
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_404')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 본론07(self.ctx)


class 본론07(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6102], visible=True) # Ishura Voice 00001292
        self.set_conversation(type=2, spawnId=11001244, script='$52000026_QD__SEPERATEGROUP_BERSERKER__15$', arg4=5, arg5=0) # 음성 코드 00001292
        self.set_skip(state=영상01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 영상01(self.ctx)


class 영상01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_effect(triggerIds=[6102], visible=False) # Ishura Voice 00001292

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상02(self.ctx)


class 영상02(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Royal_IshuraRemember.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상03(self.ctx)


class 영상03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 영상04(self.ctx)


class 영상04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 정리01(self.ctx)


class 정리01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3600, enable=True)
        self.set_effect(triggerIds=[6105], visible=True) # 음성 코드 00001159
        self.set_conversation(type=2, spawnId=11001244, script='$52000026_QD__SEPERATEGROUP_BERSERKER__16$', arg4=6, arg5=0) # 음성 코드 00001159
        self.set_skip(state=정리02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 정리02(self.ctx)


class 정리02(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[6103], visible=False) # Ishura Voice 00001293

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 반대01(self.ctx)


class 반대01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000076, script='$52000026_QD__SEPERATEGROUP_BERSERKER__17$', arg4=4, arg5=0)
        self.set_skip(state=반대02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 반대02(self.ctx)


class 반대02(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=3601, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 반대03(self.ctx)


class 반대03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001586, script='$52000026_QD__SEPERATEGROUP_BERSERKER__18$', arg4=4, arg5=0)
        self.set_skip(state=반대04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 반대04(self.ctx)


class 반대04(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.move_npc(spawnId=1201, patrolName='MS2PatrolData_1203')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 반대05(self.ctx)


class 반대05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3602, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 반대06(self.ctx)


class 반대06(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001584, script='$52000026_QD__SEPERATEGROUP_BERSERKER__19$', arg4=4, arg5=0)
        self.set_skip(state=반대07)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 반대07(self.ctx)


class 반대07(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1003')
        self.select_camera(triggerId=3603, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 반대08(self.ctx)


class 반대08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3604, enable=True)
        self.set_conversation(type=2, spawnId=11000015, script='$52000026_QD__SEPERATEGROUP_BERSERKER__20$', arg4=4, arg5=0)
        self.set_skip(state=반대09)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 반대09(self.ctx)


class 반대09(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.destroy_monster(spawnIds=[1201,1001])
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_1103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 반대10(self.ctx)


class 반대10(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=901, patrolName='MS2PatrolData_903')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 요약01(self.ctx)


class 요약01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3700, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 요약02(self.ctx)


class 요약02(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1101,901])
        self.set_conversation(type=2, spawnId=11000601, script='$52000026_QD__SEPERATEGROUP_BERSERKER__21$', arg4=3, arg5=0)
        self.set_skip(state=요약03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 요약03(self.ctx)


class 요약03(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_conversation(type=2, spawnId=11000601, script='$52000026_QD__SEPERATEGROUP_BERSERKER__22$', arg4=4, arg5=0)
        self.set_skip(state=요약04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 요약04(self.ctx)


class 요약04(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.select_camera(triggerId=3800, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 요약05(self.ctx)


class 요약05(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6005], visible=True) # Asimov Voice 00001341
        self.set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_BERSERKER__23$', arg4=9, arg5=0) # 음성 코드 00001341
        self.set_skip(state=요약06)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 요약06(self.ctx)


class 요약06(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6005], visible=False) # Asimov Voice 00001341
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 요약07(self.ctx)


class 요약07(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6007], visible=True) # 음성 코드 00000561
        self.set_conversation(type=2, spawnId=11000031, script='$52000026_QD__SEPERATEGROUP_BERSERKER__24$', arg4=4, arg5=0) # 음성 코드 00000561
        self.set_skip(state=연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출종료01(self.ctx)


class 연출종료01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[6007], visible=False) # Asimov Voice 00001342
        self.select_camera(triggerId=3801, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연출종료02(self.ctx)


class 연출종료02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=3801, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 업적발생(self.ctx)


class 업적발생(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9001, type='trigger', achieve='SeperateGroup')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 강제퇴장(self.ctx)


class 강제퇴장(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000001, portalId=17, boxId=9001)

    def on_exit(self):
        self.set_sound(triggerId=10000, enable=False) # TriaAttack


initial_state = 대기
