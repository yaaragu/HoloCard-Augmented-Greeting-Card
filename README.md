# HoloCard-Augmented-Greeting-Card
Augmented Greeting Card App

Create a project
Download latest Vuforia package for Unity 
** Vuforia package only builds for Android & IoS apps
Open a unity (latest version), create a project, delete main camera, and install package 
In the new project and scene
Add VR Camera
Go to https://developer.vuforia.com/targetmanager/licenseManager/licenseListing and get access key to add to the Vufuria ARCamera 
Change world center mode > device tracking 
Add Image Target 
Upload the Image Target wanted, download in unity format, import to assets
ARCamera > Click load Image Target & Activate 
Add a Image Target Gameobject (Prefab) as a child and change the Image Target Behaviour (Database and Image Target) accordingly 
Find the image target asset and change it’s texture type to “Spirte (2D & UI)” >save > if it doesnt work add the original photo file to the project asset folder
Create Plain
Make a plane in the same size as the image target 
add to it a ground texture (if you want) GPJ
child of it to Image Target
Add character (asset)
 Child it to image target
Add text 3D (asset)
test

Build Android App locally 
Unity Preferences 
External tools - Android (make sure to set the path to SDK, JDK) 
Build Settings 
Select Android > switch platform
 Player settings: 
Set company name (e.g. Com.AugmentMyCard.Android.DemoCard)
Name of the demo (e.g. DemoBDayCard)
Other Settings
Bundle identifier = same as company name (e.g. Com.AugmentMyCard.Android.DemoCard)
Publish settings 
Select create new keystore and set it + password (important to remember)
Key > select the key created and add password
save
Build
Build APK (set name)

--
Other guides that can be use as reference:
http://programminghistorian.org/lessons/intro-to-augmented-reality-with-unity 
https://www.youtube.com/watch?v=Fgd21lbhikU&t=867s 
