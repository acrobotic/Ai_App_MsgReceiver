#ifndef _SYSTEM_STATE_H_
#define _SYSTEM_STATE_H_
#if defined(ARDUINO) && ARDUINO >= 100 
 #include "Arduino.h"
#else
 #include "WProgram.h"
#endif

class SystemState {

    public:
        SystemState();
        void initialize();
};

extern SystemState systemState;

#endif
