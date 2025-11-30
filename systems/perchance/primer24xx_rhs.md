```
<p align="left" >
  <button onclick="update()">QUERY DATABASE</button><br><br>
  ====================================================<br>
  === PROTECTORATE INTEL. DIR. / PERSONNEL DOSSIER ===<br>
  ====================================================<br>
  : RETRIEVED VIA......: REMOTE HAND PRINTER 72 DPI<br>
  : EXTRACTION ENCODE .: #{A-Z}{A-Z}-{0-9}{0-9}-{0-9}{A-Z}{A-Z}<br>
  ====================================================<br>
  <br>
  >> SUBJECT IDENTIFICATION <<<br>
  <br>
  NAME................: [ct = cult.selectOne, ct.name.upperCase]<br>
  ALIAS(ES)...........: N/A<br>
  ORIGIN CULTURE......: [cu = ct.culture.selectOne, cu.cuname]<br>
  CULT AFFILIATION....: [ct.bgname]<br>
  RANK................: [ct.rank.upperCase]<br>
  SUBJECT CONCEPT.....: [concept.upperCase]<br>
  BEHAVIORAL TAGS.....: [virtue.upperCase] / [vice.upperCase]<br>
  AGE.................: [age=dfour.selectOne+dfour.selectOne+10]        (BAND: D4)<br>
  PHYSICAL NOTES......: [physique.upperCase] / [skin.upperCase] SKIN <br> 
  FACIAL STRUCTURE....: [face.upperCase]<br>
  HAIR................: [hair.upperCase]<br>
  VOCAL PATTERN.......: [speech.upperCase]<br>
  <br>
  ----------------------------------------------------<br>
  <br>
  >> SKILLS PROFILE <<<br>
  <br>
  -- CLASS D8 --<br>
  [cu.skill.selectUnique(2).join("&#60;br&#62;").upperCase]<br><br>
  -- CLASS D10 --<br>
  [ct.skill.selectUnique(1).join("&#60;br&#62;").upperCase]<br><br>
  -- CLASS D12 --<br>
  N/A<br><br>
  ----------------------------------------------------<br>
  <br>
  >> KNOWN PERFORMANCE DEVIATIONS <<<br>
  <br>
  -- POTENTIALS --<br>
  N/A<br><br>
  -- HANDICAPS --<br>
  N/A<br><br>
  <br>
  ----------------------------------------------------<br>
  <br>
  >> ISSUED EQUIPMENT <<<br>
  <br>
  BACKPACK<br>
  [ct.equip.upperCase]<br>
  UNIDENTIFIED SMALL MELEE WEAPON<br>
  [ct.cash] (x RANK)<br>
  <br>
  ----------------------------------------------------<br>
  <br>
  >> MPF - MEMETIC PROPAGATION FORECAST <<<br>
  <br>
  ALLIES .............: 1<br>
  AUTHORITY ..........: 1<br>
  RENOWN .............: 1<br>
  RESOURCES ..........: 1<br>
  SECRETS ............: 1<br>
  NETWORK ............: 1<br>
  <br>
  ====================================================<br>
  === ********* END OF DOT-MATRIX RECORD ********* ===<br>
  ====================================================<br>
</p>

<!-- The line below makes it so if your device is in dark mode, then the default text color is switched to white, and the default background color is switch to black. -->
<style> html { color-scheme: light; font-family:monospace; font-size:100%; color:#d93933; background-color: #DDE0E7;} </style>

```