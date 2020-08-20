# tap-signonsite

## Connecting tap-signonsite

### Requirements

To set up tap-signonsite in Stitch, you need:

- **Your API secret key**. This provides company-level access to your account.

### Setup

To get your SignOnSite API key, log into the [SignOnSite portal](https://app.signonsite.com.au/login) with an admin account, and go to the [settings page](https://app.signonsite.com.au/companies/5084/settings). Click on the button at the bottom to generate the secret API key. SignOnSite [provides documentation](https://support.signonsite.com.au/en/articles/4209421-api) for these steps.

---

## tap-signonsite Replication

Site attendances are replicated based on date, so when the tap runs it will only pull in new rows since the last run.

Sites, users, and customers have no date field to filter by, so all records are returned each time.

Note that user and company information is pulled from the site attendance records, so only unique rows for users and companies who have new site attendances since the last run will be returned.

---

## tap-signonsite Table Schemas

Note that documentation is only available to existing SignOnSite customers, per the [API help article](https://support.signonsite.com.au/en/articles/4209421-api).

- Table name: Sites
- Description: Simple list of all sites in the system. Note that deleted sites aren't returned
- Replicated fully
- Primary key column(s): id

* Table name: Attendances
* Description: Site visits, with timestamps for start and end, and links to company and user. Also tracks site inductions.
* Replicated incrementally
* Primary key column(s): id
* Bookmark column(s): signon_at

- Table name: Users
- Description: Basic user identifiers like name and email.
- Replicated fully from incremental attendances
- Primary key column(s): id

* Table name: Companies
* Description: Company name.
* Replicated fully from incremental attendances
* Primary key column(s): id
