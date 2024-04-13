import numpy as np 
import matplotlib.pyplot as plt 
from classes import Energia, Eletrolisador
from functions import plot_graph, write_txt, wh2, lcoh, write_excel


def parameters_present():
    e = Energia('a',0,0,0)
    t = e.t
    wacc = 8/100
    year = 'present'
    ########### Energia ################
    ### custos energias
    # Solar
    capex_sol = 320*0.2 # USD/kW
    opex_sol = 0.02 # %
    cf_sol = 0.25

    # Wind Onshore
    capex_WindOnshore = 450*0.2 # USD/kW - EPE
    opex_WindOnshore = 90/capex_WindOnshore # %/ano 0.2
    cf_WindOnshore = 0.4
    
    # wind offshore
    capex_WindOffshore = 1225*0.2 # USD/kW - EPE
    opex_WindOffshore = 0.04 # %
    cf_WindOffshore = 0.47
    
    # Nuclear
    capex_nuclear = 0*0.2
    opex_nuclear = 0.013
    cf_nuclear = 1 

    ######### Eletrolisador ############
    ### Custos e parametros
    # PEM parametros
    capex_pem = 1000 # USD/kW
    opex_pem = 0.02 # %

    pot_pem = 988.68 # kW
    h2_pem = 17.976 # kg/h 
    FlowRate_pem = 200 # Nm3/h
    ef_pem = 0
    pem_energy_prod1kg = 55*1.01 # kWh/kg
    lifetime_pem = 80000 # h IEA
    bar_pem = 30

    # Alkalino parametros
    capex_alk = 650 # $/kW
    opex_alk = 0.02
    
    pot_alk = 1000 # kW
    FlowRate_alk = 200
    h2_alk = FlowRate_alk*0.08988 # kg/h  nao to usando pra nada pois calculamos por fora a energia para produzir 1kg
    ef_alk = 0
    alk_energy_prod1kg = (4.8/0.08988) + (4.8/0.08988)*0.1 # kWh/kg
    lifetime_alk = 80000 # h  Datasheet
    bar_alk = 30

    # Parametros SOEC
    capex_soec = 1800 # $/kW
    opex_soec = 0.02 # %

    pot_soec = 1100 # kW
    h2_soec = 24 # kg/h nao to usando pra nada pois calculamos por fora a energia para produzir 1kg
    FlowRate_soec = h2_soec/0.08988
    soec_energy_prod1kg = 39.4 + 39.4*0.1 # kWh/kg
    ef_soec = 0
    lifetime_soec = 50000 # h IEA
    bar_soec = 1

    # Parametros AEM
    capex_aem = (469.13+258.02) # $/kW
    nao_utilizado_opex = 1

    pot_aem = 1000 # kW
    FlowRate_aem = 210 # Nm3/h
    h2_aem = 453/24 # kg/h -> So esta sendo utilizado para calcular o opex, pois energia para produzir 1kg eh calculada por fora
    aem_energy_prod1kg = 53.3 # kWh/kg
    ef_aem = 0.625 # LHV
    lifetime_aem = 20000 # h - (M. KIM et. al, 2024) - AEM Techno-economic
    bar_aem = 30

    calculate(t, wacc, capex_sol, opex_sol, cf_sol, capex_WindOnshore, opex_WindOnshore, cf_WindOnshore,
            capex_WindOffshore, opex_WindOffshore, cf_WindOffshore, capex_nuclear, opex_nuclear, cf_nuclear,
            capex_pem, opex_pem, pot_pem, h2_pem, FlowRate_pem, ef_pem, pem_energy_prod1kg, lifetime_pem, bar_pem,
            capex_alk, opex_alk, pot_alk, h2_alk, FlowRate_alk, ef_alk, alk_energy_prod1kg, lifetime_alk, bar_alk,
            capex_soec, opex_soec, pot_soec, h2_soec, FlowRate_soec, ef_soec, soec_energy_prod1kg, lifetime_soec, bar_soec,
            capex_aem, nao_utilizado_opex, pot_aem, h2_aem, FlowRate_aem, ef_aem, aem_energy_prod1kg, lifetime_aem, bar_aem, year)

