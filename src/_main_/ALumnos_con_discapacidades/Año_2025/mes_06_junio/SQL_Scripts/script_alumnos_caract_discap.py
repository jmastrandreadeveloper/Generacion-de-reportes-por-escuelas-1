import pandas as pd
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..' , '..' , '..'))
sys.path.append(project_root)
import src.tools.utils as u
import src.tools.conectDB as db
from src.tools.print_dataframe import print_dataframe as printDF 

def scriptSQL_nominal_alumnos_caractersisticas_discapacidades(lista_de_niveles , lista_de_cursos):
    
    script = """
    -- SET @fecha_desde = '2009-06-01';
    -- SET @fecha_hasta = '2010-05-31';

    SELECT
    CONCAT(e.cue,'-',c.descripcion,'-',d.division) AS 'CUE-Curso-División',
    CONCAT(e.cue,'-',d.id) AS 'CUE-División_ID', 
    a.id AS 'Alumno_ID',
    p.documento AS 'DNI',
    p.apellido AS 'Apellido',
    p.nombre AS 'Nombre',
    sex.descripcion AS 'Sexo',
    p.fecha_nacimiento AS 'Fecha Nacimiento',
    TIMESTAMPDIFF(YEAR, p.fecha_nacimiento, CURDATE()) AS 'Edad',
    nac.descripcion AS 'Nacionalidad',
    COALESCE(cgm.descripcion, c.descripcion) AS 'CURSO_NORMALIZADO',
    c.descripcion AS 'Curso',
    d.division AS 'Division',
    d.id AS 'División_ID',
    ad.fecha_desde AS 'fecha_desde',
    ad.fecha_hasta AS 'fecha_hasta',
    tur.descripcion AS 'Turno',
    mo.descripcion AS 'Modalidad',
    n.descripcion AS 'Nivel',
    g.descripcion AS 'Gestion',
    s.nombre AS 'Supervisión',
    e.id AS 'ID_escuela',
    e.cue AS 'CUE',
    e.subcue AS 'subcue',
    CONCAT(COALESCE(e.cue), '0', COALESCE(e.subcue)) AS 'CUEAnexo',
    e.numero AS 'Numero_escuela',
    e.anexo AS 'Anexo',
    CONCAT(e.numero, '-', e.anexo) AS 'Número_Anexo',
    e.nombre AS 'Escuela',
    dep.descripcion AS 'Departamento',
    l.descripcion AS 'Localidad',
    z.descripcion AS 'zona',
    amb.descripcion AS 'AMBITO',
    reg.descripcion AS 'Regional',

    -- Características pivotadas
    MAX(CASE WHEN car.descripcion = 'Intelectual' THEN car_val.valor END) AS 'Intelectual',
    MAX(CASE WHEN car.descripcion = 'Mental' THEN car_val.valor END) AS 'Mental',
    MAX(CASE WHEN car.descripcion = 'Visual' THEN car_val.valor END) AS 'Visual',
    MAX(CASE WHEN car.descripcion = 'Auditiva' THEN car_val.valor END) AS 'Auditiva',
    MAX(CASE WHEN car.descripcion = 'Motriz' THEN car_val.valor END) AS 'Motriz',
    MAX(CASE WHEN car.descripcion = '¿Tiene un docente que lo acompaña en su escolaridad?' THEN car_val.valor END) AS 'Docente_Acompañante',
    MAX(CASE WHEN car.descripcion = 'Otra discapacidad' THEN car_val.valor END) AS 'Otra_Discapacidad',
    MAX(CASE WHEN car.descripcion = 'Múltiple' THEN car_val.valor END) AS 'Múltiple',
    MAX(CASE WHEN car.descripcion = 'CUD/Cert. Médico Espec.' THEN car_val.valor END) AS 'CUD_Certificado',
    MAX(CASE WHEN car.descripcion = '¿Tiene PPI?' THEN car_val.valor END) AS 'Tiene_PPI'

    FROM escuela e
    LEFT JOIN ambito amb ON e.ambito_id = amb.id 
    JOIN nivel ni ON ni.id = e.nivel_id 
    JOIN division d ON d.escuela_id = e.id AND d.fecha_baja IS NULL
    JOIN alumno_division ad ON ad.division_id = d.id AND ad.ciclo_lectivo = 2025 AND ad.fecha_hasta IS NULL   
    -- JOIN alumno_division ad ON ad.division_id = d.id AND ad.fecha_hasta IS not NULL AND ad.ciclo_lectivo = 2025 
    JOIN alumno a ON a.id = ad.alumno_id 
    JOIN persona p ON p.id = a.persona_id 
    JOIN curso c ON c.id = d.curso_id 
    JOIN nivel n ON n.id = e.nivel_id 
    JOIN dependencia g ON g.id = e.dependencia_id 
    LEFT JOIN localidad l ON e.localidad_id = l.id 
    LEFT JOIN departamento dep ON l.departamento_id = dep.id
    LEFT JOIN supervision s ON s.id = e.supervision_id 
    LEFT JOIN zona z ON z.id = e.zona_id 
    LEFT JOIN sexo sex ON sex.id = p.sexo_id 
    LEFT JOIN regional reg ON reg.id = e.regional_id 
    LEFT JOIN modalidad mo ON mo.id = d.modalidad_id 
    LEFT JOIN turno tur ON tur.id = d.turno_id
    LEFT JOIN nacionalidad nac ON nac.id = p.nacionalidad_id
    LEFT JOIN curso cgm ON cgm.id = ad.curso_id -- ME PERMITE TRAER EL ALUMNO DE UN GRADO MULTIPLE

    -- Características
    JOIN caracteristica_alumno car_al_id ON car_al_id.alumno_id = a.id AND car_al_id.fecha_hasta IS NULL 
    JOIN caracteristica_valor car_val ON car_val.id = car_al_id.caracteristica_valor_id
    JOIN caracteristica car ON car.id = car_val.caracteristica_id
    JOIN caracteristica_tipo car_tipo ON car_tipo.id = car.caracteristica_tipo_id

    WHERE
    -- p.fecha_nacimiento BETWEEN CAST(@fecha_desde AS DATE) AND CAST(@fecha_hasta AS DATE)
    -- AND 
    car_tipo.descripcion IS NOT NULL
    AND 
    c.id IN (""" + str(lista_de_cursos) + """)
    AND
    n.id IN ( """ + str(lista_de_niveles) + """ ) 



    GROUP BY 
    a.id, p.documento, p.apellido, p.nombre, sex.descripcion, 
    p.fecha_nacimiento, nac.descripcion, c.descripcion, d.division,
    tur.descripcion, mo.descripcion, n.descripcion, g.descripcion,
    s.nombre, e.id, e.cue, e.subcue, e.numero, e.anexo, e.nombre, 
    dep.descripcion, l.descripcion, z.descripcion, amb.descripcion, reg.descripcion

    HAVING 
    `Intelectual` IS NOT NULL OR 
    `Mental` IS NOT NULL OR 
    `Visual` IS NOT NULL OR 
    `Auditiva` IS NOT NULL OR 
    `Motriz` IS NOT NULL OR 
    `Otra_Discapacidad` IS NOT NULL OR 
    `Múltiple` IS NOT NULL OR 
    `CUD_Certificado` IS NOT NULL OR 
    `Tiene_PPI` IS NOT NULL

    ORDER BY
    Nivel, 
    Gestion, 
    `Supervisión`,
    `Número_Anexo`,
    Alumno_ID


    ;    
    """

    #print(script)    
    
    return script

