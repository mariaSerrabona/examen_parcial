import Tarea_1

#definimos el método para que nos retorne los datos de cada fila

def separar_filas (fila, dataFrame):
    df_date=df._get_value(fila,'date')
    df_hour=df._get_value(fila,'hour')
    df_id_lead=df._get_value(fila,'id_lead')
    df_id_user=df._get_value(fila,'id_user')
    df_gclid=df._get_value(fila,'gclid')
    df_lead_type=df._get_value(fila,'lead_type')
    df_result=df._get_value(fila,'result')

    return df_date,df_hour, df_id_lead, df_id_user, df_gclid, df_lead_type, df_result