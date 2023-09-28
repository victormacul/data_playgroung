import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data (Substitute the path with the actual path to your Excel file)
df = pd.read_csv('c.csv')
df['Fim do Contrato'] = pd.to_datetime(df['Fim do Contrato'])

# Extract year and month
df['Year'] = df['Fim do Contrato'].dt.year
df['Month'] = df['Fim do Contrato'].dt.month
df['Year_Month'] = df['Year'].astype(str) + '-' + df['Month'].astype(str).str.zfill(2)

# Streamlit App
st.title("Análise de Cancelamentos da Ana Health")

# Plot 1: Distribution of Cancellations Over Time
st.subheader("Distribuição dos Cancelamentos ao Longo do Tempo")
cancellations_by_time = df['Year_Month'].value_counts().sort_index().reset_index()
cancellations_by_time.columns = ['Year_Month', 'Count']
fig1 = px.line(cancellations_by_time, x='Year_Month', y='Count', title='Distribuição dos Cancelamentos ao Longo do Tempo')
st.plotly_chart(fig1)

# Plot 2: Main Reasons for Cancellation
st.subheader("Principais Motivos para Cancelamento")
reasons_for_loss = df['Motivo da perda'].value_counts().reset_index()
reasons_for_loss.columns = ['Reason', 'Count']
fig2 = px.bar(reasons_for_loss, x='Count', y='Reason', orientation='h', title='Principais Motivos para Cancelamento')
st.plotly_chart(fig2)

# Plot 3: Distribution of Cancellations by Subscription Type
st.subheader("Distribuição dos Cancelamentos por Tipo de Assinatura")
subscription_type_counts = df['Tipo de Assinatura'].value_counts().reset_index()
subscription_type_counts.columns = ['Subscription Type', 'Count']
fig3 = px.bar(subscription_type_counts, x='Subscription Type', y='Count', title='Distribuição dos Cancelamentos por Tipo de Assinatura')
st.plotly_chart(fig3)

# Plot 4: Relation Between Health Plan and Cancellations
st.subheader("Relação entre o Plano de Saúde e os Cancelamentos")
health_plan_counts = df['Plano de Saúde'].value_counts().reset_index()
health_plan_counts.columns = ['Health Plan', 'Count']
fig4 = px.bar(health_plan_counts, x='Count', y='Health Plan', orientation='h', title='Relação entre o Plano de Saúde e os Cancelamentos')
st.plotly_chart(fig4)