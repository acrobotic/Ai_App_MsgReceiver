#include "Streaming.h"
#include "MessageHandler.h"

enum 
{
  cmdGetMeasurements,              // Done
};

const int rspSuccess = 1;
const int rspError = 0;

void MessageHandler::processMsg() 
{
  while (Serial.available() > 0)  
  {
    process(Serial.read());
    if (messageReady()) 
    {   
        msgSwitchYard();
        reset();
    }   
  }
  return;
}

void MessageHandler::msgSwitchYard()
{
  int cmd = readInt(0);

  switch (cmd)
  {
    case cmdGetMeasurements:
      handleGetMeasurements();
      break;

    default:
      break;
  }
}

void MessageHandler::handleGetMeasurements()
{
    Serial << '[' << rspSuccess;
    Serial << ',' << analogRead(A0); // Power
    Serial << ',' << analogRead(A1); // Battery
    Serial << ']' << endl;

//    dtostre(colorimeter.transmission.red, valueStr, DBL_PREC, 0);


}

MessageHandler messageHandler;
