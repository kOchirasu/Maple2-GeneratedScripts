""" trigger/02000253_bf/move.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2901,2902,2903,2904,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enable=False)
        self.set_effect(triggerIds=[8041], visible=False)
        self.set_effect(triggerIds=[8042], visible=False)
        self.set_effect(triggerIds=[8043], visible=False)
        self.set_effect(triggerIds=[8044], visible=False)
        self.set_interact_object(triggerIds=[10001050], state=2)
        self.set_interact_object(triggerIds=[10001051], state=2)
        self.set_interact_object(triggerIds=[10001052], state=2)
        self.set_interact_object(triggerIds=[10001053], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=906, boxId=1):
            return 벨라소환(self.ctx)


class 벨라소환(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라이동(self.ctx)


class 벨라이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)


class 랜덤선택1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return 번1(self.ctx)
        if self.random_condition(rate=33):
            return 번2(self.ctx)
        if self.random_condition(rate=34):
            return 번3(self.ctx)
        if self.random_condition(rate=34):
            return 번4(self.ctx)


class 랜덤선택1To1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return 번2(self.ctx)
        if self.random_condition(rate=34):
            return 번3(self.ctx)
        if self.random_condition(rate=34):
            return 번4(self.ctx)


class 랜덤선택1To2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return 번1(self.ctx)
        if self.random_condition(rate=34):
            return 번3(self.ctx)
        if self.random_condition(rate=34):
            return 번4(self.ctx)


class 랜덤선택1To3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return 번1(self.ctx)
        if self.random_condition(rate=34):
            return 번2(self.ctx)
        if self.random_condition(rate=34):
            return 번4(self.ctx)


class 랜덤선택1To4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return 번1(self.ctx)
        if self.random_condition(rate=34):
            return 번2(self.ctx)
        if self.random_condition(rate=34):
            return 번3(self.ctx)


class 번1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=10)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002523, textId=20002523)
        # <action name="메쉬를설정한다" arg1="265-296" arg2="0" arg3="0" arg4="200"/>
        self.set_effect(triggerIds=[8041], visible=True)
        self.set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904], enable=True)
        self.set_breakable(triggerIds=[905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.hide_guide_summary(entityId=20002523)
            return To1번1(self.ctx)


class To1번1(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8041], visible=False)
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.create_monster(spawnIds=[3001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[3001])
            self.set_interact_object(triggerIds=[10001050], state=2)
            self.set_interact_object(triggerIds=[10001051], state=2)
            self.set_interact_object(triggerIds=[10001052], state=2)
            self.set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To1(self.ctx)
        if self.monster_dead(boxIds=[3001]):
            return To2번1(self.ctx)


class To2번1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10001052], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[3001])
            self.set_interact_object(triggerIds=[10001050], state=2)
            self.set_interact_object(triggerIds=[10001051], state=2)
            self.set_interact_object(triggerIds=[10001052], state=2)
            self.set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To1(self.ctx)
        if self.object_interacted(interactIds=[10001052], stateValue=0):
            return 끝1(self.ctx)


class 번2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8042], visible=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002523, textId=20002523)
        self.set_timer(timerId='1', seconds=10)
        # <action name="메쉬를설정한다" arg1="297-328" arg2="0" arg3="0" arg4="200"/>
        self.set_breakable(triggerIds=[905,906,907,908,1905,1906,1907,1908,2905,2906,2907,2908,3905,3906,3907,3908], enable=True)
        self.set_breakable(triggerIds=[901,902,903,904,909,910,911,912,913,914,915,916,1901,1902,1903,1904,1909,1910,1911,1912,1913,1914,1915,1916,2901,2902,2903,2904,2909,2910,2911,2912,2913,2914,2915,2916,3901,3902,3903,3904,3909,3910,3911,3912,3913,3914,3915,3916], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.hide_guide_summary(entityId=20002523)
            return To1번2(self.ctx)


class To1번2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8042], visible=False)
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.create_monster(spawnIds=[3002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[3002])
            self.set_interact_object(triggerIds=[10001050], state=2)
            self.set_interact_object(triggerIds=[10001051], state=2)
            self.set_interact_object(triggerIds=[10001052], state=2)
            self.set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To2(self.ctx)
        if self.monster_dead(boxIds=[3002]):
            return To2번2(self.ctx)


class To2번2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10001051], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[3004])
            self.set_interact_object(triggerIds=[10001050], state=2)
            self.set_interact_object(triggerIds=[10001051], state=2)
            self.set_interact_object(triggerIds=[10001052], state=2)
            self.set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To2(self.ctx)
        if self.object_interacted(interactIds=[10001051], stateValue=0):
            return 끝2(self.ctx)


class 번3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8044], visible=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002523, textId=20002523)
        self.set_timer(timerId='1', seconds=10)
        # <action name="메쉬를설정한다" arg1="233-264" arg2="0" arg3="0" arg4="200"/>
        self.set_breakable(triggerIds=[909,910,911,912,1909,1910,1911,1912,2909,2910,2911,2912,3909,3910,3911,3912], enable=True)
        self.set_breakable(triggerIds=[901,902,903,904,905,906,907,908,913,914,915,916,1901,1902,1903,1904,1905,1906,1907,1908,1913,1914,1915,1916,2901,2902,2903,2904,2905,2906,2907,2908,2913,2914,2915,2916,3901,3902,3903,3904,3905,3906,3907,3908,3913,3914,3915,3916], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.hide_guide_summary(entityId=20002523)
            return To1번3(self.ctx)


class To1번3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8044], visible=False)
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.create_monster(spawnIds=[3003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[3003])
            self.set_interact_object(triggerIds=[10001050], state=2)
            self.set_interact_object(triggerIds=[10001051], state=2)
            self.set_interact_object(triggerIds=[10001052], state=2)
            self.set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To3(self.ctx)
        if self.monster_dead(boxIds=[3003]):
            return To2번3(self.ctx)


class To2번3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10001050], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[3004])
            self.set_interact_object(triggerIds=[10001050], state=2)
            self.set_interact_object(triggerIds=[10001051], state=2)
            self.set_interact_object(triggerIds=[10001052], state=2)
            self.set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To3(self.ctx)
        if self.object_interacted(interactIds=[10001050], stateValue=0):
            return 끝3(self.ctx)


class 번4(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8043], visible=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002523, textId=20002523)
        self.set_timer(timerId='1', seconds=10)
        # <action name="메쉬를설정한다" arg1="201-232" arg2="0" arg3="0" arg4="200"/>
        self.set_breakable(triggerIds=[913,914,915,916,1913,1914,1915,1916,2913,2914,2915,2916,3913,3914,3915,3916], enable=True)
        self.set_breakable(triggerIds=[901,902,903,904,905,906,907,908,909,910,911,912,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,2901,2902,2903,2904,2905,2906,2907,2908,2909,2910,2911,2912,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.hide_guide_summary(entityId=20002523)
            return To1번4(self.ctx)


class To1번4(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8043], visible=False)
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.create_monster(spawnIds=[3004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[3004])
            self.set_interact_object(triggerIds=[10001050], state=2)
            self.set_interact_object(triggerIds=[10001051], state=2)
            self.set_interact_object(triggerIds=[10001052], state=2)
            self.set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To4(self.ctx)
        if self.monster_dead(boxIds=[3004]):
            return To2번4(self.ctx)


class To2번4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10001053], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            self.destroy_monster(spawnIds=[3004])
            self.set_interact_object(triggerIds=[10001050], state=2)
            self.set_interact_object(triggerIds=[10001051], state=2)
            self.set_interact_object(triggerIds=[10001052], state=2)
            self.set_interact_object(triggerIds=[10001053], state=2)
            return 랜덤선택1To4(self.ctx)
        if self.object_interacted(interactIds=[10001053], stateValue=0):
            return 끝4(self.ctx)


class 끝1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10001050], state=2)
        self.set_interact_object(triggerIds=[10001051], state=2)
        self.set_interact_object(triggerIds=[10001052], state=2)
        self.set_interact_object(triggerIds=[10001053], state=2)
        self.set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 랜덤선택1To1(self.ctx)


class 끝2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10001050], state=2)
        self.set_interact_object(triggerIds=[10001051], state=2)
        self.set_interact_object(triggerIds=[10001052], state=2)
        self.set_interact_object(triggerIds=[10001053], state=2)
        self.set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 랜덤선택1To2(self.ctx)


class 끝3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10001050], state=2)
        self.set_interact_object(triggerIds=[10001051], state=2)
        self.set_interact_object(triggerIds=[10001052], state=2)
        self.set_interact_object(triggerIds=[10001053], state=2)
        self.set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 랜덤선택1To3(self.ctx)


class 끝4(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=0)
        self.set_interact_object(triggerIds=[10001050], state=2)
        self.set_interact_object(triggerIds=[10001051], state=2)
        self.set_interact_object(triggerIds=[10001052], state=2)
        self.set_interact_object(triggerIds=[10001053], state=2)
        self.set_breakable(triggerIds=[901,902,903,904,1901,1902,1903,1904,2901,2902,2903,2904,3901,3902,3903,3904,905,906,907,908,909,910,911,912,913,914,915,916,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,3905,3906,3907,3908,3909,3910,3911,3912,3913,3914,3915,3916], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 랜덤선택1To4(self.ctx)


initial_state = 대기