def parameters_2030():
    e = Energia('a',0,0,0)
    t = e.t
    wacc = 8/100
    year = '2030'
    ########### Energia ################
    ### custos energias
    # Solar
    capex_sol = 3200*0.2 # USD/kW
    opex_sol = 0.02 # %
    cf_sol = 0.25

    # Wind Onshore
    capex_WindOnshore = 4500*0.2 # USD/kW - EPE
    opex_WindOnshore = 90/capex_WindOnshore # %/ano 0.2
    cf_WindOnshore = 0.4
    
    # wind offshore
    capex_WindOffshore = 12250*0.2 # USD/kW - EPE
    opex_WindOffshore = 0.04 # %
    cf_WindOffshore = 0.47
    
    # Nuclear
    capex_nuclear = 24500*0.2
    opex_nuclear = 0.013
    cf_nuclear = 1 

    ######### Eletrolisador ############
    ### Custos e parametros
    # PEM parametros
    capex_pem = 1000 # USD/kW
    opex_pem = 0.02 # %

    pot_pem = 988.68 # kW
    h2_pem = 17.976 # kg/h 
    FlowRate_pem = 200 # Nm3/h
    ef_pem = 0
    pem_energy_prod1kg = 55*1.01 # kWh/kg
    lifetime_pem = 80000 # h IEA
    bar_pem = 30

    # Alkalino parametros
    capex_alk = 650 # $/kW
    opex_alk = 0.02
    
    pot_alk = 1000 # kW
    FlowRate_alk = 200
    h2_alk = FlowRate_alk*0.08988 # kg/h  nao to usando pra nada pois calculamos por fora a energia para produzir 1kg
    ef_alk = 0
    alk_energy_prod1kg = (4.8/0.08988) + (4.8/0.08988)*0.1 # kWh/kg
    lifetime_alk = 80000 # h  Datasheet
    bar_alk = 30

    # Parametros SOEC
    capex_soec = 1800 # $/kW
    opex_soec = 0.02 # %

    pot_soec = 1100 # kW
    h2_soec = 24 # kg/h nao to usando pra nada pois calculamos por fora a energia para produzir 1kg
    FlowRate_soec = h2_soec/0.08988
    soec_energy_prod1kg = 39.4 + 39.4*0.1 # kWh/kg
    ef_soec = 0
    lifetime_soec = 50000 # h IEA
    bar_soec = 1

    # Parametros AEM
    capex_aem = (469.13+258.02) # $/kW
    nao_utilizado_opex = 1

    pot_aem = 1000 # kW
    FlowRate_aem = 210 # Nm3/h
    h2_aem = 453/24 # kg/h -> So esta sendo utilizado para calcular o opex, pois energia para produzir 1kg eh calculada por fora
    aem_energy_prod1kg = 53.3 # kWh/kg
    ef_aem = 0.625 # LHV
    lifetime_aem = 20000 # h - (M. KIM et. al, 2024) - AEM Techno-economic
    bar_aem = 30

    calculate(t, wacc, capex_sol, opex_sol, cf_sol, capex_WindOnshore, opex_WindOnshore, cf_WindOnshore,
            capex_WindOffshore, opex_WindOffshore, cf_WindOffshore, capex_nuclear, opex_nuclear, cf_nuclear,
            capex_pem, opex_pem, pot_pem, h2_pem, FlowRate_pem, ef_pem, pem_energy_prod1kg, lifetime_pem, bar_pem,
            capex_alk, opex_alk, pot_alk, h2_alk, FlowRate_alk, ef_alk, alk_energy_prod1kg, lifetime_alk, bar_alk,
            capex_soec, opex_soec, pot_soec, h2_soec, FlowRate_soec, ef_soec, soec_energy_prod1kg, lifetime_soec, bar_soec,
            capex_aem, nao_utilizado_opex, pot_aem, h2_aem, FlowRate_aem, ef_aem, aem_energy_prod1kg, lifetime_aem, bar_aem, year)

