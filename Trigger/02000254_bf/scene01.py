""" trigger/02000254_bf/scene01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[107])
        self.set_mesh(trigger_ids=[3001], visible=True, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3002], visible=True, start_delay=0, interval=0, fade=0)
        self.set_effect(trigger_ids=[601], visible=False) # 칼 음성
        self.set_effect(trigger_ids=[602], visible=False) # 벨라 음성
        self.set_effect(trigger_ids=[603], visible=False) # 벨라 음성
        self.set_effect(trigger_ids=[604], visible=False) # 칼 음성
        self.set_effect(trigger_ids=[605], visible=False) # 칼 음성
        self.set_effect(trigger_ids=[606], visible=False) # 벨라 음성
        self.set_effect(trigger_ids=[607], visible=False) # 벨라 음성
        self.set_effect(trigger_ids=[608], visible=False) # 벨라 음성
        self.set_effect(trigger_ids=[401], visible=False)
        self.set_effect(trigger_ids=[402], visible=False)
        self.set_effect(trigger_ids=[403], visible=False)
        self.set_effect(trigger_ids=[404], visible=False)
        self.set_effect(trigger_ids=[405], visible=False)
        self.set_effect(trigger_ids=[406], visible=False)
        self.set_effect(trigger_ids=[407], visible=False)
        self.set_effect(trigger_ids=[408], visible=False)
        self.set_effect(trigger_ids=[409], visible=False)
        self.set_effect(trigger_ids=[410], visible=False)
        self.set_effect(trigger_ids=[411], visible=False)
        self.set_effect(trigger_ids=[412], visible=False)
        self.set_effect(trigger_ids=[413], visible=False)
        self.set_effect(trigger_ids=[414], visible=False)
        self.set_effect(trigger_ids=[415], visible=False)
        self.set_effect(trigger_ids=[416], visible=False)
        self.set_effect(trigger_ids=[417], visible=False)
        self.set_effect(trigger_ids=[418], visible=False)
        self.set_effect(trigger_ids=[419], visible=False)
        self.set_effect(trigger_ids=[420], visible=False)
        self.set_effect(trigger_ids=[421], visible=False)
        self.set_effect(trigger_ids=[422], visible=False)
        self.set_effect(trigger_ids=[423], visible=False)
        self.set_effect(trigger_ids=[424], visible=False)
        self.set_effect(trigger_ids=[425], visible=False)
        self.set_effect(trigger_ids=[426], visible=False)
        self.set_effect(trigger_ids=[427], visible=False)
        self.set_effect(trigger_ids=[428], visible=False)
        self.set_effect(trigger_ids=[429], visible=False)
        self.set_effect(trigger_ids=[430], visible=False)
        self.set_effect(trigger_ids=[431], visible=False)
        self.set_effect(trigger_ids=[432], visible=False)
        self.set_effect(trigger_ids=[433], visible=False)
        self.set_effect(trigger_ids=[434], visible=False)
        self.set_effect(trigger_ids=[435], visible=False)
        self.set_effect(trigger_ids=[436], visible=False)
        self.set_effect(trigger_ids=[437], visible=False)
        self.set_effect(trigger_ids=[438], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=901, min_users='1'):
            return 연출시작딜레이(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301, enable=True)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.set_scene_skip(state=스킵벨라이동딜레이, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대화시작(self.ctx)


class 대화시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[401], visible=False)
        self.set_timer(timer_id='1', seconds=6)
        # self.set_effect(trigger_ids=[601], visible=True)
        self.add_cinematic_talk(npc_id=11000074, illust_id='Karl_closeEye', msg='$02000254_BF__SCENE01__0$', duration=6000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사1(self.ctx)


class 벨라대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        # self.set_effect(trigger_ids=[602], visible=True)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000254_BF__SCENE01__1$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사2(self.ctx)


class 벨라대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=7)
        # self.set_effect(trigger_ids=[603], visible=True)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000254_BF__SCENE01__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 칼대사1(self.ctx)


class 칼대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        # self.set_effect(trigger_ids=[604], visible=True)
        self.add_cinematic_talk(npc_id=11000074, illust_id='Karl_closeEye', msg='$02000254_BF__SCENE01__3$', duration=5000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 칼대사2(self.ctx)


class 칼대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=5)
        # self.set_effect(trigger_ids=[605], visible=True)
        self.add_cinematic_talk(npc_id=11000074, illust_id='Karl_closeEye', msg='$02000254_BF__SCENE01__4$', duration=5000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사3(self.ctx)


class 벨라대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=6)
        # self.set_effect(trigger_ids=[606], visible=True)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000254_BF__SCENE01__5$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사4(self.ctx)


class 벨라대사4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10)
        # self.set_effect(trigger_ids=[607], visible=True)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000254_BF__SCENE01__6$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라이동(self.ctx)


class 벨라이동딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라이동(self.ctx)


class 벨라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001], visible=False, start_delay=0, interval=0, fade=0)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1')

    def on_tick(self) -> trigger_api.Trigger:
        return 카메라원위치(self.ctx)


class 카메라원위치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.select_camera_path(path_ids=[301], return_view=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 카메라원위치2(self.ctx)


class 카메라원위치2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=902, min_users='1'):
            return 쿠당탕(self.ctx)


class 쿠당탕(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])
        self.set_effect(trigger_ids=[402], visible=True)
        self.set_effect(trigger_ids=[403], visible=True)
        self.set_effect(trigger_ids=[404], visible=True)
        self.set_effect(trigger_ids=[405], visible=True)
        self.set_effect(trigger_ids=[406], visible=True)
        self.set_effect(trigger_ids=[407], visible=True)
        self.set_effect(trigger_ids=[408], visible=True)
        self.set_effect(trigger_ids=[409], visible=True)
        self.set_effect(trigger_ids=[410], visible=True)
        self.set_effect(trigger_ids=[411], visible=True)
        self.set_effect(trigger_ids=[412], visible=True)
        self.set_effect(trigger_ids=[413], visible=True)
        self.set_effect(trigger_ids=[414], visible=True)
        self.set_effect(trigger_ids=[415], visible=True)
        self.set_effect(trigger_ids=[416], visible=True)
        self.set_effect(trigger_ids=[417], visible=True)
        self.set_effect(trigger_ids=[418], visible=True)
        self.set_effect(trigger_ids=[419], visible=True)
        self.set_effect(trigger_ids=[420], visible=True)
        self.set_effect(trigger_ids=[421], visible=True)
        self.set_effect(trigger_ids=[422], visible=True)
        self.set_effect(trigger_ids=[423], visible=True)
        self.set_effect(trigger_ids=[424], visible=True)
        self.set_effect(trigger_ids=[425], visible=True)
        self.set_effect(trigger_ids=[426], visible=True)
        self.set_effect(trigger_ids=[427], visible=True)
        self.set_effect(trigger_ids=[428], visible=True)
        self.set_effect(trigger_ids=[429], visible=True)
        self.set_effect(trigger_ids=[430], visible=True)
        self.set_effect(trigger_ids=[431], visible=True)
        self.set_effect(trigger_ids=[432], visible=True)
        self.set_effect(trigger_ids=[433], visible=True)
        self.set_effect(trigger_ids=[434], visible=True)
        self.set_effect(trigger_ids=[435], visible=True)
        self.set_effect(trigger_ids=[436], visible=True)
        self.set_effect(trigger_ids=[437], visible=True)
        self.set_effect(trigger_ids=[438], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 벨라대사5(self.ctx)


class 스킵벨라이동딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timer_id='1', seconds=1)
        self.select_camera_path(path_ids=[301], return_view=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킵벨라이동(self.ctx)


class 스킵벨라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3001], visible=False, start_delay=0, interval=0, fade=0)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1')

    def on_tick(self) -> trigger_api.Trigger:
        return 스킵카메라원위치(self.ctx)


class 스킵카메라원위치(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=902, min_users='1'):
            return 스킵쿠당탕(self.ctx)


class 스킵쿠당탕(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])
        self.set_effect(trigger_ids=[402], visible=True)
        self.set_effect(trigger_ids=[403], visible=True)
        self.set_effect(trigger_ids=[404], visible=True)
        self.set_effect(trigger_ids=[405], visible=True)
        self.set_effect(trigger_ids=[406], visible=True)
        self.set_effect(trigger_ids=[407], visible=True)
        self.set_effect(trigger_ids=[408], visible=True)
        self.set_effect(trigger_ids=[409], visible=True)
        self.set_effect(trigger_ids=[410], visible=True)
        self.set_effect(trigger_ids=[411], visible=True)
        self.set_effect(trigger_ids=[412], visible=True)
        self.set_effect(trigger_ids=[413], visible=True)
        self.set_effect(trigger_ids=[414], visible=True)
        self.set_effect(trigger_ids=[415], visible=True)
        self.set_effect(trigger_ids=[416], visible=True)
        self.set_effect(trigger_ids=[417], visible=True)
        self.set_effect(trigger_ids=[418], visible=True)
        self.set_effect(trigger_ids=[419], visible=True)
        self.set_effect(trigger_ids=[420], visible=True)
        self.set_effect(trigger_ids=[421], visible=True)
        self.set_effect(trigger_ids=[422], visible=True)
        self.set_effect(trigger_ids=[423], visible=True)
        self.set_effect(trigger_ids=[424], visible=True)
        self.set_effect(trigger_ids=[425], visible=True)
        self.set_effect(trigger_ids=[426], visible=True)
        self.set_effect(trigger_ids=[427], visible=True)
        self.set_effect(trigger_ids=[428], visible=True)
        self.set_effect(trigger_ids=[429], visible=True)
        self.set_effect(trigger_ids=[430], visible=True)
        self.set_effect(trigger_ids=[431], visible=True)
        self.set_effect(trigger_ids=[432], visible=True)
        self.set_effect(trigger_ids=[433], visible=True)
        self.set_effect(trigger_ids=[434], visible=True)
        self.set_effect(trigger_ids=[435], visible=True)
        self.set_effect(trigger_ids=[436], visible=True)
        self.set_effect(trigger_ids=[437], visible=True)
        self.set_effect(trigger_ids=[438], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 벨라대사5딜레이(self.ctx)


class 벨라대사5딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 벨라대사5(self.ctx)


class 벨라대사5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301, enable=True)
        self.set_scene_skip(state=벨라이동2, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='1', seconds=6)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000254_BF__SCENE01__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사6(self.ctx)


class 벨라대사6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        # self.set_effect(trigger_ids=[608], visible=True)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000254_BF__SCENE01__8$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라이동2(self.ctx)


class 벨라이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='1', seconds=4)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 이펙트1(self.ctx)


class 이펙트1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[401], visible=True)
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라몬스터소환(self.ctx)


class 벨라몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=3)
        self.select_camera(trigger_id=303, enable=True)
        self.spawn_monster(spawn_ids=[106])
        self.spawn_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)
        self.select_camera_path(path_ids=[303], return_view=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 끝2(self.ctx)


class 끝2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301, enable=False)
        self.select_camera(trigger_id=303, enable=False)
        self.set_mesh(trigger_ids=[3002], visible=False, start_delay=0, interval=0, fade=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 시작대기중
