FROM python:3.7.4

ADD ex_1.py /
ADD test_ex_1.py /

CMD [ "python3", "./ex_1.py" ] 