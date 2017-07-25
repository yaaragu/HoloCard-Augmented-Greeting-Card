# HoloCard-Augmented-Greeting-Card
This is a fun augmented addition for a birthday greeting card. The app, once sees the back of the greeting card, triggers an additional secret massage that shows "on top of the card" - a playing puppy with a "Happy Birthday Arie" note.

This Demo was built on Unity using Vofuria SDK. It was built for Android (therefore requirs Java and Android Studio / SDK as well).

In this folder you can find:
- a demo app for android
- the example image targer for the app
- this setp by step guide to build the app

--

If you wish to create a card as well, here is a step by step process:
Download latest Vuforia package for Unity (Vuforia package only builds for Android & IoS apps).
Open a new unity project, delete the main camera from the scene, and save the new project and scene.

Install vuforia package and add VR Camera from the vuforia SDK.
Go to https://developer.vuforia.com/targetmanager/licenseManager/licenseListing and get access key to add to the Vufuria ARCamera 
Change world center mode to device tracking.
Add the desired Image Target and upload the Image Target wanted to vuforia  (the back of the greeting card), download in unity format, and import to assets.

ARCamera > Click load Image Target & Activate.
Add a Image Target Gameobject (Prefab) as a child and change the Image Target Behaviour (Database and Image Target) accordingly 
Find the image target asset and change it’s texture type to “Spirte (2D & UI)” >save > if it doesnt work add the original photo file to the project asset folder.

Create Plane, make it the same size as the image target, and add to it a ground texture (if you want) GPJ. Child of it to Image Target.

Add the character you want (asset), for example a puppy, and child it to image target.
Add text 3D (asset), for example "Happpy Birthday, You!".
Test.

Build Android App: 
Go to Unity Preferences > External tools > Android (make sure to set the path to SDK, JDK).
Go to Build Settings > Select Android > switch platform
Go to Player settings > Set company name (e.g. Com.AugmentMyCard.Android.DemoCard) and Name of the demo (e.g. DemoBDayCard).
Go to Other Settings > Bundle identifier = same as company name (e.g. Com.AugmentMyCard.Android.DemoCard)
Go to Publish settings > Select create new keystore and set it + password (important to remember). Go again to Key > select the key created and add password.
Save > Build > Build APK (set name).


--

Other guides that can be use as reference:
http://programminghistorian.org/lessons/intro-to-augmented-reality-with-unity 
https://www.youtube.com/watch?v=Fgd21lbhikU&t=867s 
