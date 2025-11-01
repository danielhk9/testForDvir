import pathlib, pytest, allure
from allure_commons.types import AttachmentType

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    alluredir = session.config.getoption("--alluredir")
    if alluredir:
        p = pathlib.Path(alluredir)
        p.mkdir(parents=True, exist_ok=True)
        (p/"environment.properties").write_text(
            "BASE_URL={}\nBROWSER={}\nHEADLESS={}\n".format(
                session.config.getoption("--base-url", default=""),
                session.config.getoption("--browser", default="chrome"),
                session.config.getoption("--headless", default=True),
            ),
            encoding="utf-8"
        )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed and "driver" in item.fixturenames:
        driver = item.funcargs.get("driver")
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{item.name}_screenshot",
                attachment_type=AttachmentType.PNG
            )
            allure.attach(driver.page_source, f"{item.name}_page_source", AttachmentType.HTML)
            allure.attach(driver.current_url, "current_url", AttachmentType.TEXT)
        except Exception:
            pass
