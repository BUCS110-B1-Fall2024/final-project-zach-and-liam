Zach and Liam: Snake Like Game
## CS110 B1 Final Project  << Semester, Year >>
Semester 1, 2024

## Team Members

Zach Serio, Liam Fowler

***

## Project Description

We Plan To Make A Game Similar To The Snake Game Where The Snake Has To Eat Objects To Grow In Size 
Without Touching The Border Or Part Of Itself. But, We Plan To Add A Twist In The Form Of Powerups 
By Pressing A Button And Potentially More

***    

## GUI Design

### Initial Design

![initial gui](CS110_Final_GUI_Draft.png)

### Final Design

![final gui] Do Not Have At The Current Moment

## Program Design

### Features

1. Snake Will Move Constantly
2. Snake Will Increase In Size After Eating An Object
3. Game Will End With Border/Other Snake Part Contact
4. Object Will Randomly Spawn At A New Spot When Eaten
5. Powerups Can Be Used By Pressing A Specific/Unqiue Button After A Certain Score Is Reached

### Classes

1. Snake: Creates Starting Snake
2. Eatable Object: Creates Object At A Random Location

3. Controller: Holds Main Program Contents 
4. Handle Events: Assigns Button Presses To Snake Movement
5. Update Models: Contains All Game Aspects, Like Out-Of-Bounds Movement
6. Draw: Draws Rectangle
7. Writing: Writes Things Such As Score On The Screen
8. Main Loop: Runs All Previous Classes

## ATP

Test 1: Verifying Snake Movement
Goal: Verify Snake Moves Based On Arrow Key Pressed
Steps: Start The Game, Press Up Key, Snake Moves Up
Expected Outcome: Snake Continuously Moves Up Until Told Otherwise

Test 2: Verifying Out-Of-Bounds
Goal: Verify Game Ends When The Snake Hits A Boundary
Steps: Start The Game, Go To A Boundary With The Previously Mentioned Arrow Keys
Expected Outcome: Game Will End Once The Snake Hits A Side Of The Screen

Test 3: Verifying Random Fruit Placement
Goal: Verify Fruit Moves To A Random Position After Claimed
Steps: Start The Game, Collect A Fruit, Fruit Moves To Another Random Position
Expected Outcome: Fruit Moves When Collected

Test 4: Score
Goal: Add Score Feature Each Time A Fruit Is Collected
Steps: Start The Game, Collect A Fruit, Score Increases
Expected Outcome: Score (Shown Or Not At The Moment) Increases When A Fruit Is Claimed

Test 5: Verifying Snake Contact 
Goal: Verify Snake Indeed Collides With Fruit
Steps: Start The Game, Collect A Fruit, See If Collision Happens
Expected Outcome: When A Fruit Is Collected, A Collision Successfully Occurs
