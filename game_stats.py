class GameStats:
  def __init__(self, ai_game):
    self.settings = ai_game.settings
    self.reset_stats()
    self.game_active = True

  def reset_stats(self):
    #初始化在游戏运行期间可能发生的统计信息
    self.ships_left = self.settings.ship_limit