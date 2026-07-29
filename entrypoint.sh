#!/bin/sh

echo "Aguardando banco de dados..."

sleep 5

echo "Executando migrations..."
flask db upgrade

echo "Iniciando aplicação..."
python app.py