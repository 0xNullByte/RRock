
class RRock:
    _pi = 3.141592653589793
    '''
    @@ This library solve most of " Reservoir Rocks Properties " equations.
        resources : [pdf file]
        documentation : [ github readme.md ]
    
    -@- Todo
    [ Rock properties ] :
            Porosity (φ)                [done]
            Permeability (k)            [done]
            Resistivity (Rw, Rt, Ro)    [done]
            Thickness (h)               [done]
            Compressibility (c)        [Not yet]
            Water saturation (Sw)      [Not yet]
            Wettability (θ)            [not yet]
            Capillary pressure (Pc)    [not yet]
    '''
    def __init__(self) -> None:
        pass

    '''
    [@] Porosities Methods :
        1 - porosity            ==> Vp / Vb
        2 - Total porosity      ==> Vpt / Vb
        3 - Effective porosity  ==> Vpe / vb
    '''
    def Porosity(self, Pore_volume: float, Bulk_volume: float) -> float:
        '''
        Definition : Porosity (φ) the ratio of the pore volume (Vp) to the bulk volume (Vb) of the rock.
        @@ Porosity can be expressed as a fraction or as a percentage
            - By default method will return __fraction__
        '''
        return float('{:.3f}'.format(Pore_volume/ Bulk_volume))
    
    def Tporosity(self, Total_Pore_volume: float, Bulk_volume: float) -> float:
        '''
        Definition : the ratio of the total pore volume (Vpt) to the bulk volume.
        @@ Porosity can be expressed as a fraction or as a percentage
            - By default method will return __fraction__
        '''
        return float('{:.3f}'.format(Total_Pore_volume/ Bulk_volume))
    def Eporosity(self, effective_Pore_volume: float, Bulk_volume: float) -> float:
        '''
        Definition : the ratio of the interconnected pore volume to the bulk volume.
        * effective pore volume [ interconnected pore volume ]
        @@ Porosity can be expressed as a fraction or as a percentage
            - By default method will return __fraction__
        '''
        return float('{:.3f}'.format(effective_Pore_volume/ Bulk_volume))
    
    
    '''
    [@] Averaging Porosity
        1 - Thickness-weighted average porosity
        2 - Areal-weighted average porosity
        3 - Volume-weighted average porosity
    '''
    # Thickness-weighted average porosity
    def Tavg(self, p: float, h: float) -> float:
        ''' 
            φ1 * h1 + φ2 * h2 + φ3 * h3 + φ4 *h4
    φ ̄ = ────────────────────────────────────────
                h1 + h2 + h3 + h4
        '''
        return float('{:.3f}'.format(sum(map(lambda x, y : x * y , p, h)) / sum(h)))

    # Areal-weighted average porosity
    def Aavg(self, p: float, a: float) -> float:
        '''
            φ1 * A1 + φ2 * A2 + φ3 * A3 + φ4 *A4
    φ ̄ = ────────────────────────────────────────
                    A1 + A2 + A3 + A4
        '''

        denominator = list(map(lambda x: x ** 2, a))
        return float('{:.3f}'.format(sum(map(lambda x, y : x * y , p, denominator)) / sum(denominator)))
    # Volume-weighted average porosity
    def Vavg(self, p: float, h: float, a: float) -> float:
        '''
            φ1 * V1 + φ2 * V2 + φ3 * V3 + φ4 *V4
    φ ̄ = ────────────────────────────────────────
                V1 + V2 + V3 + V4
        '''
        area = list(map(lambda x: x ** 2, a))
        volume = list(map(lambda x, y : x * y, h, area))
        return float('{:.3f}'.format(sum(map(lambda x, y : x * y , p, volume)) / sum(volume)))

    '''
    [@] Measurement of Bulk Volume
    [*] with two shapes:
        [Shape]                         [ Formula ]                     [ Method ]
    1 - Cylinder                ( π(r^2) * L ) = ( π/4(d^2 * L) )          bulk_Cy
    2 - Rectangular Cuboid          Length * Width * Height                bulk_Cu
        ...
    '''

    def bulk_Cy(self, L: float, d=None, r=None) -> float:
        '''
        [@] Cylinder shape
            [*] "r": radius & "L": Length & "d": diameter
        '''
        pi = RRock._pi
        if d:
            return float('{:.3f}'.format(pi/4 * (d**2) * L))
        if r:
            return float('{:.3f}'.format(pi * (r**2) * L))
        
    def bulk_Cu(self, L: float, W: float, H: float) -> float:
        '''
        [@] Rectangular Cuboid Shape
            [*] "L": Length & "W": Width & "H": Height
        '''
        return float('{:.3f}'.format(L * W * H))
    
    '''
    [@] Resistivity Relations:
        1 - Resistivity : R = rA/L
            - R = Resistivity,
            - r = resistance,
            - A = cross area of the specimen.
            - L = Lenght

        2 - Formation resistivity factor ( Archie ) : F = Ro / Rw
            - F = Formation resistivity factor
            - Ro = Rock resistivity
            - Rw = brine resistivity

        3 - [Soon]
            - [Note] : There are more to add for Resistivity Relations.
            
    '''

    # Resistivity
    def Res(self, r: float, A: float, L: float) -> float:
        '''
        @@ Definition : Resistivity is a physical property of the material.
            Resistivity Formula : R = rA/L
        '''
        return float('{:.3f}'.format(r * A / L))

    # Formation resistivity
    def FRes(self, Ro: float, Rw: float) -> float:
        '''
        @@ Definiton: the ratio of the resistivity of the rock saturated with brine (Ro) to the resistivity of the brine (Rw).
            - to account for the presence of non-conductive rock.
        '''
        return float('{:.3f}'.format(Ro / Rw))
    
    '''
    [@] Permeability
        1 - Permeability : K = q*μ*L / A * ∆p
            - q = rate of fluid flow
            - μ = Fluid viscosity
            - L = length
            - A = Area
            - ∆p = pressure difference
    '''
    
    def Permeability(self, q: float, u: float, l: float, A: float, p=None, p1=None, p2=None) -> float:
        '''
        - By default method will return __fraction__
        '''
        if p1 and p2:
            p = p1 - p2
        return float('{:.3f}'.format(q * u * l / A * p))
