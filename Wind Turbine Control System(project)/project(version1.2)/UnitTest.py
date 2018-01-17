from numpy import*
import OpenFile
import Parameter
import Formula
import CompileBlock

OpenFile.ReadWindSpeepData()
OpenFile.ReadData_ThreePhaseShortCircuit()
OpenFile.ReadData_MaxPower()
OpenFile.ReadData_MaxTorqueCurrent()


#==============================================================================
# print("number",size(Parameter.TimeSeries))
# print("TimeSeries")
# print(Parameter.TimeSeries)
# print("WindSpeed")
# print(Parameter.WindSpeed)
#==============================================================================

#==============================================================================
# for i in range(15):
#     Cp=Formula.getApproximation(i, Parameter.WindSpeed_MaxPower ,Parameter.Cp_MaxPower)
#     print(Cp)
#==============================================================================
    
for i in range(3):
    print("3phase")
    speed, pwm, power = Formula.Mode_ThreePhaseShortCircuit()
    print("speed",speed,"pwm",pwm,"power",power)
    Parameter.CurrentTime += 1
    
#speed, rpm, power = CompileBlock.evalDecision("Mode_ThreePhaseShortCircuit")    
#==============================================================================
# Parameter.RPM[0]=100
# Parameter.CurrentTime += 1
# for i in range(500):
#     print("Maxpower")
#     speed, pwm, power = Formula.Mode_MaxPower()
#     print("speed",speed,"pwm",pwm,"power",power)
#     Parameter.CurrentTime += 1
#==============================================================================

#==============================================================================
# for i in range(200):
#     speed, pwm, power = Formula.Mode_MaxTorqueCurrent()
#     print("speed",speed,"pwm",pwm,"power",power)
#     Parameter.CurrentTime += 1
# 
# sum = 0   
# Parameter.RPM[0]=100
#        
# for i in range(1000):
#     speed, pwm, power = Formula.MaxTorqueCurrent_MagBrake()
#     #print("speed",speed,"pwm",pwm,"power",power)
#     Parameter.CurrentTime += 1
#     if Parameter.RPM[i] < Parameter.RPM[i-1]:
#         sum += 1
# print("sum",sum)
# sum = 0
# Parameter.RPM[0]=100000
# for i in range(len(Parameter.TimeSeries)-1):
#     speed, pwm, power = Formula.Mode_ThreePhaseShortCircuit_MagBrake()
#     if Formula.check_RPM_Increase():
#         sum += 1
#     #print("speed",speed,"pwm",pwm,"power",power)
#     Parameter.CurrentTime += 1
# print("sum",sum)
#==============================================================================
#==============================================================================
# Parameter.RPM[0]=100
# Tsr = Formula.TSR()
# print("Tsr",Tsr)
# Cp = Formula.Cp_MaxTorqueCurrent(Tsr)
# print("Cp",Cp)
# TorqueBlade = Formula.TB(Cp)
# print("Tb",TorqueBlade)
# TorqueGeneration = Parameter.TorqueGeneration_MaxTorqueCurrent
# print("TorqueGeneration",TorqueGeneration)
# Tt = Formula.TotalateTorque(TorqueBlade, TorqueGeneration, Parameter.TorqueMachine)
# print("Tt",Tt)
# rpm=Formula.CalculateRPM(Tt)
# print("rpm",rpm)
# eff_g = Parameter.eff_g_MaxTorqueCurrent
# eff_e = Parameter.eff_e_MaxTorqueCurrent
# print("eff_g", eff_g, "eff_e", eff_e)
# power = Formula.CalculatePower(eff_g, eff_e, Tt)
# print("power",power)
# print("Current",Parameter.CurrentTime)
#==============================================================================
#==============================================================================
# 
# # Moae_ThreePhaseShortCircuit()
# i=0
# Cp = Formula.Cp_ThreePhaseShortCircuit(i)
# 
#     
# Tg = Tg = Formula.getApproximation(i, Parameter.RPM_ThreePhaseShortCircuit, Parameter.Tg_ThreePhaseShortCircuit)
#   
#     
# effg = Formula.getApproximation(i, Parameter.WindSpeed_ThreePhaseShortCircuit, Parameter.eff_g_ThreePhaseShortCircuit)
#    
# effe = Formula.getApproximation(i, Parameter.WindSpeed_ThreePhaseShortCircuit, Parameter.eff_e_ThreePhaseShortCircuit)
#    
# 
# print(Cp, Tg, effg, effe)
#    
#==============================================================================




