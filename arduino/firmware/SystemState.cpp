#include "SystemState.h"

SystemState::SystemState()
{
}

void SystemState::initialize() 
{
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}

SystemState systemState;
