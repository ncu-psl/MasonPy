C**********************************************************************
C	OPTIMAL CONTROL CODE FOR WIND TURBINE
C     TIME ~ WIND SPEED : 1 DATA PER 1 SECOND (IMPORTANT)
C**********************************************************************
C     DIMENSION SIZE
	PARAMETER (N1=4000,N3=50,PI=3.14159,THO=1.225)
C     TIME STEP & INITIAL TIME CHECKING SETUP
C     20.08=20+0.08(電磁剎車時間)
	PARAMETER (ISTEP=100,NTIM=200,TIM2=20.08)

	DIMENSION T(N1),V(N1)
	COMMON /COM2/ CP(N3),TSR(N3)
	COMMON /COM3/ RPM5(N3),Q5(N3)
	COMMON /COM4/ RPM6(N3),Q6(N3),CURT(N3)
	COMMON /COEF/ NN1,NN3,NN5,NN6
      COMMON /ROTRO/ RPM,CI
	COMMON /INDEX/ IP
	COMMON /CTIME/ T2,T4
	
	


C----------------------------------------------------------------------	
	OPEN(1,FILE='1SPEED.TXT',STATUS='OLD')
	NN1=1
11	READ(1,*,END=10) T(NN1),V(NN1)
	NN1=NN1+1
	GO TO 11
10    REWIND(1)	
	NN1=NN1-1
C----------------------------------------------------------------------

C----------------------------------------------------------------------
	OPEN(2,FILE='2INFO.TXT',STATUS='OLD')
      READ(2,*) DIA
      READ(2,*) BI
      READ(2,*) TM3,RPM83
      READ(2,*) TMG,CIMAX
      READ(2,*) OUTRPM,OUTP
      READ(2,*) GPER,EPER
C----------------------------------------------------------------------      

C----------------------------------------------------------------------
	OPEN(3,FILE='3CP-TSR.TXT',STATUS='OLD')
	NN3=1
13	READ(3,*,END=30) TSR(NN3),CP(NN3)
	NN3=NN3+1
	GO TO 13
30    REWIND(3)	
	NN3=NN3-1
C----------------------------------------------------------------------

C----------------------------------------------------------------------
	OPEN(4,FILE='4MAG.TXT',STATUS='OLD')
	READ(4,*) T44,TMAG
C----------------------------------------------------------------------

C----------------------------------------------------------------------
	OPEN(5,FILE='5PHASE.TXT',STATUS='OLD')
	NN5=1
15	READ(5,*,END=50) RPM5(NN5),Q5(NN5)
	NN5=NN5+1
	GO TO 15
50    REWIND(5)	
	NN5=NN5-1
C----------------------------------------------------------------------

C----------------------------------------------------------------------
	OPEN(6,FILE='6BandG.TXT',STATUS='OLD')
	NN6=1
16	READ(6,*,END=60) RPM6(NN6),Q6(NN6),CURT(NN6)
	NN6=NN6+1
	GO TO 16
60    REWIND(6)	
	NN6=NN6-1
C----------------------------------------------------------------------

C----------------------------------------------------------------------
	OPEN(7,FILE='7OUT.TXT',STATUS='UNKNOWN')
	RPM=0.0001
	TMP1=2.*PI*DIA/2./60.
	TMP2=2.*PI/0.5/THO/(PI*DIA*DIA/4.)


C	THE FIRST TIME STEP
C#######################################################################
	I=1
	  DT=(T(I+1)-T(I))/ISTEP
        DV=(V(I+1)-V(I))/ISTEP
      J=0
        TIME=DT*J+T(I)
        VEL =DV*J+V(I)
        TMPTSR=TMP1*RPM/VEL
        CALL C1(TG,TM,TIME) 
	 
	    CALL CSIEZ (NN3,TSR,CP,1, TMPTSR, TCP)
	    IF(TMPTSR.LE.TSR(2)) THEN
            TCP=(CP(2)-CP(1))/(TSR(2)-TSR(1))*(TMPTSR-TSR(1))+CP(1)
          ENDIF     
          TB=TCP/TMP2*(VEL**3)/(RPM/60.)
          RPM=RPM+((TB-TG-TM)/BI*DT)*30./PI
	    POWER=2.*PI*(RPM/60.)*TB*GPER*EPER
C#######################################################################
	IP1=0
	DO I=1,NN1-1
	  DT=(T(I+1)-T(I))/ISTEP
        DV=(V(I+1)-V(I))/ISTEP

        DO J=1,ISTEP
          TIME=DT*J+T(I)
          VEL =DV*J+V(I)
          TMPTSR=TMP1*RPM/VEL
C     IP=1       
	    IF(IP.EQ.1) THEN
      	  IF(RPM.GT.TM3) THEN
	        IP1=0
			CALL C4(TMG,TMAG,TG,TM,TIME,T44,CIMAX)
              GO TO 71 
            ENDIF
		  IF(RPM.LE.TM3 .AND. RPM.GT.RPM83) THEN
		    IP1=0
		  ENDIF	      
		  IF(RPM.LE.RPM83) THEN
		    IP1=IP1+1
		  ENDIF
	      IF(IP1.EQ.NTIM) THEN
		    IP1=0
	        CALL C5(TG,TM,TIME)
	        GO TO 71
		  ENDIF		  
   	      CALL C1(TG,TM,TIME)
            GO TO 71 
      	ENDIF

          
C	IP=2
          IF(IP.EQ.2) THEN
	      IF((TIME-T2).LE.TIM2) THEN
	        CALL C2(TMAG,TG,TM,TIME,T44)
	        GO TO 71
            ENDIF
            CALL C1(TG,TM,TIME)
            GO TO 71
      	ENDIF

C	IP=3
C     CALL C3 前須定意 RPMTMP=RPM
          IF(IP.EQ.3) THEN
	      IF(RPM.GT.TM3) THEN
	        IF((RPM-RPMTMP).LT.0) THEN
	          RPMTMP=RPM
	          CALL C3(TMG,TG,TM,TIME,CIMAX)
                GO TO 71
		    ENDIF 
	        CALL C4(TMG,TMAG,TG,TM,TIME,T44,CIMAX)
              GO TO 71
            ENDIF
	      CALL C1(TG,TM,TIME)
	      GO TO 71
		ENDIF


C	IP=4
          IF(IP.EQ.4) THEN
            IF(RPM.LT.TM3) THEN
		    CALL C2(TMAG,TG,TM,TIME,T44)
			GO TO 71
		  ENDIF
		  CALL C4(TMG,TMAG,TG,TM,TIME,T44,CIMAX)	 
		  GO TO 71
          ENDIF


C	IP=5
          IF(IP.EQ.5) THEN
	      IF(RPM.GT.OUTRPM .OR. POWER.GT.OUTP) THEN
              RPMTMP=RPM
	        CALL C3(TMG,TG,TM,TIME,CIMAX)
              GO TO 71	        
            ENDIF
            CALL C5(TG,TM,TIME)
            GO TO 71
          ENDIF

71        CALL CSIEZ (NN3,TSR,CP,1, TMPTSR, TCP)
	    IF(TMPTSR.LE.TSR(2)) THEN
            TCP=(CP(2)-CP(1))/(TSR(2)-TSR(1))*(TMPTSR-TSR(1))+CP(1)
          ENDIF     
          TB=TCP/TMP2*(VEL**3)/(RPM/60.)
          RPM=RPM+((TB-TG-TM)/BI*DT)*30./PI
	    IF(RPM.LE.0) RPM=0.0001
	    POWER=2.*PI*(RPM/60.)*TG*GPER*EPER
	    IF(IP.EQ.1) POWER=0.
	    IF(IP.EQ.2) POWER=0.

CCC          WRITE(7,72) TIME,RPM,TB,TG,TCP,VEL,TMPTSR,IP
CCC	       WRITE(7,*) TIME,RPM,TB,TCP,TMPTSR
	       WRITE(7,73) TIME,RPM,VEL,POWER,CI,IP