def parameters_2050():
    e = Energia('a',0,0,0)
    t = e.t
    wacc = 8/100
    year = '2050'
    ########### Energia ################
    ### custos energias
    # Solar
    capex_sol = 32000*0.2 # USD/kW
    opex_sol = 0.02 # %
    cf_sol = 0.25

    # Wind Onshore
    capex_WindOnshore = 45000*0.2 # USD/kW - EPE
    opex_WindOnshore = 90/capex_WindOnshore # %/ano 0.2
    cf_WindOnshore = 0.4
    
    # wind offshore
    capex_WindOffshore = 122500*0.2 # USD/kW - EPE
    opex_WindOffshore = 0.04 # %
    cf_WindOffshore = 0.47
    
    # Nuclear
    capex_nuclear = 245000*0.2
    opex_nuclear = 0.013
    cf_nuclear = 1 

    ######### Eletrolisador ############
    ### Custos e parametros
    # PEM parametros
    capex_pem = 1000 # USD/kW
    opex_pem = 0.02 # %

    pot_pem = 988.68 # kW
    h2_pem = 17.976 # kg/h 
    FlowRate_pem = 200 # Nm3/h
    ef_pem = 0
    pem_energy_prod1kg = 55*1.01 # kWh/kg
    lifetime_pem = 80000 # h IEA
    bar_pem = 30

    # Alkalino parametros
    capex_alk = 650 # $/kW
    opex_alk = 0.02
    
    pot_alk = 1000 # kW
    FlowRate_alk = 200
    h2_alk = FlowRate_alk*0.08988 # kg/h  nao to usando pra nada pois calculamos por fora a energia para produzir 1kg
    ef_alk = 0
    alk_energy_prod1kg = (4.8/0.08988) + (4.8/0.08988)*0.1 # kWh/kg
    lifetime_alk = 80000 # h  Datasheet
    bar_alk = 30

    # Parametros SOEC
    capex_soec = 1800 # $/kW
    opex_soec = 0.02 # %

    pot_soec = 1100 # kW
    h2_soec = 24 # kg/h nao to usando pra nada pois calculamos por fora a energia para produzir 1kg
    FlowRate_soec = h2_soec/0.08988
    soec_energy_prod1kg = 39.4 + 39.4*0.1 # kWh/kg
    ef_soec = 0
    lifetime_soec = 50000 # h IEA
    bar_soec = 1

    # Parametros AEM
    capex_aem = (469.13+258.02) # $/kW
    nao_utilizado_opex = 1

    pot_aem = 1000 # kW
    FlowRate_aem = 210 # Nm3/h
    h2_aem = 453/24 # kg/h -> So esta sendo utilizado para calcular o opex, pois energia para produzir 1kg eh calculada por fora
    aem_energy_prod1kg = 53.3 # kWh/kg
    ef_aem = 0.625 # LHV
    lifetime_aem = 20000 # h - (M. KIM et. al, 2024) - AEM Techno-economic
    bar_aem = 30

    calculate(t, wacc, capex_sol, opex_sol, cf_sol, capex_WindOnshore, opex_WindOnshore, cf_WindOnshore,
            capex_WindOffshore, opex_WindOffshore, cf_WindOffshore, capex_nuclear, opex_nuclear, cf_nuclear,
            capex_pem, opex_pem, pot_pem, h2_pem, FlowRate_pem, ef_pem, pem_energy_prod1kg, lifetime_pem, bar_pem,
            capex_alk, opex_alk, pot_alk, h2_alk, FlowRate_alk, ef_alk, alk_energy_prod1kg, lifetime_alk, bar_alk,
            capex_soec, opex_soec, pot_soec, h2_soec, FlowRate_soec, ef_soec, soec_energy_prod1kg, lifetime_soec, bar_soec,
            capex_aem, nao_utilizado_opex, pot_aem, h2_aem, FlowRate_aem, ef_aem, aem_energy_prod1kg, lifetime_aem, bar_aem, year)

