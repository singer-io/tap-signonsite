from tap_signonsite.fetch import get_all_sites


SYNC_FUNCTIONS = {
    "sites": get_all_sites,
}

SUB_STREAMS = {
    "sites": ["attendances", "companies", "users"],
}
