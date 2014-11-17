#ifndef _MESSAGE_HANDER_H_
#define _MESSAGE_HANDER_H_
#include <MsgReceiver.h>
#include "SystemState.h"
#if defined(ARDUINO) && ARDUINO >= 100
 #include "Arduino.h"
#else
 #include "WProgram.h"
#endif 

class MessageHandler : public MsgReceiver {

  public:
    void processMsg();

  private:
    void msgSwitchYard();
    void handleGetMeasurements();

};

extern MessageHandler messageHandler;
#endif

