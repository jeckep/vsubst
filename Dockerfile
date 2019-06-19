FROM python:2-alpine
COPY subst.py /subst.py
WORKDIR /

ENTRYPOINT ["python", "subst.py"]