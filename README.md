## Setup

Activate Miniforge

```bash
miniforge_activate_base # alias
```

Install the Conda environment.

```bash
mamba env create -f conda.yaml
```

## Usage

Activate Miniforge.

```
miniforge_activate_base # alias
```

Activate the Conda environment.

```bash
conda activate cgatcore
```

Run the pipeline.

```bash
python pipeline_logging.py make
# alternative to run on login node (avoids job queue)
python pipeline_logging.py make --local
```

## Cleanup

```bash
rm -rf sps-10* ctmp* logs/* results/*
```

## Standalone scripts

Simple script trying to use two loggers to store different outputs.

```bash
cd standalone
python two-loggers-v1.py
python two-loggers-v2.py
```

Cleanup.

```bash
cd standalone
rm *.log
```
