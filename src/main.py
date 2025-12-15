from user import User
import os
from dotenv import load_dotenv

load_dotenv()

canvasKey = os.getenv("CANVAS_API_KEY")
notionToken = os.getenv("NOTION_TOKEN")
notionPageId = os.getenv("NOTION_PAGE_ID")
schoolAb = os.getenv("SCHOOL_AB")
databaseId = os.getenv("DATABASE_ID")

user = User(canvasKey, notionToken, notionPageId, schoolAb, database_id=databaseId)

# if you want to create a new database, uncomment below
# user = User(canvasKey, notionToken, notionPageId, schoolAb)

courses = user.getAllCourses()
user.enterAssignmentsToNotionDb(courses)