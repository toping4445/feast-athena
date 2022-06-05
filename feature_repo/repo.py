from datetime import timedelta

from feast import Entity, Feature, FeatureView, ValueType

from feast_custom_offline_store.athena_source import AthenaSource

driver_hourly_stats = AthenaSource(
    timestamp_field="event_timestamp",
    table="driver_stats",
    database="dev",
    data_source="AwsDataCatalog",
    created_timestamp_column="created",
)

driver = Entity(
    name="driver_id",
    value_type=ValueType.INT64,
    description="driver id",
)

driver_hourly_stats_view = FeatureView(
    name="driver_hourly_stats",
    entities=["driver_id"],
    ttl=timedelta(days=365),
    features=[
        Feature(name="conv_rate", dtype=ValueType.FLOAT),
        Feature(name="acc_rate", dtype=ValueType.FLOAT),
        Feature(name="avg_daily_trips", dtype=ValueType.INT64),
    ],
    online=True,
    batch_source=driver_hourly_stats,
)
