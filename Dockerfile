FROM python
COPY . /approval_predictor
WORKDIR /approval_predictor
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit","run","final_model.py"]