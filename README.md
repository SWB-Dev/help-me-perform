# help-me-perform

A simple framework for tracking tasks, due dates, stakeholders, and generating annoying status reports.

# Design

## Enums

### STATUS

- COMPLETE
- IN_PROGRESS
- SCOPING
- REQUESTED

### GRANULARITY

- INDIVIDUAL
- GROUP
- DEPARTMENT
- ORGANIZATION

## Data Models

### Task

- STATUS -> ENUM
- NAME -> STRING
- DESCRIPTION -> NAME
- DUE_DATE -> DATE
- REQUESTER -> STAKEHOLDER
- SR_INCLUDE -> BOOL
  - Status Report Include: Flagging used to determine if this task should be included on the generated Status Report.
- LAST_SR_DATE -> DATE
  - The last date this task was included on a Status Report.
- LAST_UPDATED -> DATE
- KPIS -> LIST\<KPI>
  - The KPIs/metrics this task contributes to.

### Subtask

- TASK -> TASK
- DESCRIPTION -> STRING
- STATUS -> ENUM
- START_DATE -> DATE
- END_DATE -> DATE
- SR_INCLUDE -> BOOL
- KPIS -> LIST\<KPI>

### Stakeholder

- NAME -> STRING
- EMAIL -> STRING
- GROUP -> GROUP
- IS_LEADER -> BOOL
- TASKS -> LIST\<TASK>

### Group

- NAME -> STRING
- LEADER -> STAKEHOLDER
- AUTHORITIES -> LIST\<STAKEHOLDER>

### KPI

- NAME -> STRING
- DESCRIPTION -> STRING
- GROUPS -> LIST\<GROUP>
- GRANULARITY -> ENUM

### Status Reports

- REPORT_DATE -> DATE
- TASK -> TASK
- SUBTASK -> SUBTASK
- SEND_TO -> LIST\<STAKEHOLDER | GROUP>

## CLI - R1

\> hmp tasks

\[Status] \<Task Name> \<Due Date>

\> hmp tasks -verbose

\[Status] \<Task Name> \<Task Description> \<Due Date> \<Requester> \<Group> \<Last Updated> \<Include On Status Report> \<>

\> hmp generate -group \<group name | all> -granularity \<space-separated-list | all>