# запуск fastapi застосунку через uvicorn

# uvicorn [файл]:[змінна для застосунку] --host [ip адреса] --port [порт]

# для запуску з портом
# docker run -p 8080:8080 [назва образу]

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "application:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )
