
FROM python:3.11-slim
RUN pip3 install streamlit
COPY . / 
CMD ["streamlit","run","/cpu"]
CMD ["tail","-f","/dev/null"]

