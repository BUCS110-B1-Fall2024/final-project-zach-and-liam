Zach and Liam: Retro Snake Like Game
## CS110 B1 Final Project  << Semester, Year >>
Semester 1, 2024

## Team Members

Zach Serio, Liam Fowler

***

## Project Description

We Plan To Make A Game Similar To The Snake Game Where The Snake Has To Eat Objects To Grow In Size 
Without Touching The Border Or Part Of Itself. But, We Plan To Add A Twist In The Form Of Powerups 
By Something Specific Happening And Potentially More.

***    

## GUI Design

### Initial Design

![initial gui](CS110_Final_GUI_Draft.png)

### Final Design

![final gui] (FinalGUI.png)

## Program Design

### Features

1. Snake Will Move Constantly
2. Snake Will Increase In Size After Eating An Object
3. Game Will End With Border/Other Snake Part Contact
4. Fruit Will Randomly Spawn At A New Spot When Eaten
5. Powerups Will Happen At Specific Scores If You Reach Them (More Will Be Added Later)

### Classes

1. Snake: Creates Starting Snake
2. Eatable Object: Creates Object At A Random Location


## ATP

TEST 1: Verifying Snake Movement
GOAL: Verify Snake Moves Based On Arrow Key Pressed
STEPS: Start The Game, Press Up Key, Snake Moves Up For Example
EXPECTED OUTCOME: Snake Continuously Moves Up Until Told Otherwise

TEST 2: Verifying Out-Of-Bounds
GOAL: Verify Game Ends When The Snake Hits A Boundary
STEPS: Start The Game, Go To A Boundary With The Previously Mentioned Arrow Keys
EXPECTED OUTCOME: Game Will End Once The Snake Hits A Side Of The Screen

TEST 3: Verifying Random Fruit Placement
GOAL: Verify Fruit Moves To A Random Position After Claimed
STEPS: Start The Game, Collect A Fruit At A Set Position, Fruit Moves To Another Random Position
EXPECTED OUTCOME: Fruit Moves When Collected

TEST 4: Score
GOAL: Add Score Feature Each Time A Fruit Is Collected
STEPS: Start The Game, Collect A Fruit, Score Increases
EXPECTED: Score (Shown Or Not At The Moment) Increases When A Fruit Is Claimed
PLEASE NOTE: This Feature Works Completely On Some Computers But Not Fully On Others. We Are Still Figuring Out Why This Occurs.

TEST 5: Verifying Snake Addition
GOAL: Add 1 Rectangle To The End Of The Snake When A Fruit Is Consumed
STEPS: Start Game, Collect A Fruit, Add Rectangle
EXPECTED OUTCOME: Length Of Snake Will Increase By 1 When A Fruit Is Consumed

TEST 6: Verifying Snake Contact
GOAL: Game Will End If Contact Is Made With Snake
STEPS: Start Game, Grow To A Big Length, Hit Another Part Of The Snake
EXPECTED OUTCOME: When You Hit Another Part Of The Snake The Game Ends

TEST 7: Powerup 1 - 10s
GOAL: When You Get To A Score Of 10, You Get An Extra Point And Snake Length For Free
STEPS: Start Game, Get To 10
EXPECTED: When You Get To A Score Of 10, Score and Snake Length Automatically Increase By 1
FUTURE GOAL: Make More Powerups and Add Menu To Choose Between Them

TEST 8: Game Over Screen
GOAL: When The Game Ends, A Game Over Screen With Your Score Appears
STEPS: Play Game
EXPECTED OUTCOME: Blank Screen With Game Over Message And Score Appears When The Game Ends


