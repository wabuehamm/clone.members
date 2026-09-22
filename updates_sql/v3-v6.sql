delete from elgg_metadata where entity_guid in (select guid from elgg_entities where subtype = 'event_calendar');
delete from elgg_entities where subtype = 'event_calendar';