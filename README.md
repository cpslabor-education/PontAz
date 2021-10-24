<h1>DIFFERENCIÁLIS LEGO MOBIL ROBOT</h1>

<h3>Csapatnév: PontAz</h3>
<h4>Tagok:</h4>
<ul>
<li>Füleki Tamás</li>
<li>Császár Miksa Henrik</li>
<li>Balbach Dominik</li>
</ul>

<h2>Használt eszköz(ök)</h2>

| Megnevezés          | Gyártó | Típus                                                                            | Továbbiakban  |
| ------------------- | ------ | -------------------------------------------------------------------------------- | ------------- |
| Large Szervo motor            | LEGO   | [45502](https://www.lego.com/en-us/product/ev3-large-servo-motor-45502 "45502")  | **A**, **D**  |
| Medium Szervo motor            | LEGO   | [45503](https://www.lego.com/en-us/product/ev3-medium-servo-motor-45503 "45503") | **C**         |
| Ultrahangos szenzor | LEGO   | [45504](https://www.lego.com/en-us/product/ev3-ultrasonic-sensor-45504 "45504")  | **1.szenzor** |
| Nyomásérzékelő      | LEGO   | [45507](https://www.lego.com/en-us/product/ev3-touch-sensor-45507 "45507")       | **2.szenzor** |
| RGB szenzor         | LEGO   | [45506](https://www.lego.com/en-us/product/ev3-color-sensor-45506 "45506")       | **3.szenzor** |

<h1>1.Labor</h1>

<h2>Feladat meghatározása:</h2>

Az első labor során LEGO robot építésével foglalkoztunk. Az alapkoncepció egy differenciális robot megvalósítása volt. A végeredmény az alábbi képe(k)-en látható:

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/1.jpeg ">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/2.jpeg ">
</p>

<h2>Kivitelezés:</h2>

A roboton két fő actuator (**45502**) található melyek a mozgásában, elfordulásában segítik azt. A két motorra egy-egy kereket rögzítettünk. Ezek a kerekek külön-külön vezérelhetők, aminek a segítségével kormányozható a robot. Hátsó keréknek egy két kisebb kerékből álló, szabadon forgó szerkezetet építettünk, ami így könnyen követi a robot mozgását. A roboton egy további actuator is helyet kapott (**45503**) melynek segítségével az Ultrasonic Szenzort (**45504**) lehet 360° fokban forgatni. Továbbá két másik szenzor, egy nyomás érzékelő (**45507**), illetve egy RGB szenzor (**45506**) is helyet kapott rajta.

<h2>Megfigyelések:</h2>

A feladat elvégzése során a legnagyobb gondot a kábelmenedzsment okozta. Ezt a problémát végül egy hosszú tartóelemmel oldottuk meg. A kábelek felesleges hosszát a tartóelem köré csavarásával oldottuk meg.

<h1>2.Labor</h1>

<h2>Feladat meghatározása:</h2>

A második labor során a robot továbbfejlesztése, valamint a felprogramozás elkezdése volt a cél. Az eredményt az alábbi képeken lehet megtekinteni:

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/3.jpeg ">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/4.jpeg ">
</p>

<h2>Kivitelezés:</h2>

A robot vázát tekintve két fő fejlesztést hajtottunk végre:

<ul>
<li>Hátsó lökhárító</li>
<li>A "fej" stabilitása</li>
</ul>

A hátsó löghárító a nyomásérzékelő (**45507**) szenzor miatt került kivitelezésre. A szenzor önmagában csak egy kis ponton képes érzékelni, ezért kibővítettük az érzékelési tartományt. Egy összetett vízszintes szerkezetet rögzítettünk a nyomógombhoz, ami így a robot teljes szélességében képes érzékelni a hátulról történő ütközéseket.

A két szenzorból (Szervó motor **45503**, Ultrahangos érzékelő **45504**) álló "fej" kezdetben a legkisebb mozgásokra is érzékenyen reagált. Az állandó rezgések miatt nem lehetett pontos adatokat kinyerni az ultrahangos szenzorból, ezért a tartásuk stabilitásán dolgoztunk. Több ponton rögzítettük a rendszert, ezzel sikeresen csökkentve a rezgéseket.

Elkezdtük a robot programozását is. A szenzorok tesztelése után egyszerűbb mozgássorozatokat definiáltunk. Egy 2 másodperces előre történő, 50%-os sebességű mozgást követően az ultrahangos szenzort ±90°-ban elforgattuk. Ezt követően azt szerettük volna elérni, hogy a nyomásérzékelő, valamint az ultrahangos szenzorok segítségével megfelelő feltételek teljesülése mellett előre-hátra mozgást végezzen a robot.


<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/5.png ">
</p>

<h2>Megfigyelések:</h2>

A labor során a programozás okozott némi nehézséget, ugyanis a programunk második fele nem az elvárásainknak megfelelően működött. Ezen a téren további munka szükséges.

<h1>3.Labor</h1>

<h2>Feladat meghatározása:</h2>

A harmadik labor során a robot felprogramozása és kisebb, illetve önálló feladatok megvalósítása volt a feladat.

<h2>Kivitelezés:</h2>

A kisebb feladatok programjai alább láthatóak:
**1.Feladat:** A robot haladjon előre 1 másodpercig:

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/6.png ">
</p>

**2.Feladat:** A robot forduljon meg 2 másodpercig:

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/7.png ">
</p>

**3.Feladat:** Önálló feladat végrehajtása:

Az önálló feladat alap koncepciója a robot kivitelezésén alapszik. A robot halad egyenesen, miközben a "fej" körbepásztázza az előtte lévő teret. Ha a fej érzékel, a robot elkezd hátrálni. A gondok akkor kezdődnek, ha "fej" nem előre néz, mivel tudnunk kell a "fej" elfordulását és az 1.szenzor érzékelt távolságát, majd ebből kiszámítani a hátráláshoz szükséges pontos irányokat. 

A megoldás az volt, hogy a "fej" forgását 10 egységre osztottuk, majd minden egységben egyszer megmértük a távolságot. Minden mérés után a motor szögelfordulásából és az **1.szenzor** értekéből kiszámítottuk, hogy a robot egyenesen, jobbra vagy balra fog hátrálni, illetve hogy hány fokos szögben kell elfordulnia.

Az adatok megszerzése után továbbítottuk őket a második szálnak, ami a robot mozgásáért volt felelős. A szál egy irányértéket és egy számnagyságot kap. Az irányértéknek megfelelően vezérli a mozgásért felelős servokat (**A**, **D**), illetve a számnagyság alapján a sebességüket. 

<h2>Önálló feladat magyarázat:</h2>

A program elején három függvényt definiálunk:

Az első függvény a "fej"-et forgató motor (**C**) kalibrálására szolgál.

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/8.png ">
</p>

**Működése:**

A motor elindítjuk 30%-os sebességgel, majd 0.01 másodpercenként megnézzük, hogy a motor sebessége lecsökkent-e 10% alá, ha igen akkor feltételezhetjük, hogy a motor megállt, illetve nekiütközött valaminek. Miután megállt, elforgatjuk 90 fokot, hogy a "fej" pontosan középen legyen és előre nézzen. 

A második függvény a "fej"-et forgató motor elfordulásának tömbjét tölti fel adatokkal.

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/9.png ">
</p>

Először 5x 20, majd 10x -20, majd 5x 20 értékekkel.

Az előzőekben szó volt arról, hogy a "fej" forgását 10 egységre osztjuk fel, itt azért kell 20 különböző egység/adat, mivel feltételezzük, hogy az előbbi függvény hatására a "fej" előre néz, ezért először jobbra fordul 5 egységet, majd balra 10 egységet, aztán vissza 5 egységet és ezt ismételjük.

A harmadik függvény a "fej"-et forgató motor (**C**), illetve az 1.szenzor értéke alapján határoz meg egy irányt, illetve egy hozzá tartozó értéket.

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/10.png ">
</p>

**Működése:**

A függvénybe bekérünk 6 adatot, melyből az első kettő a negatív tartományt, a második kettő az **1.szenzor** érzékelési tartományát, az utolsó kettő a pozitív tartományt határozza meg.

Tipikusan: a negatív tartományt -1 és -180 fok közé, a pozitív tartományt 1 és 180 fok közé, a szenzor tartományát 0 és 25 közé határozzuk meg.

Először bekérjük a "fej"-et forgató motor aktuális szögelfordulását, majd ezt egy változóhoz rendeljük. Majd erről a változóról megállapítjuk, hogy melyik tartományban van benne, a negatívban vagy a pozitívban, ennek megfelelően a 'lower_bound_var' vagy a 'higher_bound_var' kap 1 értéket, ellenkező esetben 0 értéket kapnak.

Majd bekérjük az **1.szenzor** értékét és egy változóban tároljuk el azt. Erről a változóról eldöntjük, hogy benne van-e a meghatározott tartományban, ha igen akkor 'distance_var' értéket 1-re állítjuk, ha nem akkor 0-ra. 

Ezek után meghatározzuk, hogy a "fej" érzékelt-e, és ha igen akkor melyik irányban.
Először megnézzük, hogy 'distance_var' és 'lower_bound_var' értéke is 1-e, ha igen akkor egy 'lower_next_var' változónak adunk 1 értéket, ellenkező esetben 0-t. 
Ugyanezt megnézzük a 'distance_var' és a 'higher_bound_var' értékére is, ha 1 akkor a 'higher_next_var' értéke 1, ha nem akkor 0.

Végül kivonjuk a 'lower_next_var'-t és a 'higher_next_var'-t egymásból, és azt az értéket adjuk vissza ami 1, -1 illetve 0 lehet.


A függvények definiálása után kezdjük a 'main loop'-ot.

A main loop elején inicializáljuk a változó tömböt, és beállítjuk a robotot mozgató motorokat (**A**, **D**), illetve a "fej"-et mozgató motort (**C**).

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/11.png ">
</p>

A programunk egy végtelenített ciklusban fut, melyben először körbeforgatjuk a "fej"-et az inicializált tömbbel. Ezt úgy valósítottuk meg, hogy egy while loop-al a 'radar_loop_i' változó értékét növeljük, mellyel végig iterálunk a tömbön. Közben figyeljük az **1.szenzor** értékét, és ha az 25-nél kisebb akkor lelassítjuk a (**C**) motor sebességét, így olyan hatást érünk el, mintha a "fej" követné az előtte lévő tárgyat. Miután a "fej" elfordult egy egységet a 'radar_loop_i' változó értékét növeljük, majd előjegyezzük a második szálat, így párhuzamos futás érhető el.

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/12.png ">
</p>

A második szál felelős a robot mozgásáért. Ezt egy végtelenített ciklusban hajtjuk végre. Először végrehajtjuk a 'get_degrees_and_distance' függvényt melyből megkapjuk a fej irányából, és az **1.szenzor** értékéből adódó értéket, ami lehet 1, -1 vagy 0. 

Ennek megfelelően, ha az érték 1 vagy -1 akkor a robot elkezd fordulni abba a szögben amibe a "fej" éppen áll, majd megnézzük, hogy az **1.szenzor** értéke kisebb-e mint 25, és ha igen akkor az **1.szenzor** függvényében változtatjuk a hátrálás mértékét (Az **1.szenzor** értékéből levonunk 30-at és azt állítjuk be a motor sebességének.). 

Ha a visszakapott érték 0 akkor a robot előre halad 20%-os sebességgel.

<h2>Robot kinematikai modell és (pontos) méretek:</h2>

||stud|mm|
|-|-|-|
|Szélesség|26|208|
|Hosszúság|38|304|
|Tengelytáv|20.75|166|
|Kerék átmérő|7|56|
|Kerék vastagság|3.5|28|
|Tengely táv hátul|3.5|28|
|Tengely táv elöl|7|56|
|Kerék kerület|21.98|175.9|

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/13.png ">
</p>

<h1>4.Labor</h1>

<h2>Feladat meghatározása:</h2>

1.Egy saját ROS2 package létrehozása, amelyben legalább kettő Python-alapú node legyen,
az egyik node szabadon választott szabályozást valósít meg, míg a többi csomópont a robot
szenzor-aktuátor interfészét valósítja meg.

2.Webots nevű szimulátorban kell egy robotot létrehozni, ami legalább két kerekű.

<h2>Kivitelezés:</h2>

**1.Feladat:**

<p>A ROS2 package két node-ból áll, az egyiket robot-nak, a másikat pid-nek hívják.</p>
<p>A robot node az előzőekben megépített LEGO robotunkat szimulálja.</p>
<p>A robot 11 tonikot tartalmaz, melyek a különböző szenzorokat, illetve motorokat
reprezentálják. A node ezeknek a szenzoroknak megfelelően generál véletlenszerű adatokat,
melyeket 0.5 másodpercenként továbbítunk a pid node-nak, illetve kiírjuk az elküldött
értéküket.</p>

[Link a robot.py-hez](https://219.235.251.164/media/pi/16TB/deemix_dl/MusicLab(Future_Garage)/456_-_Azaleh_-_Moonlight_(Original_Mix).flac "robot.py")

```python
from numpy.core.records import array
import rclpy
from rclpy.node import Node

import random
from std_msgs.msg import String,\
                         Float64,\
                         Bool,\
                         Int32MultiArray,\
                         Int64,\
                         Int32,\
                         Float64MultiArray,\
                         Int8

import numpy as np
import random

import sys

# Segédfüggvények

#from pontaz.msg import Num

def genSin(res, j=1): # impact
    x = np.linspace(-np.pi, np.pi, res)
    y = np.sin(x*j)
    return (x, y)

def getRandInRange(min, step, max):
    return random.randrange(start=min, step=step, stop=max)

def myMap(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)


# Topikok inicializálása

class Robot(Node):
 
    def __init__(self):
        super().__init__('robot')
        # initialize topics
        self.topic_01 = self.create_publisher(Float64, 'get_amotorspeed',    10)
        self.topic_02 = self.create_publisher(Float64, 'get_amotordeg',      10)
        self.topic_03 = self.create_publisher(Float64, 'get_bmotorspeed',    10)
        self.topic_04 = self.create_publisher(Float64, 'get_bmotordeg',      10)
        self.topic_05 = self.create_publisher(Float64, 'get_cmotorspeed',    10)
        self.topic_06 = self.create_publisher(Float64, 'get_cmotordeg',      10)
        self.topic_07 = self.create_publisher(Int32,   'get_ultrasonicraw',  10)
        self.topic_08 = self.create_publisher(Bool,    'get_touchsensor',    10)
        self.topic_09 = self.create_publisher(Int32,   'get_rgbsensor_r',    10)
        self.topic_10 = self.create_publisher(Int32,   'get_rgbsensor_g',    10)
        self.topic_11 = self.create_publisher(Int32,   'get_rgbsensor_b',    10)

        # inintalize subscribers
        self.sub_01 = self.create_subscription(Int8,\
            'set_direction', self.listen_set_direction, 10)
        self.sub_02 = self.create_subscription(Float64,\
            'set_speed', self.listen_set_speed, 10)
        self.sub_03 = self.create_subscription(Int32,\
            'set_ul_real', self.listen_set_ul, 10)

        # self.publisher_ul = self.create_publisher(Float64, 'ul', 10)
        # timer sends packets in every 0.5 seconds


        # Helyi változók inicializálása, véletlen adatok generálása.


        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.computeUp = self.create_timer(0.1, self.computeUp_cr)
        self.i = 0

        # Init local variables

        self._as = 0
        self._ad = 0
        self._bs = 0
        self._bd = 0
        self._cs = 0
        self._cd = 0
        self._ul = 0
        self._ts = 0
        self._cr = 0
        self._cg = 0
        self._cb = 0

        # Init recieved varibles 

        self._l_as = 0
        self._l_bs = 0
        self._l_ul = 0

        self._dir = 0
        self._dir_speed = 0
    
    # A visszatérő adatok befogadása.

    def genDummyData(self):
        self._as = float(random.randrange(start=-100, stop=100, step=1))
        self._ad = float(random.randrange(start=0, stop=360, step=1))
        self._bs = float(random.randrange(start=-100, stop=100, step=1))
        self._bd = float(random.randrange(start=0, stop=360, step=1))
        self._cs = float(random.randrange(start=-100, stop=100, step=1))
        self._cd = float(random.randrange(start=-180, stop=180, step=1))
        self._ul = random.randrange(start=0, stop=4096, step=1)
        self._ts = bool(random.getrandbits(1))
        self._cr = random.randrange(start=0, stop=4096, step=1)
        self._cg = random.randrange(start=0, stop=4096, step=1)
        self._cb = random.randrange(start=0, stop=4096, step=1)
    
    def listen_set_direction(self, msg):
        self._dir = msg.data
    def listen_set_speed(self, msg):
        self._dir_speed = msg.data
    def listen_set_ul(self, msg):
        self._l_ul = msg.data

      
    # Miután a pid node feldolgozta az adatokat, visszaküldi a robot node-nak és az hasznosítja őket oly formában, hogy a robot az előzőekben megfelelően működjön.

    def computeUp_cr(self):
        if self._dir == 1:
            self._l_as = 50
            self._l_bs = self._cd
            if self._l_ul < 25:
                self._l_as = self._dir_speed
                self._l_bs = self._dir_speed
        elif self._dir == -1:
            self._l_as = -50
            self._l_bs = self._cd
            if self._l_ul < 25:
                self._l_as = self._dir_speed
                self._l_bs = self._dir_speed
        elif self._dir == 0:
            self._l_as = -20
            self._l_bs = -20
        else:
            self._l_as = self._dir_speed
            self._l_as = self._dir_speed
        self.get_logger().info(
            f'The robot go "{("Left" if self._dir == 1 else "Right" if self._dir == -1 else "Straight")}"'\
            +f' at {(self._l_as, self._l_bs)} speed'
        )
        
        # Az időzített küldő funkció

    def timer_callback(self):
        self.genDummyData()
        # Messages types 
        msg_amotorspeed = Float64()
        msg_amotordeg = Float64()
        msg_bmotorspeed = Float64()
        msg_bmotordeg = Float64()
        msg_cmotorspeed = Float64()
        msg_cmotordeg = Float64()

        msg_ultrasonicraw = Int32()

        msg_touchsensor = Bool()

        msg_rgbsensor_r = Int32()
        msg_rgbsensor_g = Int32()
        msg_rgbsensor_b = Int32()
        
        #msg.data = 'Hello World: %d' % self.i
        #msg.data = self.robot.msgData()+str(self.i)
        # Get sensors data
        msg_amotorspeed.data = self._as
        msg_amotordeg.data = self._ad
        msg_bmotorspeed.data = self._bs
        msg_bmotordeg.data = self._bd
        msg_cmotorspeed.data = self._cs
        msg_cmotordeg.data = self._cd
        #msg_cmotorspeed.data = float(random.randrange(
        #    start=int(myMap(abs(int(genSin(100, 2)[0][
        #        self.i if self.i < 100 else int(myMap(self.i, 0, self.i, 0, 100))
        #    ]*4096)), 0, 5000, 0, 4096)), stop=4096)
        #)
        #msg_cmotordeg.data = float(random.randrange(
        #    start=abs(int(genSin(100, 2)[1][
        #        self.i if self.i < 100 else int(myMap(self.i, 0, self.i, 0, 100))
        #    ]*4096)), stop=4096)

        # Az időzített küldő folytatása, adatok kiírása.

        #)
        msg_ultrasonicraw.data = self._ul
        msg_touchsensor.data = self._ts
        #r = int(random.randrange(0, 4096, 1))
        #g = int(random.randrange(0, 4096, 1))
        #b = int(random.randrange(0, 4096, 1))
        #r = 4096
        #g = 4096
        #b = 4096

        #msg_rgbsensor.data = (r<<24|g<<12|b)
        msg_rgbsensor_r.data = self._cr
        msg_rgbsensor_g.data = self._cg
        msg_rgbsensor_b.data = self._cb

        #msg_motor.data = float(random.random())
        #self.robot.Tick(self.i)

        self.topic_01.publish(msg_amotorspeed)
        self.topic_02.publish(msg_amotordeg)
        self.topic_03.publish(msg_bmotorspeed)
        self.topic_04.publish(msg_bmotordeg)
        self.topic_05.publish(msg_cmotorspeed)
        self.topic_06.publish(msg_cmotordeg)
        self.topic_07.publish(msg_ultrasonicraw)
        self.topic_08.publish(msg_touchsensor)
        self.topic_09.publish(msg_rgbsensor_r)
        self.topic_10.publish(msg_rgbsensor_g)
        self.topic_11.publish(msg_rgbsensor_b)
        #self.publisher_ul.publish(msg_ul)
        #self.get_logger().info('---------------------------------------')
        self.get_logger().info(f'[{self.i}]Publishing topic_01: "{msg_amotorspeed.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_02: "{msg_amotordeg.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_03: "{msg_bmotorspeed.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_04: "{msg_bmotordeg.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_05: "{msg_cmotorspeed.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_06: "{msg_cmotordeg.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_07: "{msg_ultrasonicraw.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_08: "{msg_touchsensor.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_09: "{msg_rgbsensor_r.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_10: "{msg_rgbsensor_g.data}"')
        self.get_logger().info(f'[{self.i}]Publishing topic_11: "{msg_rgbsensor_b.data}"')
        
        #self.get_logger().info('---------------------------------------')
        self.i += 1

    # A pid node feliratkozik, az első node 11 tonikjára amiket feldolgoz, majd visszaküld a robot node-nak.

def main(args=None):
    rclpy.init(args=args)

    robot = Robot()

    rclpy.spin(robot)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robot.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

<p>Az adatok feldolgozása és kiíratása egy olyan függvényben történik, mely bekéri a változókat,
az ezekkel a változókkal végrehajtani kívánt transzformációt, a loggolás érdekében a változók
neveit, illetve ha vissza szeretnénk az eredményt küldeni az előző node-nak, akkor a
visszaküldő függvényt a topic változóját, illetve az üzenet típusát is meg kell adnunk.</p>

<p>Az adatokat 0.2 másodpercenként küldjük vissza a robot node-nak.</p>

<p>Könyvtárak bekérése, segédfüggvény.</p>

[Link a pid.py-hez](https://github.com/robotlabor-education/PontAz/blob/main/04_Labor/air_ws/src/pontaz/pontaz/pid.py "pid.py")

```python
from numpy.core.fromnumeric import var
import rclpy
from rclpy.node import Node

from std_msgs.msg import String,\
                         Float64,\
                         Int32,\
                         Bool,\
                         Int8
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def myMap(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)



class Pid(Node):

    def __init__(self):
        super().__init__('pid')
        
        #subscription = node.create_subscription(
        #String, 'topic', lambda msg: node.get_logger().info('I heard: "%s"' % msg.data), 10)

        # Init subscribers

        self.sub_01 = self.create_subscription(Float64, 'get_amotorspeed', self.listener_callback_as, 10)
        self.sub_02 = self.create_subscription(Float64, 'get_amotordeg', self.listener_callback_ad, 10)
        self.sub_03 = self.create_subscription(Float64, 'get_bmotorspeed', self.listener_callback_bs, 10)
        self.sub_04 = self.create_subscription(Float64, 'get_bmotordeg', self.listener_callback_bd, 10)
        self.sub_05 = self.create_subscription(Float64, 'get_cmotorspeed', self.listener_callback_cs, 10)
        self.sub_06 = self.create_subscription(Float64, 'get_cmotordeg', self.listener_callback_cd, 10)
        self.sub_07 = self.create_subscription(Int32, 'get_ultrasonicraw', self.listener_callback_ul, 10)
        self.sub_08 = self.create_subscription(Bool, 'get_touchsensor', self.listener_callback_ts, 10)
        self.sub_09 = self.create_subscription(Int32, 'get_rgbsensor_r', self.listener_callback_cr, 10)
        self.sub_10 = self.create_subscription(Int32, 'get_rgbsensor_g', self.listener_callback_cg, 10)
        self.sub_11 = self.create_subscription(Int32, 'get_rgbsensor_b', self.listener_callback_cb, 10)
        
        # Init publishers

        self.pub_01 = self.create_publisher(Int8, 'set_direction', 10)
        self.pub_02 = self.create_publisher(Float64, 'set_speed', 10)
        self.pub_03 = self.create_publisher(Int32, 'set_ul_real', 10)

        self.timer = self.create_timer(0.2, self.compute_data)

        #self.sub_01  # prevent unused variable warning
        
        self._as = [0]
        self._ad = [0]
        self._bs = [0]
        self._bd = [0]
        self._cs = [0]
        self._cd = [0]
        self._ul = [0]
        self._ts = [0]
        self._cr = [0]
        self._cg = [0]
        self._cb = [0]
        #plt.show(block=True)

  # A beérkezett változók eltárolása, illetve azok utolsó 10 értékének.

    def listener_callback_as(self, msg):
        self._as.append(msg.data)
        self._as = self._as[-9:]
    def listener_callback_ad(self, msg):
        self._ad.append(msg.data)
        self._ad = self._ad[-9:]
    def listener_callback_bs(self, msg):
        self._bs.append(msg.data)
        self._bs = self._bs[-9:]
    def listener_callback_bd(self, msg):
        self._bd.append(msg.data)
        self._bd = self._bd[-9:]
    def listener_callback_cs(self, msg):
        self._cs.append(msg.data)
        self._bd = self._bd[-9:]
    def listener_callback_cd(self, msg):
        self._cd.append(msg.data)
        self._cd = self._cd[-9:]
    def listener_callback_ul(self, msg):
        self._ul.append(msg.data)
        self._ul = self._ul[-9:]
    def listener_callback_ts(self, msg):
        self._ts.append(msg.data)
        self._ts = self._ts[-9:]
    def listener_callback_cr(self, msg):
        self._cr.append(msg.data)
        self._cr = self._cr[-9:]
    def listener_callback_cg(self, msg):
        self._cg.append(msg.data)
        self._cg = self._cg[-9:]
    def listener_callback_cb(self, msg):
        self._cb.append(msg.data)
        self._cb = self._cb[-9:]

    def sendPub(self, where, type, msg):
        obj = type()
        obj.data = msg
        #method = getattr(Pid.__init__, where)
        #print(type(where))
        where.publish(obj)

# A compute logger funkció, melyben loggoljuk, és végrehajtjuk a beadott változókat és függvényeket.

    def computeLogger(self, variables, command, names=None, ret=None): # self, variable, command
        #arg_list = [*args]
        #variable = arg_list[0]
        #command = arg_list[1]
        for variable, name in zip(variables, names):
            last_read_data = variable[-1:]
        #var_name = f'{variable=}'.partition('=')[0]
        #var_name = [ i for i, a in locals().items() if a == variable][0]
        #var_name = str(arg_list[0])
            self.get_logger().info(f'Last read data of {name}: "{last_read_data}"')
            self.get_logger().info(f'Data of {name}: "{variable}"')
            avg_of_read_data = np.average(variable)
            self.get_logger().info(f'Avg of read data: "{avg_of_read_data}"')
            trans_data = command(variables)
            self.get_logger().info(f'Trans data of {name}: "{trans_data}"')
            self.get_logger().info('--------------------------------------------------------------------------')

        if ret != None:
            self.get_logger().info('Response sent!')
            if ret.__len__() > 1:
                for i in range(ret.__len__()):
                    ret[i][0](ret[i][1], ret[i][2], trans_data[i])
            else:
                ret[0][0](ret[0][1], ret[0][2], trans_data)
        
        # A következő funkció a robot fejének elfordulásából és a szenzor távolságából számolja ki az irányokat, illetve sebességéket.

    def ul_raw_to_real(self, raw):
        return int(myMap(raw, 0.0, 4096.0, 0.0, 255.0))

    def get_degrees_and_distance(self, variables):
        neg_low = -180
        neg_high = -1
        pos_low = 1
        pos_high = 180
        ul_min = 0
        ul_max = 25
        d_v = 0
        ul_real = self.ul_raw_to_real(variables[1][-1])
        low_b = 1 if variables[0][-1] > neg_low and variables[0][-1] < neg_high else 0
        high_b = 1 if variables[0][-1] > pos_low and variables[0][-1] < pos_high else 0
        d_v = 1 if ul_real > ul_min and ul_real < ul_max else 0
        l_n_v = 1 if d_v and low_b else 0
        h_n_v = 1 if d_v and high_b else 0
        i = l_n_v - h_n_v
        if i == 1:
            #return "Left_Back_at_"+str(variables[0][-1])+"_speed"
            return (1, variables[0][-1]-30.0, ul_real)
        elif i == -1:
            #return "Right_Back_at_"+str(variables[0][-1])+"_speed"
            return (-1, variables[0][-1]-30.0, ul_real)
        elif i == 0:
            #return "Back_at_"+str(variables[0][-1])+"_speed"
            return (0, variables[0][-1]-30.0, ul_real)
        else:
            #return "Straight"
            return (3, 100.0, ul_real)


# A compute_data függvény minden 0.2 másodpercenként feldolgozza az adatokat, és lehetőség szerint visszaküldi őket.


    def compute_data(self):
        #last_read_data_as = self._as[-1:]
        #self.get_logger().info(f'Last read data: "{last_read_data_as}"')
        #avg_of_last_read_data_as = np.average(self._as)
        #trans_data = (now_data*2)
        #self.get_logger().info(f'Avg of read data: "{avg_of_last_read_data_as}", len: "{self._as.__len__()}"')
        #self.get_logger().info(f'Last 10 item:{self._as}')

        self.computeLogger(
            [self._as], 
            lambda x: 1 if x[0][-1] > 50 else 0 if x[0][-1] < -50 else 1, 
            names=["_as"]
        )
        self.computeLogger(
            [self._ts],
            lambda x: "Pressed" if x[0][-1] else "Released",
            names=["_ts"]
        )
        self.computeLogger(
            [self._cr, self._cg, self._cb], 
            lambda x: "White" if x[0][-1] > 200 and x[1][-1] > 200 and x[2][-1] > 200 else "Black"\
                      if x[0][-1] < 50 and x[1][-1] < 50 and x[2][-1] < 50 else "Blue", 
            names=["R", "G", "B"]
        )
        self.computeLogger(
            [self._cd, self._ul],
            self.get_degrees_and_distance,
            names=["Head"],
            ret=[[self.sendPub, self.pub_01, Int8],
                 [self.sendPub, self.pub_02, Float64],
                 [self.sendPub, self.pub_03, Int32]
            ]
        )
    
        





def main(args=None):
    rclpy.init(args=args)

    pid = Pid()
    rclpy.spin(pid)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pid.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

```

**2.Feladat:**
<p>A második feladat egy robot megvalósítása volt Webots-ban.</p>

Képek az elkészült robotról:

<img width="300" src="https://github.com/robotlabor-education/PontAz/tree/main/04_Labor/img/wb01.png">
<img width="300" src="https://github.com/robotlabor-education/PontAz/tree/main/04_Labor/img/wb02.png">

<img width="300" src="https://github.com/robotlabor-education/PontAz/tree/main/04_Labor/img/wb03.png">
<p>A piros-zöld robot 2 távolságmérővel van ellátva, ha falhoz, vagy egyéb objektumhoz közelít,
akkor hátrál és megfordul. A narancs-sárga robot az a,w,s,d gombokkal irányítható.</p>
<img width="300" src="https://github.com/robotlabor-education/PontAz/tree/main/04_Labor/img/wb04.png">


[Link a Webots PROTO-hoz](https://github.com/robotlabor-education/PontAz/blob/main/04_Labor/pontaz_webots_simulation/protos/FourWheelsRobot.proto "robot.py")


Ubuntu 20.04