import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError

def main():

        st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
        email = st.text_input("Email Vendedor")
        data = st.date_input("Data da venda")
        hora = st.time_input("hora venda")
        valor = st.number_input("valor venda")
        quantidade = st.number_input("quantidade da venda")
        produto = st.selectbox("Produto:",["A","B", "C"])

        if st.button("Salvar"):
        
            try:
                data_hora = datetime.combine(data,hora)

                venda = Vendas(
                        email = email,
                        data=data_hora,
                        valor = valor,
                        quantidade = quantidade,
                        produto = produto
                )
                st.write(venda)
            except ValidationError as e:
                st.error(f"Deu erro{e}")

if __name__ == "__main__":
            main()