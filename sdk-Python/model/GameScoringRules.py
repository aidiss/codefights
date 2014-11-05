from model.Area import Area 

"""
 * scoring rules of the game: knows what hit causes what damage.
 *
 * @author Aidis Stukas
"""



class GameScoringRules(object):
  """docstring for GameScoringRules"""
  NOSE_SCORE = 10;
  JAW_SCORE = 8;
  BELLY_SCORE = 6;
  GROIN_SCORE = 4;
  LEGS_SCORE = 3;

  LIFEPOINTS = 150;

  @staticmethod
  def calculateScore(attacks, blocks):
    rez = 0

    if attacks:
      for attack in attacks:
        if attack in blocks:
          continue
        rez = rez + GameScoringRules.getAttackSeverity(attack)

    return rez

  def getAttackSeverity(attack):
    if attack == Area.NOSE:
      return GameScoringRules.NOSE_SCORE

    elif attack == Area.JAW:
      return GameScoringRules.JAW_SCORE

    elif attack == Area.GROIN:
      return GameScoringRules.GROIN_SCORE

    elif attack == Area.BELLY:
      return GameScoringRules.BELLY_SCORE

    elif attack == Area.LEGS:
      return GameScoringRules.LEGS_SCORE
      
    else:
      'Unknown attack vector: '

  def isMoveLegal(move):
    attacks = move.getAttacks()
    blocks =  move.getBlocks()
    return (len(attacks) + len(blocks) <= 3)
