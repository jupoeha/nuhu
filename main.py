import asyncio,app_core

if __name__ == '__main__':
    #app_core.PORT=11622
    try:
        asyncio.run(app_core.main())
    except KeyboardInterrupt:
        print("\nServer stopped.")
