#########################################################
 	     Bacchetti Enrico, Lingua Marco, Shiuan-Su Wei        
                  MAFINRISK 2021-2022  									                                             
        	Numerical Methods 2nd assignment                     
            	professor: Gianluca Fusai                                                                                                                         
########################################################

A) Who did what: 
    
    Bacchetti and Lingua jointly worked on the same tasks for the whole
    duration of the project, mainly by assessing tasks simultaneously (in presence or Teams meetings by screen sharing). This, in our 
    opinion, is the best way to jointly work on numerical tasks as everyone is able to follow the whole procedure and and can contribute
    actively to the work.
    After carefully framing and discussing the various issues, many improvements have been made by trial-and-error procedures. 
    VBA macros have been manually programmed "by four hands" since they did not have any experience with VBA.
    
    Shiuan-Su provided useful readings on the topics, curated the formatting of the files and constantly checked the English grammar and 
    syntax. She was involved also in the operational work, proving the comments related to how the parameters of the SABR model do
    affect the IV smile.
    

B) What’s in this folder: reader can find 

    - A PDF file named "NM 2nd assignment_Task1_Bacchetti_Lingua_ShiuanSu", which contains the report concerning the first point of
    the assignment (SABR calibration and MC pricing).
    - A .zip folder named "NM 2nd assignment_Task1_Bacchetti_Lingua_ShiuanSu", which contains the original LaTex file (figures included).
    - A .xlsm spreadsheet, named "NM 2nd assignment_Task1_Bacchetti_Lingua_ShiuanSu.xlsm" in which all the major computations needed to 
    address the task have been carried out.
    - A .xlsx spreadsheet, named "dataset.xlsx", is the original dataset on which results
    have been computed and presented (TESLA options quotes @closing price of 29th march, 2022).
    - A .py code, named "Aux code.py" is needed to download datasets from Yahoo and to compute implied volatilities
    with both Newton-Raphson and Bisection methods.
    - This .txt file.
    
C) How to use the spreadsheet to verify our work

    - Open spreadsheet ".xlsm", go to sheet "SABR Calibration", push button "2) Optimize" and 
      wait until the pop-up with the runtime is printed on the screen.
    - Go to "Scenario Analysis" to check the what-if investigation.       
    - Go to "OptionPricing", set a number of simulations and push-button "Compute Price". 
      
      NOTE: it may happen that this macro returns an error, often regarding the "NormSInv" function,
      especially when selecting a big number of simulations (>10000): click "end" on the warning window 
      and re-run the macro. If the problem still occurs, try again: the VBA code seems to struggle a bit
      when dealing with a such number of simulations. 
      
      Wait until calculations are done and click "ok" on the runtime pop-up.
      
      NSim is initialized on 100: we suggest starting with this value and progressively increasing it.
      
      Options price and accuracy measures are reported on the left cells in the sheet, above the histogram
      table.
      
      F(t) and a(t) (in the respective sheet) are automatically plotted by VBA, histogram has to be manually adjusted.

D) How to use the spreadsheet with other datasets: 
        

      - run the .py script, insert a ticker in line 143, release line 146 and run the whole code.
        Eventually, adjust limits for openInterest or add some more filters to variables.
        
      - copy and paste the dataset exported from the .xlsx file into the spreadsheet ".xlsm"
        
        NOTE: This sheet is built to auto-adjust based on the selected maturity. Just pick one in
        the upper right panel (sheet "Dataset"). Also, the risk-free rate is automatically interpolated,
        and only OTM options are selected. 
        
      - Go to sheet "SABR Calibration", push the button "2) Optimize" and 
        wait until the pop-up with the runtime is printed on the screen (graph has to be manually adjusted).
        
      - Go to "OptionPricing", set a number of simulations and push-button "Compute Price" (see notes in point C)
      

We tried to do our best in order to create a dynamic and self-adjusting environment, but we are aware that some improvements can be made.
      
       
      
      
      
      
      
      
      
      