""" trigger/82000012_survival/02_ride.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7100,7200,7300,7400,7500,7600,7700,7800], visible=False) # MushBalloon Regen Sound
        self.set_effect(triggerIds=[5100,5200,5300,5400,5500,5600,5700,5800], visible=False) # MushBalloon Rise Sound
        self.set_effect(triggerIds=[6100,6200,6300,6400,6500,6600,6700,6800], visible=False) # MushBalloon Disappear Sound
        self.set_user_value(key='SetRide', value=0)
        self.set_user_value(key='StartPatrol', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SetRide', value=1):
            return Ride01_Ready(self.ctx)
        if self.user_value(key='SetRide', value=2):
            return Ride02_Ready(self.ctx)
        if self.user_value(key='SetRide', value=3):
            return Ride03_Ready(self.ctx)
        if self.user_value(key='SetRide', value=4):
            return Ride04_Ready(self.ctx)
        if self.user_value(key='SetRide', value=5):
            return Ride05_Ready(self.ctx)
        if self.user_value(key='SetRide', value=6):
            return Ride06_Ready(self.ctx)
        if self.user_value(key='SetRide', value=7):
            return Ride07_Ready(self.ctx)
        if self.user_value(key='SetRide', value=8):
            return Ride08_Ready(self.ctx)


# North_To_South
class Ride01_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7100], visible=True) # MushBalloon Regen Sound
        self.create_monster(spawnIds=[110], animationEffect=False) # North_To_South
        self.write_log(logName='Survival', event='bus_01') # 서바이벌 버스 로그

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StartPatrol', value=1):
            return Ride01_StartPatrolDelay(self.ctx)


class Ride01_StartPatrolDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5100], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_111')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ride01_StartPatrol(self.ctx)


class Ride01_StartPatrol(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[110], skillId=70001081, level=1, isPlayer=True, isSkillSet=False) # MushBalloon Flying Loop Sound
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_110') # North_To_South

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[110])
        self.set_effect(triggerIds=[6100], visible=True) # MushBalloon Disappear Sound


# South_To_North
class Ride02_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7200], visible=True) # MushBalloon Regen Sound
        self.create_monster(spawnIds=[120], animationEffect=False) # South_To_North
        self.write_log(logName='Survival', event='bus_02') # 서바이벌 버스 로그

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StartPatrol', value=1):
            return Ride02_StartPatrolDelay(self.ctx)


class Ride02_StartPatrolDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5200], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawnId=120, patrolName='MS2PatrolData_121')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ride02_StartPatrol(self.ctx)


class Ride02_StartPatrol(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[120], skillId=70001081, level=1, isPlayer=True, isSkillSet=False) # MushBalloon Flying Loop Sound
        self.move_npc(spawnId=120, patrolName='MS2PatrolData_120') # South_To_North

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[120])
        self.set_effect(triggerIds=[6200], visible=True) # MushBalloon Disappear Sound


# East_To_West
class Ride03_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7300], visible=True) # MushBalloon Regen Sound
        self.create_monster(spawnIds=[130], animationEffect=False) # East_To_West
        self.write_log(logName='Survival', event='bus_03') # 서바이벌 버스 로그

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StartPatrol', value=1):
            return Ride03_StartPatrolDelay(self.ctx)


class Ride03_StartPatrolDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawnId=130, patrolName='MS2PatrolData_131')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ride03_StartPatrol(self.ctx)


class Ride03_StartPatrol(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[130], skillId=70001081, level=1, isPlayer=True, isSkillSet=False) # MushBalloon Flying Loop Sound
        self.move_npc(spawnId=130, patrolName='MS2PatrolData_130') # East_To_West

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[130])
        self.set_effect(triggerIds=[6300], visible=True) # MushBalloon Disappear Sound


# West_To_East
class Ride04_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7400], visible=True) # MushBalloon Regen Sound
        self.create_monster(spawnIds=[140], animationEffect=False) # West_To_East
        self.write_log(logName='Survival', event='bus_04') # 서바이벌 버스 로그

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StartPatrol', value=1):
            return Ride04_StartPatrolDelay(self.ctx)


class Ride04_StartPatrolDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5400], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawnId=140, patrolName='MS2PatrolData_141')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ride04_StartPatrol(self.ctx)


class Ride04_StartPatrol(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[140], skillId=70001081, level=1, isPlayer=True, isSkillSet=False) # MushBalloon Flying Loop Sound
        self.move_npc(spawnId=140, patrolName='MS2PatrolData_140') # North_To_South

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[140])
        self.set_effect(triggerIds=[6400], visible=True) # MushBalloon Disappear Sound


# West_To_East
class Ride05_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7500], visible=True) # MushBalloon Regen Sound
        self.create_monster(spawnIds=[150], animationEffect=False) # NorthWest_To_SouthEast
        self.write_log(logName='Survival', event='bus_05') # 서바이벌 버스 로그

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StartPatrol', value=1):
            return Ride05_StartPatrolDelay(self.ctx)


class Ride05_StartPatrolDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5500], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawnId=150, patrolName='MS2PatrolData_151')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ride05_StartPatrol(self.ctx)


class Ride05_StartPatrol(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[150], skillId=70001081, level=1, isPlayer=True, isSkillSet=False) # MushBalloon Flying Loop Sound
        self.move_npc(spawnId=150, patrolName='MS2PatrolData_150') # NorthWest_To_SouthEast

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[150])
        self.set_effect(triggerIds=[6500], visible=True) # MushBalloon Disappear Sound


# NorthEast_To_SouthWest
class Ride06_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7600], visible=True) # MushBalloon Regen Sound
        self.create_monster(spawnIds=[160], animationEffect=False) # NorthEast_To_SouthWest
        self.write_log(logName='Survival', event='bus_06') # 서바이벌 버스 로그

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StartPatrol', value=1):
            return Ride06_StartPatrolDelay(self.ctx)


class Ride06_StartPatrolDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5600], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawnId=160, patrolName='MS2PatrolData_161')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ride06_StartPatrol(self.ctx)


class Ride06_StartPatrol(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[160], skillId=70001081, level=1, isPlayer=True, isSkillSet=False) # MushBalloon Flying Loop Sound
        self.move_npc(spawnId=160, patrolName='MS2PatrolData_160') # NorthEast_To_SouthWest

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[160])
        self.set_effect(triggerIds=[6600], visible=True) # MushBalloon Disappear Sound


# SouthWest_To_NorthEast
class Ride07_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7700], visible=True) # MushBalloon Regen Sound
        self.create_monster(spawnIds=[170], animationEffect=False) # SouthWest_To_NorthEast
        self.write_log(logName='Survival', event='bus_07') # 서바이벌 버스 로그

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StartPatrol', value=1):
            return Ride07_StartPatrolDelay(self.ctx)


class Ride07_StartPatrolDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5700], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawnId=170, patrolName='MS2PatrolData_171')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ride07_StartPatrol(self.ctx)


class Ride07_StartPatrol(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[170], skillId=70001081, level=1, isPlayer=True, isSkillSet=False) # MushBalloon Flying Loop Sound
        self.move_npc(spawnId=170, patrolName='MS2PatrolData_170') # SouthWest_To_NorthEast

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[170])
        self.set_effect(triggerIds=[6700], visible=True) # MushBalloon Disappear Sound


# SouthEast_To_NorthWest
class Ride08_Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7800], visible=True) # MushBalloon Regen Sound
        self.create_monster(spawnIds=[180], animationEffect=False) # SouthEast_To_NorthWest
        self.write_log(logName='Survival', event='bus_08') # 서바이벌 버스 로그

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='StartPatrol', value=1):
            return Ride08_StartPatrolDelay(self.ctx)


class Ride08_StartPatrolDelay(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5800], visible=True) # MushBalloon Rise Sound
        self.move_npc(spawnId=180, patrolName='MS2PatrolData_181')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Ride08_StartPatrol(self.ctx)


class Ride08_StartPatrol(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[180], skillId=70001081, level=1, isPlayer=True, isSkillSet=False) # MushBalloon Flying Loop Sound
        self.move_npc(spawnId=180, patrolName='MS2PatrolData_180') # SouthEast_To_NorthWest

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=32000):
            return Quit(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[180])
        self.set_effect(triggerIds=[6800], visible=True) # MushBalloon Disappear Sound


class Quit(common.Trigger):
    def on_enter(self):
        self.write_log(logName='Survival', event='bus_end') # 서바이벌 버스 로그


initial_state = Wait
