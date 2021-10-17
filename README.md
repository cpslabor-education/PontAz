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
| Szervo motor            | LEGO   | [45502](https://www.lego.com/en-us/product/ev3-large-servo-motor-45502 "45502")  | **A**, **D**  |
| Szervo motor            | LEGO   | [45503](https://www.lego.com/en-us/product/ev3-medium-servo-motor-45503 "45503") | **C**         |
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

Az önálló feladat alap koncepciója a robot kivitelezésén alapszik. A robot halad egyenesen, miközben a ’fej’ körbepásztázza az előtte lévő teret. Ha a fej érzékel, a robot elkezd hátrálni. A gondok akkor kezdődnek, ha ’fej’ nem előre néz, mivel tudnunk kell a ’fej’ elfordulását és az 1.szenzor érzékelt távolságát, majd ebből kiszámítani a hátráláshoz szükséges pontos irányokat. 

A megoldás az volt, hogy a ’fej’ forgását 10 egységre osztottuk, majd minden egységben egyszer megmértük a távolságot. Minden mérés után a motor szögelfordulásából és az 1.szenzor értekéből kiszámítottuk, hogy a robot egyenesen, jobbra vagy balra fog hátrálni, illetve hogy hány fokos szögben kell elfordulnia.

Az adatok megszerzése után továbbítottuk őket a második szálnak, ami a robot mozgásáért volt felelős. A szál egy irányértéket és egy számnagyságot kap. Az irányértéknek megfelelően vezérli a mozgásért felelős servokat (A, D), illetve a számnagyság alapján a sebességüket. 

<h2>Önálló feladat magyarázat:</h2>

A program elején három függvényt definiálunk:

Az első függvény a "fej"-et forgató motor (**C**) kalibrálására szolgál.

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/8.png ">
</p>

Működése:

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

Működése:

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

A programunk egy végtelenített ciklusban fut, melyben először körbeforgatjuk a 'fej'-et az inicializált tömbbel. Ezt úgy valósítottuk meg, hogy egy while loop-al a 'radar_loop_i' változó értékét növeljük, mellyel végig iterálunk a tömbön. Közben figyeljük az **1.szenzor** értékét, és ha az 25-nél kisebb akkor lelassítjuk a (**C**) motor sebességét, így olyan hatást érünk el, mintha a "fej" követné az előtte lévő tárgyat. Miután a "fej" elfordult egy egységet a 'radar_loop_i' változó értékét növeljük, majd előjegyezzük a második szálat, így párhuzamos futás érhető el.

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







Ubuntu 20.04