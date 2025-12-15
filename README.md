# Canvas-Notion Assignment Tracker
A Python script that loads your assignments, due or completed, from your Canvas account straight into your Notion dashboard.

### Acknowledgements
This extension uses original source code belonging to [@dpshade](https://github.com/dpshade), but features additional customisation. [Link to the original repo](https://github.com/dpshade/canvas-notion-api).

### Disclaimer
This extension is specialised for NUS students, especially with how Semesters and Weeks are computed. If you are a non-NUS student, please edit `scripts/date_helpers.py` and `config/schema.py`

## How to Setup
1. Create a `.env` file in the root with the following:
    `CANVAS_API_KEY=
    NOTION_TOKEN=
    NOTION_PAGE_ID=
    SCHOOL_AB=
    DATABASE_ID=`
### Canvas
1. Go into your school's Canvas page, preferably the dashboard and homepage
2. Copy the part of your Canvas URL that is after ***"https://"***. This is the `SCHOOL_AB`. For NUS students, this would be [canvas.nus.edu.sg](canvas.nus.edu.sg)
3. Go into settings
4. Scroll down to "Approved integrations"
5. Click new access token
6. Save and store the token they provide as the `CANVAS_API_KEY`

## Notion
1. Set up an account if you haven't already
2. Create a new page
3. Create a new Notion integration ([instructions](https://developers.notion.com/docs/create-a-notion-integration))
4. Copy the internal integration secret as the `NOTION_KEY`
5. Share the page with a workspace integration
6. Copy the page ID of the page you wish to hold the database. Store this as the `NOTION_PAGE_ID`
7. (optional) To connect to an existing database, select "Copy link to view" and copy the database id as `DATABASE_ID`

## In the code
Call the desired functions and run `main.py` to execute.

[Dylan Shade's Notion website with visuals and more](https://dylan-shade-creations.super.site/canvas-notion-api)


Here are some useful documents if you would like to tweak the properties yourself!

[Canvas Instructure API](https://developerdocs.instructure.com/services/canvas/resources/assignments)
[Notion Developers API](https://developers.notion.com/reference/intro)
