import numpy as np




class Action(object):
    END_OF_PERIOD = 'End of period
    STEAL = 'steal',
    TOV = 'turnover

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


def is_tov() {
    prob_tov = get_ratio(this.def.tov_force, this.off.tov_avoid, Action.TOV)
    if prob_tov > np.random.random():
        pass
    
    prob_stl = get_ratio(this.def.tov_force, this.off.tov_avoid, Action.STL)
    if prob_stl > np.random.random():
        pass
    # Steal 4-8
    # help / one-on-one determines defensive side
    # creator / passing determines offensive side
    
    # TOV
    # Determined by creator / passing

