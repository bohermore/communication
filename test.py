import random



class Action(object):
    END_OF_PERIOD = 'End of period
    STL = 'Steal',
    TOV = 'Turnover

PROB = {
    Action.TOV: (0.07, 0.1),
    Action.STL: (0.04, 0.08),

}


def get_ratio(num, den, stat):
    param = PROB[stat]
    delta = param.max - param.min
    ratio = (num * param.scale)/ (num + den)
    value = param.min + ratio * delta
    return value
    

    
def possession_step():
    
    # Intentional foul
    
    # Intentionally run out clock
    
    # Accidentally run out clock
    
    # TOVs
    # - Steal?
    
    # Non shooting fouls
    # - - FT Made
    # - - FT Missed
    # - - - OREB
    # - - - DREB
    
    
    # Don't forget team rebounds
    
    # Shot
    # - Made
    # - Miss 
    # - Shooting foul
    # - - FT Made
    # - - FT Missed
    # - - - OREB
    # - - - DREB

def intentional_foul():
    delta = self.off.points - self.def.points
    possible_points_with_fouling = int(self.game.period_seconds_remaining / 8.0) * 3
    possible_points_without_fouling = int(self.game.period_seconds_remaining / 30.0) * 3

    if (
            self.game.period >= 4 and
            self.game.period_seconds_remaining <= 90 and
            (1 <= delta <= 8 ) and
            (possible_points_without_fouling < delta <= possible_points_with_fouling)
    ):
        pass

    
    
def run_out_clock():
    # No reset to 14 on off rebounds
    # Intentional
    if self.game.period >= 4 and self.off.pts > self.def.pts and self.seconds_in_period <= 24.0:
        pass
    
    # Accidental
    # TODO:

def is_tov() {
    # Determined by creator / passing
    tov_threshold = get_ratio(this.def.tov_force, this.off.tov_avoid, Action.TOV)
    if random.random() < tov_threshold:
        pass

    # help / one-on-one determines defensive side
    # creator / passing determines offensive side
    stl_threshold = get_ratio(this.def.tov_force, this.off.tov_avoid, Action.STL)
    if random.random() < stl_threshold:
        pass

    