def ejecutarConsulta(script , db_connection):
    print('... ejecutando consulta ...')
    dF_discap = pd.read_sql_query(script, con = db_connection)
    # reemplazar Nan por 0 (cero)..
    dF_discap.fillna(0 , inplace=True)    
    return dF_discap

lista_de_niveles = " 2 , 8 , 24 , 26 "

# c.id IN	(	
					
# 					-- '1' 	, -- 1° AÑO NIVEL 3 (Sec. Or.)
# 					-- '2' 	, -- 2° AÑO NIVEL 3 (Sec. Or.)
# 					-- '3' 	, -- 3° AÑO NIVEL 3 (Sec. Or.)
# 					-- '4' 	, -- 4° AÑO NIVEL 3 (Sec. Or.)
# 					-- '5' 	, -- 5° AÑO NIVEL 3 (Sec. Or.)
# 					-- '6' 	, -- 6° AÑO NIVEL 3 (Sec. Or.)
					
# 					'7' 	, -- 1° GRADO NIVEL 2 (Primaria)
# 					'8' 	, -- 2° GRADO NIVEL 2 (Primaria)
# 					'9' 	, -- 3° GRADO NIVEL 2 (Primaria)
# 					'10' 	, -- 4° GRADO NIVEL 2 (Primaria)
# 					'11' 	, -- 5° GRADO NIVEL 2 (Primaria)
# 					'12' 	, -- 6° GRADO NIVEL 2 (Primaria)
# 					'13' 	, -- 7° GRADO NIVEL 2 (Primaria)
					
# 					'20' 	, -- Sala 5
# 					'21' 	  -- Sala 4
					
					
					
# 					-- '71' 	, -- GRADO MULTIPLE NIVEL 2 (Primaria)
					
# 					-- '14' 	, -- 1° AÑO NIVEL 3 (Sec. Tec.)
# 					-- '15' 	, -- 1° AÑO NIVEL 3 (Sec. Tec.)
# 					-- '16' 	, -- 1° AÑO NIVEL 3 (Sec. Tec.)
# 					-- '17' 	, -- 1° AÑO NIVEL 3 (Sec. Tec.)
# 					-- '18' 	, -- 1° AÑO NIVEL 3 (Sec. Tec.)
# 					-- '19' 	  -- 1° AÑO NIVEL 3 (Sec. Tec.)
# 				)

lista_de_cursos = " 7 , 8 , 9 , 10 , 11 , 12 , 13 , 20 , 21 "

PATH_files = 'E:/GitHub/python_data_analysis_v3/src/_main_/ALumnos_con_discapacidades/Año_2025/mes_06_junio/data/raw/'

df_ = ejecutarConsulta(scriptSQL_nominal_alumnos_caractersisticas_discapacidades( lista_de_niveles ,  lista_de_cursos ) , db.conectarseAlaBD())
u.guardar_dataframe_a_csv(df_,'/src/_main_/ALumnos_con_discapacidades/Año_2025/mes_06_junio/data/raw/_df_nominal_alumnos_con_discapacidades.csv')
#printDF('nominal con discapacidades - ' , df_,numfilas = 20)


print('... fin del script ...')
