<h1>DIFFERENCIÁLIS LEGO MOBIL ROBOT</h1>

<h3>Csapatnév: PontAz</h3>
<h4>Tagok:</h4>
<ul>
<li>Füleki Tamás</li>
<li>Császár Miksa Henrik</li>
<li>Balbach Dominik</li>
</ul>

<h2>Használt eszköz(ök)</h2>

| Megnevezés | Gyártó  |  Típus |
| ------------ | ------------ | ------------ |
| DC motor | LEGO | [45502](https://www.lego.com/en-us/product/ev3-large-servo-motor-45502 "45502") |
| DC motor | LEGO | [45503](https://www.lego.com/en-us/product/ev3-medium-servo-motor-45503 "45503") |
| Ultrahangos szenzor | LEGO | [45504](https://www.lego.com/en-us/product/ev3-ultrasonic-sensor-45504 "45504") |
| Nyomásérzékelő | LEGO | [45507](https://www.lego.com/en-us/product/ev3-touch-sensor-45507 "45507") |
| RGB szenzor | LEGO | [45506](https://www.lego.com/en-us/product/ev3-color-sensor-45506 "45506") |

<h1>1.Labor</h1>

<h2>Feladat meghatározása:</h2>

Az első labor során LEGO robot építésével foglalkoztunk. Az alapkoncepció egy differenciális robot megvalósítása volt. A végeredmény az alábbi képe(k)-en látható: 

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/image1.jpeg ">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/image2.jpeg ">
</p>

<h2>Kivitelezés:</h2>

A roboton két fő actuator (**45502**) található melyek a mozgásában, elfordulásában segítik azt. A két motorra egy-egy kereket rögzítettünk. Ezek a kerekek külön-külön vezérelhetők, aminek a segítségével kormányozható a robot. Hátsó keréknek egy két kisebb kerékből álló, szabadon forgó szerkezetet építettünk, ami így könnyen követi a robot mozgását. A roboton egy további actuator is helyet kapott (**45503**) melynek segítségével az Ultrasonic Szenzort (**45504**) lehet 360° fokban forgatni. Továbbá két másik szenzor, egy nyomás érzékelő (**45507**), illetve egy RGB szenzor (**45506**) is helyet kapott rajta.

<h2>Megfigyelések:</h2>

A feladat elvégzése során a legnagyobb gondot a kábelmenedzsment okozta. Ezt a problémát végül egy hosszú tartóelemmel oldottuk meg. A kábelek felesleges hosszát a tartóelem köré csavarásával oldottuk meg.

<h1>2.Labor</h1>

<h2>Feladat meghatározása:</h2>

A második labor során a robot továbbfejlesztése, valamint a felprogramozás elkezdése volt a cél. Az eredményt az alábbi képeken lehet megtekinteni:

<p align="left">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/image3.jpeg ">
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/image4.jpeg ">
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
  <img width="300" src="https://github.com/robotlabor-education/PontAz/blob/main/img/image5.jpeg ">
</p>

<h2>Megfigyelések:</h2>

A labor során a programozás okozott némi nehézséget, ugyanis a programunk második fele nem az elvárásainknak megfelelően működött. Ezen a téren további munka szükséges.









Ubuntu 20.04
