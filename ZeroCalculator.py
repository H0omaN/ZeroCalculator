import glob
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
#import numpy.ma as ma
from PIL import Image




folder="/srv/ccrc/data60/z5194283/Data/LargerDomain/"
IMERG_files=glob.glob(folder+"IMERG_HHFV06B/Selected/*.nc")
IMERG_files.sort()
MRMS_files = glob.glob(folder+"MRMS-RegriddedLargeDomain-6Days-30min/Selected/*.nc")
MRMS_files.sort()
#outputfolder="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/ModeOutPut-Modified/"
#outpufiles=glob.glob(outputfolder+"*_obj.nc")
#outpufiles.sort() 
IMERGZeros=list()
MRMSZeros=list()
IMERGIRZeros=list()
Timestep=list()
ACC_Sensor=list()
i=0
for file in IMERG_files:
    IMERGfile = Dataset(file, 'r')
    MRMSfile= Dataset(MRMS_files[i], 'r')
    IMERGData=IMERGfile.variables['precipitationCal'][0,:,:] 
    IMERGData[IMERGData<0]=0
    IMERGIRData=IMERGfile.variables['IRprecipitation'][0,:,:]
    IMERGIRData[IMERGIRData<0]=0
    MRMSData=MRMSfile.variables['PrecipRate_0mabovemeansealevel'][0,:,:]
    MRMSData[MRMSData<0]=0 
    
    # counting zero valuesat each datasets
    IMERGZeros.append(len(IMERGData)*len(IMERGData[0])-np.count_nonzero(IMERGData))
    MRMSZeros.append(len(MRMSData)*len(MRMSData[0])-np.count_nonzero(MRMSData))
    IMERGIRZeros.append(len(IMERGIRData)*len(IMERGIRData[0])-np.count_nonzero(IMERGIRData))
    
    ## finding sensors at each timestep
#    Modeoutput = Dataset(outpufiles[i], 'r')
#    IMERGMask=Modeoutput.variables['fcst_clus_id'][:,:] 
    
    # Isolating the main cluster
#    IMERGMask[IMERGMask<0]=1
#    IMERGMask[IMERGMask>1]=1
#    SensorType=IMERGfile.variables['HQprecipSource'][:,:]
#    SensorType[SensorType<0]=0
#    SensorTypeFiltered=np.multiply(np.transpose(SensorType), IMERGMask) 
#    S1=ma.getdata(SensorTypeFiltered)
#    ACC_Sensor.append(np.max(S1))
    Timestep.append(i)        
    i=i+1
    

#plt.subplot(2,1,1)
#plt.bar(Timestep,ACC_Sensor)
#plt.title('PMW Sensors')
##plt.legend(loc='lower right') 
#plt.ylabel("Sensor ID")  
##plt.xlabel("Intensity (mm/hr)")  
#plt.yticks(np.arange(0, 12, step=1)) 
#plt.xticks(np.arange(0, 74, step=1))  
#plt.grid()
#plt.tight_layout()


#plt.subplot(2,1,2)
plt.plot(Timestep,IMERGZeros,label='IMERG-Zeros')
plt.plot(Timestep,MRMSZeros,label='MRMS-Zeros')
plt.plot(Timestep,IMERGIRZeros,label='IR-Zeros')
plt.legend(loc='lower right') 
plt.xlabel("Timestep (30 min)") 
plt.ylabel("No. of Zeros") 
plt.xticks(np.arange(0, 153, step=10))  
plt.grid()
plt.tight_layout()  


#

#
## Creating images of sensors and all positive pixel values
#i=0
#for file in IMERG_files:
#    IMERGfile = Dataset(file, 'r')
#    IMERGData=IMERGfile.variables['precipitationCal'][:,:] 
#    IMERGData[IMERGData<0]=0
#    IMERGData[IMERGData>0]=1
#    MRMSfile= Dataset(MRMS_files[i], 'r')
#    MRMSData=MRMSfile.variables['PrecipRate_0mabovemeansealevel'][0,:,:]
#    MRMSData[MRMSData<0]=0 
#    MRMSData[MRMSData>0]=1 
#    SensorType=IMERGfile.variables['HQprecipSource'][:,:]
#    SensorType[SensorType<0]=0
#    SensorType[SensorType>0]=1
#    
#    
##    img = Image.open("data_mask_1354_2030.png")
##    background = Image.open("background_1354_2030.png")    
##    background.paste(img, (0, 0), img)
##    background.save('how_to_superimpose_two_images_01.png',"PNG")
##    Modeoutput = Dataset(file, 'r')
##    IMERGMask=Modeoutput.variables['fcst_obj_raw'][:,:]    
##    MRMSMask=Modeoutput.variables['obs_obj_raw'][:,:]
#    plt.subplot(1,2,1)
#    plt.title('I'+str(i))
##    plt.imshow(np.transpose(SensorType))
#    plt.imshow(np.transpose(IMERGData)+np.transpose(SensorType))
##    plt.scatter(126,111,color='red',s=2)
#    
#    plt.xticks([])
#    plt.yticks([])
#    plt.subplot(1,2,2)
#    plt.title('M'+str(i))
#    plt.imshow(MRMSData)
##    plt.scatter(126,111,color='red',s=2)
#    
#    plt.xticks([])
#    plt.yticks([])
#    
#    
#    
#    mng = plt.get_current_fig_manager()
#    mng.window.showMaximized()
#    plt.tight_layout()
#    plt.savefig('/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/2dImagesOutputs/Withoutmask/'+str(i)+'.png',dpi=600)
#    plt.close()
#    i=i+1
#    #
