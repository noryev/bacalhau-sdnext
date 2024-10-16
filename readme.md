

Bacalhau startup command

bacalhau run \
  --id-only \
  --wait \
  --input http://127.0.0.1:5000/process \
  --input ./sdnext_job.py=/sdnext_job.py \
  --network=full \
  python:3.9 \
  -- python3 /sdnext_job.py