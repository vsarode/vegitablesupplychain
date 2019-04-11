#!/usr/bin/env bash
export PYTHONPATH=$pwd;
export DJANGO_SETTINGS_MODULE=vegitablesupplychain.db.settings.local;
python vegitablesupplychain/conf/service_app.py