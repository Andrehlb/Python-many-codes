# Agenda-Planner Estudos 26/06/2025
from datetime import datetime, timedelta
import pandas as pd
# Removed ace_tools import as it could not be resolved

# Data de início do planner
start_date = datetime.strptime("2025-06-24", "%Y-%m-%d")

# Estrutura da agenda semanal com foco em stacks e projetos
agenda = {
    "Segunda": ["CS50P (1h)", "Portal de Ingressos - Back-end ou Front-end (2h)"],
    "Terça": ["Python Developer DIO (2h)", "Modelagem de Dados com PostgreSQL (1h)"],
    "Quarta": ["AdaTech Back-End (2h)", "Revisar Multigeracional ou IA Generativa AWS (1h)"],
    "Quinta": ["Portal de Ingressos - Front-end React (2h)", "Ajustes UI/UX ou rotas"],
    "Sexta": ["IA Generativa AWS (1h)", "LinkedIn/GitHub Update ou estudo de vagas (1h)"],
    "Sábado": ["Revisão geral + push GitHub + testes (2h+)", "Deploy AWS / CI básico"],
    "Domingo": ["Livre ou aprofundamento técnico (Docker, CI/CD, PostgreSQL, etc)"]
}

# Gerar o planner para 2 semanas a partir da data inicial
planner = []
for i in range(14):
    day = start_date + timedelta(days=i)
    weekday_name = day.strftime("%A")
    day_name_pt = {
        "Monday": "Segunda",
        "Tuesday": "Terça",
        "Wednesday": "Quarta",
        "Thursday": "Quinta",
        "Friday": "Sexta",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }[weekday_name]
    
    atividades = agenda.get(day_name_pt, [])
    planner.append({
        "Data": day.strftime("%d/%m/%Y"),
        "Dia da Semana": day_name_pt,
        "Atividades Planejadas": " / ".join(atividades)
    })

df_planner = pd.DataFrame(planner)
# Display the dataframe using Pandas' built-in method
print("Planner de Estudos - 2 Semanas")
print(df_planner)
