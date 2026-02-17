import asyncio
from playwright.async_api import async_playwright

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent

playwright = None
browser = None
page = None


async def init_browser():
    global playwright, browser, page
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()


async def close_browser():
    await browser.close()
    await playwright.stop()



@tool
async def open_page(url: str) -> str:
    """Open a webpage and return HTML + visible text."""
    await page.goto(url, timeout=60000)
    await page.wait_for_load_state("domcontentloaded")
    await asyncio.sleep(1)

    html = await page.content()
    text = await page.inner_text("body")

    return (
        "=== HTML (truncated) ===\n"
        + html[:3000]
        + "\n\n=== VISIBLE TEXT (truncated) ===\n"
        + text[:3000]
    )


@tool
async def scroll_page() -> str:
    """Scroll the page and return updated visible text."""
    await page.wait_for_load_state("domcontentloaded")

    try:
        await page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )
    except Exception:
        await page.wait_for_load_state("domcontentloaded")

    await asyncio.sleep(1)
    text = await page.inner_text("body")
    return text[:4000]


@tool
async def read_visible_text() -> str:
    """Read visible text from the webpage."""
    await page.wait_for_load_state("domcontentloaded")
    text = await page.inner_text("body")
    return text[:4000]


tools = [open_page, scroll_page, read_visible_text]

model = ChatOllama(
    model="qwen2.5",
    temperature=0
)

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=(
        "You are a web browsing AI.\n"
        "You can open pages, scroll, and read content.\n"
        "After each action, analyze the page.\n"
        "If the user asks to explain a site, summarize clearly."
    )
)


async def main():
    await init_browser()
    goal=input("enter the goal:")

    result = await agent.ainvoke(
        {"messages": [HumanMessage(content=goal)]}
    )

    print("\nFINAL OUTPUT\n")
    print(result["messages"][-1].content)

    await close_browser()


if __name__ == "__main__":
    asyncio.run(main()) 
