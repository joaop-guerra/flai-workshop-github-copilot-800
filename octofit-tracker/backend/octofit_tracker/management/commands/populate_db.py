from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')

        # Delete in order to respect foreign keys
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating users (superheroes)...')

        # Marvel heroes
        ironman = User.objects.create(
            username='ironman',
            email='ironman@avengers.com',
            password='pbkdf2_sha256$ironman',
        )
        spiderman = User.objects.create(
            username='spiderman',
            email='spiderman@avengers.com',
            password='pbkdf2_sha256$spiderman',
        )
        thor = User.objects.create(
            username='thor',
            email='thor@avengers.com',
            password='pbkdf2_sha256$thor',
        )
        blackwidow = User.objects.create(
            username='blackwidow',
            email='blackwidow@avengers.com',
            password='pbkdf2_sha256$blackwidow',
        )
        hulk = User.objects.create(
            username='hulk',
            email='hulk@avengers.com',
            password='pbkdf2_sha256$hulk',
        )

        # DC heroes
        batman = User.objects.create(
            username='batman',
            email='batman@justiceleague.com',
            password='pbkdf2_sha256$batman',
        )
        superman = User.objects.create(
            username='superman',
            email='superman@justiceleague.com',
            password='pbkdf2_sha256$superman',
        )
        wonderwoman = User.objects.create(
            username='wonderwoman',
            email='wonderwoman@justiceleague.com',
            password='pbkdf2_sha256$wonderwoman',
        )
        flash = User.objects.create(
            username='flash',
            email='flash@justiceleague.com',
            password='pbkdf2_sha256$flash',
        )
        aquaman = User.objects.create(
            username='aquaman',
            email='aquaman@justiceleague.com',
            password='pbkdf2_sha256$aquaman',
        )

        self.stdout.write('Creating teams...')

        team_marvel = Team.objects.create(name='Team Marvel')
        team_marvel.members.add(ironman, spiderman, thor, blackwidow, hulk)

        team_dc = Team.objects.create(name='Team DC')
        team_dc.members.add(batman, superman, wonderwoman, flash, aquaman)

        self.stdout.write('Creating activities...')

        activities_data = [
            (ironman, 'Strength Training', 60, '2024-01-10'),
            (spiderman, 'Running', 45, '2024-01-11'),
            (thor, 'Hammer Throw', 30, '2024-01-12'),
            (blackwidow, 'Martial Arts', 90, '2024-01-13'),
            (hulk, 'Weightlifting', 120, '2024-01-14'),
            (batman, 'Obstacle Course', 75, '2024-01-10'),
            (superman, 'Flight Training', 60, '2024-01-11'),
            (wonderwoman, 'Combat Training', 90, '2024-01-12'),
            (flash, 'Sprint Training', 20, '2024-01-13'),
            (aquaman, 'Swimming', 50, '2024-01-14'),
        ]

        for user, activity_type, duration, date in activities_data:
            Activity.objects.create(
                user=user,
                activity_type=activity_type,
                duration=duration,
                date=parse_date(date),
            )

        self.stdout.write('Creating leaderboard entries...')

        leaderboard_data = [
            (ironman, 950),
            (spiderman, 870),
            (thor, 920),
            (blackwidow, 880),
            (hulk, 1000),
            (batman, 910),
            (superman, 980),
            (wonderwoman, 960),
            (flash, 990),
            (aquaman, 850),
        ]

        for user, score in leaderboard_data:
            Leaderboard.objects.create(user=user, score=score)

        self.stdout.write('Creating workouts...')

        workouts_data = [
            ('Avengers Endurance Run', 'A 10km run inspired by the Avengers', 60),
            ('Spider Agility Circuit', 'High-intensity agility drills', 45),
            ('Thor Thunder Strength', 'Heavy compound lifts', 75),
            ('Black Widow HIIT', 'High-intensity interval training', 30),
            ('Hulk Smash Powerlifting', 'Maximum strength training', 90),
            ('Bat Cave Circuit', 'Full-body Batman-style workout', 60),
            ('Super Speed Intervals', 'Sprint intervals for the Flash', 25),
            ('Amazonian Warrior Training', 'Wonder Woman combat conditioning', 80),
            ('Kryptonian Strength', 'Superman-level strength training', 70),
            ('Atlantis Swim Challenge', 'Aquaman long-distance swim', 55),
        ]

        for name, description, duration in workouts_data:
            Workout.objects.create(
                name=name,
                description=description,
                duration=duration,
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated octofit_db with superhero test data!'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'  Users: {User.objects.count()}'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'  Teams: {Team.objects.count()}'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'  Activities: {Activity.objects.count()}'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'  Leaderboard entries: {Leaderboard.objects.count()}'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'  Workouts: {Workout.objects.count()}'
        ))
