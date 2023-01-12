from character_dict import Master_dict
import random

# To generate random chracters


class RandomChars:

  def generate_dict(self, selected):

    self.selected = selected
    Master_list_keys = list(Master_dict.keys())
    random_keys = random.sample(Master_list_keys, self.selected)
    global random_dict
    random_dict = {}
    for key in random_keys:
      random_dict[key] = Master_dict[key]
    return random_dict


# To generate option one correct and other wrong

  def get_options(self, key):
    self.key_now = key
    d = random.randint(1, 2)
    if d == 1:
      option1 = self.key_now
      option2 = random.choice(list(Master_dict.keys()))
    else:
      option1 = random.choice(list(Master_dict.keys()))
      option2 = self.key_now

    return option1, option2