72	    FORMAT(F11.2,2X,6(F10.5,2X),I3)
73	    FORMAT(F11.2,2X,4(F10.5,2X),I3)	 
	  ENDDO
      ENDDO

      END




C     THREE PHASE SHORT
	SUBROUTINE C1(TG,TM,TIME)
	PARAMETER (N1=4000,N3=50,PI=3.14159,THO=1.225)
	COMMON /COM3/ RPM5(N3),Q5(N3)
	COMMON /COEF/ NN1,NN3,NN5,NN6
      COMMON /ROTRO/ RPM,CI
	COMMON /INDEX/ IP
	COMMON /CTIME/ T2,T4
      CALL CSIEZ (NN5,RPM5,Q5,1, RPM, TG)
	IF(RPM.LE.RPM5(2)) THEN
        TG=(Q5(2)-Q5(1))/(RPM5(2)-RPM5(1))*(RPM-RPM5(1))+Q5(1)
      ENDIF  
      TM=0.
	CI=0.
	IP=1
 	T2=TIME
      T4=TIME
 	RETURN
	END


C     THREE PHASE SHORT + MAG. BRAKE
	SUBROUTINE C2(TMAG,TG,TM,TIME,T44)
	PARAMETER (N1=4000,N3=50,PI=3.14159,THO=1.225)
	COMMON /COM3/ RPM5(N3),Q5(N3)
	COMMON /COEF/ NN1,NN3,NN5,NN6
      COMMON /ROTRO/ RPM,CI
	COMMON /INDEX/ IP
	COMMON /CTIME/ T2,T4
      CALL CSIEZ (NN5,RPM5,Q5,1, RPM, TG)
	IF(RPM.LE.RPM5(2)) THEN
        TG=(Q5(2)-Q5(1))/(RPM5(2)-RPM5(1))*(RPM-RPM5(1))+Q5(1)
      ENDIF 
	TM=0.
	CI=0.
 	IF((TIME-T2).GE.T44) TM=TMAG
 	IP=2
      T4=TIME
	RETURN
	END
	


C     MAG. CURRENT
	SUBROUTINE C3(TMG,TG,TM,TIME,CIMAX)
	COMMON /INDEX/ IP
	COMMON /CTIME/ T2,T4
      COMMON /ROTRO/ RPM,CI
      TG=TMG
      TM=0.
	IP=3
	T2=TIME
	T4=TIME
	CI=CIMAX
 	RETURN
	END


C     MAG. CURRENT + MAG. BRAKE
	SUBROUTINE C4(TMG,TMAG,TG,TM,TIME,T44,CIMAX)
	COMMON /INDEX/ IP
	COMMON /CTIME/ T2,T4
      COMMON /ROTRO/ RPM,CI
      TG=TMG
      TM=0.
	IP=4
	T2=TIME
	IF((TIME-T4).GE.T44) TM=TMAG
	CI=CIMAX
	RETURN
	END	

	
C     MAX. POWER
	SUBROUTINE C5(TG,TM,TIME)
	PARAMETER (N1=4000,N3=50,PI=3.14159,THO=1.225)
	COMMON /COM4/ RPM6(N3),Q6(N3),CURT(N3)
	COMMON /COEF/ NN1,NN3,NN5,NN6
      COMMON /ROTRO/ RPM,CI
	COMMON /INDEX/ IP
	COMMON /CTIME/ T2,T4
      CALL CSIEZ (NN6,RPM6,Q6,1, RPM, TG)
      CALL CSIEZ (NN6,RPM6,CURT,1, RPM, CI)
	IF(RPM.LE.RPM6(1)) THEN
        TG=(Q6(1)-0.)/(RPM6(1)-0.)*(RPM-0.)+0.
      ENDIF 
 	IF(RPM.LE.RPM6(1)) THEN
        CI=(CURT(1)-0.)/(RPM6(1)-0.)*(RPM-0.)+0.
      ENDIF
      TM=0.
	IP=5
 	T2=TIME
	T4=TIME
	RETURN
	END		