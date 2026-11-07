# test_logic.py

import unittest
from logic import Task, TaskManager


class TestTask(unittest.TestCase):
    def test_mark_done(self):
        task = Task("Дело", "2025-11-01")
        self.assertFalse(task.done)
        task.mark_done()
        self.assertTrue(task.done)

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            Task("", "2025-11-01")
        with self.assertRaises(ValueError):
            Task("   ", "2025-11-01")


class TestTaskManager(unittest.TestCase):
    def test_add_and_count(self):
        m = TaskManager()
        m.add_task("Дело 1", "2025-11-01")
        m.add_task("Дело 2", "2025-11-02")
        self.assertEqual(m.count(), 2)

    def test_remove_missing_raises(self):
        m = TaskManager()
        with self.assertRaises(ValueError):
            m.remove_task("Нет такого")

    def test_mark_done_missing_raises(self):
        m = TaskManager()
        with self.assertRaises(ValueError):
            m.mark_done("Нет такого")

    def test_get_pending(self):
        m = TaskManager()
        m.add_task("Сделать 1", "2025-11-01")
        m.add_task("Сделать 2", "2025-11-02")
        m.mark_done("Сделать 1")
        pending = m.get_pending()
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0].title, "Сделать 2")

    # Задание 3.5 (со звёздочкой)
    def test_find_by_title(self):
        m = TaskManager()
        m.add_task("Купить хлеб", "2025-11-01")
        m.add_task("Полить цветы", "2025-11-02")
        m.add_task("Сходить в магазин", "2025-11-03")
        
        results = m.find_by_title("куп")
        self.assertEqual(len(results), 2)
        titles = [t.title for t in results]
        self.assertIn("Купить хлеб", titles)
        self.assertIn("Сходить в магазин", titles)