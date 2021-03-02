# Personal FHICT Repo

## Welcome

I'd like to welcome you to my personal FHICT repo. This repo is meant for sharing code I've created during my school career. Feel free to take a look, or try some scripts that I've created.

## FHICT

If you're wondering what FHICT actually stands for, let me explain. FH stands for "Fontys Hogescholen" and ICT stands for "Information & Communication Technology". Fontys is the place I'm currently studying at, which is located in Eindhoven, the Netherlands. ICT is the bachelor's degree in IT in my country.

## About Me

Nothing here yet...

## Flowchart Demo

This is a test!
```mermaid
graph LR
A(Start)
B{RB = pressed?}
B1[Display msg]
B2[P1 makes choise]
B3[CPU makes choise]
C(End)
C1{Is P1 = CPU?}
C2[Tie]
D{P1 = Rock?}
D1{P1 = Paper?}
D2{P1 = Scissors?}
E{CPU = Paper?}
E1{CPU = Scissors?}
E2{CPU = Rock?}
F(P1 Wins)
F1(CPU Wins)
A --> B
B -->|NO| B1
B -->|YES| B2
B1 --> C
B2 --> B3
B3 --> C1
C1 -->|YES| C2
C2 --> C
C1 -->|NO| D
D -->|YES| E
D -->|NO| D1
E -->|YES| F1
E -->|NO| F
D1 -->|YES| E1
D1 -->|NO| D2
D2 -->|NO| B1
E1 -->|YES| F1
E1 -->|NO| F
F --> C
F1 --> C
D2 -->|YES| E2
E2 -->|YES| F
E2 -->|NO| F1
```

## Sources
