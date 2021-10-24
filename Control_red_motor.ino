//Código para el Control de la red de difracción del Monocromador
int ledTest = 13;
//
// Include the Stepper library:
#include <Stepper.h>

// Define number of steps per revolution:
const int stepsPerRevolution = 64; //Steps per revolution for 28-BYJ48 stepper motor

// Initialize the stepper library on pins 8 through 11:
Stepper myStepper = Stepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  //apagar led 13
  pinMode(ledTest, OUTPUT);
  digitalWrite(ledTest, LOW);
  //open up the serial port 
  Serial.begin(115200);
  // Set the motor speed (RPMs):
  myStepper.setSpeed(100);
}

void loop() {

  while (Serial.available() > 0) {
    
    int steps = Serial.parseInt();
    delay(500);
    Serial.write(steps);
    //Serial.print(steps);
    myStepper.step(steps);
    }

}
