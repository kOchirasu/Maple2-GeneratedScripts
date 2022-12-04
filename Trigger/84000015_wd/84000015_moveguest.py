""" trigger/84000015_wd/84000015_moveguest.xml """
import trigger_api


class 초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='Weddingceremonystartsready', value=0) # 초기화
        self.set_user_value(key='Weddingceremonyfail', value=0) # 초기화

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_hall_state(hallState='weddingComplete'):
            return 종료(self.ctx)
        if self.user_value(key='Weddingceremonystartsready', value=1):
            self.set_user_value(key='Weddingceremonystartsready', value=0)
            return 새로운하객있는지감지(self.ctx)


class 새로운하객있는지감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wedding_hall_state(hallState='weddingComplete'):
            return 종료(self.ctx)
        if self.user_value(key='Weddingceremonyfail', value=1):
            self.set_user_value(key='Weddingceremonyfail', value=0)
            return 시작(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 방금입장한하객은하객석으로위치이동(self.ctx)


class 방금입장한하객은하객석으로위치이동(trigger_api.Trigger):
    def on_enter(self):
        self.wedding_move_user(entryType='Guest', mapId=84000015, portalIds=[22,23], boxId=701) # 799번 박스(입장구역)에 있는 하객들은 22,23번으로 랜덤이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 새로운하객있는지감지(self.ctx)


class 하객은버진로드밖으로위치이동(trigger_api.Trigger):
    def on_enter(self):
        self.wedding_move_user(entryType='Guest', mapId=84000015, portalIds=[22,23], boxId=701) # 701번 박스(버진로드)에 있는 하객들은 22,23번으로 랜덤이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 새로운하객있는지감지(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 초기화
