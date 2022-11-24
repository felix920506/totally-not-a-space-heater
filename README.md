# totally-not-a-space-heater
A project attempting to control a folding@home rig based on room temperature with a microcontroller

## Where this all started, written 2022 Nov 24
  I am a college student living in on-campus housing provided by the school. It's now late November and it's frequently getting below 0°C outside. To make matters worse, the heating in the housing provided by the school isn't working properly. It doesn't go above 70°F (21.1°C) to begin with. What's worse, it switches itself to cooling almost everyday evening. One night I grabbed a thermometer I had for cooking and stuck it in the vent. It was blowing out cold air at around 7°C. I have made multiple reports to housing staff, but nothing has been done. So I had no choice but to get a space heater. 4 maintenance requests and 1 confiscated space heater later, still nothing has been done as far as I can tell.

So I hatched a plan: Computers kick out all the power they consume as heat, so why not get a computer designed to kick out as much heat as possible on the cheap? I went on ebay and amazon, looking for parts. Obviously I'm not going to spend a fortune on things like 13 gen Core i9s and RTX 4090s, so I went back in time, looking for older parts. I intended to run Folding@home on this box as opposed to Furmark so at least the world is getting something out of it The final configuration I ended with is as follows:
  - Intel Core i3-2100
  - Gigabyte GA-Z77P-D3
  - Single 8GB stick of DDR3 from Teamgroup
  - Radeon R9 290X GPU from XFX
  - Radeon R9 290 GPU from XFX
  - NZXT H510 Case
  - Silicon Power A55 250GB SSD
  - FSP Hydro G Pro 850W Power Supply
  - Asus PCE-AC58BT Wifi Card
 
  As for why I chose these parts, I initially thought about picking up old Xeons, but most of those motherboards either 1.Cost a fortune, 2.are dead, 3. Are from questionable sources, 4.are special form factors, or a combination of the above conditions. So I moved to using GPUs as the primary heat source. The CPU then, shifted to some cheap part that will run those GPUs. So what GPUs then? Nvidia vs AMD is the age old question. Since I intended to use Linux, I chose AMD. This one was easy, but what AMD card? Since I'm on a budget, RX Vega and newer were quickly ruled out. For heating purposes I want a card that kicks out the most heat, efficiency is the last thing I care about, so I landed on the 28nm "Southern Island" series cards. as for why the 290/290X, because they cost quite a bit less than the newer 390/390X and about the same as HD79x0/280/280X. Since I spotted 2 at a nice price, I picked up both, giving me 500w of heat from the GPUs. Platform then, I want something that is relatively cheap but still stable, so I landed on the Sandy Bridge/ Ivy Bridge generation. CPU was easy enough given the amount of cheap CPUs that have been thrown out by businesses and schools over the years. Motherboard was also easy enough, I wanted a board that has 2 x16 physical slots and GA-Z77P-D3 immediately caught my attention for being relatively cheap. Memory and storage were also easy, ones that will boot is all that is needed. The case I'm a bit concerned but I could just leave off the side panel. Power supply then, since this system is going to consume quite a bit of juice, I wanted something that wouldn't blow up. I originally wanted to use a Seasonic Focus GX unit, but it was out of stock, so I went with my second choice. Wifi card was also easy, I have used this AC card in another build before and I know that it uses an Intel AC-9260 chipset. Knowing that it's an Intel chipset on a simple adapter card, this was a no-brainer.
  Then I thought, why not make a thermostat that will turn on and off the heating according to the room temperature? So I gathered a bunch of parts on amazon and started waiting. This is where I'm at right now.

## Project Goals (2022 Nov 24)

  - [ ] Start and pause Folding based on room temperature
  - [ ] Vary heat output based on heating needs
  - [ ] Expand to multiple machines
  - [ ] Connections over Serial, Wifi and Bluetooth
