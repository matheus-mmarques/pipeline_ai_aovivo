import streamlit as st
from datetime import datetime, time

def main():

        st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
        email = st.text_input("Email Vendedor")
        data = st.date_input("Data da venda")
        hora = st.time_input("hora venda")
        valor = st.number_input("valor venda")
        quantidade = st.number_input("quantidade da venda")
        produto = st.selectbox("Produto:",["A","B", "C"])

        if st.button("Salvar"):
                
                data_hora = datetime.combine(data,hora)
                st.write("**Dados da venda:**")
                st.write(f"Email do vendedor {email}")
                st.write(f"Data e Hora da Compra {data_hora}")
                st.write(f"Valor da venda: R$ {valor:.2f}")
                st.write(f"Quantidade: {quantidade}")
                st.write(f"Produto: {produto}") 
if __name__ == "__main__":
            main()