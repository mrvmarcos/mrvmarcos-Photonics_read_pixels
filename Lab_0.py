import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to your Excel file
excel_file_path = r'C:\Users\marco\Documents\4º Ing Fisc+Inds gmu\Segundo Cuatri\Material Science\Homework\Photonics\Absorption measurments.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Perform operations on the DataFrame as needed
# rest the last column to the 1,2,3,4 and 5
Data_pbs= df['pbs raw'][8:216]-df['dark'][8:216]
Data_100uM= df['100uM fitc raw'][8:216]-df['dark'][8:216]
Data_50uM= df['50 uM fitc raw'][8:216]-df['dark'][8:216]
Data_water= df['water raw'][8:216]-df['dark'][8:216]
Data_empty= df['empty cuvette'][8:216]-df['dark'][8:216]

Data=[Data_pbs, Data_100uM, Data_50uM, Data_water, Data_empty]

#from row 8 to 216, make a plot with the colum A against the column B, take the names from the header

for i in range(0,5):
    plt.plot(df['Unnamed: 0'][8:216], Data[i], label=df.columns[i+1])
plt.xlabel('Wavelength (nm)')
plt.ylabel('Nº of photons')
plt.title('Number of photons vs. Wavelength')
plt.legend()
plt.show()



