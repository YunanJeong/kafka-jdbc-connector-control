# kafka-jdbc-connector-control

- 데이터 소스 db구조는 제각각,백의DB,천의Table에서 데이터를 편하게 긁어오자.
- JDBC Source Connector로 DB에서 데이터를 Kafka로 가져오는 경우
- 1테이블당 1커넥터 쓰는 구조
  - 커넥터 개수가 만단위가 될 수 있어서 JVM 관리 필수
  - whitelist, blacklist 옵션을 쓰면 단일 커넥터로 여러 테이블을 읽을 수 있지만,query 모드를 못쓰기 때문에 자유도가 급락한다.
- 그렇다고 아예 커넥터를 안쓰고 개별 Producer앱을 만들면
  - 어떻게든 구현은 되겠지만, 향후 운영난이도가 급상승
- 트레이드오프를 감안하여 적당할 때 사용해야 함

## tree

```
├──image/
│  ├─ Dockerfile
│  ├─ requirements.txt
│  └─ register.py
└─ connector-registrar/
   ├─ Chart.yaml
   ├─ values.yaml
   └─ templates/
      ├─ _helpers.tpl
      ├─ NOTES.txt
      └─ job.yaml
```