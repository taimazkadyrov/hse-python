#!/bin/bash

# Перебираем все директории task_XX
for task_dir in sem_01/task_*/; do
    echo "Running tests in $task_dir"
    # Переходим в директорию и запускаем тесты
    (cd "$task_dir" && python -m pytest test.py -v)
done