from obsidio import ObsidIO
from chronio import ChronIO
from cfg import NwdConfig, Config, NwdTestConfig
from files import (
  write_lines,
  path_exists,
) 
from gdp import GarDinPlot

# COPYING FROM MAGICKAL_RECORD OP_GAR_REPORT.PY

def get_config_lines():
  config_lines = [
    f"- Status: SCRIPT IN PROGRESS NOT TESTED",
    f"- NWD FOLDER: ~/nwd",
  ]
  return config_lines


def get_cet_lines(chron: ChronIO, obio: ObsidIO):
  cet_lines = []
  if not obio.last_loaded_vault:
    msg = "no vault loaded at time of report generation"
    print("no vault loaded at time of report generation")
    cet_lines.append(msg)
    return cet_lines
  year = 24
  codes = chron.get_all_sabbat_codes()
  cet_file_names = []
  while year < 27:
    for code in codes:
      look_for = code + str(year)
      vault_path = obio.get_src_md_file_path(look_for)
      if path_exists(vault_path):
        cet_file_names.append(look_for)
    year += 1
  for fname in cet_file_names:
    link = "[[" + fname + "]]"
    cet_lines.append(link)
  return cet_lines

def get_vhale_lines():
  vhale_lines = [
    "vhales go here",
    "more vhales go here"
  ]
  return vhale_lines


def get_place_lines():
  place_lines = [
    "place_lines",
    "go_here"
  ]
  return place_lines


def get_practice_lines():
  practices = [
    "breath meditations",
    "mind meditations",
    "ritual work",
    "card work",
  ]
  # TODO: load these from Obsidian using ObsidIO and latest verified vault and configuration
  return practices


def get_timestamp_lines(chron: ChronIO):
  timestamp_lines = [
    f"- {chron.get_timestamp()}",
  ]
  return timestamp_lines

def report(chron: ChronIO, obio: ObsidIO):
  report_lines = []
  # Greeting
  report_lines.append("Welcome toTha GarDin...")
  report_lines.append("")
  # TimeStamp
  report_lines.append("# TimeStamp")
  for line in get_timestamp_lines(chron):
    report_lines.append(line)
  # GarDinPlot (formerly: Configuration)
  report_lines.append("# GarDinPlot")
  for line in get_config_lines():
    report_lines.append(line)
  # Cets
  report_lines.append("# Cets")
  for line in get_cet_lines(chron, obio):
    report_lines.append(line)
  # Activities (formerly: Practices)
  report_lines.append("# Activities")
  for line in get_practice_lines():
    report_lines.append(line)
  # Places
  report_lines.append("# Places")
  for line in get_place_lines():
    report_lines.append(line)
  # Vhales
  report_lines.append("# Vhales")
  for line in get_vhale_lines():
    report_lines.append(line)
  return report_lines

def till(gdp: GarDinPlot):  
  chron = ChronIO()
  print(f"tilling GarDinPlot for {gdp.cfg.nwd_folder()}")
  obio = ObsidIO(gdp.cfg)
  cfg_files = obio.get_cfg_files()
  if len(cfg_files) > 0:
    md_file = cfg_files[0]
    obio.load_vaults(md_file)
  gr_file_path = "~/nwd/gdp/GarDinEr_RepOrT.md"
  report_lines = report(chron, obio)
  if(len(report_lines) > 0):
    write_lines(gr_file_path, report_lines, True)
    print(f"{len(report_lines)} lines written to {gr_file_path}")
  else:
    print("nothing to write, aborting...")

if __name__ == '__main__':
  # gdp_nwd_test = GarDinPlot(NwdTestConfig())
  # till(gdp_nwd_test)

  gdp_nwd_config = GarDinPlot(NwdConfig())
  till(gdp_nwd_config)
  
  # GarDinPlotConfig goes here, which takes an arbitrary vault folder and treats it as all intake folders