#!/bin/bash
activate () {
  . venv/bin/activate
}

export FLASK_DEBUG=true
export APP=routes
echo $$
flask --app $APP run

