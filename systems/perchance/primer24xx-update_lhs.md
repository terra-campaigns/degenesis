```
trace_updates
  1
    text = [hcOutput] &░░and<br>[hcOutput]<br><br>EXPELLED FROM CULT..................................<br>UPDATE CULT TO CLANNER, FIRST RANK..................<br>*** NO FURTHER UPDATES ENCOUNTERED *** ........|END|
    end = |░░░PLEASSTOP ░░░ PROCEDURE NOW░░░░░|
    relations = Negative relation to other subject found
  2
    text = [hcOutput]<br><br>*** NO FURTHER UPDATES ENCOUNTERED *** ........|END|
    end = |░░░PLEASE STOP THE PROCE░░░E NOW░░░░|
    relations = No additional subject relations found
  3
    text = [hcOutput]<br><br>UPDATE SKILLS PROFILE, CONSULT CULTURAL DATABASES...<br>*** FURTHER UPDATES MAY EXIST ***...............|OK|
    end = |FURTHER UPDATES MAY ░░░AVAILABLE|
    relations = Neutral relation to other subject found
  4
    text = [hcOutput]<br><br>UPDATE SKILLS PROFILE, CONSULT CULT DATABASES.......<br>UPDATE POTENTIAL, CONSULT CULT DATABASES............<br>*** FURTHER UPDATES MAY EXIST ***.........|░░░OK░░|
    end = |░░░░░░░ UPDATES MAY BE AVAILABLE|
    relations = No additional subject relations found
  5
    text = [hcOutput]<br><br>RANK PROMOTION .... SUBJECT MEETS REQUIREMENTS......<br>*** FURTHER UPDATES MAY EXIST ***...............|OK|
    end = |FURTHER UPDAT░░░MAY BE AVAILABLE|
    relations = Positive relation to other subject found
  6
    text = RANK PROMOTION .... SUBJECT MEETS REQUIREMENTS......<br>UPDATE SKILLS PROFILE, CONSULT SUBJECT CONCEPT DB...<br>*** FURTHER UPDATES MAY EXIST ***...............|OK|
    end = |FURTHER UPDATES MAY BE AVAIL░░░E|
    relations = No additional subject relations found

hcOutput
  [handicaps[ticked].selectOne.upperCase]

ticked // Using Dynamic Odds
  none ^[!d4.checked && !d6.checked && !d8.checked && !d10.checked && !d12.checked && !d20.checked]
  
  d4   ^[ d4.checked && !d6.checked && !d8.checked && !d10.checked && !d12.checked && !d20.checked]
  d6   ^[!d4.checked &&  d6.checked && !d8.checked && !d10.checked && !d12.checked && !d20.checked]
  d8   ^[!d4.checked && !d6.checked &&  d8.checked && !d10.checked && !d12.checked && !d20.checked]
  d10  ^[!d4.checked && !d6.checked && !d8.checked &&  d10.checked && !d12.checked && !d20.checked]
  d12  ^[!d4.checked && !d6.checked && !d8.checked && !d10.checked &&  d12.checked && !d20.checked]
  d20  ^[!d4.checked && !d6.checked && !d8.checked && !d10.checked && !d12.checked &&  d20.checked]
  
  {d4|d6}   ^[ d4.checked &&  d6.checked && !d8.checked && !d10.checked && !d12.checked && !d20.checked]
  {d4|d8}   ^[ d4.checked && !d6.checked &&  d8.checked && !d10.checked && !d12.checked && !d20.checked]
  {d4|d10}  ^[ d4.checked && !d6.checked && !d8.checked &&  d10.checked && !d12.checked && !d20.checked]
  {d4|d12}  ^[ d4.checked && !d6.checked && !d8.checked && !d10.checked &&  d12.checked && !d20.checked]
  {d4|d20}  ^[ d4.checked && !d6.checked && !d8.checked && !d10.checked && !d12.checked &&  d20.checked]
  
  {d6|d8}   ^[!d4.checked &&  d6.checked &&  d8.checked && !d10.checked && !d12.checked && !d20.checked]
  {d6|d10}  ^[!d4.checked &&  d6.checked && !d8.checked &&  d10.checked && !d12.checked && !d20.checked]
  {d6|d12}  ^[!d4.checked &&  d6.checked && !d8.checked && !d10.checked &&  d12.checked && !d20.checked]
  {d6|d20}  ^[!d4.checked &&  d6.checked && !d8.checked && !d10.checked && !d12.checked &&  d20.checked]
  
  {d8|d10}  ^[!d4.checked && !d6.checked &&  d8.checked &&  d10.checked && !d12.checked && !d20.checked]
  {d8|d12}  ^[!d4.checked && !d6.checked &&  d8.checked && !d10.checked &&  d12.checked && !d20.checked]
  {d8|d20}  ^[!d4.checked && !d6.checked &&  d8.checked && !d10.checked && !d12.checked &&  d20.checked]
  
  {d10|d12} ^[!d4.checked && !d6.checked && !d8.checked &&  d10.checked &&  d12.checked && !d20.checked]
  {d10|d20} ^[!d4.checked && !d6.checked && !d8.checked &&  d10.checked && !d12.checked &&  d20.checked]
  
  {d12|d20} ^[!d4.checked && !d6.checked && !d8.checked && !d10.checked &&  d12.checked &&  d20.checked]
  
  {d4|d6|d8}    ^[ d4.checked &&  d6.checked &&  d8.checked && !d10.checked && !d12.checked && !d20.checked]
  {d4|d6|d10}   ^[ d4.checked &&  d6.checked && !d8.checked &&  d10.checked && !d12.checked && !d20.checked]
  {d4|d6|d12}   ^[ d4.checked &&  d6.checked && !d8.checked && !d10.checked &&  d12.checked && !d20.checked]
  {d4|d6|d20}   ^[ d4.checked &&  d6.checked && !d8.checked && !d10.checked && !d12.checked &&  d20.checked]
  {d4|d8|d10}   ^[ d4.checked && !d6.checked &&  d8.checked &&  d10.checked && !d12.checked && !d20.checked]
  {d4|d8|d12}   ^[ d4.checked && !d6.checked &&  d8.checked && !d10.checked &&  d12.checked && !d20.checked]
  {d4|d8|d20}   ^[ d4.checked && !d6.checked &&  d8.checked && !d10.checked && !d12.checked &&  d20.checked]
  {d4|d10|d12}  ^[ d4.checked && !d6.checked && !d8.checked &&  d10.checked &&  d12.checked && !d20.checked]
  {d4|d10|d20}  ^[ d4.checked && !d6.checked && !d8.checked &&  d10.checked && !d12.checked &&  d20.checked]
  {d4|d12|d20}  ^[ d4.checked && !d6.checked && !d8.checked && !d10.checked &&  d12.checked &&  d20.checked]
  
  {d6|d8|d10}   ^[!d4.checked &&  d6.checked &&  d8.checked &&  d10.checked && !d12.checked && !d20.checked]
  {d6|d8|d12}   ^[!d4.checked &&  d6.checked &&  d8.checked && !d10.checked &&  d12.checked && !d20.checked]
  {d6|d8|d20}   ^[!d4.checked &&  d6.checked &&  d8.checked && !d10.checked && !d12.checked &&  d20.checked]
  {d6|d10|d12}  ^[!d4.checked &&  d6.checked && !d8.checked &&  d10.checked &&  d12.checked && !d20.checked]
  {d6|d10|d20}  ^[!d4.checked &&  d6.checked && !d8.checked &&  d10.checked && !d12.checked &&  d20.checked]
  {d6|d12|d20}  ^[!d4.checked &&  d6.checked && !d8.checked && !d10.checked &&  d12.checked &&  d20.checked]
  
  {d8|d10|d12}  ^[!d4.checked && !d6.checked &&  d8.checked &&  d10.checked &&  d12.checked && !d20.checked]
  {d8|d10|d20}  ^[!d4.checked && !d6.checked &&  d8.checked &&  d10.checked && !d12.checked &&  d20.checked]
  {d8|d12|d20}  ^[!d4.checked && !d6.checked &&  d8.checked && !d10.checked &&  d12.checked &&  d20.checked]
  
  {d10|d12|d20} ^[!d4.checked && !d6.checked && !d8.checked &&  d10.checked &&  d12.checked &&  d20.checked]
  
  {d4|d6|d8|d10}    ^[ d4.checked &&  d6.checked &&  d8.checked &&  d10.checked && !d12.checked && !d20.checked]
  {d4|d6|d8|d12}    ^[ d4.checked &&  d6.checked &&  d8.checked && !d10.checked &&  d12.checked && !d20.checked]
  {d4|d6|d8|d20}    ^[ d4.checked &&  d6.checked &&  d8.checked && !d10.checked && !d12.checked &&  d20.checked]
  {d4|d6|d10|d12}   ^[ d4.checked &&  d6.checked && !d8.checked &&  d10.checked &&  d12.checked && !d20.checked]
  {d4|d6|d10|d20}   ^[ d4.checked &&  d6.checked && !d8.checked &&  d10.checked && !d12.checked &&  d20.checked]
  {d4|d6|d12|d20}   ^[ d4.checked &&  d6.checked && !d8.checked && !d10.checked &&  d12.checked &&  d20.checked]
  {d4|d8|d10|d12}   ^[ d4.checked && !d6.checked &&  d8.checked &&  d10.checked &&  d12.checked && !d20.checked]
  {d4|d8|d10|d20}   ^[ d4.checked && !d6.checked &&  d8.checked &&  d10.checked && !d12.checked &&  d20.checked]
  {d4|d8|d12|d20}   ^[ d4.checked && !d6.checked &&  d8.checked && !d10.checked &&  d12.checked &&  d20.checked]
  {d4|d10|d12|d20}  ^[ d4.checked && !d6.checked && !d8.checked &&  d10.checked &&  d12.checked &&  d20.checked]
  
  {d6|d8|d10|d12}   ^[!d4.checked &&  d6.checked &&  d8.checked &&  d10.checked &&  d12.checked && !d20.checked]
  {d6|d8|d10|d20}   ^[!d4.checked &&  d6.checked &&  d8.checked &&  d10.checked && !d12.checked &&  d20.checked]
  {d6|d8|d12|d20}   ^[!d4.checked &&  d6.checked &&  d8.checked && !d10.checked &&  d12.checked &&  d20.checked]
  {d6|d10|d12|d20}  ^[!d4.checked &&  d6.checked && !d8.checked &&  d10.checked &&  d12.checked &&  d20.checked]
  
  {d8|d10|d12|d20}  ^[!d4.checked && !d6.checked &&  d8.checked &&  d10.checked &&  d12.checked &&  d20.checked]
  
  {d4|d6|d8|d10|d12}   ^[ d4.checked &&  d6.checked &&  d8.checked &&  d10.checked &&  d12.checked && !d20.checked]
  {d4|d6|d8|d10|d20}   ^[ d4.checked &&  d6.checked &&  d8.checked &&  d10.checked && !d12.checked &&  d20.checked]
  {d4|d6|d8|d12|d20}   ^[ d4.checked &&  d6.checked &&  d8.checked && !d10.checked &&  d12.checked &&  d20.checked]
  {d4|d6|d10|d12|d20}  ^[ d4.checked &&  d6.checked && !d8.checked &&  d10.checked &&  d12.checked &&  d20.checked]
  {d4|d8|d10|d12|d20}  ^[ d4.checked && !d6.checked &&  d8.checked &&  d10.checked &&  d12.checked &&  d20.checked]
  {d6|d8|d10|d12|d20}  ^[!d4.checked &&  d6.checked &&  d8.checked &&  d10.checked &&  d12.checked &&  d20.checked]
  
  {d4|d6|d8|d10|d12|d20} ^[ d4.checked &&  d6.checked &&  d8.checked &&  d10.checked &&  d12.checked &&  d20.checked]


handicaps
  d4
    Bruises linger longer than they should
    Fingernails crack from minor impacts
    Cuts close slowly from malnutrition
    Sudden dizziness after blows to the head
    A faint rash from contaminated water
    Metallic smell in sweat (early spore trace)
    Persistent cough from smoke or fungal air
    Surface wounds swell aggressively
    Low fevers after dirty injuries
    Sharp rib pains from past blows
    Skin peeling in small patches
    Breath hitching in spore-rich zones
    Hands tremble after strenuous tasks
    Nightmares replay violence
    Old wounds throb in cold
    Ringing ears after loud shocks
    Sudden nosebleeds during stress
    Glowing specks under the skin (microreactivity)
    Shortness of breath after mild running
    Rib spasms from internal bruising
    Vision flickering dark during exertion
    Stomach cramps from bad food
    Lungs burn in fungal areas
    Sweet-spore odor on breath
  d6
    Knees click and grind when rising
    Lower back twinges during lifting
    Pulsing headaches behind eyes
    Arms tire quickly
    Skin bruises easily
    Dry cough after spore exposure
    Immune resistance fading
    Minor cuts scabbing slowly
    Night sweats without fever
    Chest tightness during work
    Overwhelming fatigue waves
    Red threadlike veins in eye whites
  d8
    Unstable weight changes
    Knees ache after walking
    Digestive complaints
    Muscles slow to wake in mornings
    Cold-triggered body aches
    Minor fungal rashes
    Softened near vision
    Permanent ear ringing
    Stiff spine after long sitting
    Growing light sensitivity
    Occasional vertigo
    Luminescent spots on inner arms
  d10
    Short breath climbing stairs
    Unpredictable blood pressure
    Heart skipping under stress
    Tight throat during exertion
    Evening ankle swelling
    Grey phlegm in spore zones
    Weather-triggered bone pain
    Stiffening fingers
    Grinding hips
    Shoulder freezes mid-lift
    Deep nightly bone ache
    Yellowed or thickened nails
  d12
    Tingling extremities
    Random leg weakness
    Memory slips
    Sudden tremors
    Phantom pains in old scars
    Branching skin patterns (filaments)
    Thick, slow-clotting blood
    Spontaneous bruises
    Chronic swelling joints
    Periodic fevers
    Dim vision at twilight
    Green-tinted scabs
  d20
    Harsh rasping breath
    Bloody cough fits
    Long recovery from colds
    Shallow sleep
    Chest heaviness
    Pale dust exhaled in spore regions
    Frequent fractures
    Compressing spine
    Loosening teeth
    Constant rib ache
    Weak hand strength
    Bone nodules from fungal intrusion
    Shoulders freezing painfully
    Knees buckling
    Fingers curling involuntarily
    Rapid mobility decline
    Pain standing upright
    Crystalized greenish joint fluid
    Liver swelling and jaundice
    Kidney stabbing pain
    Persistent gut cramps
    Chronic nausea
    Severe dehydration
    Internal fungal spread across organs
    Seizures under stress
    Fogged vision
    Sudden collapses
    Burning limb numbness
    Slurred speech
    Spore-light hallucinations
    Chest pain while resting
    Fainting spells
    Severe arrhythmia
    Cold sweat episodes
    Purple lips on exertion
    Faint glow in heart tissue
    Failed temperature regulation
    Waxy pale skin
    Irregular shallow breath
    Persistent confusion
    Cascading organ shutdown
    Spore blooms visible under skin
    Thready fading pulse
    Long unresponsive periods
    Whispered breathing
    Cold, hollow limbs
    Soft delirium
    Final stillness as spores settle
```