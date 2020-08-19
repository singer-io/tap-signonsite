import singer
import singer.metrics as metrics
from singer import metadata
from singer.bookmarks import get_bookmark
from tap_signonsite.utility import get_all_pages, formatDate


def get_all_sites(schemas, state, mdata):
    extraction_time = singer.utils.now()

    with metrics.record_counter("sites") as s_counter:
        with metrics.record_counter("attendances") as a_counter:
            for response in get_all_pages("sites", "/sites"):
                sites = response["data"]
                for site in sites:
                    # handle sites record
                    with singer.Transformer() as transformer:
                        rec = transformer.transform(
                            site, schemas["sites"], metadata=metadata.to_map(mdata)
                        )
                    singer.write_record("sites", rec, time_extracted=extraction_time)
                    s_counter.increment()

                    # sync attendances if that schema is present (only there if selected)
                    if schemas.get("attendances"):
                        site_id = site["id"]

                        for attendance in get_attendances(
                            site_id, schemas["attendances"], state, mdata
                        ):
                            singer.write_record(
                                "attendances",
                                attendance,
                                time_extracted=extraction_time,
                            )
                            a_counter.increment()

                # Update attendances bookmark at the end
                if schemas.get("attendances"):
                    print(
                        "Going to write attendances bookmark",
                        formatDate(extraction_time),
                    )
                    singer.write_bookmark(
                        state, "attendances", "since", formatDate(extraction_time),
                    )

    return state


def get_attendances(site_id, schema, state, mdata):
    bookmark_value = get_bookmark(state, "attendances", "since")

    for response in get_all_pages(
        "attendances", "/sites/{}/attendances".format(site_id), bookmark_value
    ):
        attendances = response["data"]
        for attendance in attendances:
            with singer.Transformer() as transformer:
                rec = transformer.transform(
                    attendance, schema, metadata=metadata.to_map(mdata)
                )
            yield rec

    return state
