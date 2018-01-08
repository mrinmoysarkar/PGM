2017-05-23 Scenarios
====================

This collection contains six scenarios with a variety of settings and results. As with the
previous data set, each scenario is recorded and its logs converted into a SQLite3 database. Each
scenario contains two files:

 - `custd.sqlite3`: main SQLite3 database containing all JAUS and MAVLink messages.
 - `video.mp4`: video recording of MAVLink map view during scenario
 
Videos are recorded using h.264 lossless compression and may be difficult to play. Suggested players
include VLC (cross-platform) or MPC-HC (Windows). They can also be converted using `ffmpeg`.

## Database structure

 - `jaus`: base table for all JAUS messages. The `type` indicates which of the detail tables to
     reference for each message.
 - `jaus_*`: detail tables for JAUS messages
 - `mavlink`: base table for all MavLink messages
 - `mavlink_*`: detail tables for MavLink messages
 - `system_state`: state transitions for the entire system

## Scenario 1

 - **Search area**: northwest
 - **Orientation**: diagonal
 - **Tarp location**: northwest of center
 - **Result**: tarp found and confirmed
 
From MAVLink System_state Table:

"0"	"2017-05-24 03:06:03.827954"	"Hold"						0 		ms
"1"	"2017-05-24 03:06:45.906884"	"Fly Orbit and Observe"		42079	ms
"2"	"2017-05-24 03:07:20.760367"	"Fly Search Pattern"		76932	ms
"3"	"2017-05-24 03:09:46.439167"	"Survey Target"				222611	ms
"4"	"2017-05-24 03:10:58.720320"	"Fly Orbit and Observe"		294892	ms
"5"	"2017-05-24 03:12:57.897034"	"Hold"						414069	ms

## Scenario 2

 - **Search area**: north
 - **Orientation**: diagonal
 - **Tarp location**: none
 - **Result**: no tarp found
 - **Notes**: the video file for this scenario was invalid and is thus omitted
 
From MAVLink System_state Table:

"0"	"2017-05-24 03:19:23.131891"	"Hold"						0		ms
"1"	"2017-05-24 03:20:05.174019"	"Fly Orbit and Observe"		42042	ms
"2"	"2017-05-24 03:20:51.275709"	"Fly Search Pattern"		88144	ms
"3"	"2017-05-24 03:26:56.453546"	"Fly Orbit and Observe"		453321	ms
"4"	"2017-05-24 03:28:43.867313"	"Hold"						560735	ms
 
## Scenario 3

 - **Search area**: south
 - **Orientation**: flat
 - **Tarp location**: near runway
 - **Result**: tarp found and but not confirmed
 - **Notes**: this is the "quick" 2-minute scenario
 
From MAVLink System_state Table:

"0"	"2017-05-24 03:34:33.607872"	"Hold"						0		ms
"1"	"2017-05-24 03:35:15.844721"	"Fly Orbit and Observe"		42237	ms
"2"	"2017-05-24 03:35:48.198449"	"Fly Search Pattern"		74590	ms
"3"	"2017-05-24 03:35:56.949499"	"Survey Target"				80341	ms
"4"	"2017-05-24 03:36:38.896474"	"Fly Orbit and Observe"		125288	ms
"5"	"2017-05-24 03:38:05.158304"	"Hold"						211550	ms
 
## Scenario 4

 - **Search area**: south
 - **Orientation**: flat
 - **Tarp location**: none
 - **Result**: tarp false positive at but disconfirmed
 
From MAVLink System_state Table:

"0"	"2017-05-24 03:43:42.205462"	"Hold"						0		ms
"1"	"2017-05-24 03:44:24.292838"	"Fly Orbit and Observe"		42088	ms
"2"	"2017-05-24 03:44:56.607829"	"Fly Search Pattern"		74403	ms
"3"	"2017-05-24 03:47:21.729214"	"Survey Target"				219524	ms
"4"	"2017-05-24 03:47:24.650969"	"Fly Orbit and Observe"		222446	ms
"5"	"2017-05-24 03:48:47.766576"	"Fly Search Pattern"		305561	ms
"6"	"2017-05-24 03:49:59.301575"	"Fly Orbit and Observe"		377096	ms
"7"	"2017-05-24 03:51:37.466869"	"Hold"						475262	ms
 
## Scenario 5

 - **Search area**: south
 - **Orientation**: flat
 - **Tarp location**: none
 - **Result**: no tarp found
 
From MAVLink System_state Table:

"0"	"2017-05-24 03:53:38.415849"	"Hold"						0		ms
"1"	"2017-05-24 03:54:20.675894"	"Fly Orbit and Observe"		42260	ms
"2"	"2017-05-24 03:54:52.918031"	"Fly Search Pattern"		74502	ms
"3"	"2017-05-24 04:03:25.770960"	"Fly Orbit and Observe"		587355	ms
"4"	"2017-05-24 04:04:48.675605"	"Hold"						670260	ms
 
## Scenario 6

 - **Search area**: across runway
 - **Orientation**: diagonal
 - **Tarp location**: near west end of runway
 - **Result**: tarp missed during takeoff (camera not running) but later found and confirmed
 
From MAVLink System_state Table:

"0"	"2017-05-24 04:10:00.625494"	"Hold"						0		ms
"1"	"2017-05-24 04:10:43.030571"	"Fly Orbit and Observe"		42406	ms
"2"	"2017-05-24 04:11:19.229131"	"Fly Search Pattern"		78604	ms
"3"	"2017-05-24 04:12:14.736148"	"Survey Target"				134111	ms
"4"	"2017-05-24 04:14:39.317167"	"Fly Orbit and Observe"		278692	ms
"5"	"2017-05-24 04:16:14.385563"	"Hold"						373760	ms
 

