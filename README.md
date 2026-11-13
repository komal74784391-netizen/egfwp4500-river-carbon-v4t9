# egfwp4500-river-carbon-v4t9

Reference implementation for the paper:

**"Riverine Carbon Flux Estimation from Dense Stream Sensor Networks"**
James Thomas, Amara Okonkwo, Maja Lindqvist.
*Journal of Geophysical Research: Biogeosciences*, 2019.

The repository contains the full Bayesian mixing model used in the paper, together
with the preprocessing scripts for the 62-catchment stream-chemistry dataset.

## Layout
- `src/river_carbon/mixing.py` -- Bayesian mixing model and sampler
- `src/river_carbon/flux.py` -- catchment export integration
- `scripts/prepare_inputs.py` -- dataset preparation
- `requirements.txt`

## Quick start
```bash
pip install -r requirements.txt
python scripts/prepare_inputs.py --config configs/basins.yaml
```

## License
MIT. See `LICENSE`.
