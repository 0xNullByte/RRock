from RRock import *
r = RRock()

# Porosity
print("# Porosity")

poreVolume = 2.26
bulkVolume = 10

porosity = r.Porosity(poreVolume, bulkVolume)
print(porosity)
print(porosity * 100)
# OutPut : 0.226
# OutPut : 22.6%

# Averaging Porosity
print("# Averaging Porosity")
raduis = [200, 700, 1200, 2000]
porosity  = [0.05, 0.12, 0.22, 0.3]
heigth = [5, 10, 15, 20]

# Thickness-weighted average porosity
thickness_weighted_average = r.Tavg(porosity, heigth)
print(thickness_weighted_average)

# Areal-weighted average porosity
areal_weighted_average = r.Aavg(porosity, raduis)
print(areal_weighted_average)

#Volume-weighted average porosity
volume_weighted_average = r.Vavg(porosity, heigth, raduis)
print(volume_weighted_average)

print(thickness_weighted_average, areal_weighted_average, volume_weighted_average)
# output :
# thickness_weighted_average : 0.215
# areal_weighted_average     : 0.264
# volume_weighted_average    : 0.275

# Measurement of Bulk Volume
print("# Measurement of Bulk Volume")
# Rectangular Cuboid Shape:
print("# Rectangular Cuboid Shape")
lenght, whidth, height = 7, 5, 2
print(r.bulk_Cu(lenght, whidth, height))
# Output : 70.0

# Cylinder shape using : diameter:
print("# Cylinder shape using : diameter")
lenght, diameter = 10, 2
print(r.bulk_Cy(lenght, d=diameter))
# Output :31.416

# Cylinder shape using : raduis
print("# Cylinder shape using : raduis")
lenght , radius = 10, 2
print(r.bulk_Cy(lenght, r=radius))
# Output : 125.664

# Resistivity
print("# Resistivity")
resistance = 2
lenght = 10
area = r.bulk_Cy(lenght, r=3)

resistivity = r.Res(resistance, area, lenght)
print(resistivity)
# output : 56.549

# Formation resistivity
print("# Formation resistivity")
Ro = 2
Rw = 0.07
formation_resistivity = r.FRes(Ro, Rw)
print(formation_resistivity)
# output : 28.571

# Permeability
print("# Permeability")
fluid_flow = 40.02
viscosity =  0.017
lenght = 10
area = r._pi * (8 ** 2)

pressure_1 = 17.50
pressure_2 = 6.10
delta_pressure = 11.40

permeability = r.Permeability(fluid_flow, viscosity, lenght, area, delta_pressure)
permeability2 = r.Permeability(fluid_flow, viscosity, lenght, area, p1 = pressure_1, p2 = pressure_2 )

print(permeability)
print(permeability * 1000)
print(permeability == permeability2)
# output : 0.386 Darcy
# output : 386.0 mD
# output : True
