# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EstablecimientosEdparvularia2021(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    agno = models.FloatField(blank=True, null=True)
    id_estab = models.FloatField(blank=True, null=True)
    origen = models.FloatField(blank=True, null=True)
    nom_estab = models.CharField(max_length=254, blank=True, null=True)
    cod_reg_es = models.FloatField(blank=True, null=True)
    cod_pro_es = models.FloatField(blank=True, null=True)
    cod_com_es = models.FloatField(blank=True, null=True)
    nom_com_es = models.CharField(max_length=254, blank=True, null=True)
    cod_deprov = models.FloatField(blank=True, null=True)
    nom_deprov = models.CharField(max_length=254, blank=True, null=True)
    dependenci = models.FloatField(blank=True, null=True)
    rural_esta = models.FloatField(blank=True, null=True)
    estado_est = models.FloatField(blank=True, null=True)
    sc_men_si = models.FloatField(blank=True, null=True)
    sc_men_h = models.FloatField(blank=True, null=True)
    sc_men_m = models.FloatField(blank=True, null=True)
    sc_may_h = models.FloatField(blank=True, null=True)
    sc_may_m = models.FloatField(blank=True, null=True)
    med_men_si = models.FloatField(blank=True, null=True)
    med_men_h = models.FloatField(blank=True, null=True)
    med_men_m = models.FloatField(blank=True, null=True)
    med_may_si = models.FloatField(blank=True, null=True)
    med_may_h = models.FloatField(blank=True, null=True)
    med_may_m = models.FloatField(blank=True, null=True)
    nt1_si = models.FloatField(blank=True, null=True)
    nt1_h = models.FloatField(blank=True, null=True)
    nt1_m = models.FloatField(blank=True, null=True)
    nt2_si = models.FloatField(blank=True, null=True)
    nt2_h = models.FloatField(blank=True, null=True)
    nt2_m = models.FloatField(blank=True, null=True)
    n_total = models.FloatField(blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    numero = models.FloatField(blank=True, null=True)
    referencia = models.CharField(max_length=254, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Establecimientos_EdParvularia2021'


class PuntosMonumentosNacionales(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    cut_com = models.CharField(max_length=5, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=25, blank=True, null=True)
    comuna = models.CharField(max_length=25, blank=True, null=True)
    codigo = models.CharField(max_length=14, blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    coord_este = models.FloatField(blank=True, null=True)
    coord_nort = models.FloatField(blank=True, null=True)
    sup_ofc_mt = models.FloatField(blank=True, null=True)
    sup_ofc_ha = models.FloatField(blank=True, null=True)
    actualizac = models.DateField(blank=True, null=True)
    tipo_decre = models.CharField(max_length=37, blank=True, null=True)
    num_dec = models.BigIntegerField(blank=True, null=True)
    fch_dec = models.DateField(blank=True, null=True)
    pub_dec = models.DateField(blank=True, null=True)
    obs_dpa = models.CharField(max_length=254, blank=True, null=True)
    imagen = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Puntos_Monumentos_Nacionales'


class V4RecuadroChs(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    desc_field = models.CharField(db_column='desc_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'V4_Recuadro_CHS'


class V4LimiteInternacional50K(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    pais_c = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'V4_limite_internacional_50k'


class AtractivosTuristicos2020(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    codatrac = models.CharField(max_length=254, blank=True, null=True)
    jerarquia = models.CharField(max_length=254, blank=True, null=True)
    categoria = models.CharField(max_length=254, blank=True, null=True)
    tipo = models.CharField(max_length=254, blank=True, null=True)
    subtipo = models.CharField(max_length=254, blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    provincia = models.CharField(max_length=254, blank=True, null=True)
    comuna = models.CharField(max_length=254, blank=True, null=True)
    localidad = models.CharField(max_length=254, blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=254, blank=True, null=True)
    propiedad = models.CharField(max_length=254, blank=True, null=True)
    administra = models.CharField(max_length=254, blank=True, null=True)
    distcr = models.CharField(max_length=254, blank=True, null=True)
    cr = models.CharField(max_length=254, blank=True, null=True)
    distcc = models.CharField(max_length=254, blank=True, null=True)
    cc = models.CharField(max_length=254, blank=True, null=True)
    loc_urbana = models.CharField(max_length=254, blank=True, null=True)
    estacional = models.CharField(max_length=254, blank=True, null=True)
    uso_tur = models.CharField(max_length=254, blank=True, null=True)
    demanda = models.CharField(max_length=254, blank=True, null=True)
    servicios = models.CharField(max_length=254, blank=True, null=True)
    cod_reg = models.BigIntegerField(blank=True, null=True)
    cod_prov = models.BigIntegerField(blank=True, null=True)
    cod_com = models.BigIntegerField(blank=True, null=True)
    descripcio = models.CharField(max_length=254, blank=True, null=True)
    estado_1 = models.CharField(max_length=254, blank=True, null=True)
    point_x = models.FloatField(blank=True, null=True)
    point_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atractivos_turisticos_2020'


class CircuitosTuristicos2015(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    circuito = models.CharField(max_length=80, blank=True, null=True)
    ruta = models.CharField(max_length=50, blank=True, null=True)
    exten_km = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuitos _turisticos_2015'


class Ciudades2017(models.Model):
    idp = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    region = models.CharField(max_length=5, blank=True, null=True)
    nom_region = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=5, blank=True, null=True)
    nom_provin = models.CharField(max_length=25, blank=True, null=True)
    comuna = models.CharField(max_length=10, blank=True, null=True)
    nom_comuna = models.CharField(max_length=25, blank=True, null=True)
    urbano = models.CharField(max_length=35, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.CharField(max_length=6, blank=True, null=True)
    tot_person = models.FloatField(blank=True, null=True)
    hombres = models.FloatField(blank=True, null=True)
    mujeres = models.FloatField(blank=True, null=True)
    tot_viv = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudades_2017'


class Colegios2021(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    agno = models.FloatField(blank=True, null=True)
    rbd = models.FloatField(blank=True, null=True)
    dgv_rbd = models.FloatField(blank=True, null=True)
    nom_rbd = models.CharField(max_length=254, blank=True, null=True)
    tipo_sost = models.FloatField(blank=True, null=True)
    cod_reg_rb = models.FloatField(blank=True, null=True)
    nom_reg_rb = models.CharField(max_length=254, blank=True, null=True)
    cod_pro_rb = models.FloatField(blank=True, null=True)
    cod_com_rb = models.FloatField(blank=True, null=True)
    nom_com_rb = models.CharField(max_length=254, blank=True, null=True)
    cod_deprov = models.FloatField(blank=True, null=True)
    nom_deprov = models.CharField(max_length=254, blank=True, null=True)
    tipo_depen = models.FloatField(blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    numero = models.FloatField(blank=True, null=True)
    referencia = models.CharField(max_length=254, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    mat_parv = models.FloatField(blank=True, null=True)
    mat_bas_re = models.FloatField(blank=True, null=True)
    mat_bas_ad = models.FloatField(blank=True, null=True)
    mat_esp = models.FloatField(blank=True, null=True)
    mat_mhc_re = models.FloatField(blank=True, null=True)
    mat_mhc_ad = models.FloatField(blank=True, null=True)
    mat_mtp_re = models.FloatField(blank=True, null=True)
    mat_mtp_ad = models.FloatField(blank=True, null=True)
    mat_total = models.FloatField(blank=True, null=True)
    mat_hom_to = models.FloatField(blank=True, null=True)
    mat_muj_to = models.FloatField(blank=True, null=True)
    mat_si_tot = models.FloatField(blank=True, null=True)
    cur_sim_to = models.FloatField(blank=True, null=True)
    cur_comb_t = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colegios_2021'


class CompaniaBomberos(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    cut_cia = models.CharField(max_length=50, blank=True, null=True)
    compañia = models.CharField(max_length=50, blank=True, null=True)
    cut_cuerpo = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    id_2002 = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    id_2002_20 = models.CharField(max_length=10, blank=True, null=True)
    nombre_1 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compania_bomberos'


class Comunas2020(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    cut_reg = models.CharField(max_length=10, blank=True, null=True)
    cut_prov = models.CharField(max_length=10, blank=True, null=True)
    cut_com = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    comuna = models.CharField(max_length=50, blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunas_2020'


class Conurbaciones2017(models.Model):
    idp = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.BigIntegerField(blank=True, null=True)
    cod_region = models.FloatField(blank=True, null=True)
    nom_region = models.CharField(max_length=50, blank=True, null=True)
    conurb = models.CharField(max_length=50, blank=True, null=True)
    tot_person = models.FloatField(blank=True, null=True)
    hombres = models.FloatField(blank=True, null=True)
    mujeres = models.FloatField(blank=True, null=True)
    tot_viv = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conurbaciones_2017'


class CuartelesCarabineros(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre_reg = models.CharField(max_length=254, blank=True, null=True)
    nombre_pro = models.CharField(max_length=254, blank=True, null=True)
    nombre_com = models.CharField(max_length=254, blank=True, null=True)
    nombre_uni = models.CharField(max_length=254, blank=True, null=True)
    tipo_de_un = models.CharField(max_length=254, blank=True, null=True)
    tipo_de_vi = models.CharField(max_length=254, blank=True, null=True)
    nombre_de = models.CharField(max_length=254, blank=True, null=True)
    numero = models.CharField(max_length=254, blank=True, null=True)
    point_x = models.FloatField(blank=True, null=True)
    point_y = models.FloatField(blank=True, null=True)
    hecho = models.CharField(max_length=50, blank=True, null=True)
    rg = models.FloatField(blank=True, null=True)
    prefectura = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    zona = models.CharField(max_length=100, blank=True, null=True)
    uni_cod = models.CharField(max_length=5, blank=True, null=True)
    unid_encri = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuarteles_carabineros'


class CuerposBomberos(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid = models.BigIntegerField(blank=True, null=True)
    nombre_del = models.CharField(max_length=254, blank=True, null=True)
    tipo_de_vl = models.CharField(max_length=254, blank=True, null=True)
    numeració = models.CharField(max_length=254, blank=True, null=True)
    nombre_de = models.CharField(max_length=254, blank=True, null=True)
    comuna = models.CharField(max_length=254, blank=True, null=True)
    provincia = models.CharField(max_length=254, blank=True, null=True)
    región = models.CharField(max_length=254, blank=True, null=True)
    fid_cl_com = models.BigIntegerField(blank=True, null=True)
    id_2002 = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fid_cl_reg = models.BigIntegerField(blank=True, null=True)
    id_2002_20 = models.CharField(max_length=10, blank=True, null=True)
    nombre_1 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuerpos_bomberos'


class Embalses2016(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    codreg = models.CharField(max_length=3, blank=True, null=True)
    nomreg = models.CharField(max_length=50, blank=True, null=True)
    codcom = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    estcon = models.CharField(max_length=25, blank=True, null=True)
    año_contr = models.CharField(max_length=15, blank=True, null=True)
    nomcom = models.CharField(max_length=50, blank=True, null=True)
    alt_muro = models.BigIntegerField(blank=True, null=True)
    cota = models.BigIntegerField(blank=True, null=True)
    mxlocation = models.CharField(max_length=12, blank=True, null=True)
    mxsiteid = models.CharField(max_length=12, blank=True, null=True)
    fuente_inf = models.CharField(max_length=254, blank=True, null=True)
    propiet = models.CharField(max_length=254, blank=True, null=True)
    rut = models.CharField(max_length=254, blank=True, null=True)
    fuente_nat = models.CharField(max_length=254, blank=True, null=True)
    uso_embal = models.CharField(max_length=254, blank=True, null=True)
    tipo_embal = models.CharField(max_length=254, blank=True, null=True)
    mon_dga = models.CharField(max_length=30, blank=True, null=True)
    tamaño_em = models.CharField(max_length=30, blank=True, null=True)
    este_84 = models.BigIntegerField(blank=True, null=True)
    norte_84 = models.BigIntegerField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'embalses_2016'


class EstablecimientosSalud2021(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    c_ant = models.CharField(max_length=254, blank=True, null=True)
    c_vig = models.FloatField(blank=True, null=True)
    c_mad = models.CharField(max_length=254, blank=True, null=True)
    c_nmad = models.CharField(max_length=254, blank=True, null=True)
    c_reg = models.FloatField(blank=True, null=True)
    nom_reg = models.CharField(max_length=254, blank=True, null=True)
    c_depend = models.FloatField(blank=True, null=True)
    depen = models.CharField(max_length=254, blank=True, null=True)
    perenec = models.CharField(max_length=254, blank=True, null=True)
    tipo = models.CharField(max_length=254, blank=True, null=True)
    ambito = models.CharField(max_length=254, blank=True, null=True)
    urgencia = models.CharField(max_length=254, blank=True, null=True)
    certifica = models.CharField(max_length=254, blank=True, null=True)
    depen_a = models.CharField(max_length=254, blank=True, null=True)
    nivel = models.CharField(max_length=254, blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    c_com = models.CharField(max_length=254, blank=True, null=True)
    nom_com = models.CharField(max_length=254, blank=True, null=True)
    via = models.CharField(max_length=254, blank=True, null=True)
    numero = models.FloatField(blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    fono = models.CharField(max_length=254, blank=True, null=True)
    f_inicio = models.DateField(blank=True, null=True)
    f_reaper = models.CharField(max_length=254, blank=True, null=True)
    sapu = models.CharField(max_length=254, blank=True, null=True)
    f_cambio = models.CharField(max_length=254, blank=True, null=True)
    tipo_camb = models.CharField(max_length=254, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    prestador = models.CharField(max_length=254, blank=True, null=True)
    estado = models.CharField(max_length=254, blank=True, null=True)
    nivel_com = models.CharField(max_length=254, blank=True, null=True)
    modalidad = models.CharField(max_length=254, blank=True, null=True)
    coord_x = models.FloatField(blank=True, null=True)
    coord_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establecimientos_salud_2021'


class EstacionesMeteorologicas(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    region = models.CharField(max_length=254, blank=True, null=True)
    cod_bna = models.CharField(max_length=254, blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    estado = models.CharField(max_length=254, blank=True, null=True)
    este_84 = models.BigIntegerField(blank=True, null=True)
    norte_84 = models.BigIntegerField(blank=True, null=True)
    cod_cuen = models.CharField(max_length=12, blank=True, null=True)
    cod_subc = models.CharField(max_length=10, blank=True, null=True)
    cod_ssubc = models.CharField(max_length=10, blank=True, null=True)
    nom_ssubc = models.CharField(max_length=100, blank=True, null=True)
    nom_cuen = models.CharField(max_length=100, blank=True, null=True)
    nom_subc = models.CharField(max_length=100, blank=True, null=True)
    cine_reg = models.CharField(max_length=10, blank=True, null=True)
    cod_reg = models.BigIntegerField(blank=True, null=True)
    nom_reg = models.CharField(max_length=50, blank=True, null=True)
    cine_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_prov = models.BigIntegerField(blank=True, null=True)
    nom_prov = models.CharField(max_length=50, blank=True, null=True)
    cine_com = models.CharField(max_length=10, blank=True, null=True)
    cod_com = models.BigIntegerField(blank=True, null=True)
    nom_com = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estaciones_meteorologicas'


class IntitucionesSuperiores2020(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    año = models.FloatField(blank=True, null=True)
    cod_inst = models.FloatField(blank=True, null=True)
    tipo_inst = models.CharField(max_length=254, blank=True, null=True)
    nombre_ins = models.CharField(max_length=254, blank=True, null=True)
    nombre_inm = models.CharField(max_length=254, blank=True, null=True)
    cod_region = models.FloatField(blank=True, null=True)
    región = models.CharField(max_length=254, blank=True, null=True)
    cod_provin = models.FloatField(blank=True, null=True)
    provincia = models.CharField(max_length=254, blank=True, null=True)
    cod_comuna = models.FloatField(blank=True, null=True)
    comuna = models.CharField(max_length=254, blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    numero_di = models.FloatField(blank=True, null=True)
    lugar_refe = models.CharField(max_length=254, blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intituciones_superiores_2020'


class JardinesInfantilesIntegra(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    fuente = models.CharField(max_length=254, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    comuna = models.CharField(max_length=254, blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    modalidad = models.CharField(max_length=254, blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    telefono = models.FloatField(blank=True, null=True)
    zona = models.CharField(max_length=254, blank=True, null=True)
    macronivel = models.CharField(max_length=254, blank=True, null=True)
    cap_sc = models.FloatField(blank=True, null=True)
    cap_pa = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jardines_infantiles_integra'


class Museos(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    cut_com = models.CharField(max_length=5, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=25, blank=True, null=True)
    comuna = models.CharField(max_length=25, blank=True, null=True)
    aid_rmc = models.FloatField(blank=True, null=True)
    fecha_mod = models.CharField(max_length=254, blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    tipo_inst = models.CharField(max_length=254, blank=True, null=True)
    depend = models.CharField(max_length=254, blank=True, null=True)
    subdepend = models.CharField(max_length=254, blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    arq = models.CharField(max_length=254, blank=True, null=True)
    arte = models.CharField(max_length=254, blank=True, null=True)
    ciencias = models.CharField(max_length=254, blank=True, null=True)
    etno = models.CharField(max_length=254, blank=True, null=True)
    historia = models.CharField(max_length=254, blank=True, null=True)
    hist_nat = models.CharField(max_length=254, blank=True, null=True)
    paleo = models.CharField(max_length=254, blank=True, null=True)
    otra = models.CharField(max_length=254, blank=True, null=True)
    cobro_ent = models.CharField(max_length=254, blank=True, null=True)
    act_ext = models.CharField(max_length=254, blank=True, null=True)
    visit_guia = models.CharField(max_length=254, blank=True, null=True)
    audioguias = models.CharField(max_length=254, blank=True, null=True)
    cursos = models.CharField(max_length=254, blank=True, null=True)
    mat_didact = models.CharField(max_length=254, blank=True, null=True)
    biblioteca = models.CharField(max_length=254, blank=True, null=True)
    real_virt = models.CharField(max_length=254, blank=True, null=True)
    mh = models.CharField(max_length=254, blank=True, null=True)
    zt = models.CharField(max_length=254, blank=True, null=True)
    mon_arq = models.CharField(max_length=254, blank=True, null=True)
    sn = models.CharField(max_length=254, blank=True, null=True)
    ich = models.CharField(max_length=254, blank=True, null=True)
    zch = models.CharField(max_length=254, blank=True, null=True)
    spm = models.CharField(max_length=254, blank=True, null=True)
    pat_no_pro = models.CharField(max_length=254, blank=True, null=True)
    no_patrim = models.CharField(max_length=254, blank=True, null=True)
    web = models.CharField(max_length=254, blank=True, null=True)
    web_nac = models.CharField(max_length=254, blank=True, null=True)
    web_rmc = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    telefono = models.FloatField(blank=True, null=True)
    actualiza = models.CharField(max_length=254, blank=True, null=True)
    imagen = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'museos'


class Pdi(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    num = models.FloatField(blank=True, null=True)
    institucio = models.CharField(max_length=254, blank=True, null=True)
    tipo_unid = models.CharField(max_length=254, blank=True, null=True)
    sigla = models.CharField(max_length=254, blank=True, null=True)
    categoria = models.CharField(max_length=254, blank=True, null=True)
    nom_unid = models.CharField(max_length=254, blank=True, null=True)
    nom_vial = models.CharField(max_length=254, blank=True, null=True)
    num_2 = models.FloatField(blank=True, null=True)
    comuna = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    num_reg = models.CharField(max_length=254, blank=True, null=True)
    point_x = models.FloatField(blank=True, null=True)
    point_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdi'


class PlanCuadranteCarabineros(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    cua_codigo = models.CharField(max_length=11, blank=True, null=True)
    cua_sup = models.FloatField(blank=True, null=True)
    comuna = models.CharField(max_length=254, blank=True, null=True)
    unidad = models.CharField(max_length=254, blank=True, null=True)
    destacamen = models.CharField(max_length=254, blank=True, null=True)
    prefectura = models.CharField(max_length=254, blank=True, null=True)
    zona = models.CharField(max_length=254, blank=True, null=True)
    num_cuad = models.CharField(max_length=254, blank=True, null=True)
    cua_descri = models.CharField(max_length=254, blank=True, null=True)
    cua_tipo = models.CharField(max_length=254, blank=True, null=True)
    cua_estado = models.CharField(max_length=254, blank=True, null=True)
    cua_ftermi = models.CharField(max_length=254, blank=True, null=True)
    uni_codigo = models.CharField(max_length=254, blank=True, null=True)
    cua_ano = models.CharField(max_length=254, blank=True, null=True)
    cod_aupol = models.CharField(max_length=254, blank=True, null=True)
    com_codigo = models.CharField(max_length=254, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    cod_destac = models.CharField(max_length=18, blank=True, null=True)
    tooltip = models.CharField(max_length=254, blank=True, null=True)
    cod = models.CharField(max_length=20, blank=True, null=True)
    sup_km2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan_cuadrante_carabineros'


class PlantasDesaladoras(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    planta = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    compa_a = models.CharField(db_column='compa��a', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    operaci_n = models.CharField(db_column='operaci�n', max_length=254, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    l_s_desala = models.FloatField(blank=True, null=True)
    l_s_mar_im = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=254, blank=True, null=True)
    estado = models.CharField(max_length=254, blank=True, null=True)
    region = models.CharField(max_length=254, blank=True, null=True)
    observacio = models.CharField(max_length=254, blank=True, null=True)
    este_84 = models.IntegerField(blank=True, null=True)
    norte_84 = models.IntegerField(blank=True, null=True)
    num_mapa = models.IntegerField(blank=True, null=True)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    num_mapa2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plantas_desaladoras'


class PoligonosMonumentosNacionales(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    cut_com = models.CharField(max_length=5, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=25, blank=True, null=True)
    comuna = models.CharField(max_length=25, blank=True, null=True)
    codigo = models.CharField(max_length=14, blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    coord_este = models.FloatField(blank=True, null=True)
    coord_nort = models.FloatField(blank=True, null=True)
    sup_ofc_mt = models.FloatField(blank=True, null=True)
    sup_ofc_ha = models.FloatField(blank=True, null=True)
    actualizac = models.DateField(blank=True, null=True)
    tipo_decre = models.CharField(max_length=37, blank=True, null=True)
    num_dec = models.BigIntegerField(blank=True, null=True)
    fch_dec = models.DateField(blank=True, null=True)
    pub_dec = models.DateField(blank=True, null=True)
    obs_dpa = models.CharField(max_length=254, blank=True, null=True)
    imagen = models.CharField(max_length=254, blank=True, null=True)
    st_area_sh = models.FloatField(blank=True, null=True)
    st_length_field = models.FloatField(db_column='st_length_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'poligonos_Monumentos_Nacionales'


class Provincias2020(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    cut_reg = models.CharField(max_length=10, blank=True, null=True)
    cut_prov = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincias_2020'


class Regiones2020(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    cut_reg = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regiones_2020'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class TerritoriosDeSalud(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    cod_ss = models.FloatField(blank=True, null=True)
    nom_ss = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'territorios_de_salud'


class ZonasClimaticasKoppen30Nov2016(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    koppen_fin = models.CharField(max_length=254, blank=True, null=True)
    denominaci = models.CharField(max_length=254, blank=True, null=True)
    pp_mm = models.FloatField(blank=True, null=True)
    tmed = models.FloatField(blank=True, null=True)
    alt_min = models.FloatField(blank=True, null=True)
    alt_max = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas_climaticas_koppen_30_nov_2016'


class ZonasTuristicas2020(models.Model):
    idpk = models.AutoField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    región = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas_turisticas_2020'
