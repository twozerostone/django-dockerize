from rest_framework.test import APITestCase
from education.models import (
    Curriculum, CurriculumDivision, Lecture,
    LectureDivision, Lesson, CurriculumLecture,
    CurriculumStudent, CurriculumProgress
)
from cert.models import CustomUser


class EducationTests(APITestCase):
    """
    curriculum 분류를 만듬 (curriculum_div)
    curriculum을 만듬 (curriculum_one)
    curriculum을 하나 더 만듬 (curriculum_two)
    temp_curriculum을 만듬
    lecture 분류를 만듬 (lecture_div)
    lecture를 만듬 (lecture_one)
    lecture를 하나 더 만듬 (lecture_two)
    lesson을 만듬 (lesson_one)
    lesson을 하나 더 만듬 (lesson_two)
    student를 만듬 (member)
    """
    def setUp(self):
        self.curriculum_div_one = CurriculumDivision.objects.create(name="한컵 커리큘럼")
        self.curriculum_div_two = CurriculumDivision.objects.create(name="두컵 커리큘럼")
        self.curriculum_one = Curriculum.objects.create(
            title="커리큘럼 첫번째",
            password="1",
            division=self.curriculum_div_one.id,
            subject="이곳은 첫번째 커리큘럼의 주제이다.",
            public=True,
            contents="이곳은 첫번째 커리큘럼의 내용이라고 할 수 있다.",
            start_date="2020-12-22 10:00:00",
            end_date="2021-02-22 10:00:00"
        )
        self.curriculum_two = Curriculum.objects.create(
            title="커리큘럼 두번째",
            password="1",
            division=self.curriculum_div_two.id,
            subject="이곳은 두번째 커리큘럼의 주제이다.",
            public=True,
            contents="이곳은 두번째 커리큘럼의 내용이라고 할 수 있다.",
            start_date="2020-12-22 10:00:00",
            end_date="2021-02-22 10:00:00"
        )
        self.curriculum_one.set_password('123123')
        self.curriculum_two.set_password('456456')
        self.curriculum_one.save()
        self.curriculum_two.save()
        self.lecture_div_one = LectureDivision.objects.create(name="한컵 강의")
        self.lecture_div_two = LectureDivision.objects.create(name="두컵 강의")
        self.lecture_one = Lecture.objects.create(
            title="강좌 첫번째",
            category=self.lecture_div_one.id,
            difficult="심화",
            public=True,
            contents="이곳은 첫번째 강좌의 내용이라고 할 수 있다."
        )
        self.lecture_two = Lecture.objects.create(
            title="강좌 두번째",
            category=self.lecture_div_two.id,
            difficult="기초",
            public=True,
            contents="이곳은 두번째 강좌의 내용이라고 할 수 있다."
        )
        self.lesson_one = Lesson.objects.create(
            title="강의 첫번째",
            url="https://www.youtube.com/watch?v=5qap5aO4i9A",
            contents="여기는 첫번째 강의의 내용이라고 할 수 있다."
        )
        self.lesson_two = Lesson.objects.create(
            title="강의 두번째",
            url="https://www.youtube.com/watch?v=5qap5aO4i9A",
            contents="여기는 첫번째 강의의 내용이라고 할 수 있다."
        )
        self.student = CustomUser.objects.create(
            password='1',
            user_id='testuser',
            email='dev@de1v.com',
            name='imtest',
        )
        self.progress = CurriculumProgress.objects.create(
            student=self.student.id,
            curriculum=self.curriculum_one.id,
            lecture=self.lecture_one.id,
            lesson=self.lesson_one.id
        )
        self.student.set_password('123123')
        self.student.save()

    """
    테스트 시작
    -----------------------------------------------------------
    curriculum 분류를 삭제하면 curriculum 사라지는지
    curriculum 시작날짜가 종료날짜보다 미래의 시간인지 확인
    """
    def test_curriculum_div_delete(self):
        self.curriculum_div_one.delete()
        assert Curriculum.objects.count() == 1

        self.curriculum_div_two.delete()
        assert Curriculum.objects.count() == 0

    def test_curriculum_end_date(self):

    """
    lecture 분류를 삭제하면 lecture 사라지는지
    lecture 삭제하면 lesson 사라지는지
    """
    def test_lecture_div_delete(self):
        self.lecture_div_one.delete()
        assert Lecture.objects.count() == 1

        self.lecture_dive_two.delete()
        assert Lecture.objects.count() == 0

    def test_lecture_delete(self):
        self.lecture_one.delete()
        assert Lesson.objects.count() == 1

        self.lecture_two.delete()
        assert Lesson.objects.count() == 0
    """
    관계 table 확인
    -----------------------------------------------------------
    curriculum - student 관계 table

    curriculum 삭제
    student 삭제
    """
    def test_curriculum_student_delete(self):
        self.curriculum_one.student.add(self.student.id)
        self.curriculum_two.student.add(self.student.id)
        curriculum_id = self.curriculum_one.id
        self.curriculum_one.delete()
        self.assertFalse(CurriculumStudent.objects.filter(curriculum_id=curriculum_id).exists())

        student_id = self.student.id
        self.student.delete()
        self.assertFalse(CurriculumStudent.objects.filter(user_id=student_id).exists())
    """
    curriculum - lecture 관계 table

    curriculum 삭제
    lecture 삭제
    curriculum 에 lecture 넣기
    """
    def test_curriculum_lecture_delete(self):
        self.curriculum_one.lecture.add(self.lecture_one.id)
        self.curriculum_two.lecture.add(self.lecture_two.id)
        curriculum_id = self.curriculum_one.id
        self.curriculum_one.delete()
        self.assertFalse(CurriculumLecture.objects.filter(curriculum_id=curriculum_id).exists())

        lecture_id = self.lecture_two.id
        self.lecture_two.delete()
        self.assertFalse(CurriculumLecture.objects.filter(lecture_id=lecture_id).exists())
    """
    student - curriculum - lecture - lesson table (curriculum 내 학생 학습률의 위한 table)

    lecture 삭제
    student 삭제
    curriculum 삭제
    lesson 삭제
    """
    def test_progress_delete_student(self):
        self.student.delete()
        assert CurriculumProgress.objects.count() == 0

    def test_progress_delete_curriculum(self):
        self.curriculum_one.delete()
        assert CurriculumProgress.objects.count() == 0

    def test_progress_delete_lecture(self):
        self.lecture_one.delete()
        assert CurriculumProgress.objects.count() == 0
    
    def test_progress_delete_lesson(self):
        self.lesson_one.delete()
        assert CurriculumProgress.objects.count() == 0