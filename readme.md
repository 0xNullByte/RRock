# _Reservoir Rock’s Properties_
## _Reservoir Rock Properties: summary_

The **reservoir rock properties** that are of most interest to development geologists and reservoir engineers (amongst others) are **Porosity**, **Compressibility**, and **Permeability**. Porosity is a rock property that defines the fraction of the rock volume that is occupied by the pore volume. Compressibility is the rock property that governs the relative change in the pore volume when pressure is either increased or decreased. Finally, permeability is the rock property that is a measure of the ease (or difficulty) with which liquids or gases can flow through a porous medium.
___
## _About Project_

**I made this project to solve most of <u>Reservoir Rocks Properties</u> equations, for save time & accurate results via [Python language](https://en.wikipedia.org/wiki/Python_(programming_language))**

| Rock properties           | status |  method's                     |
| -------------------------- | ---- | -------------------------------|
| Porosity (φ)               | Done | [ Porosiry, Tporosity, Eporosity ]
| Permeability  (k)          | Done | [ Permeability ]
| Resistivity  (Rw, Rt, Ro)  | Done | [ Res, FRes ]
| Averaging Porosity         | Done | [ Tavg, Aavg, Vavg ]
| fluid saturation (Sf)      | Soon | 
| Compressibility (c)        | Soon |
| Wettability (θ)            | Soon |
| Capillary pressure (Pc)    | Soon |


# _documentation_
- ### Porosity (φ) 
    - [Porosity](https://github.com/0xNullByte/RRock#porosity-%CF%86-1)
    - [total porosity](https://github.com/0xNullByte/RRock#porosity-%CF%86-1)
    - [effective porosity](https://github.com/0xNullByte/RRock#porosity-%CF%86-1)

- ### Measurement of Bulk Volume (Vb)
    - [Cylinder Shape](https://github.com/0xNullByte/RRock#measurement-of-bulk-volume-vb-1)
    - [Rectangular Cuboid Shape](https://github.com/0xNullByte/RRock#measurement-of-bulk-volume-vb-1)

- ### Resistivity  (Rw, Rt, Ro)
    - [Resistivity](https://github.com/0xNullByte/RRock/blob/master/readme.md#resistivity)
    - [Formation resistivity](https://github.com/0xNullByte/RRock/blob/master/readme.md#formation-resistivity)

- ### Permeability (k)
  - [Permeability](https://github.com/0xNullByte/RRock/blob/master/readme.md#permeability)

- ### Averaging Porosity 
    - [Thickness-weighted average porosity](https://github.com/0xNullByte/RRock#thickness-weighted-average-porosity)
    - [Areal-weighted average porosity](https://github.com/0xNullByte/RRock#areal-weighted-average-porosity)
    - [Volume-weighted average porosity](https://github.com/0xNullByte/RRock#volume-weighted-average-porosity)

<br>

________
> # Porosity (φ) 
> ### RRock.Porosity(Pore_volume: float, Bulk_volume: float) -> float [RRock.Porositey](link)
>- all the porosity method's do same formula:  Volume / Volume
>- So you can skip the another [porosity] method's # `Until add some Ai Stuff`
>- and By default method's will return **fraction**
> ```python
>def Porosity(self, Pore_volume: float, Bulk_volume: float) -> float:
>        '''
>        Definition : Porosity (φ) the ratio of the pore volume (Vp) to the bulk volume (Vb) of the rock.
>
>        @@ Porosity can be expressed as a fraction or as a percentage
>           - By default method will return __fraction__
>       '''
>        return float('{:.3f}'.format(Pore_volume/ Bulk_volume))
>```
>```python
>from RRock import *
>r = RRock()
>
>poreVolume = 2.26
>bulkVolume = 10
>
>porosity = r.Porosity(poreVolume, bulkVolume)
>print(porosity)
>print(porosity * 100)
># OutPut : 0.226
># OutPut : 22.6%
>```
____________
<br>

># Averaging Porosity
> ## Thickness-weighted average porosity
> ### RRock.Tavg(self, p: float, h: float) -> float [RRock.Tavg](link)
>```python
> def Tavg(self, p: float, h: float) -> float:
>        '''
>                    φ1 * h1 + φ2 * h2 + φ3 * h3 + φ4 *h4
>           φ¯ =   ────────────────────────────────────────
>                            h1 + h2 + h3 + h4
>           
>        '''
>        return float('{:.3f}'.format(sum(map(lambda x, y : x * y , p, h)) / sum(h)))
>```
> ## Areal-weighted average porosity
> ### RRock.Aavg(self, p: float, a: float) -> float [RRock.Aavg](link)
>```python
> def Aavg(self, p: float, a: float) -> float:
>        '''
>                    φ1 * A1 + φ2 * A2 + φ3 * A3 + φ4 *A4
>           φ¯ =   ────────────────────────────────────────
>                            A1 + A2 + A3 + A4
>        '''
>        denominator  = list(map(lambda x: x ** 2, a))
>        return float('{:.3f}'.format(sum(map(lambda x, y : x * y , p, denominator)) / sum(denominator)))
>```
> ## Volume-weighted average porosity
> ### RRock.Vavg(self, p: float, h: float, a: float) -> float [RRock.Vavg](link)
> ```python
>def Vavg(self, p: float, h: float, a: float) -> float:
>        '''
>                    φ1 * V1 + φ2 * V2 + φ3 * V3 + φ4 *V4
>           φ¯ =   ────────────────────────────────────────
>                            V1 + V2 + V3 + V4
>        '''
>        area  = list(map(lambda x: x ** 2, a))
>        volume  = list(map(lambda x, y : x * y, h, area))
>        return float('{:.3f}'.format(sum(map(lambda x, y : x * y , p, volume)) / sum(volume)))
> ```
> ```python
>from RRock import RRock
>r = RRock()
>
># Averaging Porosity
>raduis = [200, 700, 1200, 2000]
>porosity  = [0.05, 0.12, 0.22, 0.3]
>heigth = [5, 10, 15, 20]
>
># Thickness-weighted average porosity
>thickness_weighted_average = r.Tavg(porosity, heigth)
>print(thickness_weighted_average)
>
># Areal-weighted average porosity
>areal_weighted_average = r.Aavg(porosity, raduis)
>print(areal_weighted_average)
>
>#Volume-weighted average porosity
>volume_weighted_average = r.Vavg(porosity, heigth, raduis)
>print(volume_weighted_average)
>
>print(thickness_weighted_average, areal_weighted_average, volume_weighted_average)
># output : 
># thickness_weighted_average : 0.215 
># areal_weighted_average     : 0.264 
># volume_weighted_average    : 0.275
>```
_______
<br>

> # Measurement of Bulk Volume (Vb)
>|         Shape            |           Formula           |  Method   |
>| ------------------------ | --------------------------- | --------- |
>|     Cylinder             | π(r^2) * L =  π/4(d^2) * L  |  bulk_Cy  |
>| Rectangular Cuboid Shape |  Length * Width * Height    |  bulk_Cu  |

> ### RRock.bulk_Cy(self, L: float, d=None, r=None) -> float [RRock.bulk_Cy](link)
>```python
>   def bulk_Cy(self, L: float, d=None, r=None) -> float:
>        '''
>        [@] Cylinder shape 
>            [*] "r": radius & "L": Length & "d": diameter
>        '''
>        pi = RRock.__pi
>        if d:
>            return float('{:.3f}'.format(pi/4 * (d**2) * L))
>        if r:
>            return float('{:.3f}'.format(pi * (r**2) * L))
>```
> ### RRock.bulk_Cu(self, L: float, W: float, H: float) -> float [RRock.bulk_Cu](link)
>```python        
>    def bulk_Cu(self, L: float, W: float, H: float) -> float:
>        '''
>        [@] Rectangular Cuboid Shape 
>            [*] "L": Length & "W": Width & "H": Height 
>        '''
>        return float('{:.3f}'.format(L * W * H))
> ```
>```python
>from RRock import *
>r = RRock()
># Rectangular Cuboid Shape:
>lenght, whidth, height = 7, 5, 2
>print(r.bulk_Cu(lenght, whidth, height))
># Output : 70.0
>
># Cylinder shape using : diameter:
>lenght, diameter = 10, 2
>print(r.bulk_Cy(lenght, d=diameter))
># Output :31.416
>
># Cylinder shape using : raduis
>lenght , radius = 10, 2
>print(r.bulk_Cy(lenght, r=radius))
># Output : 125.664
>```
____________
<br>

> # Resistivity 
> ### RRock.Res(self, r: float, A: float, L: float) -> float [RRock.Res](link)
>```python
>def Res(self, r: float, A: float, L: float) -> float:
>        '''
>        @@ Definition : Resistivity is a physical property of the material.
>            Resistivity Formula : R = rA/L
>        '''
>        return float('{:.3f}'.format(r * A / L))
>```
># Formation resistivity
> ### RRock.FRes(self, Ro: float, Rw: float) -> float [RRock.FRes](link)
>```python
>def FRes(self, Ro: float, Rw: float) -> float:
>        '''
>         @@ Definiton: the ratio of the resistivity of the rock saturated with brine (Ro) to the resistivity of the brine (Rw).
>            - to account for the presence of non-conductive rock.
>        '''
>        return float('{:.3f}'.format(Ro / Rw))
>```
> ```python
> from RRock import RRock
>r = RRock()
>
># Resistivity
>resistance = 2
>lenght = 10
>area = r.bulk_Cy(lenght, r=3)
>
>resistivity = r.Res(resistance, area, lenght)
>print(resistivity)
># output : 56.549
>
># Formation resistivity
>Ro = 2
>Rw = 0.07
>formation_resistivity = r.FRes(Ro, Rw)
>print(formation_resistivity)
># output : 28.571
>```
____________
<br>

> # Permeability
> ### Permeability(self, q: float, u: float, l: float, A: float, p=None, p1=None, p2=None) -> float [RRock.Permeability](link)
> - there are two different ways to enter pressure
>   1. Permeability(*args, p = ∆p) 
>   2. Permeability(*args, p1 = pressure1, p2 = pressure2)
> ```python
>     def Permeability(self, q: float, u: float, l: float, A: float, p=None, p1=None, p2=None) -> float:
>        '''
>            - By default method will return __fraction__ [ Darcy ]
>        '''
>        if p1 and p2:
>            p = p1 - p2
>        return float('{:.3f}'.format(q * u * l / A * p))
>```
>```python
>from RRock import RRock
>r = RRock()
>
># Permeability
>fluid_flow = 40.02
>viscosity =  0.017 
>lenght = 10
>area = r._pi * (8 ** 2)
>
>pressure_1 = 17.50
>pressure_2 = 6.10
>delta_pressure = 11.40
>
>
>permeability = r.Permeability(fluid_flow, viscosity, lenght, area, delta_pressure)
>permeability2 = r.Permeability(fluid_flow, viscosity, lenght, area, p1 = pressure_1, p2 = pressure_2 )
>
>print(permeability)
>print(permeability * 1000)
>print(permeability == permeability2)
># output : 0.386 Darcy
># output : 386.0 mD
># output : True
>```
