import pendulum
# Airflow 3.0 부터 아래 경로로 import 합니다.
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

# Airflow 2.10.5 이하 버전에서 실습시 아래 경로에서 import 하세요.
#from airflow.operators.bash import BashOperator
#from airflow import DAG

with DAG(
    dag_id="dags_bash_operator", # dag_id 는 보통 파일명을 따라감
    schedule="0 0 * * *", # 분 시 일 월 요일  # None,
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), #tz=UTC:=세계표준시, 9시간 늦게 설정되어 있음
    catchup=False, #catchup=False: 과거의 DAG 실행을 건너뛰고 최신 실행만 수행
    # dagrun_timeout=datetime.timedelta(minutes=60), #DAG 실행 제한 시간 - 60분 이상 걸리면 실패 처리
    # tags=["example", "example2", "example3"], 
    # params={"example_key": "example_value"}, #task에 공통적으로 넘겨줄 파라미터들
) as dag:
    bash_t1 = BashOperator( #task 객체명 bash_t1
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME; echo good", #$HOSTNAME 이라는 환경변수 출력
    )

    # bash_t3 = BashOperator(
    #     task_id="bash_t3",
    #     bash_command="echo $HOSTNAME; echo good",
    # )

    # bash_t4 = BashOperator(
    #     task_id="bash_t4",
    #     bash_command="echo $HOSTNAME; echo good",
    # )

    bash_t1 >> bash_t2  #태스크들의 실행 순서 관계 적어주기  t1->t2->t3->t4 순으로 실행됨
    # bash_t1 >> bash_t2 >> bash_t3 >> bash_t4 #태스크들의 실행 순서 관계 적어주기  t1->t2->t3->t4 순으로 실행됨