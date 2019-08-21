# CLIght
CLI interface for lifx API. CLI is written using "click" library. API usage is done with "pifx", but due to lack of some features (like infrared light managing) it will be replaced/rewritten.

To use it on your system:
  1. Install all the dependencies `pip3 install -r requirements.txt`
  2. Set environment variable "LIFX_API" to your LIFX API key... 
   or just make app read it from your system. (Challenge accepted ^^)
  3. Rename it to whatever you'd like command to be (like "clight")
  4. chmod a+x <filename>
  5. Put it into your bin folder. It could be `~/.local/bin`, `~/bin` or even... `~/.my_superior_script_for_managing_light` 0_o
  
I could just write script to do all the things but... I'm lazy as hell ^^
