# CLIght
CLI interface for lifx API. CLI is written using "click" library. API usage is done with "pifx", but due to lack of some features (like infrared light managing) it will be replaced/rewritten.

To use it on your system:
  1. Set environment variable "LIFX_API" to your LIFX API key... 
   or just make app read it from your system. (Challenge accepted ^^)
  2. Rename it to whatever you'd like command to be (like "clight")
  3. chmod a+x <filename>
  4. Put it into your bin folder. It could be `~/.local/bin`, `~/bin` or even... `~/.my_superior_script_for_managing_light` 0_o
