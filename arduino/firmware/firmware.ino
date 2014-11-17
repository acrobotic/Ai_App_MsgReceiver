#include <MsgReceiver.h>
#include "MessageHandler.h"

void setup() {
  systemState.initialize();
}

void loop() { 
  messageHandler.processMsg(); 
}
