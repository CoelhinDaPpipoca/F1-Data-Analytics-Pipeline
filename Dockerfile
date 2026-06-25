FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD python main.py && streamlit run dashboard.py --server.address=0.0.0.0