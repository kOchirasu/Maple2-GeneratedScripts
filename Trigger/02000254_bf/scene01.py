""" trigger/02000254_bf/scene01.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101])
        self.create_monster(spawnIds=[107])
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[601], visible=False) # 칼 음성
        self.set_effect(triggerIds=[602], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[603], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[604], visible=False) # 칼 음성
        self.set_effect(triggerIds=[605], visible=False) # 칼 음성
        self.set_effect(triggerIds=[606], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[607], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[608], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[401], visible=False)
        self.set_effect(triggerIds=[402], visible=False)
        self.set_effect(triggerIds=[403], visible=False)
        self.set_effect(triggerIds=[404], visible=False)
        self.set_effect(triggerIds=[405], visible=False)
        self.set_effect(triggerIds=[406], visible=False)
        self.set_effect(triggerIds=[407], visible=False)
        self.set_effect(triggerIds=[408], visible=False)
        self.set_effect(triggerIds=[409], visible=False)
        self.set_effect(triggerIds=[410], visible=False)
        self.set_effect(triggerIds=[411], visible=False)
        self.set_effect(triggerIds=[412], visible=False)
        self.set_effect(triggerIds=[413], visible=False)
        self.set_effect(triggerIds=[414], visible=False)
        self.set_effect(triggerIds=[415], visible=False)
        self.set_effect(triggerIds=[416], visible=False)
        self.set_effect(triggerIds=[417], visible=False)
        self.set_effect(triggerIds=[418], visible=False)
        self.set_effect(triggerIds=[419], visible=False)
        self.set_effect(triggerIds=[420], visible=False)
        self.set_effect(triggerIds=[421], visible=False)
        self.set_effect(triggerIds=[422], visible=False)
        self.set_effect(triggerIds=[423], visible=False)
        self.set_effect(triggerIds=[424], visible=False)
        self.set_effect(triggerIds=[425], visible=False)
        self.set_effect(triggerIds=[426], visible=False)
        self.set_effect(triggerIds=[427], visible=False)
        self.set_effect(triggerIds=[428], visible=False)
        self.set_effect(triggerIds=[429], visible=False)
        self.set_effect(triggerIds=[430], visible=False)
        self.set_effect(triggerIds=[431], visible=False)
        self.set_effect(triggerIds=[432], visible=False)
        self.set_effect(triggerIds=[433], visible=False)
        self.set_effect(triggerIds=[434], visible=False)
        self.set_effect(triggerIds=[435], visible=False)
        self.set_effect(triggerIds=[436], visible=False)
        self.set_effect(triggerIds=[437], visible=False)
        self.set_effect(triggerIds=[438], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=901, boxId=1):
            return 연출시작딜레이(self.ctx)


class 연출시작딜레이(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_scene_skip(state=스킵벨라이동딜레이, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대화시작(self.ctx)


class 대화시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[401], visible=False)
        self.set_timer(timerId='1', seconds=6)
        # <action name="이펙트를설정한다" arg1="601" arg2="1"/>
        self.add_cinematic_talk(npcId=11000074, illustId='Karl_closeEye', msg='$02000254_BF__SCENE01__0$', duration=6000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사1(self.ctx)


class 벨라대사1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        # <action name="이펙트를설정한다" arg1="602" arg2="1"/>
        self.set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__1$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사2(self.ctx)


class 벨라대사2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=7)
        # <action name="이펙트를설정한다" arg1="603" arg2="1"/>
        self.set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__2$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 칼대사1(self.ctx)


class 칼대사1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)
        # <action name="이펙트를설정한다" arg1="604" arg2="1"/>
        self.add_cinematic_talk(npcId=11000074, illustId='Karl_closeEye', msg='$02000254_BF__SCENE01__3$', duration=5000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 칼대사2(self.ctx)


class 칼대사2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)
        # <action name="이펙트를설정한다" arg1="605" arg2="1"/>
        self.add_cinematic_talk(npcId=11000074, illustId='Karl_closeEye', msg='$02000254_BF__SCENE01__4$', duration=5000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사3(self.ctx)


class 벨라대사3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)
        # <action name="이펙트를설정한다" arg1="606" arg2="1"/>
        self.set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__5$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사4(self.ctx)


class 벨라대사4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)
        # <action name="이펙트를설정한다" arg1="607" arg2="1"/>
        self.set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__6$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라이동(self.ctx)


class 벨라이동딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라이동(self.ctx)


class 벨라이동(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 카메라원위치(self.ctx)


class 카메라원위치(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 카메라원위치2(self.ctx)


class 카메라원위치2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=902, boxId=1):
            return 쿠당탕(self.ctx)


class 쿠당탕(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102])
        self.set_effect(triggerIds=[402], visible=True)
        self.set_effect(triggerIds=[403], visible=True)
        self.set_effect(triggerIds=[404], visible=True)
        self.set_effect(triggerIds=[405], visible=True)
        self.set_effect(triggerIds=[406], visible=True)
        self.set_effect(triggerIds=[407], visible=True)
        self.set_effect(triggerIds=[408], visible=True)
        self.set_effect(triggerIds=[409], visible=True)
        self.set_effect(triggerIds=[410], visible=True)
        self.set_effect(triggerIds=[411], visible=True)
        self.set_effect(triggerIds=[412], visible=True)
        self.set_effect(triggerIds=[413], visible=True)
        self.set_effect(triggerIds=[414], visible=True)
        self.set_effect(triggerIds=[415], visible=True)
        self.set_effect(triggerIds=[416], visible=True)
        self.set_effect(triggerIds=[417], visible=True)
        self.set_effect(triggerIds=[418], visible=True)
        self.set_effect(triggerIds=[419], visible=True)
        self.set_effect(triggerIds=[420], visible=True)
        self.set_effect(triggerIds=[421], visible=True)
        self.set_effect(triggerIds=[422], visible=True)
        self.set_effect(triggerIds=[423], visible=True)
        self.set_effect(triggerIds=[424], visible=True)
        self.set_effect(triggerIds=[425], visible=True)
        self.set_effect(triggerIds=[426], visible=True)
        self.set_effect(triggerIds=[427], visible=True)
        self.set_effect(triggerIds=[428], visible=True)
        self.set_effect(triggerIds=[429], visible=True)
        self.set_effect(triggerIds=[430], visible=True)
        self.set_effect(triggerIds=[431], visible=True)
        self.set_effect(triggerIds=[432], visible=True)
        self.set_effect(triggerIds=[433], visible=True)
        self.set_effect(triggerIds=[434], visible=True)
        self.set_effect(triggerIds=[435], visible=True)
        self.set_effect(triggerIds=[436], visible=True)
        self.set_effect(triggerIds=[437], visible=True)
        self.set_effect(triggerIds=[438], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.true(arg1=True):
            return 벨라대사5(self.ctx)


class 스킵벨라이동딜레이(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timerId='1', seconds=1)
        self.select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 스킵벨라이동(self.ctx)


class 스킵벨라이동(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_1')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스킵카메라원위치(self.ctx)


class 스킵카메라원위치(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=902, boxId=1):
            return 스킵쿠당탕(self.ctx)


class 스킵쿠당탕(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102])
        self.set_effect(triggerIds=[402], visible=True)
        self.set_effect(triggerIds=[403], visible=True)
        self.set_effect(triggerIds=[404], visible=True)
        self.set_effect(triggerIds=[405], visible=True)
        self.set_effect(triggerIds=[406], visible=True)
        self.set_effect(triggerIds=[407], visible=True)
        self.set_effect(triggerIds=[408], visible=True)
        self.set_effect(triggerIds=[409], visible=True)
        self.set_effect(triggerIds=[410], visible=True)
        self.set_effect(triggerIds=[411], visible=True)
        self.set_effect(triggerIds=[412], visible=True)
        self.set_effect(triggerIds=[413], visible=True)
        self.set_effect(triggerIds=[414], visible=True)
        self.set_effect(triggerIds=[415], visible=True)
        self.set_effect(triggerIds=[416], visible=True)
        self.set_effect(triggerIds=[417], visible=True)
        self.set_effect(triggerIds=[418], visible=True)
        self.set_effect(triggerIds=[419], visible=True)
        self.set_effect(triggerIds=[420], visible=True)
        self.set_effect(triggerIds=[421], visible=True)
        self.set_effect(triggerIds=[422], visible=True)
        self.set_effect(triggerIds=[423], visible=True)
        self.set_effect(triggerIds=[424], visible=True)
        self.set_effect(triggerIds=[425], visible=True)
        self.set_effect(triggerIds=[426], visible=True)
        self.set_effect(triggerIds=[427], visible=True)
        self.set_effect(triggerIds=[428], visible=True)
        self.set_effect(triggerIds=[429], visible=True)
        self.set_effect(triggerIds=[430], visible=True)
        self.set_effect(triggerIds=[431], visible=True)
        self.set_effect(triggerIds=[432], visible=True)
        self.set_effect(triggerIds=[433], visible=True)
        self.set_effect(triggerIds=[434], visible=True)
        self.set_effect(triggerIds=[435], visible=True)
        self.set_effect(triggerIds=[436], visible=True)
        self.set_effect(triggerIds=[437], visible=True)
        self.set_effect(triggerIds=[438], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.true(arg1=True):
            return 벨라대사5딜레이(self.ctx)


class 벨라대사5딜레이(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 벨라대사5(self.ctx)


class 벨라대사5(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=True)
        self.set_scene_skip(state=벨라이동2, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='1', seconds=6)
        self.set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__7$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사6(self.ctx)


class 벨라대사6(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        # <action name="이펙트를설정한다" arg1="608" arg2="1"/>
        self.set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__8$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라이동2(self.ctx)


class 벨라이동2(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='1', seconds=4)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 이펙트1(self.ctx)


class 이펙트1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[401], visible=True)
        self.destroy_monster(spawnIds=[102])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라몬스터소환(self.ctx)


class 벨라몬스터소환(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.select_camera(triggerId=303, enable=True)
        self.create_monster(spawnIds=[106])
        self.create_monster(spawnIds=[103])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 끝(self.ctx)


class 끝(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.select_camera_path(pathIds=[303], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 끝2(self.ctx)


class 끝2(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=False)
        self.select_camera(triggerId=303, enable=False)
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 시작대기중
