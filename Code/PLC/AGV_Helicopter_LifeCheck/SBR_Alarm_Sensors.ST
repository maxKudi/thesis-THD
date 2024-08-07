AutoShop            2.4  5.03                                                                                                           ��  CLVTItem              �             �             �             ��// Scada Information Mapping

// Motor Mapping
// AGV Motion Supervision
IF MM1_status THEN
	motorData[0] := TRUE;
ELSE
	motorData[0] := FALSE;
END_IF;

IF MM2_status THEN
	motorData[1] := TRUE;
ELSE
	motorData[1] := FALSE;
END_IF;

IF MM3_status THEN
	motorData[2] := TRUE;
ELSE
	motorData[2] := FALSE;
END_IF;

IF MM4_status THEN
	motorData[3] := TRUE;
ELSE
	motorData[3] := FALSE;
END_IF;

// Gripper Motion Supervision
IF GM1_status THEN
	motorData[4] := TRUE;
ELSE
	motorData[4] := FALSE;
END_IF;

IF GM2_status THEN
	motorData[5] := TRUE;
ELSE
	motorData[5] := FALSE;
END_IF;

IF GM3_status THEN
	motorData[6] := TRUE;
ELSE
	motorData[6] := FALSE;
END_IF;

IF GM4_status THEN
	motorData[7] := TRUE;
ELSE
	motorData[7] := FALSE;
END_IF;


// Gripper Arm Stepper Motor Supervision
IF SG1_status THEN
	motorData[8] := TRUE;
ELSE
	motorData[8] := FALSE;
END_IF;

IF SG2_status THEN
	motorData[9] := TRUE;
ELSE
	motorData[9] := FALSE;
END_IF;

IF SG3_status THEN
	motorData[10] := TRUE;
ELSE
	motorData[10] := FALSE;
END_IF;

IF SG4_status THEN
	motorData[11] := TRUE;
ELSE
	motorData[11] := FALSE;
END_IF;

// LiftUP and LiftDOWN Supervision
IF Lift_MotorUP THEN
	motorData[12] := TRUE;
ELSE
	motorData[12] := FALSE;
END_IF;

IF Lift_MotorDOWN THEN
	motorData[13] := TRUE;
ELSE
	motorData[13] := FALSE;
END_IF;

// Digital Sensor Mapping

// Arm Retracted Supervision
IF SeRVLS1 THEN
	digitalSensorData[0] := TRUE; 
ELSE
	digitalSensorData[0] := FALSE; 
END_IF;

IF SeRVLS2 THEN
	digitalSensorData[1] := TRUE; 
ELSE
	digitalSensorData[1] := FALSE; 
END_IF;

IF SeRVLS3 THEN
	digitalSensorData[2] := TRUE; 
ELSE
	digitalSensorData[2] := FALSE; 
END_IF;

IF SeRVLS4 THEN
	digitalSensorData[3] := TRUE; 
ELSE
	digitalSensorData[3] := FALSE; 
END_IF;

// Arm Extended Supervision
IF SeFWLS1 THEN
	digitalSensorData[4] := TRUE; 
ELSE
	digitalSensorData[4] := FALSE; 
END_IF;

IF SeFWLS2 THEN
	digitalSensorData[5] := TRUE; 
ELSE
	digitalSensorData[5] := FALSE; 
END_IF;

IF SeFWLS3 THEN
	digitalSensorData[6] := TRUE; 
ELSE
	digitalSensorData[6] := FALSE; 
END_IF;

IF SeFWLS4 THEN
	digitalSensorData[7] := TRUE; 
ELSE
	digitalSensorData[7] := FALSE; 
END_IF;


// Gripper Open Supervision
IF SeGPOP1 THEN
	digitalSensorData[8] := TRUE; 
ELSE
	digitalSensorData[8] := FALSE; 
END_IF;

IF SeGPOP2 THEN
	digitalSensorData[9] := TRUE; 
ELSE
	digitalSensorData[9] := FALSE; 
END_IF;

IF SeGPOP3 THEN
	digitalSensorData[10] := TRUE; 
ELSE
	digitalSensorData[10] := FALSE; 
END_IF;

IF SeGPOP4 THEN
	digitalSensorData[11] := TRUE; 
ELSE
	digitalSensorData[11] := FALSE; 
END_IF;


// Analog Sensor Mapping

// Pipe Center location sensor Supervision
IF actualSensorValueK5 > 0 THEN
	analogSensorData[0] := TRUE; 
ELSE
	analogSensorData[0] := FALSE; 
END_IF;

IF actualSensorValueK6 > 0 THEN
	analogSensorData[1] := TRUE; 
ELSE
	analogSensorData[1] := FALSE; 
END_IF;

IF actualSensorValueK7 > 0 THEN
	analogSensorData[2] := TRUE; 
ELSE
	analogSensorData[2] := FALSE; 
END_IF;

IF actualSensorValueK8 > 0 THEN
	analogSensorData[3] := TRUE; 
ELSE
	analogSensorData[3] := FALSE; 
END_IF;

// Lift Operation Limit Supervision
IF SeLICO1 > 0 OR SeLICO2 > 0  THEN
	analogSensorData[4] := TRUE; 
ELSE
	analogSensorData[4] := FALSE; 
END_IF;
    