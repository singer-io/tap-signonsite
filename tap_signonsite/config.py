from tap_signonsite.fetch import get_all_sites


KEY_PROPERTIES = {
    "sites": ["id"],
    "attendances": ["id"],
    "companies": ["id"],
    "users": ["id"],
}

SYNC_FUNCTIONS = {
    "sites": get_all_sites,
}

SUB_STREAMS = {
    "sites": ["attendances", "companies", "users"],
}
