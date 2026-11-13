"""Prepare stream-chemistry inputs for the river carbon pipeline."""

import argparse
import json
from pathlib import Path


def load_station_records(path: Path) -> list:
    records = []
    with path.open() as handle:
        for line in handle:
            payload = json.loads(line)
            records.append(
                {
                    "station": payload["station_id"],
                    "date": payload["sample_date"],
                    "doc_mg_l": float(payload["dissolved_organic_carbon"]),
                    "delta13c": float(payload["delta13c"]),
                }
            )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--input", type=Path, default=Path("data/stations.jsonl"))
    args = parser.parse_args()
    records = load_station_records(args.input)
    print(f"loaded {len(records)} station records")


if __name__ == "__main__":
    main()
