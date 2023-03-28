import pytest
from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===
# THIS IS THE OLD GET EMOJI
# """
# GET /emoji
# """
# def test_get_emoji(web_client):
#     response = web_client.get("/emoji")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ":)"

# # === End Example Code ===

##########################################################
#       BEGINNING OF HTML/PLAYWRIGHT BASED TESTS         #
##########################################################

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

"""
When we visit /albums, we get a list of albums 
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    page.goto(f"http://{test_web_address}/albums")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")
    body_tag = page.locator(("body"))
    expect(body_tag).to_contain_text("Title: album0\nReleased: 2000")
    expect(body_tag).to_contain_text("Title: album1\nReleased: 2001")
    expect(body_tag).to_contain_text("Title: album2\nReleased: 2002")
    expect(body_tag).to_contain_text("Title: album3\nReleased: 2003")
    expect(body_tag).to_contain_text("Title: album4\nReleased: 2004")

"""
When we visit /albums/<id> we get a page with single album information back
"""
def test_get_one_album(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    body_tag = page.locator("body")
    expect(h1_tag).to_have_text("album0")
    expect(body_tag).to_contain_text("Pixies")

def test_diff_one_album(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/2")
    h1_tag = page.locator("h1")
    body_tag = page.locator("body")
    expect(h1_tag).to_have_text("album1")
    expect(body_tag).to_contain_text("Pixies")