import numpy as np


class Eletrolisador:
    # Define as caracteristicas do eletrolisador
    def __init__(self, name, pot, h2, capex, opex, efficiency, lifetime, FlowRate, Pressure):
        self.name = name
        self.pot = pot
        self.h2 = h2
        self.capex = capex
        self.opex = opex
        self.ef = efficiency
        self.lifetime = lifetime
        self.FlowRate = FlowRate
        self.Pressure = Pressure

    def capexCompressor(self):
        NumCompressor = 1 
        IsotropricCoefficient = 1.4 
        CompressorEfficiency = 0.75 
        M = 2.016 # Massa molecular hidrogenio
        R = 8.314 # Constante gas ideal
        T = 310 # temperatura
        Z = 1.03 # Fator de compressibilidade
        p0 = 70 # Output pressure
        Q = self.FlowRate
        pi = self.Pressure
        
        Pcomp = Q*((R*T*Z)/(CompressorEfficiency*M))*(NumCompressor/(IsotropricCoefficient-1))*((p0/pi)**((IsotropricCoefficient-1)/(NumCompressor)) - 1)*10**-3
        capex_compressor = 12600*(Pcomp/10)**0.9
        return capex_compressor

    # Energia para produzir 1kg de hidrogenio
    def energy_prod_1kg(self):
        energy_1kg = self.pot/self.h2
        tot_energy = energy_1kg+energy_1kg*0.1
        return tot_energy
    
    # Calcula o capex e opex total, com base na potencia multiplicada pelo preco por kW
    def electrolyser_capex_opex(self):
        CapexCompressor = self.capexCompressor()
        if 'AEM' in self.name.upper():
            CapexElectrolyzer = self.capex*self.pot
            capex_total = (CapexElectrolyzer+CapexCompressor)*0.66
            # Material - 2.5% | Labor - 5.0%   Deionized water - 0.01$/kg | Electrolyte (KOH) 2.75$/kg | Steam 0.01$/kg
            opex_total = (0.025+0.05)*capex_total + (0.01 + 2.75 + 0.01)*(self.h2)

        else:  
            CapexElectrolyzer = self.capex*self.pot
            capex_total = (CapexElectrolyzer+CapexCompressor)*0.66
            opex_total = self.opex*capex_total
        
        print('=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(f'{self.name} Capex compressor = {CapexCompressor*10**-3:.2f} k$')
        print(f'{self.name} Capex total {capex_total*10**-3:.2f} k$')
        print(f'{self.name} Opex total {opex_total*10**-3:.2f} k$')
        print('=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        return capex_total, opex_total
    

class Energia:
    def __init__(self, name, capex, opex, cf):
        self.name = name
        self.capex = capex
        self.opex = opex
        self.cf = cf
        self.t = 20

    """
    Total capex e opex da fonte energia com base na potência do eletrolisador.
    As potências dos eletrolisadores estão próximas de 1 MW então o capex e o opex são similares
    Essa fórmula multiplica o capex pelo total de energia que minha planta deve ter com base no fator de capacidade
    Se meu eletrolisador tem 1 MW e cf_sol 0.25, minha planta deve ter 1 MW/0.25 = 4 WM
    """
    def energy_total_capex_opex(self,pot,cf, nome, lifetime, capex_battery, opex_battery):
        PlantPower = pot/cf
        CapexEnergyToStore = capex_battery*(PlantPower - pot)*0.66

        plantLifetime = self.t*365*24 # hours lifetime 
        TimeOperationElectrolyser = plantLifetime/lifetime
        ciclosEletrolisador = np.ceil(TimeOperationElectrolyser)

        capex_energy = self.capex*(PlantPower)*0.66 + CapexEnergyToStore # capex_energy = self.capex*(pot/cf)
        tot_opex_energy = self.opex*capex_energy + opex_battery*CapexEnergyToStore

        print('---------------------------------')
        print(f'O {nome} - {self.name} tem {ciclosEletrolisador:.2f} ciclos')
        print(f'{self.name} - {nome} Capex total {capex_energy * 10**-6:.2f} M$')
        print(f'{self.name} - {nome} Opex total {tot_opex_energy*10**-6:.2f} M$')
        print('---------------------------------')
        return capex_energy, tot_opex_energy, ciclosEletrolisador # Ta funcionando

    def energy_no_storage_CapexOpex(self,pot,cf, nome, lifetime):
        PlantPower = pot
        plantLifetime = self.t*365*24 # Tempo de vida em horas
        TimeOperationElectrolyser = plantLifetime/lifetime
        ciclosEletrolisador = np.ceil(TimeOperationElectrolyser)*cf

        capex_energy = self.capex*(PlantPower)*0.66  # capex_energy = self.capex*(pot/cf)
        tot_opex_energy = self.opex*capex_energy

        print('---------------------------------')
        print(f'O {nome} - {self.name} tem {ciclosEletrolisador:.2f} ciclos')
        print(f'{self.name} - {nome} Capex total {capex_energy * 10**-6:.2f} M$')
        print(f'{self.name} - {nome} Opex total {tot_opex_energy*10**-6:.2f} M$')
        print('---------------------------------')
        return capex_energy, tot_opex_energy, ciclosEletrolisador # Ta funcionando
