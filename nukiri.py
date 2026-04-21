
from myriad import ChronIO, ObsidIO

# COPYING FROM MAGICKAL_RECORD OP_GAR_REPORT.PY

def get_config_lines():
  config_lines = [
    f"- Status: SCRIPT IN PROGRESS NOT TESTED",
    f"- NWD FOLDER: ~/nwd",
  ]
  return config_lines


def get_cet_lines(obio: ObsidIO, chron: ChronIO):
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


def get_timestamp_lines(chron: ChronIO):
  timestamp_lines = [
    f"- {chron.get_timestamp()}",
  ]
  return timestamp_lines

def report():
  report_lines = []
  # Greeting
  report_lines.append("Welcome toTha GarDin...")
  report_lines.append("")
  # TimeStamp
  report_lines.append("# TimeStamp")
  for line in get_timestamp_lines():
    report_lines.append(line)
  # GarDinPlot (formerly: Configuration)
  report_lines.append("# GarDinPlot")
  for line in get_config_lines():
    report_lines.append(line)
  # Cets
  report_lines.append("# Cets")
  for line in get_cet_lines():
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

def main():
  gr_file_path = "~/nwd/gdp/GarDinEr_RepOrT.md"
  report_lines = report()
  if(len(report_lines) > 0):
    write_lines(gr_file_path, report_lines, True)
    print(f"{len(report_lines)} lines written to {gr_file_path}")
  else:
    print("nothing to write, aborting...")

if __name__ == '__main__':
  main()