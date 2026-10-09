class Settings:

    # Базовый url
    BASE_URL = "https://saucedemo.com"

    # Пользователи учётки
    USERS_PASSWORD = {
                       "standard_user": "secret_sauce",
                       "problem_user": "secret_sauce",
                       "performance_glitch_user": "secret_sauce",
                        "error_user": "secret_sauce",
                        "visual_user": "secret_sauce"
                      }

    INVALID_LOGIN_PASSWORD  = {
                      "standard": "standard_user: ",
                      "problem": ": 57437665476584",
                      "performance": "performance_glitch_user: jdijgjcfjfdf",
                      "error": "error_user: secret_sauce1",
                      "visual": "visual_user: 574376#$%$^%@56231654"
    }


settings = Settings()