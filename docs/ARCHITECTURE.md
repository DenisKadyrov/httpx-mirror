ARCHITECTURE
------------

## Class Overview

- `App`: central entrypoint and dependency injector
- `Proxy`: forwards HTTP requests and logs traffic
- `SQLiteLogger`: logs full requests/responses to a DB
- `RequestLogic`: filtering, metrics, replay, and export over stored logs
- `HttpClient`: wrapper for `httpx.AsyncClient`
- `Config`: configurations for everyting

## Diagram

+----------------+         +-------------------+
|     CLI        |  --->   |      App          |
+----------------+         +-------------------+
                                   |
            +-------------+--------+------------+-----------+
            |             |                     |           |
        Proxy        SQLiteLogger       RequestLogic   HttpClient
 
                      
