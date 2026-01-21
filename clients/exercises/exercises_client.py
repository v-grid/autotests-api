from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient

class GetExercisesQweryDict(TypedDict):
    """
        Описание структуры запроса на получение упражнений.
    """
    courseId: str

class CreateExercisesQweryDict(TypedDict):
    """
        Описание структуры запроса на создание упражнений.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesQweryDict(TypedDict):
    """
        Описание структуры запроса на изменение упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
        Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQweryDict) -> Response:
        """
            Метод получения списка упражнений.

            :param query: Словарь с courseId.
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
            Метод получения упражнения.

            :param query: Идентификатор упражнения exercise_id.
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises{exercise_id}")

    def create_exercises_api(self, request: CreateExercisesQweryDict) -> Response:
        """
            Метод создания упражнения.

            :param query: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercises_api(self, exercise_id: str, request:UpdateExercisesQweryDict) -> Response:
        """
            Метод изменения упражнения.

            :param query: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
            Метод удаления упражнения.

            :param query: Идентификатор упражнения exercise_id.
            :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises{exercise_id}")





