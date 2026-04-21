from datetime import datetime

#############################
# BEGIN CONSTANTS
#############################

BEL_ALIASES = [
  "Beltane"
]

LTH_ALIASES = [
  "Litha",
  "Midsummer"
]

LMS_ALIASES = [
  "Lammas",
]

MBN_ALIASES = [
  "Mabon",
]

SMH_ALIASES = [
  "Samhain",
]

YUL_ALIASES = [
  "Yule",
]

IMB_ALIASES = [
  "Imbolc",
]

OST_ALIASES = [
  "Ostara",
]

#############################
# END CONSTANTS
#############################

class Sabbat():
  def __init__(self, prefix, aliases, date_stamp: str):
    self.prefix = prefix
    self.aliases = aliases
    self.year = date_stamp[:2]
    self.month = date_stamp[2:4]
    self.day = date_stamp[4:6]

  def __str__(self):
    return f"{self.aliases[0]} 20{str(self.year)}"
  
  def as_date_stamp(self):
    return f"{self.year}{self.month}{self.day}"
  
  def as_string_code(self):
    return f"{self.prefix}{self.year}"

class ChronIO:
  def get_all_sabbat_codes(self):
    codes = [
      "SMH",
      "YUL",
      "IMB",
      "OST",
      "BEL",
      "LTH",
      "LMS",
      "MBN",
    ]
    return codes

  def get_all_aliases(self, letter_code):
    match letter_code:
      case "SMH":
        return SMH_ALIASES
      case "YUL":
        return YUL_ALIASES
      case "IMB":
        return IMB_ALIASES
      case "OST":
        return OST_ALIASES
      case "BEL":
        return BEL_ALIASES
      case "LTH":
        return LTH_ALIASES
      case "LMS":
        return LMS_ALIASES
      case "MBN":
        return MBN_ALIASES


  def get_suffix(self, current_sfx=""):
    debugging = False
    now = datetime.now()
    # year
    current_year = now.strftime("%y")
    if debugging:
      print(f"current_sfx: {current_sfx} current_year: {current_year}")
    if len(current_sfx) < len(current_year):
      return current_year
    # year, month
    current_month = now.strftime("%y%m")
    if debugging:
      print(f"current_sfx: {current_sfx} current_month: {current_month}")
    if len(current_sfx) < len(current_month):
      return current_month
    # year, month, day
    current_day = now.strftime("%y%m%d")
    if debugging:
      print(f"current_sfx: {current_sfx} current_day: {current_day}")
    if len(current_sfx) < len(current_day):
      return current_day
    # year, month, day, hour
    current_hour = now.strftime("%y%m%d%H")
    if debugging:
      print(f"current_sfx: {current_sfx} current_hour: {current_hour}")
    if len(current_sfx) < len(current_hour):
      return current_hour
    # year, month, day, hour, minute
    current_min = now.strftime("%y%m%d%H%M")
    if debugging:
      print(f"current_sfx: {current_sfx} current_min: {current_min}")
    if len(current_sfx) < len(current_min):
      return current_min
    # year, month, day, hour, minute, second
    current_sec = now.strftime("%y%m%d%H%M%S")
    if debugging:
      print(f"current_sfx: {current_sfx} current_sec: {current_sec}")
    if len(current_sfx) <= len(current_sec):
      return current_sec
    if debugging:
      print(f"current_sfx: {current_sfx}")
    return current_sfx

  def get_timestamp(self):
    now = datetime.now()
    timestamp_string = now.strftime("%Y%m%d%H%M%S")
    return timestamp_string

  def get_sabbat(self, letter_code) -> Sabbat:
    match letter_code:
      case "BEL25":
        aliases = BEL_ALIASES
        sbt = Sabbat("BEL", aliases, "250501")
        return sbt
      case "LTH25":
        aliases = LTH_ALIASES
        sbt = Sabbat("LTH", aliases, "250621")
        return sbt
      case "LMS25":
        aliases = LMS_ALIASES
        sbt = Sabbat("LMS", aliases, "25")
        return sbt
      case "MBN25":
        aliases = MBN_ALIASES
        sbt = Sabbat("MBN", aliases, "25")
        return sbt
      case "SMH25":
        aliases = SMH_ALIASES
        sbt = Sabbat("SMH", aliases, "25")
        return sbt
      case "YUL25":
        aliases = YUL_ALIASES
        sbt = Sabbat("YUL", aliases, "25")
        return sbt
      case "IMB26":
        aliases = IMB_ALIASES
        sbt = Sabbat("IMB", aliases, "26")
        return sbt
      case "OST26":
        aliases = OST_ALIASES
        sbt = Sabbat("OST", aliases, "26")
        return sbt
      case "BEL26":
        aliases = BEL_ALIASES
        sbt = Sabbat("BEL", aliases, "26")
        return sbt
      case "LTH26":
        aliases = LTH_ALIASES
        sbt = Sabbat("LTH", aliases, "26")
        return sbt
      case "LMS26":
        aliases = LMS_ALIASES
        sbt = Sabbat("LMS", aliases, "26")
        return sbt
      case "MBN26":
        aliases = MBN_ALIASES
        sbt = Sabbat("MBN", aliases, "26")
        return sbt
      case "SMH26":
        aliases = SMH_ALIASES
        sbt = Sabbat("SMH", aliases, "26")
        return sbt
      case "YUL26":
        aliases = YUL_ALIASES
        sbt = Sabbat("YUL", aliases, "26")
        return sbt
      
