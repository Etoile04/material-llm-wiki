"""Message schemas for ref-gap-fill pipeline: GapRequest (input) and DataSet (output)."""

from dataclasses import dataclass, field, asdict
import json
import uuid
from datetime import datetime
from pathlib import Path

SCHEMA_VERSION_REQUEST = "ref-gap-fill/GapRequest/v1"
SCHEMA_VERSION_DATASET = "ref-gap-fill/DataSet/v1"
VALID_STATUSES = {"complete", "partial", "failed"}
VALID_PRIORITIES = {"high", "normal", "low"}
VALID_METHODS = {"DFT", "experimental", "any"}

# Load valid property names from property-mapping.json
_PROPERTY_NAMES: set[str] | None = None

def _load_valid_properties() -> set[str]:
    global _PROPERTY_NAMES
    if _PROPERTY_NAMES is not None:
        return _PROPERTY_NAMES
    mapping_path = Path(__file__).resolve().parent.parent / "data" / "property-mapping.json"
    with open(mapping_path) as f:
        data = json.load(f)
    _PROPERTY_NAMES = {m["ref_property"] for m in data["mappings"]}
    return _PROPERTY_NAMES


@dataclass
class GapRequestItem:
    element_system: str          # required, e.g. "U-Mo"
    phase: str = ""              # optional, e.g. "BCC"
    properties: list[str] = field(default_factory=list)  # required, e.g. ["C11", "C12"]
    preferred_method: str = "any"   # DFT | experimental | any
    temperature_k: int = 0
    priority: str = "normal"     # high | normal | low


@dataclass
class GapRequest:
    schema_version: str = SCHEMA_VERSION_REQUEST
    request_id: str = ""
    timestamp: str = ""
    items: list[GapRequestItem] = field(default_factory=list)

    def __post_init__(self):
        if not self.request_id:
            self.request_id = str(uuid.uuid4())
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


@dataclass
class DataSetStats:
    total_requested: int = 0
    from_cache: int = 0
    from_express: int = 0
    gaps_remaining: int = 0


@dataclass
class DataSet:
    schema_version: str = SCHEMA_VERSION_DATASET
    request_id: str = ""
    status: str = ""            # complete | partial | failed
    stats: DataSetStats = field(default_factory=DataSetStats)
    data: list[dict] = field(default_factory=list)   # RefValue dicts
    gaps: list[dict] = field(default_factory=list)    # remaining gaps


# ── Serialization / Deserialization ──

def _dataclass_to_json(obj) -> str:
    return json.dumps(asdict(obj), ensure_ascii=False, indent=2)


def gap_request_to_json(req: GapRequest) -> str:
    return _dataclass_to_json(req)


def gap_request_from_json(s: str) -> GapRequest:
    d = json.loads(s)
    items = [GapRequestItem(**i) for i in d.get("items", [])]
    return GapRequest(
        schema_version=d.get("schema_version", SCHEMA_VERSION_REQUEST),
        request_id=d.get("request_id", ""),
        timestamp=d.get("timestamp", ""),
        items=items,
    )


def data_set_to_json(ds: DataSet) -> str:
    return _dataclass_to_json(ds)


def data_set_from_json(s: str) -> DataSet:
    d = json.loads(s)
    stats_d = d.get("stats", {})
    stats = DataSetStats(
        total_requested=stats_d.get("total_requested", 0),
        from_cache=stats_d.get("from_cache", 0),
        from_express=stats_d.get("from_express", 0),
        gaps_remaining=stats_d.get("gaps_remaining", 0),
    )
    return DataSet(
        schema_version=d.get("schema_version", SCHEMA_VERSION_DATASET),
        request_id=d.get("request_id", ""),
        status=d.get("status", ""),
        stats=stats,
        data=d.get("data", []),
        gaps=d.get("gaps", []),
    )


# ── Validation ──

def validate_gap_request(req: GapRequest) -> list[str]:
    """Return list of validation error strings. Empty = valid."""
    errors: list[str] = []
    valid_props = _load_valid_properties()
    for i, item in enumerate(req.items):
        if not item.element_system.strip():
            errors.append(f"items[{i}].element_system must be non-empty")
        if item.preferred_method not in VALID_METHODS:
            errors.append(f"items[{i}].preferred_method '{item.preferred_method}' not in {VALID_METHODS}")
        if item.priority not in VALID_PRIORITIES:
            errors.append(f"items[{i}].priority '{item.priority}' not in {VALID_PRIORITIES}")
        for prop in item.properties:
            if prop not in valid_props:
                errors.append(f"items[{i}].properties: '{prop}' not in valid property names")
    return errors


def validate_data_set(ds: DataSet) -> list[str]:
    """Return list of validation error strings. Empty = valid."""
    errors: list[str] = []
    if ds.status not in VALID_STATUSES:
        errors.append(f"status '{ds.status}' not in {VALID_STATUSES}")
    return errors