def calculate(t, wacc, capex_sol, opex_sol, cf_sol, capex_WindOnshore, opex_WindOnshore, cf_WindOnshore,
            capex_WindOffshore, opex_WindOffshore, cf_WindOffshore, capex_nuclear, opex_nuclear, cf_nuclear,
            capex_pem, opex_pem, pot_pem, h2_pem, FlowRate_pem, ef_pem, pem_energy_prod1kg, lifetime_pem, bar_pem,
            capex_alk, opex_alk, pot_alk, h2_alk, FlowRate_alk, ef_alk, alk_energy_prod1kg, lifetime_alk, bar_alk,
            capex_soec, opex_soec, pot_soec, h2_soec, FlowRate_soec, ef_soec, soec_energy_prod1kg, lifetime_soec, bar_soec,
            capex_aem, nao_utilizado_opex, pot_aem, h2_aem, FlowRate_aem, ef_aem, aem_energy_prod1kg, lifetime_aem, bar_aem, year):
    
    solar = Energia('Solar', capex_sol, opex_sol, cf_sol)
    WindOnshore =Energia('WindOnshore', capex_WindOnshore, opex_WindOnshore, cf_WindOnshore)
    WindOffshore = Energia('WindOffshore', capex_WindOffshore, opex_WindOffshore, cf_WindOffshore)
    nuclear = Energia('Nuclear', capex_nuclear, opex_nuclear, cf_nuclear)

    # Eletrolisadores
    pem = Eletrolisador('PEM-HyLYZER-200', pot_pem, h2_pem, capex_pem, opex_pem, ef_pem, lifetime_pem, FlowRate_pem, bar_pem)
    alk = Eletrolisador('Alkaline P200', pot_alk, h2_alk, capex_alk, opex_alk, ef_alk, lifetime_alk, FlowRate_alk, bar_alk)
    soec = Eletrolisador('SOEC FuelCell Energy', pot_soec, h2_soec, capex_soec, opex_soec, ef_soec, lifetime_soec, FlowRate_soec, bar_soec)
    aem = Eletrolisador('AEM Nexus 1000',pot_aem, h2_aem, capex_aem, nao_utilizado_opex, ef_aem, lifetime_aem, FlowRate_aem, bar_aem)

    ############# Calculos #################
    ### Total capex opex energias, que é parecido porque as plantas tem apriximadamente 1 MW
    # Energias Capex e Opex PEM
    tot_capex_solar_pem, tot_opex_solar_pem, ciclo_pem_solar = solar.energy_total_capex_opex(pem.pot,cf_sol, pem.name, lifetime_pem) # Entro com a potencia pois a potencia instalada é com base na potencia do eletrolisador e do cf
    tot_capex_WindOnshore_pem, tot_opex_WindOnshore_pem, ciclo_pem_WindOnshore = WindOnshore.energy_total_capex_opex(pem.pot, cf_WindOnshore, pem.name, lifetime_pem)
    tot_capex_WindOffshore_pem, tot_opex_WindOffshore_pem, ciclo_pem_WindOffshore = WindOffshore.energy_total_capex_opex(pem.pot, cf_WindOffshore, pem.name, lifetime_pem)
    tot_capex_nuclear_pem, tot_opex_nuclear_pem, ciclo_pem_nuclear = nuclear.energy_total_capex_opex(pem.pot, cf_nuclear, pem.name, lifetime_pem)

    # Energia Capex e Opex AWE
    tot_capex_solar_alk, tot_opex_solar_alk, ciclo_alk_solar = solar.energy_total_capex_opex(alk.pot, cf_sol, alk.name, lifetime_alk)
    tot_capex_WindOnshore_alk, tot_opex_WindOnshore_alk, ciclo_alk_WindOnshore = WindOnshore.energy_total_capex_opex(alk.pot, cf_WindOnshore, alk.name, lifetime_alk)
    tot_capex_WindOffshore_alk, tot_opex_WindOffshore_alk, ciclo_alk_WindOffshore = WindOffshore.energy_total_capex_opex(alk.pot, cf_WindOffshore, alk.name, lifetime_alk)
    tot_capex_nuclear_alk, tot_opex_nuclear_alk, ciclo_alk_nuclear = nuclear.energy_total_capex_opex(alk.pot, cf_nuclear, alk.name, lifetime_alk)

    # Energia Capex e Opex SEOC
    tot_capex_solar_soec, tot_opex_solar_soec, ciclo_soec_solar = solar.energy_total_capex_opex(soec.pot, cf_sol, soec.name, lifetime_soec)
    tot_capex_WindOnshore_soec, tot_opex_WindOnshore_soec, ciclo_soec_WindOnshore = WindOnshore.energy_total_capex_opex(soec.pot, cf_WindOnshore, soec.name, lifetime_soec)
    tot_capex_WindOffshore_soec, tot_opex_WindOffshore_soec, ciclo_soec_WindOffshore = WindOffshore.energy_total_capex_opex(soec.pot, cf_WindOffshore, soec.name, lifetime_soec)
    tot_capex_nuclear_soec, tot_opex_nuclear_soec, ciclo_soec_nuclear = nuclear.energy_total_capex_opex(soec.pot, cf_nuclear, soec.name, lifetime_soec)

    # Energia capex opex AEM
    tot_capex_solar_aem, tot_opex_solar_aem, ciclo_aem_solar = solar.energy_total_capex_opex(aem.pot, cf_sol, aem.name, lifetime_aem)    
    tot_capex_WindOnshore_aem, tot_opex_WindOnshore_aem, ciclo_aem_WindOnshore = WindOnshore.energy_total_capex_opex(aem.pot, cf_WindOnshore, aem.name, lifetime_aem)
    tot_capex_WindOffshore_aem, tot_opex_WindOffshore_aem, ciclo_aem_WindOffshore = WindOffshore.energy_total_capex_opex(aem.pot, cf_WindOffshore, aem.name, lifetime_aem)
    tot_capex_nuclear_aem, tot_opex_nuclear_aem, ciclo_aem_nuclear = nuclear.energy_total_capex_opex(aem.pot, cf_nuclear, aem.name, lifetime_aem)

    #########
    ####### Eletrolisador Capex e opex ##### Busco na classe o valor do meu capex e opex total
    tot_cap_pem, tot_op_pem = pem.electrolyser_capex_opex()
    tot_cap_alk, tot_op_alk = alk.electrolyser_capex_opex()
    tot_cap_soec, tot_op_soec = soec.electrolyser_capex_opex()
    tot_cap_aem, tot_op_aem = aem.electrolyser_capex_opex()

    ## producao de H2
    # PEM Energias
    wh2_pem_solar = wh2(pem.pot, pem_energy_prod1kg, pem.name, cf_sol)
    wh2_pem_WindOnshore = wh2(pem.pot, pem_energy_prod1kg, pem.name, cf_WindOnshore)
    wh2_pem_WindOffshore = wh2(pem.pot, pem_energy_prod1kg, pem.name, cf_WindOffshore)
    wh2_pem_nuclear = wh2(pem.pot, pem_energy_prod1kg, pem.name, cf_nuclear)

    # Alkalino producao anual h2
    wh2_alk_solar = wh2(alk.pot, alk_energy_prod1kg, alk.name, cf_sol)
    wh2_alk_WindOnshore = wh2(alk.pot, alk_energy_prod1kg, alk.name, cf_WindOnshore)
    wh2_alk_WindOffShore = wh2(alk.pot, alk_energy_prod1kg, alk.name, cf_WindOffshore)
    wh2_alk_nuclear = wh2(alk.pot, alk_energy_prod1kg, alk.name, cf_nuclear)

    # SOEC producao anual h2
    wh2_soec_solar = wh2(soec.pot, soec_energy_prod1kg, soec.name,cf_sol)
    wh2_soec_WindOnshore = wh2(soec.pot, soec_energy_prod1kg, soec.name, cf_WindOnshore)
    wh2_soec_WindOffshore = wh2(soec.pot, soec_energy_prod1kg, soec.name, cf_WindOffshore)
    wh2_soec_nuclear = wh2(soec.pot, soec_energy_prod1kg, soec.name, cf_nuclear)

    # AEM producao anual h2
    wh2_aem_solar = wh2(aem.pot, aem_energy_prod1kg, aem.name, cf_sol)
    wh2_aem_WindOnshore = wh2(aem.pot, aem_energy_prod1kg, aem.name, cf_WindOnshore)
    wh2_aem_WindOffshore = wh2(aem.pot, aem_energy_prod1kg, aem.name, cf_WindOffshore)
    wh2_aem_nuclear = wh2(aem.pot, aem_energy_prod1kg, aem.name, cf_nuclear)


    ### Calculo lcoh
    # Pem
    lcoh_pem_pv = lcoh(tot_cap_pem, tot_op_pem, tot_capex_solar_pem, tot_opex_solar_pem, ciclo_pem_solar, wh2_pem_solar, t, pem.name, solar.name, wacc)
    lcoh_pem_WindOnshore = lcoh(tot_cap_pem, tot_op_pem, tot_capex_WindOnshore_pem, tot_opex_WindOnshore_pem, ciclo_pem_WindOnshore, wh2_pem_WindOnshore, t, pem.name, WindOnshore.name, wacc)
    lcoh_pem_WindOffshore = lcoh(tot_cap_pem, tot_op_pem, tot_capex_WindOffshore_pem, tot_opex_WindOffshore_pem, ciclo_pem_WindOffshore, wh2_pem_WindOffshore, t, pem.name, WindOffshore.name, wacc)
    lcoh_pem_nuclear = lcoh(tot_cap_pem, tot_op_pem, tot_capex_nuclear_pem, tot_opex_nuclear_pem, ciclo_pem_nuclear, wh2_pem_nuclear, t, pem.name, nuclear.name, wacc)

    # Alkalino
    lcoh_alk_pv = lcoh(tot_cap_alk, tot_op_alk, tot_capex_solar_alk, tot_opex_solar_alk, ciclo_alk_solar, wh2_alk_solar, t, alk.name, solar.name, wacc)
    lcoh_alk_WindOnshore = lcoh(tot_cap_alk, tot_op_alk, tot_capex_WindOnshore_alk, tot_opex_WindOnshore_alk, ciclo_alk_WindOnshore, wh2_alk_WindOnshore,t, alk.name, WindOnshore.name, wacc)
    lcoh_alk_WindOffshore = lcoh(tot_cap_alk, tot_op_alk, tot_capex_WindOffshore_alk, tot_opex_WindOffshore_alk, ciclo_alk_WindOffshore, wh2_alk_WindOffShore,t, alk.name, WindOffshore.name, wacc)
    lcoh_alk_nuclear = lcoh(tot_cap_alk, tot_op_alk, tot_capex_nuclear_alk, tot_opex_nuclear_alk, ciclo_alk_nuclear, wh2_alk_nuclear,t, alk.name, nuclear.name, wacc)

    # SOEC
    lcoh_soec_pv = lcoh(tot_cap_soec, tot_op_soec, tot_capex_solar_soec, tot_opex_solar_soec, ciclo_soec_solar, wh2_soec_solar, t, soec.name, solar.name, wacc)
    lcoh_soec_WindOnshore = lcoh(tot_cap_soec, tot_op_soec, tot_capex_WindOnshore_soec, tot_opex_WindOnshore_soec, ciclo_soec_WindOnshore, wh2_soec_WindOnshore, t, soec.name, WindOnshore.name, wacc)
    lcoh_soec_WindOffshore = lcoh(tot_cap_soec, tot_op_soec, tot_capex_WindOffshore_soec, tot_opex_WindOffshore_soec, ciclo_soec_WindOffshore, wh2_soec_WindOffshore, t, soec.name, WindOffshore.name, wacc)
    lcoh_soec_nuclear = lcoh(tot_cap_soec, tot_op_soec, tot_capex_nuclear_soec, tot_opex_nuclear_soec, ciclo_soec_nuclear, wh2_soec_nuclear, t, soec.name, nuclear.name, wacc)
    
    # AEM
    lcoh_aem_pv = lcoh(tot_cap_aem, tot_op_aem, tot_capex_solar_aem, tot_opex_solar_aem, ciclo_aem_solar, wh2_aem_solar, t, aem.name, solar.name, wacc)
    lcoh_aem_WindOnshore = lcoh(tot_cap_aem, tot_op_aem, tot_capex_WindOnshore_aem, tot_opex_WindOnshore_aem, ciclo_aem_WindOnshore, wh2_aem_WindOnshore, t, aem.name, WindOnshore.name, wacc)
    lcoh_aem_WindOffshore = lcoh(tot_cap_aem, tot_op_aem, tot_capex_WindOffshore_aem, tot_opex_WindOffshore_aem, ciclo_aem_WindOffshore, wh2_aem_WindOffshore, t, aem.name, WindOffshore.name, wacc)
    lcoh_aem_nuclear = lcoh(tot_cap_aem, tot_op_aem, tot_capex_nuclear_aem, tot_opex_nuclear_aem, ciclo_aem_nuclear, wh2_aem_nuclear, t, aem.name, nuclear.name, wacc)


    print('\n')
    print(f'Solar PEM LCOH = {lcoh_pem_pv:.2f} $/kg')
    print(f'WindOnshore PEM LCOH = {lcoh_pem_WindOnshore:.2f} $/kg')
    print(f'WindOffshore PEM LCOH = {lcoh_pem_WindOffshore:.2f} $/kg')
    print(f'Nuclear PEM LCOH = {lcoh_pem_nuclear:.2f} $/kg')
    print('\n')
    print(f'Solar AWE LCOH = {lcoh_alk_pv:.2f} $/kg')
    print(f'WindOnshore AWE LCOH = {lcoh_alk_WindOnshore:.2f} $/kg')
    print(f'WindOffshore AWE LCOH = {lcoh_alk_WindOffshore:.2f} $/kg')
    print(f'Nuclear AWE LCOH = {lcoh_alk_nuclear:.2f} $/kg')
    print('\n')
    print(f'Solar SOEC LCOH = {lcoh_soec_pv:.2f} $/kg')
    print(f'WindOnshore SOEC LCOH = {lcoh_soec_WindOnshore:.2f} $/kg')
    print(f'WindOffshore SOEC LCOH = {lcoh_soec_WindOffshore:.2f} $/kg')
    print(f'Nuclear SOEC LCOH = {lcoh_soec_nuclear:.2f} $/kg')
    print('\n')
    print(f'Solar AEM LCOH = {lcoh_aem_pv:.2f} $/kg')
    print(f'WindOnshore AEM LCOH = {lcoh_aem_WindOnshore:.2f} $/kg')
    print(f'WindOffshore AEM LCOH = {lcoh_aem_WindOffshore:.2f} $/kg')
    print(f'Nuclear AEM LCOH = {lcoh_aem_nuclear:.2f} $/kg')    


    plot_graph(lcoh_pem_pv, lcoh_pem_WindOnshore, lcoh_pem_WindOffshore, lcoh_pem_nuclear, lcoh_alk_pv, lcoh_alk_WindOnshore,lcoh_alk_WindOffshore, lcoh_alk_nuclear, 
               lcoh_soec_pv, lcoh_soec_WindOnshore, lcoh_soec_WindOffshore, lcoh_soec_nuclear, lcoh_aem_pv, lcoh_aem_WindOnshore, lcoh_aem_WindOffshore, lcoh_aem_nuclear, year)
    
    write_txt(lcoh_pem_pv, lcoh_pem_WindOnshore, lcoh_pem_WindOffshore, lcoh_pem_nuclear,
          lcoh_alk_pv, lcoh_alk_WindOnshore, lcoh_alk_WindOffshore, lcoh_alk_nuclear,
          lcoh_soec_pv, lcoh_soec_WindOnshore, lcoh_soec_WindOffshore, lcoh_soec_nuclear,
          lcoh_aem_pv, lcoh_aem_WindOnshore, lcoh_aem_WindOffshore, lcoh_aem_nuclear, year)
    
    #write_excel()
    
def main():
    parameters_present()
    parameters_2030()
    parameters_2050()

if __name__ == '__main__':
    main()
