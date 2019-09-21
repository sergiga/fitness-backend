from django.db import models


class Workout(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Round(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    workout = models.ForeignKey(Workout, null=True, on_delete=models.SET_NULL, related_name='rounds')

    def __str__(self):
        return '{}. Order: {}'.format(self.name, self.order)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    rounds = models.ManyToManyField(Round, through='RoundSet', related_name='exercises')

    def __str__(self):
        return self.name


class RoundSet(models.Model):
    order = models.IntegerField()
    repetitions = models.IntegerField(null=True)
    seconds = models.IntegerField(null=True)

    workout_round = models.ForeignKey(Round, related_name='sets', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, related_name='sets', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}. Order: {}'.format(self.workout_round.name, self.exercise.name, self.order)


class Muscle(models.Model):
    name = models.CharField(max_length=100)

    exercises = models.ManyToManyField(Exercise, blank=True, related_name='muscles')

    def __str__(self):
        return self.name
